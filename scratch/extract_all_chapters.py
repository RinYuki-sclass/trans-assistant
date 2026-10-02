import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

cache_dir = r"d:\Nhung\RIDI\trans-assistant\scratch\talebed_cache"
target_base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phan-dien-truyen-nguoc-dinh-cong-khong-lam-nua\chapters"

all_paragraphs = []
page_files = sorted([f for f in os.listdir(cache_dir) if f.startswith("page_") and f.endswith(".html")])
print(f"Reading {len(page_files)} cached pages...")

for pf in page_files:
    file_path = os.path.join(cache_dir, pf)
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    m = re.search(r'<div class="read-content">(.*?)</div>\s*</div>\s*<div class="px-6', html, re.DOTALL)
    if m:
        paragraphs = re.findall(r'<p>(.*?)</p>', m.group(1))
        for p in paragraphs:
            p_strip = p.strip()
            if p_strip:
                all_paragraphs.append(p_strip)
    else:
        print(f"Warning: match failed for {pf}")

print(f"Total paragraphs collected: {len(all_paragraphs)}")

# Locate all chapter boundaries
# A chapter boundary is a paragraph matching r'^第\s*(\d+)\s*章\s*(.*)'
chapter_points = []
for idx, p in enumerate(all_paragraphs):
    m = re.search(r'^第\s*(\d+)\s*章\s*(.*)', p)
    if m:
        raw_num = int(m.group(1))
        title = m.group(2).strip()
        chapter_points.append({
            'idx': idx,
            'raw_num': raw_num,
            'title': title,
            'header': p
        })

print(f"Found {len(chapter_points)} chapter points in total.")
for cp in chapter_points:
    print(f"  Raw Ch {cp['raw_num']:02d} [p_idx {cp['idx']}]: {cp['header']}")

# Story chapters start from raw_num == 2 (which is Story Chapter 1)
# Raw Ch 2 corresponds to Story Chapter 1, Raw Ch 3 corresponds to Story Chapter 2, ..., Raw Ch N corresponds to Story Chapter N - 1
chapters_to_save = []
for i in range(len(chapter_points)):
    cp = chapter_points[i]
    if cp['raw_num'] < 2:
        continue # skip "第1章 书签"
    
    # Check if this chapter is locked
    if "[锁]" in cp['title'] or "此章节已锁" in cp['title']:
        print(f"Stopping before locked chapter: {cp['header']}")
        break
        
    story_ch_num = cp['raw_num'] - 1
    start_idx = cp['idx']
    
    if i + 1 < len(chapter_points):
        end_idx = chapter_points[i+1]['idx']
    else:
        end_idx = len(all_paragraphs)
        
    # Content is between start_idx + 1 and end_idx
    content_paras = all_paragraphs[start_idx + 1 : end_idx]
    
    # Filter out any ending watermarks / copyright notes
    clean_paras = []
    for p in content_paras:
        # ignore copyright footer if at end of file
        if "本书名称:" in p or "㏄南风整理推荐" in p or "如有侵权" in p or "本作品来自互联网" in p:
            continue
        p_clean = re.sub(r'<.*?>', '', p).strip()
        if p_clean:
            clean_paras.append(p_clean)
            
    chapters_to_save.append({
        'ch_num': story_ch_num,
        'title': cp['title'],
        'header': cp['header'],
        'paragraphs': clean_paras
    })

print(f"\nReady to write {len(chapters_to_save)} chapters to novel_projects chapters directory...")

for ch in chapters_to_save:
    ch_num = ch['ch_num']
    folder_name = f"ch_{ch_num:03d}"
    ch_dir = os.path.join(target_base_dir, folder_name)
    os.makedirs(ch_dir, exist_ok=True)
    
    file_path = os.path.join(ch_dir, "source.md")
    title_line = f"Chương {ch_num}: {ch['title']}" if ch['title'] else f"Chương {ch_num}: {ch['header']}"
    
    lines = [
        "---",
        f"title: {title_line}",
        "---",
        "",
        ch['header'],
        ""
    ]
    for p in ch['paragraphs']:
        lines.append(p)
        lines.append("")
        
    content_str = "\n".join(lines).strip() + "\n"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content_str)
        
    print(f"Saved {folder_name}/source.md: {title_line} ({len(ch['paragraphs'])} paragraphs)")

print(f"\nSuccessfully wrote {len(chapters_to_save)} chapters!")
