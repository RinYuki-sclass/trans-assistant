from bs4 import BeautifulSoup
import re

with open('scratch/uh1_60s.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("1. Searching for ajax / fetch / postid / fcn in script tags:")
for i, s in enumerate(soup.find_all('script')):
    txt = s.string or s.get_text()
    if 'ajax' in txt.lower() or 'action' in txt.lower() or 'postid' in txt.lower() or 'chapter' in txt.lower():
        print(f"Script [{i}] id='{s.get('id')}':")
        # Print relevant lines
        for line in txt.splitlines():
            line_str = line.strip()
            if any(k in line_str.lower() for k in ['ajax', 'action', 'post', 'chapter', 'content', 'fetch', 'nonce', 'b64']):
                print("  ", line_str[:120].encode('ascii', 'ignore').decode())

print("\n2. Checking post ID and article data attributes:")
art = soup.select_one('article')
if art:
    print("Article tag attrs:", art.attrs)

print("Body tag attrs/classes:", soup.body.get('class'))
