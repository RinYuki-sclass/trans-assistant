import os
import sys
import re
import json
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'cong-lieu-na-ca-truc-nam-long-ngao-thien')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
TOC_PATH = os.path.join(PROJECT_DIR, 'TOC.md')
INDEX_PATH = os.path.join(PROJECT_DIR, 'chapters_index.json')
CONFIG_PATH = os.path.join(PROJECT_DIR, 'config.json')

os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

CN_NUM = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}

def cn2int(s):
    s = s.strip()
    if s.isdigit():
        return int(s)
    if len(s) == 1:
        return CN_NUM.get(s, 0)
    if len(s) == 2:
        if s[0] == '十':
            return 10 + CN_NUM.get(s[1], 0)
        elif s[1] == '十':
            return CN_NUM.get(s[0], 0) * 10
    if len(s) == 3 and s[1] == '十':
        return CN_NUM.get(s[0], 0) * 10 + CN_NUM.get(s[2], 0)
    try:
        return int(s)
    except Exception:
        return 0

def clean_para(raw):
    raw = raw.replace('\xa0', ' ').replace('\u3000', ' ')
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
    url = f'https://www.52shuku.net/jiakong/25_b/bkcPn_{p}.html' if p > 1 else 'https://www.52shuku.net/jiakong/25_b/bkcPn.html'
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
    max_pages = 166
    print(f"=== Đang cào toàn bộ {max_pages} trang từ 52shuku cho 'Công Liễu Na Cá Trực Nam Long Ngạo Thiên' ===")
    with ThreadPoolExecutor(max_workers=16) as ex:
        pages_dict = dict(ex.map(fetch_page, range(2, max_pages + 1)))

    print("=== Tổng hợp toàn bộ dòng văn bản theo thứ tự trang ===")
    all_lines = []
    for p in range(2, max_pages + 1):
        for line in pages_dict.get(p, []):
            all_lines.append((p, line))

    print(f"Tổng số dòng thu được: {len(all_lines)}")

    # Nhận diện vị trí các chương
    chapters = []
    current_ch = None
    heading_regex = re.compile(r'^(第[0-9一二三四五六七八九十百]+章|番外[一二三四五六七八九十0-9]*)\s*(.*)$')

    for p, line in all_lines:
        m = heading_regex.match(line)
        if m:
            raw_h = m.group(1)
            ch_title = m.group(2).strip()
            num_match = re.search(r'\d+', raw_h)
            if num_match:
                ch_num = int(num_match.group(0))
            else:
                cn_match = re.search(r'[一二三四五六七八九十百]+', raw_h)
                ch_num = cn2int(cn_match.group(0)) if cn_match else len(chapters) + 1

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
                if '《攻了那个直男龙傲天》' in line or line.startswith('小说简介：') or '作者：风流客' in line:
                    continue
                current_ch['paragraphs'].append(line)

    if current_ch:
        chapters.append(current_ch)

    print(f"=== Đã bóc tách thành công {len(chapters)} chương! ===")

    chapters_index_data = []
    toc_lines = [
        "# MỤC LỤC: Công Liễu Na Cá Trực Nam Long Ngạo Thiên (攻了那个直男龙傲天)",
        "",
        "- **Tác giả:** Phong Lưu Khách (风流客)",
        "- **Thể loại:** Đam mỹ, Chủ công, Xuyên thư, Tiên hiệp, Tu chân, Cường cường, Trọng sinh, Hài hước, 1v1, HE.",
        f"- **Tổng số chương:** {len(chapters)} chương (Đã cào đủ toàn bộ)",
        "",
        "---",
        "",
        "### Danh sách chương raw đã nạp:",
        ""
    ]

    raw_full_content = []

    for idx, ch in enumerate(chapters, start=1):
        ch_id = f"ch_{idx:03d}"
        ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
        os.makedirs(ch_dir, exist_ok=True)

        source_file = os.path.join(ch_dir, 'source.md')
        full_ch_text = f"{ch['raw_heading']}\n\n" + "\n\n".join(ch['paragraphs'])

        with open(source_file, 'w', encoding='utf-8') as f:
            f.write(full_ch_text + "\n")

        raw_full_content.append(full_ch_text)

        chapters_index_data.append({
            'chapter_id': ch_id,
            'chapter_number': idx,
            'title': ch['title'] or ch['raw_heading'],
            'start_page': ch['start_page'],
            'paragraphs_count': len(ch['paragraphs']),
            'has_source': True,
            'has_translation': False,
            'status': 'raw_ready'
        })

        toc_lines.append(f"- **Chương {idx}:** {ch['raw_heading']} (Trang {ch['start_page']}) | *{len(ch['paragraphs'])} đoạn*")

    # Ghi chapters_index.json
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(chapters_index_data, f, ensure_ascii=False, indent=2)

    # Ghi TOC.md
    with open(TOC_PATH, 'w', encoding='utf-8') as f:
        f.write("\n".join(toc_lines) + "\n")

    # Ghi raw_full.md
    with open(os.path.join(PROJECT_DIR, 'raw_full.md'), 'w', encoding='utf-8') as f:
        f.write("\n\n---\n\n".join(raw_full_content) + "\n")

    # Cập nhật config.json
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        cfg['chapters_count'] = len(chapters)
        cfg['status'] = 'raw_ready'
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)

    print(f"HOÀN TẤT: Đã ghi {len(chapters)} chương vào {CHAPTERS_DIR}")

if __name__ == '__main__':
    main()
