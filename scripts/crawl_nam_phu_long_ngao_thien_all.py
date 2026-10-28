import urllib.request
import re
import html
import os
import sys
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')

GMT7 = timezone(timedelta(hours=7))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'nam-phụ-khiến-long-ngạo-thiên-mang-thai')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
CACHE_DIR = os.path.join(BASE_DIR, 'scratch', 'pages_cache')
os.makedirs(CHAPTERS_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.52shuku.net/chongsheng/07_b/bjTU9.html'
}

TOTAL_PAGES = 313

def clean_paragraph(raw_p):
    p = re.sub(r'<[^>]+>', '', raw_p)
    p = html.unescape(p).strip()
    p = re.sub(r'^[　\s]+', '', p)
    return p

def fetch_single_page(page_num):
    cache_file = os.path.join(CACHE_DIR, f"page_{page_num}.json")
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                return page_num, json.load(f)
        except Exception:
            pass

    url = f"https://www.52shuku.net/chongsheng/07_b/bjTU9_{page_num}.html"
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                text = resp.read().decode('utf-8', errors='ignore')
                raw_paras = re.findall(r'<p>(.*?)</p>', text)
                cleaned = []
                for p in raw_paras:
                    cp = clean_paragraph(p)
                    if not cp:
                        continue
                    if '52书库' in cp or '排行榜单' in cp or 'www.52shuku.net' in cp or '传送门' in cp or 'Tips：' in cp:
                        continue
                    if cp.startswith('《男配让龙傲天') and page_num == 2 and len(cp) < 40:
                        continue
                    cleaned.append(cp)
                
                with open(cache_file, 'w', encoding='utf-8') as f:
                    json.dump(cleaned, f, ensure_ascii=False)
                return page_num, cleaned
        except Exception as e:
            if attempt == 3:
                print(f"Error fetching page {page_num}: {e}")
                return page_num, []
            time.sleep(1 + attempt)
    return page_num, []

def crawl_all_pages():
    print(f"Fetching pages 2 to {TOTAL_PAGES}...")
    pages_data = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_single_page, p): p for p in range(2, TOTAL_PAGES + 1)}
        done_count = 0
        for f in as_completed(futures):
            p_num, paras = f.result()
            pages_data[p_num] = paras
            done_count += 1
            if done_count % 30 == 0 or done_count == len(futures):
                print(f"Progress: {done_count}/{len(futures)} pages fetched.")
    return pages_data

def segment_into_chapters(pages_data):
    # Flatten all paragraphs in order
    all_paras = []
    for p_num in range(2, TOTAL_PAGES + 1):
        all_paras.extend(pages_data.get(p_num, []))

    print(f"Total raw paragraphs across all pages: {len(all_paras)}")

    # We skip metadata before 第1章
    start_idx = -1
    for i, p in enumerate(all_paras):
        if re.match(r'^第\s*1\s*章', p):
            start_idx = i
            break
    
    if start_idx != -1:
        print(f"Found 第1章 at index {start_idx}. Truncating preceding text.")
        all_paras = all_paras[start_idx:]

    chapters = []
    current_ch = None

    chapter_pattern = re.compile(r'^(第\s*\d+\s*章.*|番外.*)$')

    for p in all_paras:
        m = chapter_pattern.match(p)
        if m:
            if current_ch:
                chapters.append(current_ch)
            header_text = p.strip()
            current_ch = {
                'title_zh': header_text,
                'paragraphs': [header_text]
            }
        else:
            if current_ch:
                current_ch['paragraphs'].append(p)
            else:
                # If before any chapter header
                current_ch = {
                    'title_zh': '第 1 章',
                    'paragraphs': ['第 1 章', p]
                }

    if current_ch:
        chapters.append(current_ch)

    print(f"Segmented into {len(chapters)} chapters.")
    return chapters

