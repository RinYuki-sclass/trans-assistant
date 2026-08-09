import httpx
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

def fetch_cherrymist_series_chapters(url: str) -> dict:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    with httpx.Client(headers=headers, timeout=20, follow_redirects=True) as client:
        r = client.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Extract story title
        h1 = soup.select_one('h1.story__title') or soup.select_one('h1.entry-title') or soup.find('h1')
        series_title = (h1.get_text(strip=True) if h1 else 'Cherry Mist Story').strip()
        
        chapters = []
        seen_urls = set()
        
        groups = soup.select('.chapter-group, .story-chapters, .chapter-list')
        if not groups:
            groups = [soup]
            
        for group in groups:
            for a in group.find_all('a', href=True):
                ch_url = a['href']
                if ch_url in seen_urls:
                    continue
                # Match chapter links or post_type=fcn_chapter
                if '/chapter/' in ch_url or 'fcn_chapter' in ch_url or ('/story/' in url and '/story/' not in ch_url and 'fictioneer' not in ch_url):
                    seen_urls.add(ch_url)
                    ch_title = a.get_text(strip=True)
                    if not ch_title:
                        continue
                    
                    num_match = re.search(r'\d+', ch_title)
                    ch_num = int(num_match.group()) if num_match else len(chapters) + 1
                    
                    chapters.append({
                        "id": ch_url,
                        "chapter_number": ch_num,
                        "title": ch_title,
                        "slug": ch_url.rstrip("/").split("/")[-1],
                        "price": 0,
                        "url": ch_url,
                    })
                    
        return {
            "series_title": series_title,
            "series_id": url,
            "chapters": chapters,
        }

res = fetch_cherrymist_series_chapters('https://cherrymist.cafe/story/the-unruly-hero-became-younger/')
print("Series Title:", res["series_title"].encode('ascii', 'ignore').decode())
print("Chapters found:", len(res["chapters"]))
print("Sample first 3:", [c["title"] for c in res["chapters"][:3]])
print("Sample last 3:", [c["title"] for c in res["chapters"][-3:]])
