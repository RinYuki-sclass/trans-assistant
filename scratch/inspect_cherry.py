import httpx
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

urls_to_check = [
    'https://cherrymist.cafe/chapter/uh-1/',
    'https://cherrymist.cafe/chapter/uh-2/',
    'https://cherrymist.cafe/chapter/uh-5/',
    'https://cherrymist.cafe/?post_type=fcn_chapter&p=456812',
]

with httpx.Client(headers=headers, timeout=20, follow_redirects=True) as client:
    for url in urls_to_check:
        try:
            r = client.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            
            # Find all divs or main content
            text_els = soup.select('.chapter-content, .fictioneer-chapter-text, #chapter-content, article, main, .entry-content, .text-main')
            print(f"URL: {url}")
            print(f"  Title: {title.strip()}")
            print(f"  Raw HTML len: {len(r.text)}")
            
            # Search for large text blocks or p tags
            p_tags = soup.find_all('p')
            print(f"  Total <p> tags: {len(p_tags)}")
            
            # Search for div with class containing text or chapter or content
            for el in soup.find_all(['div', 'article', 'section']):
                cls = ' '.join(el.get('class') or [])
                txt = el.get_text(strip=True)
                if len(txt) > 500:
                    print(f"    Container <{el.name} class='{cls}'>: {len(txt)} chars")
            print('-'*50)
        except Exception as e:
            print(f"URL: {url} Error: {e}")
