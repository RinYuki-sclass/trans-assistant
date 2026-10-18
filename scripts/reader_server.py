import os
import sys
import json
import uuid
import threading
import time
import shutil
import urllib.parse
from typing import Dict, List, Optional

# Thêm đường dẫn scripts vào sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from starlette.applications import Starlette
from starlette.responses import JSONResponse, FileResponse, Response
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from crawler.general_crawler import detect_and_get_manga_info, detect_and_get_chapter_images, search_manga_haccbl
from crawler.haccbl_crawler import download_chapter_images, get_scraper, clean_slug

# Thư mục dữ liệu
DATA_DIR = os.path.join(BASE_DIR, "data")
LIBRARY_DIR = os.path.join(DATA_DIR, "cubari_library")
STATIC_READER_DIR = os.path.join(BASE_DIR, "static", "reader")
TRANS_OUTPUT_DIR = os.path.join(BASE_DIR, "output", "manhwa_history")
CACHE_DIR = os.path.join(DATA_DIR, "cache", "proxy_images")

os.makedirs(LIBRARY_DIR, exist_ok=True)
os.makedirs(STATIC_READER_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

# Quản lý tiến trình tải (Thread-safe)
active_downloads: Dict[str, Dict] = {}
downloads_lock = threading.Lock()

def clean_old_cache(max_age_days: int = 7, max_size_mb: int = 1000):
    """
    Tự động dọn dẹp cache ảnh proxy:
    - Xóa các file cũ hơn max_age_days
    - Nếu tổng dung lượng vượt quá max_size_mb, tự động xóa các file cũ nhất
    """
    try:
        if not os.path.exists(CACHE_DIR):
            return
        now = time.time()
        max_age_sec = max_age_days * 86400
        files = []
        total_size = 0
        for f in os.listdir(CACHE_DIR):
            fp = os.path.join(CACHE_DIR, f)
            if os.path.isfile(fp):
                try:
                    st_stat = os.stat(fp)
                    files.append((fp, st_stat.st_mtime, st_stat.st_size))
                    total_size += st_stat.st_size
                except Exception:
                    pass

        # 1. Xóa file quá hạn
        for fp, mtime, sz in files:
            if now - mtime > max_age_sec:
                try:
                    os.remove(fp)
                    total_size -= sz
                except Exception:
                    pass

        # 2. Giới hạn tổng dung lượng cache
        max_bytes = max_size_mb * 1024 * 1024
        if total_size > max_bytes:
            remaining = [f for f in files if os.path.exists(f[0])]
            remaining.sort(key=lambda x: x[1])
            for fp, mtime, sz in remaining:
                if total_size <= max_bytes:
                    break
                try:
                    os.remove(fp)
                    total_size -= sz
                except Exception:
                    pass
    except Exception as e:
        print(f"[cache-cleanup] Lỗi: {e}")

# Chạy dọn cache ngầm định kỳ
def _periodic_cache_cleaner():
    while True:
        clean_old_cache()
        time.sleep(21600)  # 6 tiếng quét 1 lần

threading.Thread(target=_periodic_cache_cleaner, daemon=True).start()

# ---------------------------------------------
# CÁC HÀM TIỆN ÍCH
# ---------------------------------------------

def scan_local_library() -> List[Dict]:
    """
    Quét thư mục data/cubari_library và output/manhwa_history
    """
    mangas = []

    # 1. Quét data/cubari_library
    if os.path.exists(LIBRARY_DIR):
        for item in sorted(os.listdir(LIBRARY_DIR)):
            manga_path = os.path.join(LIBRARY_DIR, item)
            if os.path.isdir(manga_path):
                info_file = os.path.join(manga_path, "info.json")
                manga_info = {
                    "slug": item,
                    "title": item.replace("-", " ").title(),
                    "cover": "",
                    "source": "cubari_library",
                    "chapters": []
                }
                if os.path.exists(info_file):
                    try:
                        with open(info_file, "r", encoding="utf-8") as f:
                            saved_info = json.load(f)
                            manga_info.update(saved_info)
                    except Exception:
                        pass

                # Quét các chapter trong thư mục
                chapters = []
                for ch_item in sorted(os.listdir(manga_path)):
                    ch_path = os.path.join(manga_path, ch_item)
                    if os.path.isdir(ch_path):
                        # Đếm số ảnh
                        img_files = [
                            f for f in sorted(os.listdir(ch_path))
                            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))
                        ]
                        if img_files:
                            chapters.append({
                                "slug": ch_item,
                                "title": ch_item.replace("-", " ").title(),
                                "pages_count": len(img_files),
                                "source_type": "local",
                                "manga_slug": item
                            })
                
                manga_info["chapters"] = chapters
                manga_info["total_chapters"] = len(chapters)
                if chapters:
                    mangas.append(manga_info)

    # 2. Quét output/manhwa_history (tích hợp tool dịch)
    if os.path.exists(TRANS_OUTPUT_DIR):
        trans_chapters = []
        for ch_item in sorted(os.listdir(TRANS_OUTPUT_DIR)):
            ch_path = os.path.join(TRANS_OUTPUT_DIR, ch_item)
            if os.path.isdir(ch_path):
                img_dir = os.path.join(ch_path, "images")
                target_dir = img_dir if os.path.exists(img_dir) else ch_path
                img_files = [
                    f for f in sorted(os.listdir(target_dir))
                    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))
                ]
                has_script = os.path.exists(os.path.join(ch_path, "script.txt"))
                if img_files:
                    trans_chapters.append({
                        "slug": ch_item,
                        "title": ch_item,
                        "pages_count": len(img_files),
                        "has_script": has_script,
                        "source_type": "trans_tool",
                        "manga_slug": "trans-tool-history"
                    })

        if trans_chapters:
            mangas.append({
                "slug": "trans-tool-history",
                "title": "⚡ Trans-Tool: Bản Dịch Dự Án",
                "cover": "",
                "source": "trans_tool",
                "chapters": trans_chapters,
                "total_chapters": len(trans_chapters)
            })

    return mangas

