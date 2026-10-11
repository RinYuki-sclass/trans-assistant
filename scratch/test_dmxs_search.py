import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.dmxs.org/',
    'Origin': 'https://www.dmxs.org'
}

queries = ['在霸总文学里装弯', '装弯后霸总', '半斤墨水', '蔺唯']

for q in queries:
    data = urllib.parse.urlencode({
        'keyboard': q.encode('gb2312', errors='replace'),
        'show': 'title',
        'classid': '0'
    }).encode('ascii')
    
    req = urllib.request.Request('https://www.dmxs.org/e/search/indexsearch.php', data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            final_url = r.geturl()
            html = r.read().decode('gb18030', errors='ignore')
            print(f"Query: {q} -> Final URL: {final_url}, len: {len(html)}")
            matches = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
            for href, text in matches:
                clean_text = re.sub(r'<[^>]+>', '', text).strip()
                if any(k in clean_text for k in ['霸总', '装弯', '蔺唯', '半斤']):
                    print(f"   Match: {clean_text} -> {href}")
    except Exception as e:
        print(f"Error {q}: {e}")
