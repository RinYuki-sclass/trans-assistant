import httpx
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

stories = [
    'https://cherrymist.cafe/story/heart-barter/',
    'https://cherrymist.cafe/story/the-circumstances-of-the-crown-princess/',
    'https://cherrymist.cafe/story/peach-pink-2791/',
]

with httpx.Client(headers=headers, timeout=20, follow_redirects=True) as client:
    for story_url in stories:
        try:
            r = client.get(story_url)
            soup = BeautifulSoup(r.text, 'html.parser')
            print(f"\nStory: {story_url}")
            print(f"  Title: {soup.title.string.strip() if soup.title else ''}")
            
            # Find chapter links
            ch_links = []
            for g in soup.select('.chapter-group, .story-chapters'):
                for a in g.find_all('a', href=True):
                    ch_links.append(a['href'])
                    
            print(f"  Total chapters found: {len(ch_links)}")
            
            # Test first chapter
            if ch_links:
                first_ch_url = ch_links[0]
                r_ch = client.get(first_ch_url)
                soup_ch = BeautifulSoup(r_ch.text, 'html.parser')
                print(f"  First chapter URL: {first_ch_url}")
                print(f"    Raw HTML len: {len(r_ch.text)}")
                
                # Test content selectors
                _CONTENT_SELECTORS = [
                    "div#chapter-content-text",
                    "div.chapter-content-text",
                    "div.chapter__content",
                    "div#chapter-content",
                    "div.fictioneer-chapter-text",
                    "article.fcn_chapter",
                    "div.entry-content",
                    "div.post-content",
                    "article",
                ]
                
                found_sel = None
                for sel in _CONTENT_SELECTORS:
                    el = soup_ch.select_one(sel)
                    if el and len(el.get_text(strip=True)) > 200:
                        found_sel = sel
                        p_count = len(el.find_all('p'))
                        print(f"    ✅ MATCHED SELECTOR '{sel}': {len(el.get_text(strip=True))} chars, {p_count} <p> tags!")
                        paras = [p.get_text(strip=True) for p in el.find_all('p') if len(p.get_text(strip=True)) > 10]
                        if paras:
                            print(f"       Sample P: {paras[0][:80].encode('ascii', 'ignore').decode()}")
                        break
                if not found_sel:
                    print("    ❌ No matching content selector found (locked/empty)")
        except Exception as e:
            print(f"  Error checking {story_url}: {e}")
