import os
import sys
import re
import json
import urllib.request
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

GMT7 = timezone(timedelta(hours=7))
BASE_DIR = r"d:\Nhung\trans-tool"
PROJECT_DIR = os.path.join(BASE_DIR, "novel_projects", "tiến-hành-cứu-rỗi-phản-diện-bi-tình")
CHAPTERS_DIR = os.path.join(PROJECT_DIR, "chapters")
CONFIG_PATH = os.path.join(PROJECT_DIR, "config.json")

os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.52shuku.net/'
}

AD_PATTERNS = [
    r'目录\s*上一页',
    r'上一页\s*下一页',
    r'哦豁[，,]小伙伴们',
    r'传送门[：:]',
    r'Tips[：:]',
    r'如果觉得52',
    r'排行榜单',
    r'52shuku',
    r'52书库'
]

def clean_paragraph_text(raw_text):
    text = raw_text.replace('\xa0', ' ').replace('\u3000', ' ').strip()
    for pat in AD_PATTERNS:
        text = re.split(pat, text)[0].strip()
    return text

def fetch_page(page_num):
    url = f"https://www.52shuku.net/chongsheng/b/bjLCF_{page_num}.html"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            art = soup.find('article', class_='article-content')
            if not art:
                return page_num, []
            paras = []
            for p in art.find_all('p'):
                cleaned = clean_paragraph_text(p.get_text())
                if cleaned:
                    # Tách các dòng con nếu có \n hoặc \r\n trong p
                    sub_lines = [line.strip() for line in cleaned.splitlines() if line.strip()]
                    paras.extend(sub_lines)
            return page_num, paras
    except Exception as e:
        print(f"Error fetching page {page_num}: {e}")
        return page_num, []

def main():
    print("=== BẮT ĐẦU CRAWL RAW ARC 1 (CHƯƠNG 1 - 34) TỪ 52SHUKU ===")
    start_page = 2
    end_page = 75  # Page 76 begins Chapter 35 (Arc 2)

    print(f"1. Tải song song {end_page - start_page + 1} trang (trang {start_page} đến {end_page})...")
    pages_dict = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_page, p): p for p in range(start_page, end_page + 1)}
        for f in as_completed(futures):
            p, paras = f.result()
            pages_dict[p] = paras

    print(f"-> Đã tải xong {len(pages_dict)} trang.")

    # Gom toàn bộ paragraph theo thứ tự trang
    all_lines = []
    for p in range(start_page, end_page + 1):
        lines = pages_dict.get(p, [])
        all_lines.extend(lines)

    print(f"-> Tổng số dòng thô sau lọc quảng cáo: {len(all_lines)}")

    # Tách chương
    chapters = []
    current_ch = None

    # Tìm điểm bắt đầu của Chương 1
    start_idx = 0
    for idx, line in enumerate(all_lines):
        if re.match(r'^第1章\s+', line):
            start_idx = idx
            break

    print(f"-> Điểm bắt đầu Chương 1 tại dòng số {start_idx}")

    for line in all_lines[start_idx:]:
        # Nhận diện tiêu đề chương: "第X章 ..."
        ch_match = re.match(r'^(第[0-9]+章\s*[^\n\r]+)', line)
        if ch_match:
            ch_title = ch_match.group(1).strip()
            ch_num = int(re.search(r'第([0-9]+)章', ch_title).group(1))
            
            if ch_num > 34:
                # Đã sang Arc 2
                break

            current_ch = {
                "chapter_number": ch_num,
                "title": ch_title,
                "paragraphs": []
            }
            chapters.append(current_ch)
        else:
            if current_ch is not None:
                current_ch["paragraphs"].append(line)

    print(f"\n-> Đã bóc tách thành công đầy đủ {len(chapters)}/34 chương của Arc 1:")
    for ch in chapters:
        print(f"   [c{ch['chapter_number']:02d}] {ch['title']} ({len(ch['paragraphs'])} đoạn)")

    # Lưu vào từng thư mục chapters/c<STT>/source.md
    print("\n2. Lưu các chương vào hệ thống chapters/...")
    now_iso = datetime.now(GMT7).isoformat()

    for ch in chapters:
        c_num = ch["chapter_number"]
        ch_dir = os.path.join(CHAPTERS_DIR, f"c{c_num}")
        os.makedirs(ch_dir, exist_ok=True)

        source_path = os.path.join(ch_dir, "source.md")
        meta_path = os.path.join(ch_dir, "meta.json")

        # Nội dung source.md: Header chương + các đoạn phân cách \n\n
        content_lines = [f"# {ch['title']}", ""]
        content_lines.extend(ch["paragraphs"])
        source_content = "\n\n".join(content_lines) + "\n"

        with open(source_path, "w", encoding="utf-8") as f:
            f.write(source_content)

        # Meta.json
        meta_data = {
            "chapter_number": c_num,
            "title_zh": ch["title"],
            "source": "52shuku",
            "source_book_url": "https://www.52shuku.net/chongsheng/b/bjLCF.html",
            "crawled_at": now_iso,
            "total_paragraphs": len(ch["paragraphs"]),
            "total_chars": sum(len(p) for p in ch["paragraphs"]),
            "status": "raw_available"
        }

        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=2)

    # Cập nhật config.json
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            cfg.setdefault("raw_links", {})["52shuku"] = "https://www.52shuku.net/chongsheng/b/bjLCF.html"
            cfg["arc_1_crawled_chapters"] = len(chapters)
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump(cfg, f, ensure_ascii=False, indent=2)
            print("-> Đã cập nhật config.json với số lượng 34 chương Arc 1.")
        except Exception as e:
            print(f"Warning updating config: {e}")

    print("\n=== HOÀN TẤT CRAWL TOÀN BỘ 34/34 CHƯƠNG RAW ARC 1! ===")

if __name__ == '__main__':
    main()
