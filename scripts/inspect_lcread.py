import urllib.request
import re

url = "https://lcread.com/bookpage/273136/index.html"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('gbk', errors='ignore')

# print sections around chapters or description
print("Page text snippet:")
clean = re.sub(r'<[^>]+>', '\n', html)
lines = [l.strip() for l in clean.split('\n') if l.strip()]
for l in lines[:50]:
    print(l)
