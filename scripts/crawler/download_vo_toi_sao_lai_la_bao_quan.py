import sys
import re
import os
import json
import time
from concurrent.futures import ThreadPoolExecutor
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_SLUG = "vợ-tôi-sao-lại-là-bạo-quân-phản-diện"
PROJECT_DIR = os.path.join(BASE_DIR, "novel_projects", PROJECT_SLUG)
CHAPTERS_DIR = os.path.join(PROJECT_DIR, "chapters")
MEMORY_DIR = os.path.join(PROJECT_DIR, "memory")

BASE_URL = 'https://www.52shuku.net/jiakong/01_b/bkfqY_{}.html'
PAGES = list(range(2, 186))

def fetch_page(p):
    url = BASE_URL.format(p)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                soup = BeautifulSoup(html, 'html.parser')
                art = soup.find('article', class_='article-content')
                return p, art.get_text() if art else ''
        except Exception as e:
            time.sleep(1 + attempt)
    return p, ''

def is_noise_line(line):
    s = line.strip()
    if not s:
        return True
    noise_patterns = [
        r'52书库',
        r'www\.52shuku\.net',
        r'52shuku',
        r'小贴士:找看好看得小说',
        r'传送门：排行榜单',
        r'哦豁，小伙伴们如果觉得',
        r'目录\s*上一页',
        r'上一页\s*下一页',
        r'目录\s*下一页',
        r'开始阅读\s*\|\s*阅读记录'
    ]
    for np in noise_patterns:
        if re.search(np, s):
            return True
    return False

def clean_paragraph(p):
    p = p.replace('\xa0', ' ').replace('\u3000', ' ').strip()
    # Normalize multiple spaces inside
    p = re.sub(r' +', ' ', p)
    return p

def main():
    print("=" * 60)
    print("🚀 BẮT ĐẦU CÀO TOÀN BỘ 89 CHƯƠNG CHO DỰ ÁN NOVEL")
    print(f"📖 Tên dự án: {PROJECT_SLUG}")
    print("=" * 60)

    os.makedirs(CHAPTERS_DIR, exist_ok=True)
    os.makedirs(MEMORY_DIR, exist_ok=True)

    print(f"[*] Đang tải {len(PAGES)} trang từ 52shuku...")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_page, PAGES))

    results.sort(key=lambda x: x[0])
    print(f"[+] Hoàn tất tải {len(results)} trang trong {time.time() - start_time:.2f}s")

    # Combine text
    all_lines = []
    for p, text in results:
        lines = text.split('\n')
        for l in lines:
            cleaned = clean_paragraph(l)
            if cleaned and not is_noise_line(cleaned):
                all_lines.append(cleaned)

    # Locate chapter headings
    ch_indices = []
    for idx, line in enumerate(all_lines):
        m = re.match(r'^第(\d+)章\s*(.*)$', line)
        if m:
            ch_num = int(m.group(1))
            ch_title = m.group(2).strip()
            ch_indices.append((ch_num, ch_title, idx))

    print(f"[+] Tìm thấy {len(ch_indices)} tiêu đề chương.")

    # Split into chapters
    chapters = []
    for i in range(len(ch_indices)):
        num, title, start_idx = ch_indices[i]
        end_idx = ch_indices[i+1][2] if i + 1 < len(ch_indices) else len(all_lines)
        ch_paras = all_lines[start_idx:end_idx]
        chapters.append((num, title, ch_paras))

    print(f"[+] Đã chia thành {len(chapters)} chương.")

    # Write each chapter
    for num, title, paras in chapters:
        ch_id = f"ch_{num:03d}"
        ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
        os.makedirs(ch_dir, exist_ok=True)

        source_path = os.path.join(ch_dir, "source.md")
        
        # Ensure header is paras[0]
        # Then each subsequent paragraph separated by \n\n
        content = "\n\n".join(paras)
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(content + "\n")

    print(f"✅ Đã ghi thành công toàn bộ {len(chapters)} chương vào {CHAPTERS_DIR}!")

if __name__ == '__main__':
    main()
