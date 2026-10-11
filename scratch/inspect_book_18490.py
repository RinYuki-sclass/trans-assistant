import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.dmxs.org/'
}

url = 'https://www.dmxs.org/cycs/18490.html'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as r:
    html = r.read().decode('gb18030', errors='ignore')

print('HTML length:', len(html))

# Look for chapter list or view links
links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
view_links = [l for l in links if 'view' in l[0] or '18490' in l[0]]
print(f'Total view/18490 links: {len(view_links)}')
for l in view_links[:10]:
    print(' ', l[0], re.sub(r'<[^>]+>', '', l[1]).strip())

if view_links:
    print('Last 5 links:')
    for l in view_links[-5:]:
        print(' ', l[0], re.sub(r'<[^>]+>', '', l[1]).strip())
