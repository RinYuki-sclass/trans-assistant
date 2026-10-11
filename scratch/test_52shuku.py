import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

urls = [
    'https://www.52shuku.vip/qitabl/26027.html',
    'https://www.52shuku.vip/m/qitabl/26027.html',
    'https://www.52shuku.net/qitabl/26027.html',
    'https://www.52shuku.net/m/qitabl/26027.html'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        print(f"URL: {u} -> Status 200, len: {len(html)}")
        # Look for chapters or page count
        # In 52shuku, usually chapters are pagination like 26027_2.html or chapter list
        links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html)
        ch_links = [l for l in links if '26027' in l[0]]
        print(f"  Found {len(ch_links)} links matching 26027")
        if ch_links:
            print("  First 5:", ch_links[:5])
            print("  Last 5:", ch_links[-5:])
        break
    except Exception as e:
        print(f"URL: {u} -> Error: {e}")
