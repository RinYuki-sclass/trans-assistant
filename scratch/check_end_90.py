import urllib.request
import re
import html
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.dmxs.org/cycs/18490.html'
}

u = 'https://www.dmxs.org/view/6-18490-90.html'
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10) as r:
    html_str = r.read().decode('gb18030', errors='ignore')

cm = re.search(r'<div class="read_chapterDetail">(.*?)</div>', html_str, re.DOTALL)
if cm:
    body = cm.group(1)
    paras = re.findall(r'<p>(.*?)</p>', body, re.DOTALL)
    for p in paras[-10:]:
        print(html.unescape(re.sub(r'<[^>]+>', '', p)).strip())
