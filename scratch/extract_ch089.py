import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

res = fetch_series_chapters('https://czbooks.net/n/skdocoml0kd')
chs = res['chapters']

p183 = crawl_chapter(chs[182]['url'])['paragraphs']
p184 = crawl_chapter(chs[183]['url'])['paragraphs']
p185 = crawl_chapter(chs[184]['url'])['paragraphs']
p186 = crawl_chapter(chs[185]['url'])['paragraphs']

# On p183, chapter starts at index 36 (after 35: 第88章)
p183_ch89 = p183[36:]
p184_ch89 = p184
p185_ch89 = p185
p186_ch89 = p186[:27] # up to index 26 (index 27 is 第89章)

all_paras = p183_ch89 + p184_ch89 + p185_ch89 + p186_ch89
print(f"p183 count: {len(p183_ch89)}")
print(f"p184 count: {len(p184_ch89)}")
print(f"p185 count: {len(p185_ch89)}")
print(f"p186 count: {len(p186_ch89)}")
print(f"Total raw paras: {len(all_paras)}")

print("\n--- First 3 paras ---")
for i in range(3):
    print(f"{i}: {all_paras[i]}")

print("\n--- Last 3 paras ---")
for i in range(-3, 0):
    print(f"{i}: {all_paras[i]}")
