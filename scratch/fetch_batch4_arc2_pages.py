import sys
import os
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

def fetch_batch4_pages():
    cache_file = 'scratch/batch4_arc2_raw_pages.json'
    cached = {}
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                cached = json.load(f)
        except Exception:
            cached = {}

    # Check batch3 cache for page 110, 111, 112, 113
    b3_cache_file = 'scratch/batch3_arc2_raw_pages.json'
    if os.path.exists(b3_cache_file):
        try:
            with open(b3_cache_file, 'r', encoding='utf-8') as f:
                b3_cached = json.load(f)
                for p_str in ['110', '111', '112', '113']:
                    if p_str in b3_cached:
                        cached[p_str] = b3_cached[p_str]
        except Exception:
            pass

    res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
    chs = res['chapters']
    print(f"Total CZBooks chapter pages: {len(chs)}")

    # We need pages 110 to 126 (0-indexed: 109 to 125)
    needed_pages = list(range(109, min(126, len(chs))))
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
                    print(f"-> Success: {len(paras)} paras")
                    success = True
                    break
            except Exception as e:
                print(f"  Attempt {attempt+1} failed: {e}")
                time.sleep(2)

        if not success:
            print(f"FAILED to fetch page {page_num}!")

        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(cached, f, ensure_ascii=False, indent=2)
        time.sleep(0.5)

    print(f"Done caching Batch 4 Arc 2 pages. Total cached: {len(cached)}")

if __name__ == '__main__':
    fetch_batch4_pages()
