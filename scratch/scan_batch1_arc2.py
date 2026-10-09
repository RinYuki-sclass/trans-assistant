import sys
import re
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

def scan():
    print("Fetching series chapters list...")
    res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
    chs = res['chapters']
    print(f"Total pages: {len(chs)}")

    found = []
    # Scan pages 66 to 85 (0-indexed: 65 to 84)
    for p_idx in range(65, min(85, len(chs))):
        try:
            c = crawl_chapter(chs[p_idx]['url'])
            paras = c.get('paragraphs', [])
            for para_idx, p in enumerate(paras):
                m = re.match(r'^(第\s*(\d+)\s*章(?:\s+.*)?)$', p.strip())
                if m:
                    found.append({
                        'page': p_idx + 1,
                        'p_idx': p_idx,
                        'para_idx': para_idx,
                        'header': m.group(1),
                        'num': int(m.group(2))
                    })
        except Exception as ex:
            print(f"Error page {p_idx+1}: {ex}")
        time.sleep(0.1)

    print(f"\n--- FOUND {len(found)} CHAPTER HEADERS ---")
    for f in found:
        print(f"Ch {f['num']:03d}: Page {f['page']}, Para {f['para_idx']} | {f['header']}")

    # Save to file
    with open('scratch/batch1_arc2_headers.json', 'w', encoding='utf-8') as fp:
        json.dump(found, fp, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    scan()
