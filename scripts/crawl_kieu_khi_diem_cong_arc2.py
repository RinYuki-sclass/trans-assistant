import urllib.request
import re
import html
import time
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')

GMT7 = timezone(timedelta(hours=7))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'kieu-khi-diem-cong-luon-bi-phan-dien-nham-vao')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.dmxs.org/cycs/14206.html'
}

AD_PATTERNS = [
    r'请收藏本站：https://www\.dmxs\.org。耽美小说网手机版：https://m\.dmxs\.org',
    r'耽美小说网\s*https://www\.dmxs\.org',
    r'https://www\.dmxs\.org',
    r'本站域名.*',
    r'（本章完）'
]

def clean_paragraph(raw_text):
    text = html.unescape(raw_text)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('\xa0', ' ').replace('\u3000', ' ').strip()
    for pat in AD_PATTERNS:
        text = re.sub(pat, '', text).strip()
    return text

def fetch_page(idx):
    url = f'https://www.dmxs.org/view/6-14206-{idx}.html'
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                html_str = content.decode('gb18030', errors='ignore')

            title = f"第{idx}章"
            tm = re.search(r'<div class="read_chapterName[^"]*">\s*<h1>(.*?)</h1>', html_str, re.DOTALL)
            if tm:
                raw_t = re.sub(r'<[^>]+>', '', tm.group(1)).strip()
                if raw_t:
                    title = raw_t

            cm = re.search(r'<div class="read_chapterDetail">(.*?)</div>', html_str, re.DOTALL)
            if not cm:
                raise ValueError("Could not find read_chapterDetail in page")

            body = cm.group(1)
            raw_paras = re.findall(r'<p>(.*?)</p>', body, re.DOTALL)
            cleaned_paras = [clean_paragraph(p) for p in raw_paras if clean_paragraph(p)]

            return {
                'page_idx': idx,
                'title': title,
                'paras': cleaned_paras,
                'url': url
            }
        except Exception as e:
            time.sleep(1)
            if attempt == 3:
                print(f"Error fetching page {idx} from {url}: {e}")
                return None

def main():
    start_page = 79
    end_page = 144
    print(f"=== BẮT ĐẦU CRAWL RAW THẾ GIỚI 2 (ABO) TỪ TRANG {start_page} ĐẾN {end_page} ===")
    
    pages = {}
    with ThreadPoolExecutor(max_workers=8) as executor:
        futs = {executor.submit(fetch_page, p): p for p in range(start_page, end_page + 1)}
        for f in as_completed(futs):
            res = f.result()
            if res:
                pages[res['page_idx']] = res

    print(f"Đã tải thành công {len(pages)}/{end_page - start_page + 1} trang.")

    # Combine all paragraphs in page order
    all_paras = []
    page_records = []
    for p in range(start_page, end_page + 1):
        if p in pages:
            data = pages[p]
            all_paras.extend(data['paras'])
            page_records.append(data)

    print(f"Tổng số đoạn văn thô thu thập được: {len(all_paras)}")

    # Save a complete combined file for Arc 2
    raw_arc2_path = os.path.join(PROJECT_DIR, 'raw_arc2_abo_full.md')
    with open(raw_arc2_path, 'w', encoding='utf-8') as f:
        f.write("# Thế Giới 2: ABO - 娇气甜攻总被反派盯上[快穿] (Raw Toàn Bộ Arc 2)\n\n")
        for data in page_records:
            f.write(f"## {data['title']} (Trang {data['page_idx']})\n\n")
            f.write("\n\n".join(data['paras']) + "\n\n")

    print(f"Đã lưu toàn bộ raw Arc 2 tại: {raw_arc2_path}")

    # Also save individual chapter/page folders in chapters/
    for i, data in enumerate(page_records, start=1):
        ch_folder = os.path.join(CHAPTERS_DIR, f"p{data['page_idx']}")
        os.makedirs(ch_folder, exist_ok=True)
        
        source_content = f"# {data['title']}\n\n" + "\n\n".join(data['paras']) + "\n"
        with open(os.path.join(ch_folder, 'source.md'), 'w', encoding='utf-8') as f:
            f.write(source_content)
            
        meta = {
            'page': data['page_idx'],
            'arc': 2,
            'arc_name': 'ABO',
            'title': data['title'],
            'paragraph_count': len(data['paras']),
            'source_url': data['url'],
            'crawled_at': datetime.now(GMT7).isoformat()
        }
        with open(os.path.join(ch_folder, 'meta.json'), 'w', encoding='utf-8') as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"Đã tạo {len(page_records)} thư mục trang trong {CHAPTERS_DIR}")

if __name__ == '__main__':
    main()
