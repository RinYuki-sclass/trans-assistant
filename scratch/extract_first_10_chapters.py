import urllib.request
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

all_paragraphs = []

print("Fetching pages 1 to 15 from Talebed...")
for page in range(1, 16):
    url = f'https://www.talebed.com/read/272625/{page}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8')
        m = re.search(r'<div class="read-content">(.*?)</div>\s*</div>\s*<div class="px-6', html, re.DOTALL)
        if not m:
            print(f"Error matching content on page {page}")
            sys.exit(1)
        paragraphs = re.findall(r'<p>(.*?)</p>', m.group(1))
        # clean paragraphs
        cleaned = [p.strip() for p in paragraphs if p.strip()]
        all_paragraphs.extend(cleaned)
        print(f"Fetched page {page:02d} ({len(cleaned)} paragraphs)")

print(f"Total paragraphs collected: {len(all_paragraphs)}")

# Locate chapter headers
chapter_indices = []
for idx, p in enumerate(all_paragraphs):
    m = re.search(r'第\s*(\d+)\s*章\s*(.*)', p)
    if m:
        num = int(m.group(1))
        title = m.group(2).strip()
        chapter_indices.append((idx, num, title, p))
        print(f"Found header at index {idx}: {p}")

# Filter to chapters 2 to 12 (corresponding to Story chapters 1 to 10 + delimiter 11)
story_chapters = []
for i in range(len(chapter_indices) - 1):
    c_idx, c_num, c_title, raw_header = chapter_indices[i]
    next_idx, next_num, _, _ = chapter_indices[i+1]
    
    # We only care about story chapters 1 to 10 (which have c_num from 2 to 11)
    if 2 <= c_num <= 11:
        story_ch_num = c_num - 1
        content_paragraphs = all_paragraphs[c_idx + 1 : next_idx]
        story_chapters.append({
            'ch_num': story_ch_num,
            'header': raw_header,
            'title': c_title,
            'paragraphs': content_paragraphs
        })

target_base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phan-dien-truyen-nguoc-dinh-cong-khong-lam-nua\chapters"

print(f"\nProcessing {len(story_chapters)} story chapters...")

for item in story_chapters:
    ch_num = item['ch_num']
    folder_name = f"ch_{ch_num:03d}"
    ch_dir = os.path.join(target_base_dir, folder_name)
    os.makedirs(ch_dir, exist_ok=True)
    
    file_path = os.path.join(ch_dir, "source.md")
    
    # Format markdown content
    title_line = f"Chương {ch_num}: {item['title']}" if item['title'] else f"Chương {ch_num}: {item['header']}"
    
    lines = [
        "---",
        f"title: {title_line}",
        "---",
        "",
        item['header'],
        ""
    ]
    
    for p in item['paragraphs']:
        # clean any html tags if any remain
        p_clean = re.sub(r'<.*?>', '', p).strip()
        if p_clean:
            lines.append(p_clean)
            lines.append("")
            
    content_str = "\n".join(lines).strip() + "\n"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content_str)
        
    print(f"Saved {folder_name}/source.md: {title_line} ({len(item['paragraphs'])} paragraphs)")

print("\nAll 10 chapters extracted and saved successfully!")
