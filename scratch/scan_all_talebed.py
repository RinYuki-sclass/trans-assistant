import urllib.request
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

def fetch_page(page):
    url = f'https://www.talebed.com/read/272625/{page}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8')
            m = re.search(r'<div class="read-content">(.*?)</div>\s*</div>\s*<div class="px-6', html, re.DOTALL)
            if m:
                paragraphs = re.findall(r'<p>(.*?)</p>', m.group(1))
                return page, [p.strip() for p in paragraphs if p.strip()]
    except Exception as e:
        print(f"Error page {page}: {e}")
    return page, []

print("Scanning pages 1 to 111...")
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_page, range(1, 112)))

results.sort(key=lambda x: x[0])

all_paragraphs = []
for p_num, paras in results:
    all_paragraphs.extend(paras)

headers = []
for idx, p in enumerate(all_paragraphs):
    m = re.search(r'第\s*(\d+)\s*章\s*(.*)', p)
    if m:
        num = int(m.group(1))
        title = m.group(2).strip()
        headers.append((num, title, p))

print(f"Total paragraphs: {len(all_paragraphs)}")
print(f"Total chapter headers found: {len(headers)}")
for num, title, raw in headers:
    print(f"Chapter {num}: {title}")
