import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch1_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p_num in sorted([int(k) for k in pages.keys()]):
    paras = pages[str(p_num)]['paragraphs']
    print(f"=== Page {p_num} (total {len(paras)}) ===")
    for i, p in enumerate(paras):
        if '第' in p and '章' in p:
            print(f"  [{i}] {p}")
        elif '作者有話說' in p:
            print(f"  [{i}] {p}")
