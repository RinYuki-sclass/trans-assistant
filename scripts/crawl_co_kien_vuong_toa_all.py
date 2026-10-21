import urllib.request
from bs4 import BeautifulSoup
import re
import concurrent.futures
import time
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_page(page_num):
    url = f"https://www.52shuku.net/jiakong/hz8x_{page_num}.html"
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            article = soup.find('article')
            if not article:
                return page_num, []
            paras = []
            for p in article.find_all('p'):
                text = p.get_text(strip=True)
                if not text:
                    continue
                if '52shuku' in text.lower() or 'tips：' in text.lower() or '传送门' in text or '如果觉得52' in text:
                    continue
                if '《基建王座》作者：' in text or '文案：' in text or '一句话简介：' in text or '立意：' in text:
                    continue
                paras.append(text)
            return page_num, paras
        except Exception as e:
            time.sleep(1.5)
    return page_num, []

print("=== BẮT ĐẦU CÀO RAW TOÀN BỘ BỘ TRUYỆN CƠ KIẾN VƯƠNG TỌA (PAGES 2 - 317) ===")
start_time = time.time()
pages_data = {}

with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
    futures = {executor.submit(fetch_page, p): p for p in range(2, 318)}
    for future in concurrent.futures.as_completed(futures):
        p_num, p_paras = future.result()
        pages_data[p_num] = p_paras

print(f"-> Hoàn thành tải {len(pages_data)} trang web trong {time.time() - start_time:.2f}s")

# Sắp xếp đoạn văn theo thứ tự các trang
all_paras = []
for p in range(2, 318):
    all_paras.extend(pages_data.get(p, []))

print(f"-> Tổng số đoạn văn trích xuất: {len(all_paras)}")

chapter_pattern = re.compile(r'^(第\s*(\d+)\s*章\s*.*|番外\s*.*)')

chapters = {}
current_ch_num = 0
current_paras = []

for p in all_paras:
    m = chapter_pattern.match(p)
    if m:
        if current_ch_num > 0 and current_paras:
            chapters[current_ch_num] = current_paras
        
        if m.group(2):
            current_ch_num = int(m.group(2))
        else:
            current_ch_num += 1
            
        current_paras = [p]
        continue
    
    if current_ch_num > 0:
        current_paras.append(p)

if current_ch_num > 0 and current_paras:
    chapters[current_ch_num] = current_paras

print(f"-> Tổng số chương hợp lệ nhận diện được: {len(chapters)}")

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\cơ-kiến-vương-tọa\chapters"
os.makedirs(base_dir, exist_ok=True)

for ch_num, paras in sorted(chapters.items()):
    ch_slug = f"ch_{ch_num:03d}"
    ch_dir = os.path.join(base_dir, ch_slug)
    os.makedirs(ch_dir, exist_ok=True)
    source_path = os.path.join(ch_dir, "source.md")
    
    content = "\n\n".join(paras)
    with open(source_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"-> Đã lưu toàn bộ {len(chapters)} chương vào {base_dir}")

# Cập nhật config.json
config_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\cơ-kiến-vương-tọa\config.json"
if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    config["chapters_count"] = len(chapters)
    config["raw_links"]["52shuku"] = "https://www.52shuku.net/jiakong/hz8x.html"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    print("-> Đã cập nhật config.json với chapters_count =", len(chapters))

print("=== HOÀN TẤT 100% CÀO TOÀN BỘ RAW ===")
