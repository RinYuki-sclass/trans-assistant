import os
import sys
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from crawler.general_crawler import detect_and_get_manga_info, detect_and_get_chapter_images
from crawler.haccbl_crawler import download_chapter_images

DATA_DIR = os.path.join(BASE_DIR, "data")
LIBRARY_DIR = os.path.join(DATA_DIR, "cubari_library")

CO_VUONG_URL = "https://truyentranhdammyy.site/manga/co-vuong-tai-ha/"

def download_co_vuong(max_chapters: int = 10):
    """
    Tải các chapter của bộ Cô Vương Tại Hạ vào Cubari Library
    """
    sys.stdout.reconfigure(encoding='utf-8')
    print("=" * 60)
    print("📥 BẮT ĐẦU TẢI TRUYỆN: CÔ VƯƠNG TẠI HẠ")
    print("=" * 60)

    # 1. Bóc tách thông tin truyện
    print(f"[*] Đang kết nối và lấy danh sách chapter từ {CO_VUONG_URL}...")
    info = detect_and_get_manga_info(CO_VUONG_URL)
    manga_title = info["title"]
    manga_slug = "co-vuong-tai-ha"
    chapters = info["chapters"]

    manga_dir = os.path.join(LIBRARY_DIR, manga_slug)
    os.makedirs(manga_dir, exist_ok=True)

    # Lưu file info.json cho manga
    info_path = os.path.join(manga_dir, "info.json")
    info_data = {
        "title": manga_title,
        "slug": manga_slug,
        "source_url": CO_VUONG_URL,
        "cover": info.get("cover", ""),
        "total_chapters": len(chapters),
        "updated_at": time.time()
    }
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(info_data, f, ensure_ascii=False, indent=2)

    print(f"[+] Tên truyện: {manga_title}")
    print(f"[+] Tổng số chapter tìm thấy: {len(chapters)}")
    print(f"[+] Thư mục: {manga_dir}\n")

    # 2. Tải các chapter
    targets = chapters[:max_chapters] if max_chapters > 0 else chapters
    total_target = len(targets)
    success = 0

    for idx, ch in enumerate(targets, 1):
        ch_title = ch["title"]
        ch_slug = ch["slug"]
        ch_url = ch["url"]
        ch_dir = os.path.join(manga_dir, ch_slug)

        # Kiểm tra nếu đã có ảnh
        if os.path.exists(ch_dir):
            existing = [f for f in os.listdir(ch_dir) if f.lower().endswith(('.jpg', '.png', '.webp', '.avif'))]
            if len(existing) >= 4:
                print(f"[{idx}/{total_target}] ⏩ Đã có sẵn {ch_title} ({len(existing)} ảnh). Bỏ qua.")
                success += 1
                continue

        os.makedirs(ch_dir, exist_ok=True)
        print(f"[{idx}/{total_target}] 🚀 Đang tải {ch_title}...")

        try:
            ch_data = detect_and_get_chapter_images(ch_url)
            images = ch_data.get("images", [])
            if not images:
                print(f"    ⚠️ Không tìm thấy ảnh trong {ch_title}!")
                continue

            print(f"    -> Tìm thấy {len(images)} ảnh. Đang tối ưu...")
            saved = download_chapter_images(images, ch_dir, referer=ch_url)
            print(f"    ✅ Hoàn tất {ch_title}: Lưu {len(saved)} ảnh vào {ch_slug}/\n")
            success += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"    ❌ Lỗi tải {ch_title}: {e}\n")

    print(f"🎉 Đã hoàn tất {success}/{total_target} chapters.")

if __name__ == "__main__":
    max_c = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    download_co_vuong(max_chapters=max_c)
