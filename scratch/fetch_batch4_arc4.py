# -*- coding: utf-8 -*-
import sys
import os
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

cache_file = 'scratch/batch4_arc4_raw_pages.json'
cached = {}
if os.path.exists(cache_file):
    try:
        with open(cache_file, 'r', encoding='utf-8') as f:
            cached = json.load(f)
    except Exception:
        cached = {}

# Also copy page 229 if in batch3
if os.path.exists('scratch/batch3_arc4_raw_pages.json'):
    try:
        with open('scratch/batch3_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
            b3 = json.load(f)
            if '229' in b3 and '229' not in cached:
                cached['229'] = b3['229']
    except Exception:
        pass

res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
chs = res['chapters']
print(f"Total series chapters: {len(chs)}")

needed_pages = list(range(229, 245)) # 0-indexed 229..244 -> Page 230..245
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
            else:
                print(f"-> Empty paras on page {page_num}, retry...")
        except Exception as e:
            print(f"-> Error fetching page {page_num}: {e}")
        time.sleep(2)

    if not success:
        print(f"Failed to fetch page {page_num}")

print("Done fetching batch 4 raw pages.")
