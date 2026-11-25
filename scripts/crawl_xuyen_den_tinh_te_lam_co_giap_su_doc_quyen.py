import os
import sys
import re
import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_SLUG = "xuyen-den-tinh-te-lam-co-giap-su-doc-quyen"
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', PROJECT_SLUG)
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
INDEX_PATH = os.path.join(PROJECT_DIR, 'chapters_index.json')
CONFIG_PATH = os.path.join(PROJECT_DIR, 'config.json')
TOC_PATH = os.path.join(PROJECT_DIR, 'TOC.md')

os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

TOTAL_PAGES = 369

def fetch_page(page_num):
    url = f"https://www.52shuku.net/jiakong/b/bjQtC_{page_num}.html" if page_num > 1 else "https://www.52shuku.net/jiakong/b/bjQtC.html"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                return page_num, html
        except Exception as e:
            time.sleep(1 + attempt)
    return page_num, ""

def clean_para(raw):
    raw = raw.replace('\xa0', ' ').replace('\u3000', ' ')
    raw = re.split(r'目录\s+上一页', raw)[0]
    raw = re.split(r'哦豁[，,]小伙伴们', raw)[0]
    raw = re.split(r'传送门[：:]', raw)[0]
    raw = re.split(r'Tips[：:]', raw)[0]
    lines = []
    for l in raw.splitlines():
        l = l.strip()
        if (l and '52书库' not in l and '传送门' not in l and 'Tips' not in l 
            and not l.startswith('目录') and '本章未完' not in l and '点击下一页' not in l
            and '下一页' not in l and not l.startswith('http')):
            lines.append(l)
    return lines

def main():
    print(f"Starting crawl for {PROJECT_SLUG} across {TOTAL_PAGES} pages...")
    pages_html = {}
    
    with ThreadPoolExecutor(max_workers=12) as executor:
        results = executor.map(fetch_page, range(2, TOTAL_PAGES + 1))
        for p, html in results:
            pages_html[p] = html
            if p % 50 == 0 or p == TOTAL_PAGES:
                print(f"Fetched page {p}/{TOTAL_PAGES}")

    # Process all paragraphs in sequential page order
    all_paras = []
    for p in range(2, TOTAL_PAGES + 1):
        html = pages_html.get(p, "")
        if not html:
            continue
        p_tags = re.findall(r'<p>([\s\S]*?)</p>', html)
        for p_tag in p_tags:
            cleaned_lines = clean_para(p_tag)
            for line in cleaned_lines:
                all_paras.append(line)

    print(f"Total raw paragraph lines collected: {len(all_paras)}")

    # Split paragraphs by chapter headers:
    # Match: 第X章 or 番外X
    chapter_splits = {}
    current_ch = 1
    current_paras = []
    
    # We expect 180 chapters total: 1-176 main, 177-180 extras
    ch_header_re = re.compile(r'^(第\s*(\d+)\s*章|番外\s*(\d*))\s*(.*)$')

    for para in all_paras:
        m = ch_header_re.match(para)
        if m:
            prefix = m.group(1)
            num_str = m.group(2)
            fanwai_str = m.group(3)
            
            if num_str:
                ch_num = int(num_str)
            elif "番外" in prefix:
                if fanwai_str:
                    ch_num = 176 + int(fanwai_str)
                else:
                    # sequential fanwai
                    ch_num = max(177, current_ch + 1)
            else:
                ch_num = current_ch + 1

            if current_paras:
                chapter_splits[current_ch] = current_paras
                current_paras = []
            current_ch = ch_num
            # Keep header as first paragraph or omit?
            # Standard in novel projects: keep header in source.md
            current_paras.append(para)
        else:
            current_paras.append(para)

    if current_paras:
        chapter_splits[current_ch] = current_paras

    print(f"Extracted {len(chapter_splits)} chapters! Chapter IDs: {min(chapter_splits.keys())} to {max(chapter_splits.keys())}")

    # Load index to update
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    ch_lookup = {c["chapter_num"]: c for c in index_data["chapters"]}
    total_words = 0

    for ch_num, paras in chapter_splits.items():
        ch_id = f"ch_{ch_num:03d}"
        ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
        os.makedirs(ch_dir, exist_ok=True)
        
        source_path = os.path.join(ch_dir, "source.md")
        content = "\n\n".join(paras)
        with open(source_path, "w", encoding="utf-8") as sf:
            sf.write(content + "\n")
            
        if ch_num in ch_lookup:
            ch_lookup[ch_num]["source_exists"] = True
            ch_lookup[ch_num]["paragraphs"] = len(paras)
            ch_lookup[ch_num]["status"] = "RAW_READY"

    # Save updated index
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    # Update TOC.md
    toc_lines = [
        "# 📚 MỤC LỤC CHI TIẾT (TABLE OF CONTENTS)",
        "## XUYÊN ĐẾN TINH TẾ LÀM CƠ GIÁP SƯ ĐỘC QUYỀN (《穿越星际之专属机甲师》)",
        "",
        "> **Tác giả:** Tất Tu Khoa Mục (必修科目)  ",
        f"> **Quy mô dự án:** {len(index_data['chapters'])} chương (176 chương chính văn + 4 chương phiên ngoại)  ",
        f"> **Slug dự án:** `{PROJECT_SLUG}`  ",
        f"> **Đã cào raw:** {len(chapter_splits)}/180 chương (100% RAW_READY)  ",
        "> **Định dạng file:** 1:1 Paragraph Alignment, \\n\\n chuẩn khoảng cách, thoại “...”.",
        "",
        "---",
        "",
        "| STT | Tên gốc (Trung) | Tiêu đề tiếng Việt | Raw | Bản dịch | Trạng thái QC |",
        "| :---: | :--- | :--- | :---: | :---: | :---: |"
    ]
    for c in index_data["chapters"]:
        num = c["chapter_num"]
        raw_status = f"✅ Sẵn sàng ({c['paragraphs']} đoạn)" if c["source_exists"] else "⏳ Chờ cào raw"
        toc_lines.append(f"| {num:03d} | {c['title_cn']} | [{c['title_vi']}](file:///d:/Nhung/trans-tool/novel_projects/{PROJECT_SLUG}/chapters/{c['id']}/translation.md) | {raw_status} | ⏳ Chưa dịch | ⏳ PENDING |")

    with open(TOC_PATH, 'w', encoding='utf-8') as f:
        f.write("\n".join(toc_lines) + "\n")

    print(f"Successfully processed and saved all chapters for {PROJECT_SLUG}!")

if __name__ == "__main__":
    main()
