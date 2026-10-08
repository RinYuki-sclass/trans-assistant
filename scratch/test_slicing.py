import json
import re

with open('scratch/raw_pages_skdfi4kimel.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Flatten all paragraphs with their source page
all_paras = []
for p in pages:
    page_num = p['page_num']
    for idx, text in enumerate(p['paragraphs']):
        all_paras.append({
            'page_num': page_num,
            'para_idx': idx,
            'text': text
        })

print(f"Total flattened paragraphs: {len(all_paras)}")

# Find header indices in flattened paragraphs
chapter_starts = []
for i, item in enumerate(all_paras):
    t = item['text']
    # Check if header
    m = re.match(r'^(第[0-9一二三四五六七八九十百千]+[章節]|番外\s*[0-9一二三四五六七八九十]*)(.*)$', t)
    if m:
        # Check if it's the 番外123 title line on page 58
        if t.strip() == '番外123':
            continue
        chapter_starts.append((i, t))

print(f"Total chapter starts identified: {len(chapter_starts)}")
for idx, (pos, title) in enumerate(chapter_starts, 1):
    print(f"{idx:02d}. Pos {pos:04d} (P.{all_paras[pos]['page_num']:02d}): {title}")