def save_chapters(chapters):
    chapter_index_list = []
    
    # Read existing chapters_index.json to keep translation/qc status of ch_001
    existing_index_path = os.path.join(PROJECT_DIR, 'chapters_index.json')
    existing_statuses = {}
    if os.path.exists(existing_index_path):
        try:
            with open(existing_index_path, 'r', encoding='utf-8') as f:
                d = json.load(f)
                for c in d.get('chapters', []):
                    existing_statuses[c['id']] = c.get('status', 'raw_ready')
        except Exception:
            pass

    toc_rows = []
    stats = {
        "pending": 0,
        "raw_ready": 0,
        "prescanned": 0,
        "translating": 0,
        "translated": 0,
        "qc_approved": 0,
        "published": 0
    }

    for idx, ch in enumerate(chapters, 1):
        ch_id = f"ch_{idx:03d}"
        ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
        os.makedirs(ch_dir, exist_ok=True)

        source_file = os.path.join(ch_dir, "source.md")
        # Save source.md
        with open(source_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(ch['paragraphs']) + "\n")

        para_count = len(ch['paragraphs'])
        word_count = sum(len(p) for p in ch['paragraphs'])
        
        status = existing_statuses.get(ch_id, "raw_ready")
        stats[status] = stats.get(status, 0) + 1

        title_vi = f"Chương {idx}: {ch['title_zh']}"
        if ch_id == "ch_001":
            title_vi = "Chương 1: Xuyên thư trói định Song Hệ Thống"

        entry = {
            "id": ch_id,
            "order": idx,
            "chapter_no": idx,
            "sub_index": None,
            "arc_id": 1,
            "arc_name": "Chính Văn",
            "title_zh": ch['title_zh'],
            "title_vi": title_vi,
            "status": status,
            "paragraph_count": para_count,
            "word_count": word_count,
            "source_url": f"https://www.52shuku.net/chongsheng/07_b/bjTU9.html",
            "updated_at": datetime.now(GMT7).isoformat()
        }
        chapter_index_list.append(entry)

        status_badge = "🟢 Đã duyệt QC" if status == "qc_approved" else ("🔵 Đã dịch" if status == "translated" else "⚪ Đã cào raw")
        link_target = f"chapters/{ch_id}/translation.md" if status in ["translated", "qc_approved"] else f"chapters/{ch_id}/source.md"
        toc_rows.append(f"| {idx} | `{ch_id}` | [{title_vi}]({link_target}) | {ch['title_zh']} | {para_count} | {status_badge} |")

    # Update chapters_index.json
    index_data = {
        "project_slug": "nam-phụ-khiến-long-ngạo-thiên-mang-thai",
        "title": "Nam Phụ Khiến Long Ngạo Thiên Mang Thai",
        "author": "Thập Ma A Lộ (什么阿路)",
        "total_chapters": len(chapters),
        "stats": stats,
        "arcs": [
            {
                "arc_id": 1,
                "arc_name": "Chính Văn & Ngoại Truyện",
                "folder_range": [
                    "ch_001",
                    f"ch_{len(chapters):03d}"
                ]
            }
        ],
        "chapters": chapter_index_list
    }

    with open(existing_index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    # Update TOC.md
    toc_path = os.path.join(PROJECT_DIR, "TOC.md")
    total = len(chapters)
    qc_count = stats.get("qc_approved", 0)
    trans_count = stats.get("translated", 0)
    raw_count = stats.get("raw_ready", 0)
    pct = round((qc_count + trans_count) / total * 100, 1) if total > 0 else 0.0

    toc_content = f"""# 📖 MỤC LỤC: Nam Phụ Khiến Long Ngạo Thiên Mang Thai
> **Tác giả:** Thập Ma A Lộ (什么阿路) | **Tiến độ:** {qc_count + trans_count}/{total} chương ({pct}%) | **Cập nhật:** {datetime.now(GMT7).strftime('%d/%m/%Y')}
> **Trạng thái:** 🟢 Đã duyệt QC ({qc_count}) | 🔵 Đã dịch ({trans_count}) | ⚪ Chưa dịch ({raw_count})

---

## 🌌 CHÍNH VĂN & NGOẠI TRUYỆN (TOÀN BỘ {total} CHƯƠNG)

| STT | Mã thư mục | Tiêu đề chương (Tiếng Việt) | Nguyên tác | Số đoạn | Trạng thái |
| :---: | :---: | :--- | :--- | :---: | :---: |
""" + "\n".join(toc_rows) + "\n"

    with open(toc_path, "w", encoding="utf-8") as f:
        f.write(toc_content)

    # Update config.json chapters_count
    config_path = os.path.join(PROJECT_DIR, "config.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            cfg["chapters_count"] = total
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(cfg, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    print(f"All done! Saved {len(chapters)} chapters, updated TOC.md and chapters_index.json.")

if __name__ == '__main__':
    data = crawl_all_pages()
    chapters = segment_into_chapters(data)
    save_chapters(chapters)
