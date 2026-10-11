import urllib.request
import re
import html
import time
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')

GMT7 = timezone(timedelta(hours=7))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'tra-nam-này-không-đáng-được-tẩy-trắng')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.dmxs.org/cycs/10452.html'
}

TOTAL_PAGES = 171

def fetch_chapter(idx):
    url = f'https://www.dmxs.org/view/6-10452-{idx}.html'
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                html_str = content.decode('gb18030', errors='ignore')

            # Extract chapter title
            title = f"渣男不配洗白 第{idx}章"
            tm = re.search(r'<div class="read_chapterName[^"]*">\s*<h1>(.*?)</h1>', html_str, re.DOTALL)
            if tm:
                raw_t = re.sub(r'<[^>]+>', '', tm.group(1)).strip()
                if raw_t:
                    title = raw_t

            # Extract detail
            cm = re.search(r'<div class="read_chapterDetail">(.*?)</div>', html_str, re.DOTALL)
            if not cm:
                raise ValueError("Could not find read_chapterDetail in page")

            body = cm.group(1)
            paras = re.findall(r'<p>(.*?)</p>', body, re.DOTALL)
            cleaned_paras = []
            for p in paras:
                p_clean = re.sub(r'<[^>]+>', '', p)
                p_clean = html.unescape(p_clean).strip()
                p_clean = re.sub(r'^[　\s]+', '', p_clean)
                if p_clean:
                    cleaned_paras.append(p_clean)

            return {
                'idx': idx,
                'title': title,
                'url': url,
                'paragraphs': cleaned_paras,
                'error': None
            }
        except Exception as e:
            if attempt == 3:
                return {
                    'idx': idx,
                    'title': f"渣男不配洗白 第{idx}章",
                    'url': url,
                    'paragraphs': [],
                    'error': str(e)
                }
            time.sleep(1 + attempt)

def main():
    print(f"Starting crawl for {TOTAL_PAGES} chapters from dmxs.org...")
    start_time = time.time()
    results = {}

    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_idx = {executor.submit(fetch_chapter, i): i for i in range(1, TOTAL_PAGES + 1)}
        completed_count = 0
        for future in as_completed(future_to_idx):
            res = future.result()
            idx = res['idx']
            results[idx] = res
            completed_count += 1
            if completed_count % 20 == 0 or completed_count == TOTAL_PAGES:
                print(f"Progress: {completed_count}/{TOTAL_PAGES} chapters crawled...")

    print("Crawl completed! Now saving chapters to project folders...")

    failed = [idx for idx, r in results.items() if r['error']]
    if failed:
        print(f"Warning: {len(failed)} chapters failed: {failed}")
        # Retry failed ones sequentially
        for f_idx in failed:
            print(f"Retrying chapter {f_idx}...")
            r = fetch_chapter(f_idx)
            results[f_idx] = r

    # Save to disk
    full_text_lines = []
    now_iso = datetime.now(GMT7).isoformat()

    for idx in range(1, TOTAL_PAGES + 1):
        res = results[idx]
        ch_id = f"ch_{idx:03d}"
        ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
        os.makedirs(ch_dir, exist_ok=True)

        title = res['title']
        paras = res['paragraphs']

        # source.md
        source_content = f"# {title}\n\n" + "\n\n".join(paras) + "\n"
        with open(os.path.join(ch_dir, 'source.md'), 'w', encoding='utf-8') as f:
            f.write(source_content)

        # meta.json
        meta = {
            "chapter_id": ch_id,
            "title": title,
            "imported_at": now_iso,
            "status": "SOURCE_READY",
            "n_paragraphs": len(paras),
            "source_url": res['url']
        }
        with open(os.path.join(ch_dir, 'meta.json'), 'w', encoding='utf-8') as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)

        # Accumulate for full TXT
        full_text_lines.append(f"=== {title} ===\n\n" + "\n\n".join(paras) + "\n\n")

    # Save combined full raw
    full_raw_path = os.path.join(PROJECT_DIR, 'full_raw_171_chapters.txt')
    with open(full_raw_path, 'w', encoding='utf-8') as f:
        f.write("".join(full_text_lines))

    # Update config.json chapters_count
    cfg_path = os.path.join(PROJECT_DIR, 'config.json')
    if os.path.exists(cfg_path):
        with open(cfg_path, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        cfg['chapters_count'] = TOTAL_PAGES
        cfg['raw_links']['dmxs_series'] = 'https://www.dmxs.org/cycs/10452.html'
        with open(cfg_path, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)

    elapsed = time.time() - start_time
    print(f"All {TOTAL_PAGES} chapters successfully saved in {elapsed:.2f}s!")
    print(f"Per-chapter dirs: {CHAPTERS_DIR}/ch_001 .. ch_{TOTAL_PAGES:03d}")
    print(f"Full combined raw: {full_raw_path}")

if __name__ == '__main__':
    main()
