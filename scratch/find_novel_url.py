import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

query = '還情債的救世主'
url = f'https://czbooks.net/s/{urllib.parse.quote(query)}'
print("Searching:", url)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        novel_items = soup.find_all('li', class_='novel-item')
        if not novel_items:
            # find all a href containing /n/
            novel_links = soup.find_all('a', href=re.compile(r'^/n/'))
            for a in novel_links:
                print(a.get('href'), a.get_text(strip=True))
        else:
            for item in novel_items:
                title_elem = item.find('a')
                print(title_elem.get('href') if title_elem else '', item.get_text(separator=' | ', strip=True))
except Exception as e:
    print("Error:", e)