# ---------------------------------------------
# CÁC API ENDPOINTS
# ---------------------------------------------

async def api_library(request):
    """Lấy danh sách các bộ truyện và chapter đã có ở local"""
    library = scan_local_library()
    return JSONResponse({"status": "success", "mangas": library})

async def api_crawl_info(request):
    """Phân tích link truyện / chapter để lấy danh sách chapters"""
    try:
        data = await request.json()
        url = data.get("url", "").strip()
        if not url:
            return JSONResponse({"status": "error", "message": "Vui lòng nhập URL hợp lệ"}, status_code=400)

        info = detect_and_get_manga_info(url)
        return JSONResponse({"status": "success", "data": info})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

def background_download_worker(task_id: str, manga_title: str, manga_slug: str, chapter_slug: str, chapter_url: str, manga_url: str = ""):
    """Worker tải ảnh chapter chạy trong background thread"""
    try:
        with downloads_lock:
            active_downloads[task_id]["status"] = "resolving"
            active_downloads[task_id]["message"] = "Đang phân tích link ảnh..."

        ch_data = detect_and_get_chapter_images(chapter_url)
        images = ch_data.get("images", [])

        if not images:
            raise Exception("Không tìm thấy ảnh nào trong chapter này")

        save_dir = os.path.join(LIBRARY_DIR, manga_slug, chapter_slug)
        os.makedirs(save_dir, exist_ok=True)

        # Lưu info.json cho manga (kèm source_url để phục vụ kiểm tra chương mới)
        import re
        manga_dir = os.path.join(LIBRARY_DIR, manga_slug)
        info_path = os.path.join(manga_dir, "info.json")
        info_data = {"slug": manga_slug, "title": manga_title}
        if os.path.exists(info_path):
            try:
                with open(info_path, "r", encoding="utf-8") as f:
                    info_data = json.load(f)
            except Exception:
                pass
        info_data["title"] = manga_title
        if manga_url:
            info_data["source_url"] = manga_url
        elif "source_url" not in info_data:
            m_manga = re.match(r'(https?://[^/]+/manga/[^/]+/)', chapter_url)
            if m_manga:
                info_data["source_url"] = m_manga.group(1)

        with open(info_path, "w", encoding="utf-8") as f:
            json.dump(info_data, f, ensure_ascii=False, indent=2)

        with downloads_lock:
            active_downloads[task_id]["status"] = "downloading"
            active_downloads[task_id]["total"] = len(images)
            active_downloads[task_id]["current"] = 0
            active_downloads[task_id]["message"] = f"Đang tải 0/{len(images)} ảnh..."

        def on_progress(current, total, filename):
            with downloads_lock:
                active_downloads[task_id]["current"] = current
                active_downloads[task_id]["total"] = total
                active_downloads[task_id]["percent"] = int((current / total) * 100)
                active_downloads[task_id]["message"] = f"Đã tải {current}/{total} ảnh ({filename})"

        download_chapter_images(images, save_dir, referer=chapter_url, progress_callback=on_progress)

        with downloads_lock:
            active_downloads[task_id]["status"] = "completed"
            active_downloads[task_id]["percent"] = 100
            active_downloads[task_id]["message"] = "Hoàn tất tải về!"
    except Exception as e:
        with downloads_lock:
            active_downloads[task_id]["status"] = "failed"
            active_downloads[task_id]["error"] = str(e)
            active_downloads[task_id]["message"] = f"Lỗi: {e}"

