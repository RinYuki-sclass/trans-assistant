import urllib.request
import time
import sys
import json
import re
from bs4 import BeautifulSoup
sys.path.insert(0, r"d:\Nhung\RIDI\trans-assistant")
from scripts.audio.crawler import _parse_czbooks_chapter, fetch_series_chapters

res = fetch_series_chapters("https://czbooks.net/n/skdfi4kimel")
chapters = res.get('chapters', [])
print(f"Total chapters/pages to fetch: {len(chapters)}")

results = []
for i, ch in enumerate(chapters, start=1):
    url = ch['url']
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                }
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode('utf-8')
            data = _parse_czbooks_chapter(html, url)
            
            # Find any chapter titles in paragraphs
            chapter_headers = []
            for p_idx, p in enumerate(data['paragraphs']):
                m = re.match(r'^(第[0-9一二三四五六七八九十百千]+[章節]|番外\s*[0-9一二三四五六七八九十]*)(.*)$', p)
                if m:
                    chapter_headers.append({'para_idx': p_idx, 'header': p})
            
            item = {
                'page_num': i,
                'title': data['title'],
                'url': url,
                'word_count': data['word_count'],
                'paragraphs': data['paragraphs'],
                'chapter_headers': chapter_headers
            }
            results.append(item)
            if i % 10 == 0 or i == len(chapters):
                print(f"[{i}/{len(chapters)}] Fetched page {i}: {len(data['paragraphs'])} paras, {data['word_count']} words. Headers: {[h['header'] for h in chapter_headers]}")
            break
        except Exception as ex:
            print(f"Retry {attempt+1} on page {i}: {ex}")
            time.sleep(1)
    time.sleep(0.3)

with open('scratch/raw_pages_skdfi4kimel.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully saved all {len(results)} pages to scratch/raw_pages_skdfi4kimel.json")
