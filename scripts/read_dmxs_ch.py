import urllib.request
import re
from bs4 import BeautifulSoup

url = 'https://www.dmxs.org/view/6-6248-1.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
raw = urllib.request.urlopen(req, timeout=10).read()
html = raw.decode('gbk', errors='ignore')
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', class_='read_chapterDetail')
print("Div length:", len(div.get_text()))
print("Sample:\n", div.get_text()[:400])
