import httpx
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

# Check series page to get chapter links
with httpx.Client(headers=headers, timeout=20, follow_redirects=True) as client:
    r = client.get('https://cherrymist.cafe/story/the-unruly-hero-became-younger/')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    chapter_links = []
    for g in soup.select('.chapter-group'):
        for a in g.find_all('a', href=True):
            href = a['href']
            txt = a.get_text(strip=True).encode('ascii', 'ignore').decode()
            chapter_links.append((txt, href))
            
    print(f"Total chapter links in series: {len(chapter_links)}")
    
    # Test checking 5 sample chapters across the list
    sample_indices = [0, 5, 10, 20, 50, len(chapter_links)-1]
    for idx in sample_indices:
        if idx < len(chapter_links):
            title, link = chapter_links[idx]
            r_ch = client.get(link)
            soup_ch = BeautifulSoup(r_ch.text, 'html.parser')
            
            # Find content block in Fictioneer theme
            # Fictioneer uses article or #chapter-content or .fictioneer-chapter-text or .entry-content or .text-main
            p_count = len(soup_ch.find_all('p'))
            print(f"Ch [{title}] ({link}): HTML len={len(r_ch.text)}, <p> count={p_count}")
            for sel in ['.fictioneer-chapter-text', '#chapter-content', '.chapter-content', '.entry-content', 'article', '.text-main']:
                el = soup_ch.select_one(sel)
                if el:
                    paras = [p.get_text(strip=True) for p in el.find_all('p') if len(p.get_text(strip=True)) > 10]
                    if paras:
                        print(f"   Selector '{sel}': {len(paras)} paras! Sample: {paras[0][:80].encode('ascii', 'ignore').decode()}")
