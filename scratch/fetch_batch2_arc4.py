import sys
import os
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

cache_file = 'scratch/batch2_arc4_raw_pages.json'
cached = {}
if os.path.exists(cache_file):
    try:
        with open(cache_file, 'r', encoding='utf-8') as f:
            cached = json.load(f)
    except Exception:
        cached = {}

res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
chs = res['chapters']

# Needed pages: 199 to 216 (0-indexed: 198 to 215)
needed_pages = list(range(198, 216))
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
            time.sleep(4 + attempt * 3)

    if not success:
        print(f"FAILED to fetch page {page_num} after retries!")
        break

    time.sleep(2)

print("Finished fetching Batch 2 pages.")
