import sys
import re
sys.path.insert(0, r"d:\Nhung\RIDI\trans-assistant")
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

res = fetch_series_chapters("https://czbooks.net/n/skdfi4kimel")
chapters = res.get('chapters', [])

for idx in [0, 1, 2, 3, 4, 10, 20]:
    if idx < len(chapters):
        c = chapters[idx]
        data = crawl_chapter(c['url'])
        txt = data.get('full_text', '')
        paras = [p.strip() for p in txt.split('\n') if p.strip()]
        ch_matches = [p for p in paras if re.search(r'第[\d一二三四五六七八九十百]+[章節頁]', p)]
        print(f"Page {idx+1} ({c['title']}): total paras {len(paras)}, chapter headers found: {ch_matches[:3]}")
