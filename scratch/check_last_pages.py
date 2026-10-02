import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

for page in [110, 111]:
    req = urllib.request.Request(f'https://www.talebed.com/read/272625/{page}', headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    m = re.search(r'<div class="read-content">(.*?)</div>\s*</div>\s*<div class="px-6', html, re.DOTALL)
    if m:
        paragraphs = re.findall(r'<p>(.*?)</p>', m.group(1))
        headers_found = [p for p in paragraphs if re.search(r'第\s*\d+\s*章', p)]
        print(f"Page {page}: {len(paragraphs)} paragraphs | Headers: {headers_found}")
        for p in paragraphs[-5:]:
            print("  End:", p[:100])
