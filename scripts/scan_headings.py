import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}

# Test scanning first 20 pages and finding chapter headings
ch_pattern = re.compile(r'(?:第\s*[0-9零一二三四五六七八九十百千万]+\s*[章回节]|番外)')

for i in range(2, 30):
    url = f"https://www.52shuku.net/xiandaidushi/9065_{i}.html"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            p_tags = re.findall(r'<p>(.*?)</p>', html, re.DOTALL)
            for pt in p_tags:
                clean = re.sub(r'<[^>]+>', '', pt).strip()
                if ch_pattern.search(clean) and len(clean) < 50:
                    print(f"Page {i}: {clean}")
    except Exception as e:
        print(f"Page {i} err: {e}")
