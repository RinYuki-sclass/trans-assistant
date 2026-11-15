import urllib.request
import re
import html
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_text(t):
    t = html.unescape(t)
    t = t.replace('&nbsp;', ' ').replace('&hellip;', '…').replace('&mdash;', '—').replace('&ldquo;', '“').replace('&rdquo;', '”')
    return t.strip()

def fetch_page(page_idx):
    url = f"https://www.52shuku.net/xiandaidushi/9065_{page_idx}.html"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
                p_tags = re.findall(r'<p>(.*?)</p>', content, re.DOTALL)
                clean_lines = []
                for p in p_tags:
                    cl = re.sub(r'<[^>]+>', '', p)
                    cl = clean_text(cl)
                    if not cl:
                        continue
                    if any(k in cl for k in ['52书库', '传送门：', '目录 上一页', '阅读记录', '上一页 下一页', '尾页']):
                        continue
                    clean_lines.append(cl)
                return page_idx, clean_lines
        except Exception as e:
            time.sleep(1)
    return page_idx, []

print("Starting download of pages 2 to 306...")
start_time = time.time()
pages_data = {}

with ThreadPoolExecutor(max_workers=15) as executor:
    futures = {executor.submit(fetch_page, p): p for p in range(2, 307)}
    for f in as_completed(futures):
        pidx, lines = f.result()
        pages_data[pidx] = lines
        if len(pages_data) % 50 == 0 or len(pages_data) == 305:
            print(f"Downloaded {len(pages_data)}/305 pages in {time.time()-start_time:.1f}s")

# Assemble all lines in page order
all_lines = []
for pidx in range(2, 307):
    all_lines.extend(pages_data.get(pidx, []))

print(f"Total lines extracted: {len(all_lines)}")

# Let's inspect chapter headings in all_lines
ch_pattern = re.compile(r'^(第\s*[0-9零一二三四五六七八九十百千万]+\s*[章回节]|番外)')
chapters_found = []
for idx, line in enumerate(all_lines):
    if ch_pattern.match(line) and len(line) < 60:
        chapters_found.append((idx, line))

print(f"Total chapter headings identified: {len(chapters_found)}")
for i, (lidx, h) in enumerate(chapters_found[:10]):
    print(f"  {i+1}: {h}")
print("  ...")
for i, (lidx, h) in enumerate(chapters_found[-5:], start=len(chapters_found)-4):
    print(f"  {i}: {h}")
