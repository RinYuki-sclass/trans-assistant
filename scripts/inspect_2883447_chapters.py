import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.jjwxc.net/onebook.php?novelid=2883447'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
html = urllib.request.urlopen(req, timeout=10).read().decode('gb18030', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr', {'itemprop': 'chapter'})
print("Total rows:", len(rows))
for r in rows:
    tds = [td.get_text(strip=True) for td in r.find_all('td')]
    link = r.find('a')
    href = link.get('href', '') if link else 'No link'
    print(f"Ch {tds[0]}: {tds[1]} | words: {tds[3]} | link: {href}")
