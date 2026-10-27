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
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'cá-mặn-ký-chủ-tổng-đối-vai-ác-nhất-kiến-chung-tình')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.dmxs.org/cycs/18479.html'
}

AD_PATTERNS = [
    r'请收藏本站：https://www.dmxs.org。耽美小说网手机版：https://m.dmxs.org',
    r'耽美小说网\s*https://www\.dmxs\.org',
    r'https://www\.dmxs\.org',
    r'本站域名.*',
]

def clean_paragraph(raw_text):
    text = html.unescape(raw_text)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('\xa0', ' ').replace('\u3000', ' ').strip()
    for pat in AD_PATTERNS:
        text = re.sub(pat, '', text).strip()
    return text

def fetch_chapter(ch_num):
    url = f'https://www.dmxs.org/view/6-18479-{ch_num}.html'
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                html_str = content.decode('gb18030', errors='ignore')

            # Extract title
            title = f"第{ch_num}章"
            tm = re.search(r'<div class="read_chapterName[^"]*">\s*<h1>(.*?)</h1>', html_str, re.DOTALL)
            if tm:
                raw_t = re.sub(r'<[^>]+>', '', tm.group(1)).strip()
                if raw_t:
                    title = raw_t

            # Extract detail
            cm = re.search(r'<div class="read_chapterDetail">(.*?)</div>', html_str, re.DOTALL)
            if not cm:
                raise ValueError("Could not find read_chapterDetail in page")

            body = cm.group(1)
            raw_paras = re.findall(r'<p>(.*?)</p>', body, re.DOTALL)
            cleaned_paras = []
            for p in raw_paras:
                p_clean = clean_paragraph(p)
                if p_clean:
                    cleaned_paras.append(p_clean)

            return {
                'ch_num': ch_num,
                'title': title,
                'paras': cleaned_paras,
                'url': url
            }
        except Exception as e:
            time.sleep(1)
            if attempt == 3:
                print(f"Error fetching chapter {ch_num} from {url}: {e}")
                return None

def save_chapter(data):
    if not data:
        return False
    ch_num = data['ch_num']
    folder_name = f"c{ch_num}"
    ch_dir = os.path.join(CHAPTERS_DIR, folder_name)
    os.makedirs(ch_dir, exist_ok=True)

    source_path = os.path.join(ch_dir, 'source.md')
    meta_path = os.path.join(ch_dir, 'meta.json')

    # Format source.md with \n\n
    source_content = f"# {data['title']}\n\n" + "\n\n".join(data['paras']) + "\n"
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(source_content)

    meta_data = {
        'chapter': ch_num,
        'title': data['title'],
        'source_url': data['url'],
        'paragraph_count': len(data['paras']),
        'crawled_at': datetime.now(GMT7).isoformat()
    }
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta_data, f, ensure_ascii=False, indent=2)

    print(f"Saved Chapter {ch_num}: {data['title']} ({len(data['paras'])} paragraphs) -> {folder_name}/source.md")
    return True

def main():
    start_ch = 1
    end_ch = 10
    print(f"=== BẮT ĐẦU CRAWL RAW CHƯƠNG {start_ch} ĐẾN {end_ch} TỪ DMXS.ORG ===")
    
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_ch = {executor.submit(fetch_chapter, c): c for c in range(start_ch, end_ch + 1)}
        for future in as_completed(future_to_ch):
            res = future.result()
            if res:
                results.append(res)

    results.sort(key=lambda x: x['ch_num'])
    for item in results:
        save_chapter(item)
    print("=== HOÀN TẤT CRAWL RAW 1-10 ===")

if __name__ == '__main__':
    main()
