import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"d:\Nhung\trans-tool")
from scripts.audio.crawler import fetch_series_chapters

res = fetch_series_chapters('https://czbooks.net/n/sk52b1bp08h')
chapters = res['chapters']
for i, ch in enumerate(chapters[:10], 1):
    print(f"{i}: {ch.get('title')} -> {ch.get('url')}")
print('...')
for i, ch in enumerate(chapters[-5:], len(chapters)-4):
    print(f"{i}: {ch.get('title')} -> {ch.get('url')}")
