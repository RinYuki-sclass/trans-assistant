import os
import sys
import re
import json
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'long-ngao-thien-tang-vi-phan-phai-dan-ha-nhat-tu')
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
    url = f'https://www.52shuku.net/jiakong/11_b/bkfRt_{p}.html'
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
    print("=== Đang cào toàn bộ 114 trang nội dung (trang 2 -> 115) từ 52shuku ===")
    with ThreadPoolExecutor(max_workers=12) as ex:
        pages_dict = dict(ex.map(fetch_page, range(2, 116)))

    print("=== Tổng hợp toàn bộ dòng văn bản theo thứ tự trang ===")
    all_lines = []
    for p in range(2, 116):
        for line in pages_dict.get(p, []):
            all_lines.append((p, line))

    print(f"Tổng số dòng thu được: {len(all_lines)}")

    # Nhận diện vị trí các chương
    chapters = []
    current_ch = None
    heading_regex = re.compile(r'^第([0-9一二三四五六七八九十百]+)章\s*(.*)$')

    for p, line in all_lines:
        m = heading_regex.match(line)
        if m:
            ch_num = cn2int(m.group(1))
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
                if '《龙傲天曾为反派诞下一子》' in line or line.startswith('简介：'):
                    continue
                current_ch['paragraphs'].append(line)

    if current_ch:
        chapters.append(current_ch)

    print(f"=== Đã bóc tách thành công {len(chapters)} chương! ===")

    chapters_index_data = []
    toc_lines = [
        "# MỤC LỤC: Long Ngạo Thiên Tằng Vi Phản Phái Đản Hạ Nhất Tử (龙傲天曾为反派诞下一子)",
        "",
        "- **Tác giả:** Phong Lưu Khách (风流客)",
        "- **Thể loại:** Đam mỹ, Chủ công, Tiên hiệp, Tu chân, Xuyên thư, Sinh tử, Phá kính trùng viên, Hài hước, HE.",
        f"- **Tổng số chương:** {len(chapters)} chương (Hoàn thành chính văn)",
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
        meta_file = os.path.join(ch_dir, 'meta.json')

        content_parts = [
            f"# 第 {ch_num} 章 {ch_title}".strip(),
            ""
        ]
        content_parts.extend(ch['paragraphs'])

        full_source_text = "\n\n".join(content_parts).strip() + "\n"
        with open(source_file, 'w', encoding='utf-8') as f:
            f.write(full_source_text)

        source_word_count = sum(len(p) for p in ch['paragraphs'])
        
        meta_data = {
            "chapter": ch_num,
            "title": f"Chương {ch_num}: {ch_title}" if ch_title else f"Chương {ch_num}",
            "raw_title": ch['raw_heading'],
            "source_word_count": source_word_count,
            "paragraphs_count": len(ch['paragraphs']),
            "status": "pending",
            "has_translation": False
        }
        with open(meta_file, 'w', encoding='utf-8') as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=2)

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

    # Cập nhật config.json
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                cfg = json.load(f)
            cfg['chapters_count'] = len(chapters)
            cfg['raw_links']['jjwxc'] = "https://www.jjwxc.net/onebook.php?novelid=10282492"
            cfg['raw_links']['52shuku'] = "https://www.52shuku.net/jiakong/11_b/bkfRt.html"
            with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
                json.dump(cfg, f, ensure_ascii=False, indent=2)
            print("Đã cập nhật config.json thành công!")
        except Exception as e:
            print(f"Lỗi cập nhật config.json: {e}")

    print(f"=== ĐÃ NẠP TOÀN BỘ {len(chapters)} CHƯƠNG RAW THÀNH CÔNG VÀO {CHAPTERS_DIR}! ===")

if __name__ == '__main__':
    main()
