import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

query = '還情債的救世主'
url = f'https://czbooks.net/s/{urllib.parse.quote(query)}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
for a in soup.find_all('a'):
    if '還情債的救世主' in a.get_text():
        print("Found:", a.get('href'), a.get_text(strip=True))
