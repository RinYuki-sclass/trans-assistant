import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://www.jjwxc.net/onebook.php?novelid=9498243'
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('gb18030', errors='ignore')

matches = re.findall(r'<tr[^>]*>.*?</tr>', html, re.DOTALL)
print(f"Total tr: {len(matches)}")
for tr in matches:
    if 'chapterid=' in tr:
        # extract title
        t = re.findall(r'<a[^>]*href="[^"]*chapterid=(\d+)"[^>]*>(.*?)</a>', tr)
        tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL)
        td_texts = [re.sub(r'<.*?>', '', td).strip() for td in tds]
        print(f"Ch: {t} | Text: {td_texts[:3]}")
