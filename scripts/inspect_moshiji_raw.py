import urllib.request
import re

url = "https://www.52shuku.net/xiandaidushi/9065.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("Page 1 length:", len(html))
        title = re.findall(r'<title>(.*?)</title>', html)
        print("Title:", title)
        # Look for total pages or pagination
        pagination = re.findall(r'<div class="page"[^>]*>(.*?)</div>', html, re.DOTALL)
        if not pagination:
            pagination = re.findall(r'<ul class="pagination"[^>]*>(.*?)</ul>', html, re.DOTALL)
        if pagination:
            print("Pagination snippet:", pagination[0][:300])
        # Look for chapter headings or text
        h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', html)
        print("H1:", h1)
        # check page links like 9065_2.html, 9065_3.html etc.
        page_links = re.findall(r'href=[\'"]([^\'"]*9065[^\'"]*\.html)[\'"]', html)
        print("Page links found:", set(page_links))
except Exception as e:
    print("Error:", e)
