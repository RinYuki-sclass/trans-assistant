import urllib.request
import re
import html
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.52shuku.net/chongsheng/07_b/bjVPq.html'
}

# Let's inspect pages around chapter headings or find all chapter headings
# First, let's see how chapters are demarcated in 52shuku: "第X章" or "第 X 章"
# Let's sample every 10 pages or scan for "第" and "章"
print("Scanning pages 2 to 222...")
for page in [2, 10, 50, 100, 150, 200, 210, 215, 220, 222]:
    u = f'https://www.52shuku.net/chongsheng/07_b/bjVPq_{page}.html'
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            html_str = r.read().decode('utf-8', errors='ignore')
        # find any line matching 第...章
        ch_matches = re.findall(r'(第\s*\d+\s*章[^\n<]*)', html_str)
        fanwai_matches = re.findall(r'(番外[^\n<]*)', html_str)
        print(f"Page {page}: ch={ch_matches[:2]}, fw={fanwai_matches[:2]}")
    except Exception as e:
        print(f"Page {page}: Error {e}")
