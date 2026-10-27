import urllib.request
import re
import html
import os
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://www.dmxs.org/cycs/18479.html'
}

AD_PATTERNS = [
    r'请收藏本站：https://www\.dmxs\.org。耽美小说网手机版：https://m\.dmxs\.org',
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

def fetch_page(p_num):
    url = f'https://www.dmxs.org/view/6-18479-{p_num}.html'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            html_str = content.decode('gb18030', errors='ignore')
        cm = re.search(r'<div class="read_chapterDetail">(.*?)</div>', html_str, re.DOTALL)
        if not cm:
            return p_num, []
        raw_paras = re.findall(r'<p>(.*?)</p>', cm.group(1), re.DOTALL)
        paras = [clean_paragraph(p) for p in raw_paras if clean_paragraph(p)]
        return p_num, paras
    except Exception as e:
        print(f'Error page {p_num}: {e}')
        return p_num, []

def main():
    print('Fetching pages 10 to 25 from dmxs.org...')
    pages = {}
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs = {ex.submit(fetch_page, p): p for p in range(10, 26)}
        for f in as_completed(futs):
            p_num, paras = f.result()
            pages[p_num] = paras

    all_paras = []
    for p in range(10, 26):
        all_paras.extend(pages.get(p, []))

    print('Total paragraphs fetched from pages 10-25:', len(all_paras))

    ch_indices = []
    for idx, p in enumerate(all_paras):
        m = re.match(r'^(#+\s*)?第\s*0*([0-9]+)\s*章', p)
        if m:
            ch_num = int(m.group(2))
            ch_indices.append((ch_num, idx, p))

    print('Found chapter headers:')
    for c in ch_indices:
        print(f'  Chapter {c[0]} at index {c[1]}: {c[2]}')

    chapters_dir = 'novel_projects/cá-mặn-ký-chủ-tổng-đối-vai-ác-nhất-kiến-chung-tình/chapters'
    for i in range(len(ch_indices)):
        ch_num, start_idx, header = ch_indices[i]
        if ch_num < 11 or ch_num > 20:
            continue
        end_idx = ch_indices[i+1][1] if i+1 < len(ch_indices) else len(all_paras)
        ch_paras = all_paras[start_idx+1:end_idx]
        
        ch_folder = os.path.join(chapters_dir, f'c{ch_num}')
        os.makedirs(ch_folder, exist_ok=True)
        
        source_content = f'# {header}\n\n' + '\n\n'.join(ch_paras) + '\n'
        with open(os.path.join(ch_folder, 'source.md'), 'w', encoding='utf-8') as f:
            f.write(source_content)
            
        meta = {
            'chapter': ch_num,
            'title': f'Chương {ch_num}',
            'original_header': header,
            'paragraph_count': len(ch_paras),
            'status': 'raw_ready'
        }
        with open(os.path.join(ch_folder, 'meta.json'), 'w', encoding='utf-8') as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
        print(f'Saved Chapter {ch_num}: {len(ch_paras)} paragraphs -> c{ch_num}/source.md')

if __name__ == '__main__':
    main()
