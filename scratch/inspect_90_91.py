import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.dmxs.org/cycs/18490.html'
}

for ch in [89, 90, 91]:
    u = f'https://www.dmxs.org/view/6-18490-{ch}.html'
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('gb18030', errors='ignore')
    print(f"Chapter {ch} len: {len(html)}")
    tm = re.search(r'<div class="read_chapterName[^"]*">\s*<h1>(.*?)</h1>', html, re.DOTALL)
    print(f"Chapter {ch} title match: {tm.group(1) if tm else None}")
    # print title or h1 tag
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', html)
    print(f"Chapter {ch} h1: {h1}")
