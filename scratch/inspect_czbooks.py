import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters

res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
chs = res['chapters']
print(f"Total pages on czbooks: {len(chs)}")
for idx in range(180, min(190, len(chs))):
    print(f"Page {idx+1}: {chs[idx]['title']} -> {chs[idx]['url']}")
