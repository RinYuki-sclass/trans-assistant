from bs4 import BeautifulSoup
import re
import json

with open('scratch/cherrymist_ch1.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("1. All script tags in HTML:")
scripts = soup.find_all('script')
print(f"Total script tags: {len(scripts)}")

for i, s in enumerate(scripts):
    s_txt = s.string or s.get_text()
    if len(s_txt) > 100:
        s_id = s.get('id') or ''
        s_src = s.get('src') or ''
        print(f"  Script [{i}] id='{s_id}' src='{s_src}' ({len(s_txt)} chars)")
        if any(k in s_txt.lower() for k in ['chapter', 'text', 'content', 'payload', 'data', 'b64', 'encode', 'decode']):
            print(f"    --> Sample text: {s_txt[:150].encode('ascii', 'ignore').decode()}")
