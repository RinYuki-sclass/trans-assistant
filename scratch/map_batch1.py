import sys
import os
import re
import time
import curl_cffi.requests as curl_req
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

def get_paras(url):
    for attempt in range(3):
        try:
            r = curl_req.get(url, impersonate='chrome120', timeout=20)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                c = soup.select_one('div.chapter-detail div.content, div.content')
                for t in c.find_all(['script', 'style', 'nav', 'footer', 'header', 'noscript', 'iframe', 'ins']):
                    t.decompose()
                return [line.strip() for line in c.get_text('\n').splitlines() if line.strip() and not line.strip().lower().startswith(('top', '52shuku', 'www.', 'czbooks'))]
        except Exception as e:
            print(f"Error {url}: {e}")
        time.sleep(1)
    return []

# Scan pages 4 to 16
series_slug = "skdocoml0kd"
# We need urls for pages. Let's load series chapters from fetch_series_chapters
from scripts.audio.crawler import fetch_series_chapters
chs = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')['chapters']

for p_num in range(4, 16):
    u = chs[p_num - 1]['url']
    paras = get_paras(u)
    headers = [(idx, p) for idx, p in enumerate(paras) if re.search(r'第\s*\d+\s*章', p)]
    print(f"Page {p_num:02d} ({len(paras)} paras): Headers = {headers}")
    time.sleep(0.5)
