import httpx
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

with httpx.Client(headers=headers, timeout=20, follow_redirects=True) as client:
    r = client.get('https://cherrymist.cafe/chapter/uh-1/')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Save formatted soup to text file to search
    with open('scratch/soup_ch1.txt', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    print("Prettified HTML saved to scratch/soup_ch1.txt. Total lines:", len(r.text.splitlines()))
