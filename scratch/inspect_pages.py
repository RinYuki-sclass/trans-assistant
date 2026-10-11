import urllib.request
import re
import html
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.52shuku.net/chongsheng/07_b/bjVPq.html'
}

for page in [2, 3, 221, 222]:
    u = f'https://www.52shuku.net/chongsheng/07_b/bjVPq_{page}.html'
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        html_str = r.read().decode('utf-8', errors='ignore')
    
    # Check title
    t = re.search(r'<h1[^>]*>(.*?)</h1>', html_str)
    # Check text container
    # Often in 52shuku it's <div class="article-content"> or id="text" or class="content"
    content_m = re.search(r'<article[^>]*>(.*?)</article>', html_str, re.DOTALL) or \
                re.search(r'<div[^>]+id="text"[^>]*>(.*?)</div>', html_str, re.DOTALL) or \
                re.search(r'<div[^>]+class="content"[^>]*>(.*?)</div>', html_str, re.DOTALL) or \
                re.search(r'<div[^>]+class="article-content"[^>]*>(.*?)</div>', html_str, re.DOTALL)
    
    print(f"Page {page}: title={t.group(1) if t else None}")
    if content_m:
        raw_body = content_m.group(1)
        paras = [p.strip() for p in re.split(r'<p>|<br\s*/?>', raw_body) if p.strip()]
        cleaned = [html.unescape(re.sub(r'<[^>]+>', '', p)).strip() for p in paras]
        cleaned = [c for c in cleaned if c and not any(ad in c for ad in ['52shuku', '52书库', '版权', '请收藏'])]
        print(f"  Paragraphs count: {len(cleaned)}")
        print(f"  First 2: {cleaned[:2]}")
        print(f"  Last 2: {cleaned[-2:]}")
    else:
        print("  Could not find content container!")
