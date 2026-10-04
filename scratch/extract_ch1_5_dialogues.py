import os
import re
import json

base = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters'
out_path = r'd:\Nhung\trans-tool\scratch\analysis_ch1_5.txt'

lines_out = []

def p(s=""):
    lines_out.append(s)

chapters = [f'ch_{i:03d}' for i in range(1, 6)]

for ch in chapters:
    src_file = os.path.join(base, ch, 'source.md')
    with open(src_file, 'r', encoding='utf-8') as f:
        text = f.read()

    p(f"\n==================== CHAPTER: {ch} ====================")
    paragraphs = [line.strip() for line in text.split('\n') if line.strip() and not line.startswith('---') and not line.startswith('title:') and not line.startswith('chapter_index:')]
    
    # Dialogues and speaker context
    p(f"Total Paragraphs: {len(paragraphs)}")
    
    dialogue_list = []
    for idx, para in enumerate(paragraphs):
        # find quotes
        quotes = re.findall(r'[“「](.*?)[”」]', para)
        if quotes:
            # check preceding/following context
            dialogue_list.append((idx + 1, para, quotes))

    p(f"Dialogues count: {len(dialogue_list)}")
    p("--- Dialogues detail ---")
    for idx, para, quotes in dialogue_list:
        p(f"P{idx}: {para}")

with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines_out))

print(f"Done. Wrote to {out_path}")