async def api_crawl_download(request):
    """Bắt đầu tải một chapter về local"""
    try:
        data = await request.json()
        chapter_url = data.get("chapter_url", "").strip()
        manga_title = data.get("manga_title", "Manhwa").strip()
        chapter_title = data.get("chapter_title", "Chapter").strip()
        manga_slug = data.get("manga_slug") or clean_slug(manga_title)
        chapter_slug = data.get("chapter_slug") or clean_slug(chapter_title)
        manga_url = data.get("manga_url", "").strip()

        if not chapter_url:
            return JSONResponse({"status": "error", "message": "Thiếu chapter_url"}, status_code=400)

        task_id = str(uuid.uuid4())[:8]
        with downloads_lock:
            active_downloads[task_id] = {
                "id": task_id,
                "manga_title": manga_title,
                "chapter_title": chapter_title,
                "manga_slug": manga_slug,
                "chapter_slug": chapter_slug,
                "chapter_url": chapter_url,
                "status": "pending",
                "current": 0,
                "total": 0,
                "percent": 0,
                "message": "Đang khởi động tiến trình tải...",
                "start_time": time.time()
            }

        thread = threading.Thread(
            target=background_download_worker,
            args=(task_id, manga_title, manga_slug, chapter_slug, chapter_url, manga_url),
            daemon=True
        )
        thread.start()

        return JSONResponse({"status": "success", "task_id": task_id})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

async def api_crawl_tasks(request):
    """Lấy danh sách các tác vụ download và tiến độ"""
    with downloads_lock:
        tasks = list(active_downloads.values())
    return JSONResponse({"status": "success", "tasks": tasks})

