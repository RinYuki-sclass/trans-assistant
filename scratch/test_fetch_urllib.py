import urllib.request
import time
import sys
from bs4 import BeautifulSoup
sys.path.insert(0, r"d:\Nhung\RIDI\trans-assistant")
from scripts.audio.crawler import _parse_czbooks_chapter, fetch_series_chapters

res = fetch_series_chapters("https://czbooks.net/n/skdfi4kimel")
chapters = res.get('chapters', [])
print(f"Total chapters/pages: {len(chapters)}")

for i in range(3):
    ch = chapters[i]
    req = urllib.request.Request(
        ch['url'],
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8')
    data = _parse_czbooks_chapter(html, ch['url'])
    print(f"Page {i+1}: title='{data['title']}', paras={len(data['paragraphs'])}, words={data['word_count']}")
    time.sleep(0.3)
