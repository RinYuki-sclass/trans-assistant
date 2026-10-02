import urllib.request
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')
cache_dir = r"d:\Nhung\RIDI\trans-assistant\scratch\talebed_cache"
os.makedirs(cache_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for page in range(1, 112):
    cache_file = os.path.join(cache_dir, f"page_{page:03d}.html")
    if os.path.exists(cache_file) and os.path.getsize(cache_file) > 1000:
        continue
    
    url = f"https://www.talebed.com/read/272625/{page}"
    success = False
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                if b'class="read-content"' in content:
                    with open(cache_file, "wb") as f:
                        f.write(content)
                    print(f"Downloaded page {page:03d} ({len(content)} bytes)")
                    success = True
                    break
                else:
                    print(f"Page {page:03d} missing read-content, retrying...")
                    time.sleep(2)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"Page {page:03d} hit 429, waiting 3s... (attempt {attempt+1})")
                time.sleep(3)
            else:
                print(f"Page {page:03d} HTTP error {e.code}, waiting 2s...")
                time.sleep(2)
        except Exception as e:
            print(f"Page {page:03d} error: {e}, waiting 2s...")
            time.sleep(2)
            
    if not success:
        print(f"FAILED to download page {page:03d}")
    time.sleep(0.3)

print("All pages cached successfully!")
