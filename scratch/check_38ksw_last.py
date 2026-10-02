import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://www.38ksw.com/95357591/469749877.html'
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('gbk', errors='ignore')
m = re.search(r'<div id="chaptercontent"[^>]*>(.*?)</div>', html, re.DOTALL)
if m:
    text = re.sub(r'<.*?>', '\n', m.group(1))
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    print(f"Total lines: {len(lines)}")
    for l in lines[:10]:
        print("  Start:", l)
    for l in lines[-10:]:
        print("  End:", l)
else:
    print("Match failed")
