import sys
import os
import re
import time
import json
import curl_cffi.requests as curl_req
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

from scripts.audio.crawler import fetch_series_chapters

def get_paras(url):
    for attempt in range(5):
        try:
            r = curl_req.get(url, impersonate='chrome120', timeout=25)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                c = soup.select_one('div.chapter-detail div.content, div.content')
                for t in c.find_all(['script', 'style', 'nav', 'footer', 'header', 'noscript', 'iframe', 'ins']):
                    t.decompose()
                return [line.strip() for line in c.get_text('\n').splitlines() if line.strip() and not line.strip().lower().startswith(('top', '52shuku', 'www.', 'czbooks'))]
            else:
                print(f"Status {r.status_code} for {url}, retrying...")
        except Exception as e:
            print(f"Error {url}: {e}, retrying...")
        time.sleep(1.5)
    return []

chs = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')['chapters']
print(f"Total CZBooks pages: {len(chs)}")

pages_data = {}
# Crawl pages 40 to 65
for p_num in range(40, 66):
    u = chs[p_num - 1]['url']
    paras = get_paras(u)
    pages_data[str(p_num)] = paras
    headers = [(idx, p) for idx, p in enumerate(paras) if re.search(r'第\s*\d+\s*章', p)]
    print(f"Page {p_num:02d} ({len(paras)} paras): Headers = {headers}")
    time.sleep(0.5)

with open('scratch/batch4_pages.json', 'w', encoding='utf-8') as f:
    json.dump(pages_data, f, ensure_ascii=False, indent=2)

print("Saved scratch/batch4_pages.json successfully!")
