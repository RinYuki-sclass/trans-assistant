import httpx
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
}

print("Fetching https://cherrymist.cafe/chapter/uh-1/ with 60s timeout...")
try:
    with httpx.Client(headers=headers, timeout=60, follow_redirects=True) as client:
        r = client.get('https://cherrymist.cafe/chapter/uh-1/')
        print("Status code:", r.status_code)
        print("Final URL:", r.url)
        print("Response length:", len(r.text))
        
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Save HTML to scratch
        with open('scratch/uh1_60s.html', 'w', encoding='utf-8') as f:
            f.write(r.text)
            
        print("Saved scratch/uh1_60s.html")
        
        # Check all paragraphs
        p_tags = soup.find_all('p')
        print(f"Total <p> tags found: {len(p_tags)}")
        
        clean_paras = [p.get_text(strip=True) for p in p_tags if len(p.get_text(strip=True)) > 20]
        print(f"Paragraphs > 20 chars count: {len(clean_paras)}")
        if clean_paras:
            print("First 3 paragraphs:")
            for p in clean_paras[:3]:
                print("  -", p[:100].encode('ascii', 'ignore').decode())
except Exception as e:
    print("Error:", e)
