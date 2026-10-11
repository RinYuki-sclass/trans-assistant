import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

u = 'https://czbooks.net/s/' + urllib.parse.quote('在霸總文學裡裝彎')
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

# find book items
items = re.findall(r'<li[^>]*class="novel-item"[^>]*>.*?</li>', html, re.DOTALL)
print('Items count:', len(items))
for item in items[:5]:
    title_m = re.search(r'class="title"[^>]*><a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', item)
    if title_m:
        print('Book:', title_m.group(2).strip(), '->', title_m.group(1))

# Also search all links with /n/
all_n = re.findall(r'href="(/n/[^"]+)"', html)
print('Unique /n/ links:', set(all_n[:10]))
