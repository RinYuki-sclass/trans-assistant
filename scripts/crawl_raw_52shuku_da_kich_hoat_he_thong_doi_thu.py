import os
import sys
import re
import json
import time
import argparse
from datetime import datetime, timezone, timedelta
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

GMT7 = timezone(timedelta(hours=7))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'đã-kích-hoạt-hệ-thống-đổi-thụ')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
JJWXC_INFO_PATH = os.path.join(PROJECT_DIR, 'jjwxc_chapters.json')

os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Load JJWXC info
JJWXC_MAP = {}
if os.path.exists(JJWXC_INFO_PATH):
    try:
        with open(JJWXC_INFO_PATH, 'r', encoding='utf-8') as f:
            raw_map = json.load(f)
            JJWXC_MAP = {int(k): v for k, v in raw_map.items()}
    except Exception as e:
        print(f"Warning: Could not load {JJWXC_INFO_PATH}: {e}")

PAGE_CACHE = {}

def clean_paragraph_text(raw_text):
    text = raw_text.replace('\xa0', ' ')
    text = re.split(r'目录\s+上一页', text)[0]
    text = re.split(r'哦豁[，,]小伙伴们', text)[0]
    text = re.split(r'传送门[：:]', text)[0]
    text = re.split(r'Tips[：:]', text)[0]
    return text.strip()

def fetch_page_paras(page_num):
    if page_num in PAGE_CACHE:
        return PAGE_CACHE[page_num]
    
    url = f"https://www.52shuku.net/chongsheng/29_b/bkc90_{page_num}.html" if page_num > 1 else "https://www.52shuku.net/chongsheng/29_b/bkc90.html"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        soup = BeautifulSoup(html, 'html.parser')
        art = soup.find('article', class_='article-content')
        if not art:
            PAGE_CACHE[page_num] = []
            return []
        
        paras = []
        for p in art.find_all('p'):
            cleaned = clean_paragraph_text(p.get_text())
            for line in cleaned.splitlines():
                line = line.strip()
                if line and not line.startswith("目录") and "52书库" not in line and "传送门" not in line and "Tips：" not in line:
                    paras.append(line)
        PAGE_CACHE[page_num] = paras
        return paras

def find_chapter_start_page(ch_num, approx_page=None):
    if approx_page is None:
        approx_page = max(1, int(ch_num * 1.85))
    
    target_pattern = re.compile(r'第\s*' + str(ch_num) + r'\s*章')
    
    # Search around approx_page (-5 to +10)
    for delta in range(0, 20):
        for sign in [-1, 1]:
            p = approx_page + delta * sign
            if p < 1 or p > 288:
                continue
            paras = fetch_page_paras(p)
            for text in paras:
                if target_pattern.search(text):
                    return p
    return None

def extract_chapter_content(ch_num, start_page):
    target_header = re.compile(r'第\s*' + str(ch_num) + r'\s*章')
    next_header = re.compile(r'第\s*' + str(ch_num + 1) + r'\s*章')
    
    ch_paras = []
    recording = False
    cur_page = start_page
    
    while cur_page <= 288:
        paras = fetch_page_paras(cur_page)
        for p in paras:
            if not recording and target_header.search(p):
                recording = True
                rem = target_header.sub('', p).strip()
                if rem:
                    ch_paras.append(rem)
                continue
            
            if recording and next_header.search(p):
                recording = False
                return ch_paras, cur_page
                
            if recording:
                ch_paras.append(p)
                
        cur_page += 1
        
    return ch_paras, cur_page

def save_chapter(ch_num, paras, start_page):
    ch_id = f"ch_{ch_num:03d}"
    ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
    os.makedirs(ch_dir, exist_ok=True)
    
    info = JJWXC_MAP.get(ch_num, {})
    ch_cn_title = info.get("desc", "").strip()
    words_expected = info.get("words", "")
    
    full_title_vn = f"Đã Kích Hoạt Hệ Thống Đổi Thụ — Chương {ch_num}: {ch_cn_title}" if ch_cn_title else f"Đã Kích Hoạt Hệ Thống Đổi Thụ — Chương {ch_num}"
    source_url = f"https://www.52shuku.net/chongsheng/29_b/bkc90_{start_page}.html"
    
    source_path = os.path.join(ch_dir, 'source.md')
    content_lines = [
        "---",
        f"title: '{full_title_vn}'",
        f"source_url: '{source_url}'",
        f"chinese_title: '第 {ch_num} 章 {ch_cn_title}'",
        f"chapter_number: {ch_num}",
        "---",
        "",
        f"第{ch_num}章 {ch_cn_title}",
        ""
    ]
    for p in paras:
        content_lines.append(p)
        content_lines.append("")
        
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(content_lines).strip() + "\n")
        
    now_iso = datetime.now(GMT7).isoformat()
    meta_path = os.path.join(ch_dir, 'meta.json')
    meta = {
        "chapter_number": ch_num,
        "title": full_title_vn,
        "chinese_title": f"第 {ch_num} 章 {ch_cn_title}",
        "status": "raw_saved",
        "created_at": now_iso,
        "word_count": sum(len(p) for p in paras),
        "source": "52shuku"
    }
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
        
    print(f"✅ Saved Chương {ch_num:03d} ({ch_cn_title}): {len(paras)} đoạn, {meta['word_count']} chữ (gốc: ~{words_expected}) -> page {start_page}")

def crawl_range(start_ch, end_ch):
    cur_p = None
    for ch in range(start_ch, end_ch + 1):
        p_start = find_chapter_start_page(ch, cur_p)
        if not p_start:
            print(f"❌ Không tìm thấy chương {ch} trên 52shuku!")
            continue
        paras, next_p = extract_chapter_content(ch, p_start)
        save_chapter(ch, paras, p_start)
        cur_p = p_start

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl raw chapters from 52shuku for Đã Kích Hoạt Hệ Thống Đổi Thụ")
    parser.add_argument("--start", type=int, default=41, help="Start chapter number (default: 41)")
    parser.add_argument("--end", type=int, default=45, help="End chapter number (default: 45)")
    args = parser.parse_args()
    
    print(f"Bắt đầu crawl từ chương {args.start} đến {args.end}...")
    crawl_range(args.start, args.end)
