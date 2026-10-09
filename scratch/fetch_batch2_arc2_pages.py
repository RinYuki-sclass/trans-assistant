import sys
import os
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

def fetch_batch2_pages():
    cache_file = 'scratch/batch2_arc2_raw_pages.json'
    cached = {}
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                cached = json.load(f)
        except Exception:
            cached = {}

    # Also check if page 79 is in batch1 cache
    b1_cache_file = 'scratch/batch1_arc2_raw_pages.json'
    if os.path.exists(b1_cache_file):
        try:
            with open(b1_cache_file, 'r', encoding='utf-8') as f:
                b1_cached = json.load(f)
                if '79' in b1_cached:
                    cached['79'] = b1_cached['79']
        except Exception:
            pass

    res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
    chs = res['chapters']

    # We need pages 79 to 94 (0-indexed: 78 to 93)
    needed_pages = list(range(78, 94))
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
                print(f"-> Error on page {page_num}: {e}")
                time.sleep(2 + attempt * 2)

        if not success:
            print(f"FAILED to fetch page {page_num} after retries!")

        time.sleep(1)

    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(cached, f, ensure_ascii=False, indent=2)

    print("Finished caching Batch 2 pages.")
    missing = [str(p+1) for p in needed_pages if str(p+1) not in cached or not cached[str(p+1)].get('paragraphs')]
    print(f"Missing pages: {missing}")

if __name__ == '__main__':
    fetch_batch2_pages()
