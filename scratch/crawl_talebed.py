import urllib.request
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

pages_data = []

for page in range(1, 15):
    url = f'https://www.talebed.com/read/272625/{page}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            match = re.search(r'<div class="read-content">(.*?)</div>\s*</div>\s*<div class="px-6', html, re.DOTALL)
            if match:
                content = match.group(1)
                paragraphs = re.findall(r'<p>(.*?)</p>', content)
                chapter_headers = [p for p in paragraphs if re.search(r'第\s*\d+\s*章', p)]
                print(f"Page {page:02d}: {len(paragraphs)} paragraphs | Headers: {chapter_headers}")
                pages_data.append((page, paragraphs))
            else:
                print(f"Page {page:02d}: Content match failed")
    except Exception as e:
        print(f"Page {page:02d} error: {e}")

# Let's inspect where chapters are
print("\n--- Summary of Chapter Headers found ---")
for page, paragraphs in pages_data:
    for idx, p in enumerate(paragraphs):
        if re.search(r'第\s*\d+\s*章', p):
            print(f"Page {page} [p{idx}]: {p}")
