import sys
sys.path.insert(0, r"d:\Nhung\RIDI\trans-assistant")
from scripts.audio.crawler import crawl_chapter

url = "https://czbooks.net/n/skdfi4kimel/sk2e5?chapterNumber=0"
res = crawl_chapter(url)
print("Title:", res.get('title'))
text = res.get('full_text', '')
print("Text length:", len(text))
paras = [p.strip() for p in text.split('\n') if p.strip()]
print("Number of paragraphs:", len(paras))
print("First 10 paragraphs:")
for p in paras[:10]:
    print(" -", p)
