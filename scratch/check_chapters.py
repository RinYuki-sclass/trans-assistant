import urllib.request, re, sys
sys.stdout.reconfigure(encoding='utf-8')
req = urllib.request.Request('https://www.talebed.com/read/272625/1', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
m = re.search(r'<div class="read-content">(.*?)</div>\s*</div>\s*<div class="px-6', html, re.DOTALL)
paragraphs = re.findall(r'<p>(.*?)</p>', m.group(1))
for i in range(50, min(70, len(paragraphs))):
    print(f"{i}: {paragraphs[i]}")
