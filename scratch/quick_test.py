import httpx
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
r = httpx.get('https://cherrymist.cafe/chapter/uh-6/', headers=headers, timeout=15)
soup = BeautifulSoup(r.text, 'html.parser')

print('Status:', r.status_code)
print('Title:', soup.title.string if soup.title else '')

# Save HTML to scratch
with open('scratch/ch6.html', 'w', encoding='utf-8') as f:
    f.write(r.text)

print('Saved ch6.html, len:', len(r.text))
