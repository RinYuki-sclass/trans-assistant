import sys
import re
import json
sys.path.insert(0, r"d:\Nhung\RIDI\trans-assistant")
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

res = fetch_series_chapters("https://czbooks.net/n/skdfi4kimel")
pages = res.get('chapters', [])
print(f"Total pages: {len(pages)}")

all_page_data = []
all_chapter_headers = []

for idx, p in enumerate(pages):
    data = crawl_chapter(p['url'])
    txt = data.get('full_text', '')
    paras = [x.strip() for x in txt.split('\n') if x.strip()]
    
    # search for chapter header patterns
    headers = []
    for p_idx, line in enumerate(paras):
        # Match e.g. 第一章, 第1章, 番外, etc.
        m = re.match(r'^(第[0-9一二三四五六七八九十百千]+[章節卷]|番外\s*[0-9一二三四五六七八九十]*)(.*)$', line)
        if m:
            headers.append((p_idx, line))
    all_page_data.append({
        'page_num': idx + 1,
        'title': p['title'],
        'url': p['url'],
        'paras': paras,
        'headers': headers
    })
    if headers:
        for h in headers:
            all_chapter_headers.append((idx + 1, h[0], h[1]))

print(f"\nTotal chapter headers found: {len(all_chapter_headers)}")
for ch in all_chapter_headers:
    print(f"Page {ch[0]}, Para {ch[1]}: {ch[2]}")

# Save raw crawled pages to scratch/skdfi4kimel_pages.json for fast access
with open('scratch/skdfi4kimel_pages.json', 'w', encoding='utf-8') as f:
    json.dump(all_page_data, f, ensure_ascii=False, indent=2)
print("Saved all pages to scratch/skdfi4kimel_pages.json")
