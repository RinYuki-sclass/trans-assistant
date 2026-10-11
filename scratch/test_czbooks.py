import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

queries = ['在霸總文學裡裝彎', '在霸总文学里装弯', '半斤墨水', '裝彎後霸總自我攻略了']

for q in queries:
    u = 'https://czbooks.net/s/' + urllib.parse.quote(q)
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        print(f"czbooks query '{q}' len: {len(html)}")
        links = re.findall(r'<a[^>]+href="(/n/[^"]+)"[^>]*>(.*?)</a>', html)
        for href, title in links:
            print(f"  {title.strip()}: https://czbooks.net{href}")
    except Exception as e:
        print(f"czbooks error '{q}': {e}")
