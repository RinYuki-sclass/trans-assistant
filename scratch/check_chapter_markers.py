import sys
sys.path.insert(0, r"d:\Nhung\RIDI\trans-assistant")
from scripts.audio.crawler import crawl_chapter

for p in range(5):
    url = f"https://czbooks.net/n/skdfi4kimel?chapterNumber={p}" # or get url from fetch_series_chapters
    # let's fetch series chapters
