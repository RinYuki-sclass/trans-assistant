import httpx
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

r = httpx.get('https://cherrymist.cafe/chapter/hb-1/', headers=headers, timeout=15)
soup = BeautifulSoup(r.text, 'html.parser')

print('Status code:', r.status_code)
print('Title:', soup.title.string if soup.title else '')

# Save HTML
with open('scratch/hb1.html', 'w', encoding='utf-8') as f:
    f.write(r.text)

print('Saved hb1.html, length:', len(r.text))
