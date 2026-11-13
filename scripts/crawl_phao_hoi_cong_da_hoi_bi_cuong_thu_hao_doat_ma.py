import os
import sys
import re
import json
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'pháo-hôi-công-dã-hội-bị-cường-thủ-hào-đoạt-ma')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
TOC_PATH = os.path.join(PROJECT_DIR, 'TOC.md')
INDEX_PATH = os.path.join(PROJECT_DIR, 'chapters_index.json')

os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_para(raw):
    raw = raw.replace('\xa0', ' ')
    raw = re.split(r'目录\s+上一页', raw)[0]
    raw = re.split(r'哦豁[，,]小伙伴们', raw)[0]
    raw = re.split(r'传送门[：:]', raw)[0]
    raw = re.split(r'Tips[：:]', raw)[0]
    lines = []
    for l in raw.splitlines():
        l = l.strip()
        if l and '52书库' not in l and '传送门' not in l and 'Tips' not in l and not l.startswith('目录'):
            lines.append(l)
    return lines

def fetch_page(p):
    url = f'https://www.52shuku.net/chongsheng/07_b/bkdb1_{p}.html'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as r:
            soup = BeautifulSoup(r.read().decode('utf-8', errors='ignore'), 'html.parser')
            art = soup.find('article', class_='article-content')
            paras = []
            if art:
                for pt in art.find_all('p'):
                    paras.extend(clean_para(pt.get_text()))
            return p, paras
    except Exception as e:
        print(f"Error fetching page {p}: {e}")
        return p, []

def main():
    print("=== Đang cào toàn bộ 180 trang từ 52shuku ===")
    with ThreadPoolExecutor(max_workers=15) as ex:
        pages_dict = dict(ex.map(fetch_page, range(2, 181)))

    print("=== Tổng hợp toàn bộ dòng văn bản ===")
    all_lines = []
    for p in range(2, 181):
        for line in pages_dict.get(p, []):
            all_lines.append((p, line))

    print(f"Tổng số dòng thu được: {len(all_lines)}")

    # Nhận diện vị trí các chương
    chapters = []
    current_ch = None

    heading_regex = re.compile(r'^第\s*(\d+)\s*章\s*(.*)$')

    for p, line in all_lines:
        m = heading_regex.match(line)
        if m:
            ch_num = int(m.group(1))
            ch_title = m.group(2).strip()
            if current_ch:
                chapters.append(current_ch)
            current_ch = {
                'number': ch_num,
                'title': ch_title,
                'raw_heading': line,
                'start_page': p,
                'paragraphs': []
            }
        else:
            if current_ch:
                # Bỏ qua dòng giới thiệu đầu sách nếu còn sót
                if '《炮灰攻也会被强取豪夺吗？》' in line or line.startswith('简介：') or '主攻单元文' in line:
                    continue
                current_ch['paragraphs'].append(line)

    if current_ch:
        chapters.append(current_ch)

    print(f"=== Đã bóc tách thành công {len(chapters)} chương! ===")

    chapters_index_data = []
    toc_lines = [
        "# MỤC LỤC: PHÁO HÔI CÔNG DÃ HỘI BỊ CƯỜNG THỦ HÀO ĐOẠT MA",
        "",
        "- **Tác giả:** Mộng Lí Hoàn Hoa Bái (梦里还花呗)",
        "- **Thể loại:** Đam mỹ, Xuyên thư, Khoái xuyên / Đơn nguyên văn, Chủ công, Cường thủ hào đoạt, Cưỡng chế ái, Điên phê thụ, 1v1, HE.",
        f"- **Tổng số chương:** {len(chapters)} chương (Bao gồm chính văn + ngoại truyện)",
        "",
        "---",
        "",
        "### Danh sách chương raw đã nạp:",
        ""
    ]

    for ch in chapters:
        ch_num = ch['number']
        ch_title = ch['title']
        ch_id = f"ch_{ch_num:03d}"
        ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
        os.makedirs(ch_dir, exist_ok=True)

        source_file = os.path.join(ch_dir, 'source.md')

        content_parts = [
            f"# 第 {ch_num} 章 {ch_title}".strip(),
            ""
        ]
        content_parts.extend(ch['paragraphs'])

        with open(source_file, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(content_parts).strip() + "\n")

        # Lưu metadata chương
        chapters_index_data.append({
            "chapter_id": ch_id,
            "chapter_number": ch_num,
            "title": ch_title,
            "start_page": ch['start_page'],
            "paragraphs_count": len(ch['paragraphs']),
            "has_source": True,
            "has_translation": False
        })

        toc_lines.append(f"- [ ] [**Chương {ch_num}:** {ch_title}](chapters/{ch_id}/source.md) ({len(ch['paragraphs'])} đoạn)")

    # Ghi chapters_index.json
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(chapters_index_data, f, ensure_ascii=False, indent=2)

    # Ghi TOC.md
    with open(TOC_PATH, 'w', encoding='utf-8') as f:
        f.write("\n".join(toc_lines) + "\n")

    print(f"=== Đã lưu xong 100% {len(chapters)} chương vào {CHAPTERS_DIR}! ===")

if __name__ == '__main__':
    main()
