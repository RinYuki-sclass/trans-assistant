import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
chs = res['chapters']

# Let's crawl pages 186 to 198 (indices 185 to 197)
pages_data = {}
for p_idx in range(185, 200):
    p_num = p_idx + 1
    c = crawl_chapter(chs[p_idx]['url'])
    paras = c.get('paragraphs', [])
    pages_data[p_num] = paras
    print(f"Page {p_num}: {len(paras)} paras")
    for i, p in enumerate(paras):
        if '第' in p and '章' in p:
            print(f"   [P{p_num} para {i}] {p}")
        elif '作者有話說' in p:
            print(f"   [P{p_num} para {i} Note] {p}")

with open('scratch/batch1_arc4_raw_pages.json', 'w', encoding='utf-8') as f:
    json.dump(pages_data, f, ensure_ascii=False, indent=2)

print("Saved batch1_arc4_raw_pages.json")
