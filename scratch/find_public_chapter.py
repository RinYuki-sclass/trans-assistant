import httpx
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

with httpx.Client(headers=headers, timeout=20, follow_redirects=True) as client:
    r = client.get('https://cherrymist.cafe/story/the-unruly-hero-became-younger/')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    all_links = []
    for g in soup.select('.chapter-group'):
        for a in g.find_all('a', href=True):
            all_links.append((a.get_text(strip=True).encode('ascii', 'ignore').decode(), a['href']))
            
    print(f"Found total {len(all_links)} chapter links on series page.")
    
    # Check first 20 links to see if any have chapter content
    for idx, (title, url) in enumerate(all_links[:30]):
        r_ch = client.get(url)
        soup_ch = BeautifulSoup(r_ch.text, 'html.parser')
        
        # Check text length inside main or article or fictioneer-chapter-text or entry-content
        # Let's check all divs with class containing chapter or text
        content_found = False
        for sel in ['.fictioneer-chapter-text', '#chapter-content', '.chapter-content', '.entry-content', 'article.fcn_chapter', 'article', 'div._text']:
            el = soup_ch.select_one(sel)
            if el:
                paras = [p.get_text(strip=True) for p in el.find_all('p') if len(p.get_text(strip=True)) > 20]
                if len(paras) > 2:
                    print(f"  ✅ Link [{idx+1}] ({title}) {url} -> FOUND {len(paras)} paras! First: {paras[0][:60].encode('ascii', 'ignore').decode()}")
                    content_found = True
                    break
        if not content_found:
            print(f"  ❌ Link [{idx+1}] ({title}) {url} -> No public paragraphs (locked/empty)")
