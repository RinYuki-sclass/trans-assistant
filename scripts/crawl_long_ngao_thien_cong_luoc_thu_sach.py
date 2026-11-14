import os
import sys
import re
import json
import urllib.request
import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'long-ngao-thien-cong-luoc-thu-sach')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
TOC_PATH = os.path.join(PROJECT_DIR, 'TOC.md')
INDEX_PATH = os.path.join(PROJECT_DIR, 'chapters_index.json')
CONFIG_PATH = os.path.join(PROJECT_DIR, 'config.json')

os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_subpage(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode('utf-8', errors='ignore')
        soup = BeautifulSoup(html, 'html.parser')
        p_tags = [p.get_text().strip() for p in soup.find_all('p') if p.get_text().strip()]
        
        # Check next subpage link
        next_subpage = None
        for a in soup.find_all('a'):
            if a.get_text().strip() == '下一页':
                href = a.get('href', '')
                if href and href.endswith('.html') and ('_' in href.split('/')[-1]):
                    next_subpage = 'https://www.shibashuwu.net' + href if href.startswith('/') else href
                    break
        return p_tags, next_subpage
    except Exception as e:
        print(f"Error fetching subpage {url}: {e}")
        return [], None

def fetch_full_chapter(ch_info):
    ch_idx, title, start_url = ch_info
    all_paras = []
    current_url = start_url
    visited = set()

    while current_url and current_url not in visited:
        visited.add(current_url)
        paras, next_url = fetch_subpage(current_url)
        all_paras.extend(paras)
        current_url = next_url

    return {
        'idx': ch_idx,
        'title': title,
        'url': start_url,
        'paragraphs': all_paras
    }

def main():
    print("=== Đang lấy danh mục chương từ shibashuwu cho 'Long Ngạo Thiên Công Lược Thủ Sách' ===")
    ch_urls = []
    for cat_p in [1, 2]:
        cat_url = f'https://www.shibashuwu.net/book/52845/catalog/{cat_p}.html'
        try:
            req = urllib.request.Request(cat_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as r:
                soup = BeautifulSoup(r.read().decode('utf-8', errors='ignore'), 'html.parser')
            for a in soup.find_all('a'):
                href = a.get('href', '')
                if '/book/52845/' in href and href.endswith('.html') and 'catalog' not in href:
                    t = a.get_text().strip()
                    if t and '更新说明' not in t:
                        full_u = 'https://www.shibashuwu.net' + href if href.startswith('/') else href
                        if full_u not in [u[1] for u in ch_urls]:
                            ch_urls.append((t, full_u))
        except Exception as e:
            print(f"Error fetching catalog {cat_p}: {e}")

    print(f"Tổng số chương tìm thấy: {len(ch_urls)}")

    tasks = [(idx, t, u) for idx, (t, u) in enumerate(ch_urls, start=1)]

    print(f"=== Đang tải toàn bộ {len(tasks)} chương (song song) ===")
    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(fetch_full_chapter, tasks))

    results.sort(key=lambda x: x['idx'])

    chapters_index_data = []
    toc_lines = [
        "# MỤC LỤC: Long Ngạo Thiên Công Lược Thủ Sách (龙傲天攻略手册)",
        "",
        "- **Tác giả:** Mỹ Cường Ái Hảo Giả (美强爱好者)",
        "- **Thể loại:** Đam mỹ, Chủ công, Xuyên thư, Tiên hiệp, Sư huynh đệ, Sinh tử, Hải Đường, Cao H, 1v1, HE.",
        f"- **Tổng số chương:** {len(results)} chương (Đã cào đủ toàn bộ)",
        "",
        "---",
        "",
        "### Danh sách chương raw đã nạp:",
        ""
    ]

    raw_full_content = []

    for item in results:
        idx = item['idx']
        ch_id = f"ch_{idx:03d}"
        ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
        os.makedirs(ch_dir, exist_ok=True)

        source_file = os.path.join(ch_dir, 'source.md')
        heading = f"第{idx}章 {item['title']}"
        full_ch_text = f"{heading}\n\n" + "\n\n".join(item['paragraphs'])

        with open(source_file, 'w', encoding='utf-8') as f:
            f.write(full_ch_text + "\n")

        raw_full_content.append(full_ch_text)

        chapters_index_data.append({
            'chapter_id': ch_id,
            'chapter_number': idx,
            'title': item['title'],
            'paragraphs_count': len(item['paragraphs']),
            'has_source': True,
            'has_translation': False,
            'status': 'raw_ready'
        })

        toc_lines.append(f"- **Chương {idx}:** {item['title']} | *{len(item['paragraphs'])} đoạn*")

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
        cfg['chapters_count'] = len(results)
        cfg['status'] = 'raw_ready'
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)

    print(f"HOÀN TẤT: Đã ghi thành công {len(results)} chương vào {CHAPTERS_DIR}")

if __name__ == '__main__':
    main()
