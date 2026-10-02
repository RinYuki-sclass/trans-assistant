import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = 'https://www.jjwxc.net/onebook.php?novelid=9498243'
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('gbk', errors='ignore')

# Match table rows for chapters
# <tr onmouseover="..." itemprop="itemListElement"> ... <td itemprop="headline"> ...
chapters = re.findall(r'<td\s+itemprop="headline"[^>]*>\s*<a[^>]*>(.*?)</a>', html)
if not chapters:
    # try another regex
    chapters = re.findall(r'<a\s+href="[^"]*novelid=9498243&chapterid=\d+"[^>]*>(.*?)</a>', html)

print(f"Total chapters found on JJWXC: {len(chapters)}")
for i, ch in enumerate(chapters, 1):
    print(f"{i}: {ch.strip()}")
