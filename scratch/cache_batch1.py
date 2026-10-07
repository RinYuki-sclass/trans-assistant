import sys
import os
import re
import time
import json
import curl_cffi.requests as curl_req
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

def get_paras(url):
    for attempt in range(3):
        try:
            r = curl_req.get(url, impersonate='chrome120', timeout=25)
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

from scripts.audio.crawler import fetch_series_chapters
chs = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')['chapters']

# Cache pages 4 to 14
pages_data = {}
for p_num in range(4, 15):
    u = chs[p_num - 1]['url']
    paras = get_paras(u)
    pages_data[p_num] = paras
    print(f"Loaded page {p_num}: {len(paras)} paras")
    time.sleep(0.3)

# Let's save cached pages to scratch/batch1_pages.json for fast access
with open('scratch/batch1_pages.json', 'w', encoding='utf-8') as f:
    json.dump(pages_data, f, ensure_ascii=False, indent=2)

print("Saved batch1_pages.json successfully!")
