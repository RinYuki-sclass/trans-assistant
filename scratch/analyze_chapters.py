import json
import re

with open('scratch/raw_pages_skdfi4kimel.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

print(f"Total pages loaded: {len(pages)}")

all_headers = []
for p in pages:
    page_num = p['page_num']
    for p_idx, line in enumerate(p['paragraphs']):
        # Search for chapter indicators
        if re.search(r'^(第[0-9一二三四五六七八九十百千]+[章節]|番外)', line):
            all_headers.append({
                'page_num': page_num,
                'para_idx': p_idx,
                'text': line
            })

print(f"\nFound {len(all_headers)} headers:")
for h in all_headers:
    print(f"P.{h['page_num']:02d} (p_{h['para_idx']:02d}): {h['text']}")
