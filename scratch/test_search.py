import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

queries = ['在霸总文学里装弯', '装弯后霸总自我攻略了']

# 1. Test DMXS
for q in queries:
    try:
        url = 'https://www.dmxs.org/search.html?searchkey=' + urllib.parse.quote(q.encode('gb18030'))
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('gb18030', errors='ignore')
        matches = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', html)
        print(f"DMXS query '{q}' matches:")
        for href, title in matches:
            if any(k in title for k in ['霸总', '装弯', '蔺唯']):
                print(f"  {title}: {href}")
    except Exception as e:
        print(f"DMXS error {q}: {e}")

# 2. Test 52shuku
for q in queries:
    try:
        url = 'https://www.52shuku.vip/search/' + urllib.parse.quote(q)
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', html)
        print(f"52shuku query '{q}' matches:")
        for href, title in matches:
            if any(k in title for k in ['霸总', '装弯', '蔺唯']):
                print(f"  {title}: {href}")
    except Exception as e:
        print(f"52shuku error {q}: {e}")
