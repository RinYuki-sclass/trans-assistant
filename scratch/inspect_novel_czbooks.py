import sys
sys.path.insert(0, r"d:\Nhung\RIDI\trans-assistant")
from scripts.audio.crawler import fetch_series_chapters

url = "https://czbooks.net/n/skdfi4kimel"
res = fetch_series_chapters(url)
print("Title:", res.get('title'))
print("Author:", res.get('author'))
print("Description:", res.get('description'))
chapters = res.get('chapters', [])
print("Total chapters/pages:", len(chapters))
if chapters:
    print("First 3 chapters:", chapters[:3])
    print("Last 3 chapters:", chapters[-3:])
