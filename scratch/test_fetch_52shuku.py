import urllib.request
import re
import html
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.52shuku.net/chongsheng/07_b/bjVPq.html'
}

def fetch_page(page_idx):
    url = f'https://www.52shuku.net/chongsheng/07_b/bjVPq_{page_idx}.html'
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                content = resp.read()
                html_str = content.decode('utf-8', errors='ignore')

            # Find content
            content_m = re.search(r'<article[^>]*>(.*?)</article>', html_str, re.DOTALL) or \
                        re.search(r'<div[^>]+id="text"[^>]*>(.*?)</div>', html_str, re.DOTALL) or \
                        re.search(r'<div[^>]+class="content"[^>]*>(.*?)</div>', html_str, re.DOTALL) or \
                        re.search(r'<div[^>]+class="article-content"[^>]*>(.*?)</div>', html_str, re.DOTALL)
            
            if not content_m:
                raise ValueError("Could not find content container")

            raw_body = content_m.group(1)
            # Remove pagination/nav block inside article
            raw_body = re.sub(r'<div class="pagination"[^>]*>.*?</div>', '', raw_body, flags=re.DOTALL)
            raw_body = re.sub(r'<div class="read_page"[^>]*>.*?</div>', '', raw_body, flags=re.DOTALL)
            
            paras = [p.strip() for p in re.split(r'<p>|<br\s*/?>', raw_body) if p.strip()]
            cleaned_paras = []
            for p in paras:
                p_clean = re.sub(r'<[^>]+>', '', p)
                p_clean = html.unescape(p_clean).strip()
                p_clean = re.sub(r'^[　\s]+', '', p_clean)
                if not p_clean:
                    continue
                if any(ad in p_clean for ad in ['52shuku', '52书库', '版权', '请收藏', '传送门：', '目录 上一页']):
                    continue
                cleaned_paras.append(p_clean)

            return {
                'page': page_idx,
                'paragraphs': cleaned_paras,
                'error': None
            }
        except Exception as e:
            if attempt == 3:
                return {
                    'page': page_idx,
                    'paragraphs': [],
                    'error': str(e)
                }
            time.sleep(1 + attempt)

# Test first 10 pages
print("Testing pages 2 to 11...")
results = []
for p in range(2, 12):
    r = fetch_page(p)
    print(f"Page {p}: {len(r['paragraphs'])} paragraphs, error={r['error']}")
    if r['paragraphs']:
        print(f"  First para: {r['paragraphs'][0][:50]}")
