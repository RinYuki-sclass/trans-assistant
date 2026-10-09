import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
chs = res['chapters']

c185 = crawl_chapter(chs[184]['url'])
c186 = crawl_chapter(chs[185]['url'])

print("=== Page 185 last 10 paras ===")
for i, p in enumerate(c185['paragraphs'][-10:]):
    print(f"{i}: {p}")

print("\n=== Page 186 first 30 paras ===")
for i, p in enumerate(c186['paragraphs'][:30]):
    print(f"{i}: {p}")
