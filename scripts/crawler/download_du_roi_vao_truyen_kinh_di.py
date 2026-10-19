import os
import sys
import io
import time
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from crawler.general_crawler import detect_and_get_manga_info, detect_and_get_chapter_images
from crawler.haccbl_crawler import get_scraper, DEFAULT_HEADERS

DATA_DIR = os.path.join(BASE_DIR, "data")
LIBRARY_DIR = os.path.join(DATA_DIR, "cubari_library")

MANGA_URL = "https://tsxx4.online/truyen-tranh/du-roi-vao-truyen-kinh-di-toi-van-phai-di-lam/"

def download_single_image(scraper, img_url, referer):
    headers = dict(DEFAULT_HEADERS)
    if referer:
        headers['Referer'] = referer
    for retry in range(3):
        try:
            res = scraper.get(img_url, headers=headers, timeout=25)
            if res.status_code == 200 and len(res.content) > 500:
                return res.content
        except Exception:
            pass
        time.sleep(0.5)
    return None

def download_chapter_fast(images, save_dir, referer=""):
    os.makedirs(save_dir, exist_ok=True)
    scraper = get_scraper()
    
    # Tải song song với ThreadPoolExecutor (max_workers=6 để vừa nhanh vừa an toàn, không bị 429)
    downloaded_map = {}
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_idx = {
            executor.submit(download_single_image, scraper, url, referer): idx
            for idx, url in enumerate(images)
        }
        for future in as_completed(future_to_idx):
            idx = future_to_idx[future]
            try:
                data = future.result()
                if data:
                    downloaded_map[idx] = data
            except Exception as e:
                print(f"      [Lỗi worker idx {idx}]: {e}")

    # Xử lý cắt ảnh & lưu webp tuần tự theo đúng thứ tự idx 0 -> N
    slice_counter = 0
    saved_files = []
    for idx in sorted(downloaded_map.keys()):
        raw_bytes = downloaded_map[idx]
        img_url = images[idx]
        try:
            im = Image.open(io.BytesIO(raw_bytes))
            w, h = im.size
            if h > 3000:
                top = 0
                while top < h:
                    bottom = min(top + 3000, h)
                    slice_im = im.crop((0, top, w, bottom))
                    slice_counter += 1
                    filename = f"{slice_counter:03d}.webp"
                    filepath = os.path.join(save_dir, filename)
                    if slice_im.mode not in ("RGB", "RGBA"):
                        slice_im = slice_im.convert("RGB")
                    slice_im.save(filepath, format="WEBP", quality=80, method=4)
                    saved_files.append(filepath)
                    top = bottom
            else:
                slice_counter += 1
                filename = f"{slice_counter:03d}.webp"
                filepath = os.path.join(save_dir, filename)
                if im.mode not in ("RGB", "RGBA"):
                    im = im.convert("RGB")
                im.save(filepath, format="WEBP", quality=80, method=4)
                saved_files.append(filepath)
        except Exception:
            slice_counter += 1
            ext = ".jpg"
            if ".png" in img_url.lower():
                ext = ".png"
            elif ".webp" in img_url.lower():
                ext = ".webp"
            elif ".avif" in img_url.lower():
                ext = ".avif"
            filename = f"{slice_counter:03d}{ext}"
            filepath = os.path.join(save_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(raw_bytes)
            saved_files.append(filepath)

    return saved_files

def run():
    print("=" * 60)
    print("📥 BẮT ĐẦU TẢI TRUYỆN: DÙ RƠI VÀO TRUYỆN KINH DỊ, TÔI VẪN PHẢI ĐI LÀM")
    print("=" * 60)

    print(f"[*] Đang lấy danh sách chapter từ: {MANGA_URL}...")
    info = detect_and_get_manga_info(MANGA_URL)
    manga_title = info["title"]
    manga_slug = info["slug"]
    chapters = info["chapters"]

    manga_dir = os.path.join(LIBRARY_DIR, manga_slug)
    os.makedirs(manga_dir, exist_ok=True)

    info_path = os.path.join(manga_dir, "info.json")
    info_data = {
        "title": manga_title,
        "slug": manga_slug,
        "source_url": MANGA_URL,
        "cover": info.get("cover", ""),
        "total_chapters": len(chapters),
        "updated_at": time.time()
    }
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(info_data, f, ensure_ascii=False, indent=2)

    print(f"[+] Tên truyện: {manga_title}")
    print(f"[+] Slug: {manga_slug}")
    print(f"[+] Tổng số chapter: {len(chapters)}")
    print(f"[+] Thư mục: {manga_dir}\n")

    total_ch = len(chapters)
    success_count = 0
    skip_count = 0
    fail_count = 0

    start_total_time = time.time()

    for idx, ch in enumerate(chapters, 1):
        ch_title = ch["title"]
        ch_slug = ch["slug"]
        ch_url = ch["url"]
        ch_dir = os.path.join(manga_dir, ch_slug)

        # Kiểm tra nếu chapter đã tải đủ
        if os.path.exists(ch_dir):
            existing = [f for f in os.listdir(ch_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))]
            if len(existing) >= 10:
                print(f"[{idx:02d}/{total_ch:02d}] ⏩ Bỏ qua {ch_title} ({ch_slug}): Đã có {len(existing)} ảnh.")
                skip_count += 1
                continue

        t0 = time.time()
        print(f"[{idx:02d}/{total_ch:02d}] 🚀 Đang tải {ch_title} ({ch_slug})...")
        try:
            ch_data = detect_and_get_chapter_images(ch_url)
            images = ch_data.get("images", [])
            if not images:
                print(f"    ⚠️ Không tìm thấy ảnh trong {ch_title}!")
                fail_count += 1
                continue

            saved = download_chapter_fast(images, ch_dir, referer=ch_url)
            elapsed = time.time() - t0
            print(f"    ✅ Hoàn tất {ch_title}: {len(saved)} ảnh ({elapsed:.1f}s)")
            success_count += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"    ❌ Lỗi tải {ch_title}: {e}")
            fail_count += 1

    info_data["updated_at"] = time.time()
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(info_data, f, ensure_ascii=False, indent=2)

    total_time = time.time() - start_total_time
    print("=" * 60)
    print("🎉 TỔNG KẾT TIẾN TRÌNH:")
    print(f" - Tải mới thành công: {success_count} chapter")
    print(f" - Đã có sẵn: {skip_count} chapter")
    print(f" - Thất bại: {fail_count} chapter")
    print(f" - Tổng thời gian: {total_time:.1f}s")
    print(f" - Thư mục lưu trữ: data/cubari_library/{manga_slug}/")
    print("=" * 60)

if __name__ == "__main__":
    run()
