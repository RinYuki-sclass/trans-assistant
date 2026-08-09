import httpx
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

with httpx.Client(headers=headers, timeout=20, follow_redirects=True) as client:
    r = client.get('https://cherrymist.cafe/chapter/uh-1/')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    print(f"Status code: {r.status_code}")
    print(f"HTML length: {len(r.text)}")
    
    # Save full HTML for debugging
    with open('scratch/uh1_full.html', 'w', encoding='utf-8') as f:
        f.write(r.text)
        
    print("\nAll elements with text > 20 chars in page:")
    for tag in soup.find_all(True):
        if tag.name not in ['html', 'body', 'script', 'style']:
            txt = tag.get_text(strip=True)
            if len(txt) > 20:
                cls = ' '.join(tag.get('class') or [])
                eid = tag.get('id') or ''
                clean_txt = txt[:120].encode('ascii', 'ignore').decode()
                print(f"  <{tag.name} id='{eid}' class='{cls}'> ({len(txt)} chars) -> {clean_txt}")
