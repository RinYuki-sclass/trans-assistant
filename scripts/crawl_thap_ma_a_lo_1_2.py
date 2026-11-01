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

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_paragraph(raw_p):
    p = re.sub(r'<[^>]+>', '', raw_p)
    p = html.unescape(p).strip()
    p = re.sub(r'^[　\s]+', '', p)
    return p

# ==============================================================================
# BOOK 1: 《路人甲压倒孤傲总裁》 (52shuku pages 2..220)
# ==============================================================================
def fetch_52shuku_page(page_num, cache_dir):
    cache_file = os.path.join(cache_dir, f"page_{page_num}.json")
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                return page_num, json.load(f)
        except Exception:
            pass

    url = f"https://www.52shuku.net/chongsheng/14_b/bjV27_{page_num}.html"
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                text = resp.read().decode('utf-8', errors='ignore')
                raw_paras = re.findall(r'<p>(.*?)</p>', text, re.S)
                cleaned = []
                for p in raw_paras:
                    cp = clean_paragraph(p)
                    if not cp:
                        continue
                    if any(skip in cp for skip in ['52书库', '排行榜单', 'www.52shuku.net', '传送门', 'Tips：']):
                        continue
                    cleaned.append(cp)
                with open(cache_file, 'w', encoding='utf-8') as f:
                    json.dump(cleaned, f, ensure_ascii=False)
                return page_num, cleaned
        except Exception as e:
            if attempt == 3:
                print(f"[Book 1] Error fetching page {page_num}: {e}")
                return page_num, []
            time.sleep(1 + attempt)
    return page_num, []

def crawl_book_1():
    slug = "người-qua-đường-giáp-đè-bẹp-tổng-tài-cô-ngạo"
    proj_dir = os.path.join(BASE_DIR, "novel_projects", slug)
    chapters_dir = os.path.join(proj_dir, "chapters")
    cache_dir = os.path.join(BASE_DIR, "scratch", "cache_bjV27")
    os.makedirs(chapters_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    total_pages = 220
    print(f"[Book 1] Fetching pages 2..{total_pages} from 52shuku...")
    pages_data = {}
    with ThreadPoolExecutor(max_workers=15) as ex:
        futs = {ex.submit(fetch_52shuku_page, p, cache_dir): p for p in range(2, total_pages + 1)}
        done = 0
        for f in as_completed(futs):
            p_num, paras = f.result()
            pages_data[p_num] = paras
            done += 1
            if done % 40 == 0 or done == len(futs):
                print(f"  Progress: {done}/{len(futs)} pages")

    all_paras = []
    for p_num in range(2, total_pages + 1):
        all_paras.extend(pages_data.get(p_num, []))

    # Find start of Chapter 1
    start_idx = 0
    for i, p in enumerate(all_paras):
        if re.match(r'^第\s*0*1\s*章', p):
            start_idx = i
            break
    all_paras = all_paras[start_idx:]

    chapter_pattern = re.compile(r'^(第\s*\d+\s*章.*|番外.*)$')
    chapters = []
    current_ch = None

    for p in all_paras:
        if chapter_pattern.match(p):
            if current_ch:
                chapters.append(current_ch)
            header = p.strip()
            current_ch = {'title_zh': header, 'paragraphs': [header]}
        else:
            if current_ch:
                current_ch['paragraphs'].append(p)

    if current_ch:
        chapters.append(current_ch)

    print(f"[Book 1] Segmented into {len(chapters)} chapters.")
    for idx, ch in enumerate(chapters, 1):
        ch_id = f"ch_{idx:03d}"
        ch_dir = os.path.join(chapters_dir, ch_id)
        os.makedirs(ch_dir, exist_ok=True)
        with open(os.path.join(ch_dir, "source.md"), "w", encoding="utf-8") as f:
            f.write("\n\n".join(ch['paragraphs']) + "\n")

    # Update config.json chapters_count
    cfg_path = os.path.join(proj_dir, "config.json")
    if os.path.exists(cfg_path):
        with open(cfg_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)
        cfg["chapters_count"] = len(chapters)
        with open(cfg_path, "w", encoding="utf-8") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)

    return slug

# ==============================================================================
# BOOK 2: 《天之骄子又怀了npc的崽[快穿]》 (JJWXC Free Chapters 1..20)
# ==============================================================================
def fetch_jjwxc_chapter(novelid, ch_num):
    url = f"https://www.jjwxc.net/onebook.php?novelid={novelid}&chapterid={ch_num}"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                html_str = resp.read().decode('gb18030', errors='ignore')
            m_title = re.search(r'<h2>(.*?)</h2>', html_str, re.S)
            ch_title = clean_paragraph(m_title.group(1)) if m_title else f"第 {ch_num} 章"
            header = f"第 {ch_num} 章 {ch_title}" if not ch_title.startswith("第") else ch_title

            idx = html_str.find('id="paragraph_comment_content"')
            if idx == -1:
                return ch_num, header, []
            start_tag_end = html_str.find('>', idx) + 1
            end_div = html_str.find('</div>', start_tag_end)
            body = html_str[start_tag_end:end_div]

            lines = [clean_paragraph(l) for l in re.split(r'<br\s*/?>|\n', body)]
            lines = [l for l in lines if l and not l.startswith('@无限好文') and '晋江文学城' not in l]

            # Check author note (readsmall)
            m_note = re.search(r'<div class="readsmall">(.*?)</div>', html_str, re.S)
            if m_note:
                note_lines = [clean_paragraph(l) for l in re.split(r'<br\s*/?>|\n', m_note.group(1))]
                note_lines = [l for l in note_lines if l and '插入书签' not in l]
                if note_lines:
                    lines.extend(note_lines)

            return ch_num, header, [header] + lines
        except Exception as e:
            if attempt == 2:
                print(f"[Book 2] Error fetching Ch {ch_num}: {e}")
            time.sleep(1 + attempt)
    return ch_num, f"第 {ch_num} 章", []

def crawl_book_2():
    slug = "thiên-chi-kiêu-tử-lại-mang-thai-con-của-npc-rồi"
    proj_dir = os.path.join(BASE_DIR, "novel_projects", slug)
    chapters_dir = os.path.join(proj_dir, "chapters")
    os.makedirs(chapters_dir, exist_ok=True)

    print("[Book 2] Fetching 20 free chapters from JJWXC (novelid=8684719)...")
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs = {ex.submit(fetch_jjwxc_chapter, 8684719, c): c for c in range(1, 21)}
        for f in as_completed(futs):
            ch_num, header, paras = f.result()
            if paras:
                ch_id = f"ch_{ch_num:03d}"
                ch_dir = os.path.join(chapters_dir, ch_id)
                os.makedirs(ch_dir, exist_ok=True)
                with open(os.path.join(ch_dir, "source.md"), "w", encoding="utf-8") as f:
                    f.write("\n\n".join(paras) + "\n")
                print(f"  Saved {ch_id}: {header} ({len(paras)} paragraphs)")

    return slug

if __name__ == '__main__':
    s1 = crawl_book_1()
    s2 = crawl_book_2()
    print("Crawling complete for:", s1, s2)
