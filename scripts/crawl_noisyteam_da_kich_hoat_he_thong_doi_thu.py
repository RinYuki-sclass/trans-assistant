import os
import sys
import re
import json
import time
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

GMT7 = timezone(timedelta(hours=7))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'đã-kích-hoạt-hệ-thống-đổi-thụ')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
os.makedirs(CHAPTERS_DIR, exist_ok=True)

INDEX_URL = 'https://noisyteam.wordpress.com/he-thong-da-kich-hoat-he-thong-doi-thu/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def get_chapter_links():
    res = requests.get(INDEX_URL, headers=HEADERS, timeout=20)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    
    links_map = {}
    for a in soup.find_all('a'):
        text = a.get_text(strip=True)
        href = a.get('href', '')
        if 'Chương ' in text and 'noisyteam.wordpress.com' in href:
            m = re.search(r'Chương\s+(\d+)', text)
            if m:
                ch_num = int(m.group(1))
                if ch_num not in links_map:
                    links_map[ch_num] = href.strip()
    
    sorted_chapters = sorted(links_map.items(), key=lambda x: x[0])
    return sorted_chapters

def clean_paragraph(text):
    text = text.replace('\xa0', ' ')
    text = re.sub(r'^[　\s]+', '', text)
    text = re.sub(r'[　\s]+$', '', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text

def parse_chapter_page(ch_num, url):
    res = requests.get(url, headers=HEADERS, timeout=20)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    
    entry = soup.find('div', class_='entry-content')
    if not entry:
        raise ValueError(f"No entry-content in {url}")
    
    # Remove unwanted tags
    for tag in list(entry.find_all(['style', 'script', 'figure', 'noscript'])):
        tag.decompose()
        
    for tag in list(entry.find_all('div')):
        if not tag or not getattr(tag, 'attrs', None):
            continue
        classes = tag.attrs.get('class') or []
        id_val = tag.attrs.get('id') or ''
        if any(c in classes for c in ['sharedaddy', 'jp-relatedposts', 'cs-rating', 'wp-block-columns', 'post-navigation-link']) or 'atatags' in id_val or 'jp-post-flair' in id_val:
            tag.decompose()
        
    paragraphs = []
    chapter_title = f"Chương {ch_num}"
    
    for elem in entry.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'blockquote', 'hr']):
        txt = elem.get_text().strip()
        if not txt:
            continue
        
        # Check for title
        if re.search(rf'Chương\s+{ch_num}\s*[:：]?', txt, re.IGNORECASE) and len(txt) < 80:
            chapter_title = txt.strip(': ')
            continue
            
        # Filter editor noise & footer artifacts
        if any(noise in txt for noise in [
            'Edit: Noisy Team',
            'Edited by Noisy Team',
            'Bạn đang đọc truyện tại Noisy',
            'Chia sẻ bài viết',
            'Like this:',
            'Loading...',
            'Đã kích hoạt hệ thống đổi thụ – Chương',
            'Related'
        ]):
            continue
            
        # Skip horizontal separator lines or empty lines
        if txt in ['---', '***', '___', '——']:
            continue
            
        cleaned = clean_paragraph(txt)
        if cleaned:
            paragraphs.append(cleaned)
            
    return chapter_title, paragraphs

def save_chapter(ch_num, chapter_title, paragraphs, url):
    ch_dir_name = f"ch_{ch_num:03d}"
    ch_folder = os.path.join(CHAPTERS_DIR, ch_dir_name)
    os.makedirs(ch_folder, exist_ok=True)
    
    trans_path = os.path.join(ch_folder, 'translation.md')
    with open(trans_path, 'w', encoding='utf-8') as f:
        f.write(f"---\ntitle: 'Đã Kích Hoạt Hệ Thống Đổi Thụ — {chapter_title}'\n---\n\n")
        f.write(f"{chapter_title}\n\n")
        f.write("\n\n".join(paragraphs))
        f.write("\n")
        
    source_path = os.path.join(ch_folder, 'source.md')
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(f"---\ntitle: 'Đã Kích Hoạt Hệ Thống Đổi Thụ — {chapter_title} (Source Noisy Team)'\nsource_url: '{url}'\n---\n\n")
        f.write(f"{chapter_title}\n\n")
        f.write("\n\n".join(paragraphs))
        f.write("\n")
        
    meta_path = os.path.join(ch_folder, 'meta.json')
    meta_data = {
        'chapter_id': ch_dir_name,
        'chapter_number': ch_num,
        'title': chapter_title,
        'n_paragraphs': len(paragraphs),
        'status': 'TRANSLATED_NOISYTEAM',
        'source_translation_url': url,
        'translator': 'Noisy Team',
        'imported_at': datetime.now(GMT7).isoformat()
    }
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta_data, f, ensure_ascii=False, indent=2)

def crawl_single_chapter(item):
    ch_num, url = item
    for attempt in range(3):
        try:
            title, paras = parse_chapter_page(ch_num, url)
            save_chapter(ch_num, title, paras, url)
            return ch_num, True, len(paras), title
        except Exception as e:
            if attempt == 2:
                return ch_num, False, str(e), url
            time.sleep(1.5)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, default=1, help='Start chapter number')
    parser.add_argument('--end', type=int, default=1, help='End chapter number')
    parser.add_argument('--workers', type=int, default=4, help='Number of worker threads')
    args = parser.parse_args()
    
    print("Fetching chapter index from Noisy Team...")
    all_links = get_chapter_links()
    print(f"Total available chapters on index: {len(all_links)}")
    
    target_links = [item for item in all_links if args.start <= item[0] <= args.end]
    print(f"Targeting {len(target_links)} chapters (Chương {args.start} -> Chương {args.end})...")
    
    success = 0
    failed = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(crawl_single_chapter, item): item for item in target_links}
        for future in as_completed(futures):
            ch_num, ok, info, extra = future.result()
            if ok:
                success += 1
                print(f"[SUCCESS] Chương {ch_num:03d}: '{extra}' ({info} đoạn)")
            else:
                failed.append((ch_num, info, extra))
                print(f"[FAILED] Chương {ch_num:03d}: Error {info} - {extra}")
                
    print(f"\nDone! Successfully saved {success}/{len(target_links)} chapters to {CHAPTERS_DIR}.")
    if failed:
        print(f"Failed chapters: {failed}")

if __name__ == '__main__':
    main()
