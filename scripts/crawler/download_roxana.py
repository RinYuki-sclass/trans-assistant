import os
import sys
import json
import time

# Đường dẫn hệ thống
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from crawler.general_crawler import detect_and_get_manga_info, detect_and_get_chapter_images
from crawler.haccbl_crawler import download_chapter_images

DATA_DIR = os.path.join(BASE_DIR, "data")
LIBRARY_DIR = os.path.join(DATA_DIR, "cubari_library")

ROXANA_URL = "https://tsxx4.online/truyen-tranh/roxana-phuong-phap-bao-ve-anh-trai-cua-nu-chinh/"

def download_all_roxana_chapters():
    """Tải toàn bộ các chapter của bộ Roxana về thư viện Cubari Library"""
    print("=" * 60)
    print("📥 BẮT ĐẦU TẢI TRUYỆN: ROXANA: PHƯƠNG PHÁP BẢO VỆ ANH TRAI CỦA NỮ CHÍNH")
    print("=" * 60)

    # 1. Bóc tách thông tin truyện
    print(f"[*] Đang kết nối và lấy danh sách chapter từ {ROXANA_URL}...")
    info = detect_and_get_manga_info(ROXANA_URL)
    manga_title = info["title"]
    manga_slug = info["slug"]
    chapters = info["chapters"]

    manga_dir = os.path.join(LIBRARY_DIR, manga_slug)
    os.makedirs(manga_dir, exist_ok=True)

    # Lưu file info.json cho manga
    info_path = os.path.join(manga_dir, "info.json")
    info_data = {
        "title": manga_title,
        "slug": manga_slug,
        "source_url": ROXANA_URL,
        "cover": info.get("cover", ""),
        "total_chapters": len(chapters),
        "updated_at": time.time()
    }
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(info_data, f, ensure_ascii=False, indent=2)

    print(f"[+] Tên truyện: {manga_title}")
    print(f"[+] Tổng số chapter tìm thấy: {len(chapters)}")
    print(f"[+] Lưu trữ tại: {manga_dir}\n")

    # 2. Tải từng chapter
    total_ch = len(chapters)
    success_count = 0
    skip_count = 0
    fail_count = 0

    for idx, ch in enumerate(chapters, 1):
        ch_title = ch["title"]
        ch_slug = ch["slug"]
        ch_url = ch["url"]
        ch_dir = os.path.join(manga_dir, ch_slug)

        # Kiểm tra nếu đã tải trước đó
        if os.path.exists(ch_dir):
            existing_imgs = [
                f for f in os.listdir(ch_dir)
                if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))
            ]
            if len(existing_imgs) >= 10:
                print(f"[{idx}/{total_ch}] ⏩ Bỏ qua {ch_title} ({ch_slug}): Đã có {len(existing_imgs)} ảnh.")
                skip_count += 1
                continue

        os.makedirs(ch_dir, exist_ok=True)
        print(f"[{idx}/{total_ch}] 🚀 Đang tải {ch_title} ({ch_url})...")

        try:
            ch_data = detect_and_get_chapter_images(ch_url)
            images = ch_data.get("images", [])

            if not images:
                print(f"    ⚠️ Không tìm thấy ảnh trong {ch_title}!")
                fail_count += 1
                continue

            print(f"    -> Tìm thấy {len(images)} ảnh. Đang lưu ảnh tối ưu...")

            def on_progress(cur, tot, fn):
                if cur % 5 == 0 or cur == tot:
                    print(f"       [{cur}/{tot}] Lưu: {fn}")

            saved = download_chapter_images(images, ch_dir, referer=ch_url, progress_callback=on_progress)
            print(f"    ✅ Hoàn tất {ch_title}: Đã lưu {len(saved)} ảnh vào {ch_slug}/\n")
            success_count += 1
            time.sleep(1)  # Giãn cách nhẹ tránh tải dồn dập
        except Exception as e:
            print(f"    ❌ Lỗi tải {ch_title}: {e}\n")
            fail_count += 1

    # Cập nhật thời gian update trong info.json
    info_data["updated_at"] = time.time()
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(info_data, f, ensure_ascii=False, indent=2)

    print("=" * 60)
    print("🎉 TỔNG KẾT TIẾN TRÌNH TẢI:")
    print(f" - Tải mới thành công: {success_count} chapter")
    print(f" - Đã có sẵn (bỏ qua): {skip_count} chapter")
    print(f" - Thất bại / Lỗi: {fail_count} chapter")
    print(f" - Thư viện đã sẵn sàng tại: data/cubari_library/{manga_slug}/")
    print("=" * 60)

if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    download_all_roxana_chapters()
