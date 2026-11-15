import urllib.request
import re

url = "https://www.52shuku.net/xiandaidushi/9065_2.html"
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("Length:", len(html))
# find all class in div or article
classes = re.findall(r'<(?:div|article|section)[^>]*class=[\'"]([^\'"]+)[\'"]', html)
print("Classes:", set(classes))

# Look for p tags
p_tags = re.findall(r'<p>(.*?)</p>', html, re.DOTALL)
print("P tags count:", len(p_tags))
for p in p_tags[:5]:
    print("P:", p.strip()[:100])