async def api_chapter_data(request):
    """
    Trả về danh sách URL ảnh để reader hiển thị
    Hỗ trợ 2 nguồn: 'local' (đã tải về) hoặc 'online' (stream qua proxy không ads)
    """
    try:
        params = request.query_params
        source_type = params.get("source", "local")
        manga_slug = params.get("manga_slug", "")
        chapter_slug = params.get("chapter_slug", "")
        online_url = params.get("url", "")

        # 1. Đọc từ local
        if source_type == "local":
            if not manga_slug or not chapter_slug:
                return JSONResponse({"status": "error", "message": "Thiếu thông tin chapter local"}, status_code=400)

            ch_dir = os.path.join(LIBRARY_DIR, manga_slug, chapter_slug)
            if not os.path.exists(ch_dir):
                return JSONResponse({"status": "error", "message": "Chưa tải chapter này về máy"}, status_code=404)

            files = [
                f for f in sorted(os.listdir(ch_dir))
                if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))
            ]
            images = [f"/data/cubari_library/{manga_slug}/{chapter_slug}/{f}" for f in files]
            return JSONResponse({
                "status": "success",
                "source": "local",
                "title": f"{manga_slug} - {chapter_slug}",
                "images": images,
                "total": len(images)
            })

        # 2. Đọc từ output/manhwa_history của tool dịch
        elif source_type == "trans_tool":
            ch_dir = os.path.join(TRANS_OUTPUT_DIR, chapter_slug)
            img_sub = os.path.join(ch_dir, "images")
            target_dir = img_sub if os.path.exists(img_sub) else ch_dir
            files = [
                f for f in sorted(os.listdir(target_dir))
                if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))
            ]
            prefix = f"/output/manhwa_history/{chapter_slug}/images" if os.path.exists(img_sub) else f"/output/manhwa_history/{chapter_slug}"
            images = [f"{prefix}/{f}" for f in files]

            # Kiểm tra file script.txt
            script_content = ""
            script_path = os.path.join(ch_dir, "script.txt")
            if os.path.exists(script_path):
                try:
                    with open(script_path, "r", encoding="utf-8") as sf:
                        script_content = sf.read()
                except Exception:
                    pass

            return JSONResponse({
                "status": "success",
                "source": "trans_tool",
                "title": chapter_slug,
                "images": images,
                "total": len(images),
                "script": script_content
            })

        # 3. Đọc online trực tiếp (Stream không dính ads qua proxy)
        elif source_type == "online":
            if not online_url:
                return JSONResponse({"status": "error", "message": "Thiếu URL online"}, status_code=400)

            ch_data = detect_and_get_chapter_images(online_url)
            raw_images = ch_data.get("images", [])

            # Route qua image proxy để không bị lỗi 403 / CORS
            proxied_images = [
                f"/api/proxy-image?url={urllib.parse.quote(img)}&referer={urllib.parse.quote(online_url)}"
                for img in raw_images
            ]
            return JSONResponse({
                "status": "success",
                "source": "online",
                "title": ch_data.get("title", "Chapter"),
                "images": proxied_images,
                "total": len(proxied_images)
            })

        return JSONResponse({"status": "error", "message": "Chế độ không hợp lệ"}, status_code=400)
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

scraper_instance = None
def get_cached_scraper():
    global scraper_instance
    if scraper_instance is None:
        scraper_instance = get_scraper()
    return scraper_instance

async def api_proxy_image(request):
    """
    Proxy và cache ảnh trực tiếp từ CDN nguồn
    Loại bỏ hoàn toàn rào cản referrer, CORS và chặn quảng cáo
    """
    try:
        img_url = request.query_params.get("url")
        referer = request.query_params.get("referer", "")
        if not img_url:
            return Response(status_code=400)

        # Hash filename cho cache
        import hashlib
        url_hash = hashlib.md5(img_url.encode('utf-8')).hexdigest()
        ext = ".jpg"
        if ".webp" in img_url.lower():
            ext = ".webp"
        elif ".avif" in img_url.lower():
            ext = ".avif"
        elif ".png" in img_url.lower():
            ext = ".png"

        cache_path = os.path.join(CACHE_DIR, f"{url_hash}{ext}")

        if os.path.exists(cache_path) and os.path.getsize(cache_path) > 500:
            return FileResponse(cache_path)

        scraper = get_cached_scraper()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        }
        if referer:
            headers['Referer'] = referer

        res = scraper.get(img_url, headers=headers, timeout=20)
        if res.status_code == 200:
            with open(cache_path, "wb") as f:
                f.write(res.content)
            content_type = res.headers.get("content-type", "image/jpeg")
            return Response(content=res.content, media_type=content_type)
        else:
            return Response(status_code=res.status_code)
    except Exception as e:
        print(f"[proxy-image] Lỗi: {e}")
        return Response(status_code=500)

async def api_crawl_search(request):
    """Tìm kiếm truyện tranh trực tiếp từ nguồn hỗ trợ"""
    try:
        q = request.query_params.get("q", "").strip()
        if not q:
            return JSONResponse({"status": "error", "message": "Vui lòng nhập từ khóa tìm kiếm"}, status_code=400)
        results = search_manga_haccbl(q)
        return JSONResponse({"status": "success", "results": results, "total": len(results)})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

