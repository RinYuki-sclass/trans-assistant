import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.dmxs.org/cycs/18490.html'
}

# 1. Test txt link
txt_url = 'https://www.dmxs.org/txt/6-18490-0.html'
print('Checking txt page:', txt_url)
try:
    req = urllib.request.Request(txt_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        txt_html = r.read().decode('gb18030', errors='ignore')
    print('Txt HTML length:', len(txt_html))
    download_links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', txt_html)
    for h, t in download_links:
        if any(x in t.lower() or x in h.lower() for x in ['txt', '下载', 'down']):
            print('Download link:', h, t)
except Exception as e:
    print('Error txt:', e)

# 2. Test chapter 91, 92, 114
for ch in [91, 100, 114, 115, 120]:
    u = f'https://www.dmxs.org/view/6-18490-{ch}.html'
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            ch_html = r.read().decode('gb18030', errors='ignore')
        tm = re.search(r'<div class="read_chapterName[^"]*">\s*<h1>(.*?)</h1>', ch_html, re.DOTALL)
        title = tm.group(1) if tm else 'No title'
        print(f"Chapter {ch}: HTTP 200, title: {title.strip()}")
    except Exception as e:
        print(f"Chapter {ch}: Error {e}")
