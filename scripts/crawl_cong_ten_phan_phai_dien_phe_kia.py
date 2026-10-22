import urllib.request
from bs4 import BeautifulSoup
import re
import concurrent.futures
import time
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_page(page_num):
    url = f"https://www.52shuku.net/chongsheng/05_b/bkcsX_{page_num}.html"
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            article = soup.find('article')
            if not article:
                return page_num, []
            paras = []
            for p in article.find_all('p'):
                text = p.get_text().replace('\xa0', ' ')
                for line in text.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    if '52shuku' in line.lower() or 'tips：' in line.lower() or '传送门' in line or '如果觉得52' in line or '小贴士' in line or '哦豁' in line or '目录' in line or '上一页' in line or '下一页' in line:
                        continue
                    if '《攻了那个疯批反派[快穿]》作者：' in line or '文案：' in line or '一句话简介：' in line or '立意：' in line:
                        continue
                    paras.append(line)
            return page_num, paras
        except Exception as e:
            time.sleep(1.0 + attempt * 0.5)
    return page_num, []

if __name__ == '__main__':
    TOTAL_PAGES = 296
    print(f"=== BẮT ĐẦU CÀO RAW TOÀN BỘ TRUYỆN: CÔNG TÊN PHẢN PHÁI ĐIÊN PHÊ KIA (PAGES 2 - {TOTAL_PAGES}) ===")
    start_time = time.time()
    pages_data = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        futures = {executor.submit(fetch_page, p): p for p in range(2, TOTAL_PAGES + 1)}
        for future in concurrent.futures.as_completed(futures):
            p_num, p_paras = future.result()
            pages_data[p_num] = p_paras
            if len(pages_data) % 50 == 0 or len(pages_data) == (TOTAL_PAGES - 1):
                print(f"-> Đã tải {len(pages_data)}/{TOTAL_PAGES - 1} trang...")

    print(f"-> Hoàn thành tải {len(pages_data)} trang web trong {time.time() - start_time:.2f}s")

    # Kiểm tra xem có trang nào rỗng không
    empty_pages = [p for p in range(2, TOTAL_PAGES + 1) if not pages_data.get(p)]
    if empty_pages:
        print(f"Cảnh báo: Có {len(empty_pages)} trang rỗng: {empty_pages}. Đang thử tải lại...")
        for p in empty_pages:
            _, paras = fetch_page(p)
            pages_data[p] = paras

    # Gộp tất cả các đoạn theo đúng thứ tự trang
    all_paras = []
    for p in range(2, TOTAL_PAGES + 1):
        all_paras.extend(pages_data.get(p, []))

    print(f"-> Tổng số đoạn trích xuất: {len(all_paras)}")

    # Nhận diện chương
    # Mẫu chương: 第1章, 第 1 章, 第1章 xxx, 番外, 番外一, 番外1...
    chapter_pattern = re.compile(r'^(第\s*(\d+)\s*章(?:\s*.*)?|番外(?:\s*.*)?)')

    # Tìm vị trí bắt đầu của Chapter 1 (bỏ qua phần văn án ở đầu nếu còn)
    start_idx = 0
    for idx, p in enumerate(all_paras):
        if re.match(r'^第\s*1\s*章', p):
            start_idx = idx
            break

    story_paras = all_paras[start_idx:]
    print(f"-> Bắt đầu từ đoạn index {start_idx} (第1章), còn lại {len(story_paras)} đoạn.")

    # Phân tách từng chương
    chapters = {}
    current_ch_num = 0
    current_paras = []
    current_title = ""

    for p in story_paras:
        m = chapter_pattern.match(p)
        if m:
            if current_ch_num > 0 and current_paras:
                chapters[current_ch_num] = {
                    "title": current_title,
                    "paras": current_paras
                }

            header_text = p.strip()
            num_match = re.search(r'第\s*(\d+)\s*章', header_text)
            if num_match:
                current_ch_num = int(num_match.group(1))
            else:
                # Trường hợp phiên ngoại không ghi số chương
                current_ch_num += 1

            current_title = header_text
            current_paras = [p]
            continue

        if current_ch_num > 0:
            current_paras.append(p)

    if current_ch_num > 0 and current_paras:
        chapters[current_ch_num] = {
            "title": current_title,
            "paras": current_paras
        }

    print(f"-> Tổng số chương nhận diện được: {len(chapters)}")
    sorted_ch_nums = sorted(chapters.keys())
    print(f"-> Chương đầu: {sorted_ch_nums[0]}, Chương cuối: {sorted_ch_nums[-1]}")

    # Kiểm tra tính liên tục của các chương
    missing_chs = []
    for expected in range(1, sorted_ch_nums[-1] + 1):
        if expected not in chapters:
            missing_chs.append(expected)

    if missing_chs:
        print(f"Cảnh báo: Thiếu các số chương: {missing_chs}")
    else:
        print(f"-> Tuyệt vời: Toàn bộ các chương từ 1 đến {sorted_ch_nums[-1]} liên tục 100% không bị ngắt quãng!")

    # Lưu vào novel_projects/công-tên-phản-phái-điên-phê-kia/chapters
    base_dir = r"novel_projects\công-tên-phản-phái-điên-phê-kia\chapters"
    os.makedirs(base_dir, exist_ok=True)

    saved_count = 0
    new_raw_count = 0
    for ch_num in sorted_ch_nums:
        ch_slug = f"ch_{ch_num:03d}"
        ch_dir = os.path.join(base_dir, ch_slug)
        os.makedirs(ch_dir, exist_ok=True)
        source_path = os.path.join(ch_dir, "source.md")
        meta_path = os.path.join(ch_dir, "meta.json")

        paras = chapters[ch_num]["paras"]
        content = "\n\n".join(paras)

        # Lưu source.md
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Cập nhật hoặc tạo meta.json
        if os.path.exists(meta_path):
            try:
                with open(meta_path, "r", encoding="utf-8") as mf:
                    meta_data = json.load(mf)
            except Exception:
                meta_data = {}
        else:
            meta_data = {}

        # Nếu chưa có status hoặc status là raw_imported, thiết lập thông tin
        if not meta_data.get("status"):
            meta_data["chapter_id"] = ch_slug
            meta_data["title"] = f"Chương {ch_num}"
            meta_data["paragraph_count"] = len(paras)
            meta_data["word_count"] = sum(len(p) for p in paras)
            meta_data["status"] = "raw_imported"
            meta_data["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S+07:00")
            new_raw_count += 1
            with open(meta_path, "w", encoding="utf-8") as mf:
                json.dump(meta_data, mf, ensure_ascii=False, indent=2)
        else:
            # Nếu đã có status (như 'translated' ở ch_001 - ch_010), bảo toàn status và cập nhật paragraph_count nếu cần
            meta_data["paragraph_count"] = len(paras)
            with open(meta_path, "w", encoding="utf-8") as mf:
                json.dump(meta_data, mf, ensure_ascii=False, indent=2)

        saved_count += 1

    print(f"-> Đã lưu thành công {saved_count} chương vào {base_dir}")
    print(f"-> Trong đó có {new_raw_count} chương raw mới được khởi tạo meta.json.")

    # Cập nhật config.json
    config_path = r"novel_projects\công-tên-phản-phái-điên-phê-kia\config.json"
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        config["chapters_count"] = len(chapters)
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        print(f"-> Đã cập nhật config.json với chapters_count = {len(chapters)}")

    print("=== HOÀN TẤT THU THẬP VÀ LƯU TOÀN BỘ RAW ===")