async def api_library_check_updates(request):
    """
    Quét các bộ truyện trong thư viện local, kiểm tra xem nguồn có chương mới hay không
    """
    try:
        updates = []
        if not os.path.exists(LIBRARY_DIR):
            return JSONResponse({"status": "success", "updates": []})

        for item in sorted(os.listdir(LIBRARY_DIR)):
            manga_path = os.path.join(LIBRARY_DIR, item)
            if not os.path.isdir(manga_path):
                continue

            info_file = os.path.join(manga_path, "info.json")
            if not os.path.exists(info_file):
                continue

            try:
                with open(info_file, "r", encoding="utf-8") as f:
                    info_data = json.load(f)
            except Exception:
                continue

            source_url = info_data.get("source_url", "").strip()
            if not source_url:
                continue

            local_chapters = [
                d for d in os.listdir(manga_path)
                if os.path.isdir(os.path.join(manga_path, d))
            ]

            try:
                remote_info = detect_and_get_manga_info(source_url)
                remote_chapters = remote_info.get("chapters", [])
                
                local_slugs = set(local_chapters)
                new_chapters = [ch for ch in remote_chapters if ch.get("slug") not in local_slugs]

                if new_chapters:
                    updates.append({
                        "manga_slug": item,
                        "manga_title": info_data.get("title", item),
                        "source_url": source_url,
                        "cover": remote_info.get("cover", ""),
                        "local_count": len(local_chapters),
                        "remote_count": len(remote_chapters),
                        "new_chapters_count": len(new_chapters),
                        "new_chapters": new_chapters
                    })
            except Exception as check_err:
                print(f"[check-update] Bỏ qua {item}: {check_err}")

        return JSONResponse({"status": "success", "updates": updates, "total_updates": len(updates)})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

async def api_library_delete_manga(request):
    """Xóa một bộ truyện khỏi thư viện local"""
    try:
        data = await request.json()
        slug = data.get("slug", "").strip()
        if not slug:
            return JSONResponse({"status": "error", "message": "Thiếu thông tin slug"}, status_code=400)

        target_dir = os.path.join(LIBRARY_DIR, slug)
        if os.path.exists(target_dir) and os.path.isdir(target_dir):
            shutil.rmtree(target_dir)
            return JSONResponse({"status": "success", "message": f"Đã xóa thành công {slug}"})

        return JSONResponse({"status": "error", "message": "Không tìm thấy bộ truyện trên máy"}, status_code=404)
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

async def serve_index(request):
    index_file = os.path.join(STATIC_READER_DIR, "index.html")
    return FileResponse(index_file)

# ---------------------------------------------
# KHỞI TẠO STARLETTE APP
# ---------------------------------------------

routes = [
    Route("/", serve_index),
    Route("/api/library", api_library, methods=["GET"]),
    Route("/api/library/check-updates", api_library_check_updates, methods=["POST"]),
    Route("/api/library/delete", api_library_delete_manga, methods=["POST"]),
    Route("/api/crawl/search", api_crawl_search, methods=["GET"]),
    Route("/api/crawl/info", api_crawl_info, methods=["POST"]),
    Route("/api/crawl/download", api_crawl_download, methods=["POST"]),
    Route("/api/crawl/tasks", api_crawl_tasks, methods=["GET"]),
    Route("/api/chapter-data", api_chapter_data, methods=["GET"]),
    Route("/api/proxy-image", api_proxy_image, methods=["GET"]),
    Mount("/static", StaticFiles(directory=STATIC_READER_DIR), name="static"),
    Mount("/data", StaticFiles(directory=DATA_DIR), name="data"),
    Mount("/output", StaticFiles(directory=os.path.join(BASE_DIR, "output")), name="output"),
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
]

app = Starlette(routes=routes, middleware=middleware)

if __name__ == "__main__":
    port = int(os.environ.get("PORT") or os.environ.get("READER_PORT") or 7860)
    print(f"\n==================================================")
    print(f"📖 CUBARI-STYLE MANHWA READER SERVER")
    print(f"🚀 Dang chay tai: http://localhost:{port}")
    print(f"📁 Local Library: {LIBRARY_DIR}")
    print(f"==================================================\n")
    uvicorn.run("reader_server:app", host="0.0.0.0", port=port, reload=False, app_dir=SCRIPTS_DIR)
