# -*- coding: utf-8 -*-
import sys
import os
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

cache_file = 'scratch/batch3_arc4_raw_pages.json'
cached = {}
if os.path.exists(cache_file):
    try:
        with open(cache_file, 'r', encoding='utf-8') as f:
            cached = json.load(f)
    except Exception:
        cached = {}

# Đọc thêm từ batch2 nếu có sẵn 213-216
if os.path.exists('scratch/batch2_arc4_raw_pages.json'):
    try:
        with open('scratch/batch2_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
            b2 = json.load(f)
            for k in ['213', '214', '215', '216']:
                if k in b2 and k not in cached:
                    cached[k] = b2[k]
    except Exception:
        pass

res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
chs = res['chapters']

# Needed pages: 213 to 229 (0-indexed: 212 to 228)
needed_pages = list(range(212, 229))
print(f"Needed pages: {[p+1 for p in needed_pages]}")

for p_idx in needed_pages:
    page_num = str(p_idx + 1)
    if page_num in cached and cached[page_num].get('paragraphs'):
        print(f"Page {page_num} already cached ({len(cached[page_num]['paragraphs'])} paras)")
        continue

    url = chs[p_idx]['url']
    success = False
    for attempt in range(5):
        try:
            print(f"Fetching page {page_num} (attempt {attempt+1})...")
            c = crawl_chapter(url)
            paras = c.get('paragraphs', [])
            if paras:
                cached[page_num] = {
                    'url': url,
                    'title': c.get('title', ''),
                    'paragraphs': paras
                }
                with open(cache_file, 'w', encoding='utf-8') as f:
                    json.dump(cached, f, ensure_ascii=False, indent=2)
                print(f"-> Success: {len(paras)} paras (Saved to cache)")
                success = True
                break
        except Exception as e:
            print(f"-> Error on page {page_num}: {e}")
            time.sleep(3 + attempt * 2)

    if not success:
        print(f"FAILED to fetch page {page_num} after retries!")
        break

    time.sleep(1.5)

print("Finished fetching Batch 3 pages.")
