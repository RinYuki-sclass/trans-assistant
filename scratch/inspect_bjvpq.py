import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.52shuku.net/'
}

url = 'https://www.52shuku.net/chongsheng/07_b/bjVPq.html'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

print('HTML length:', len(html))
# Find title
m_title = re.search(r'<title>(.*?)</title>', html)
print('Title:', m_title.group(1) if m_title else 'None')

# Check pagination or chapter links
# 52shuku often has pages like bjVPq_2.html, bjVPq_3.html... or pagination block
pagination = re.findall(r'href="([^"]*bjVPq[^"]*)"[^>]*>(.*?)</a>', html)
print('bjVPq links count:', len(pagination))
for href, text in pagination[:10]:
    print(f"  {text.strip()}: {href}")

# Check page info: "共XX页"
page_info = re.search(r'共\s*(\d+)\s*页', html)
if page_info:
    print('Total pages:', page_info.group(1))
else:
    # Look for max page number in links
    page_nums = re.findall(r'bjVPq_(\d+)\.html', html)
    if page_nums:
        print('Max page num in links:', max(map(int, page_nums)))
