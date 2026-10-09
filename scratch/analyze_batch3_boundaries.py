# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch3_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Ghép toàn bộ paragraphs từ page 213 đến 229 lại theo thứ tự
all_paras = []
for p_num in range(213, 230):
    k = str(p_num)
    if k in pages:
        p_list = pages[k].get('paragraphs', [])
        for p in p_list:
            all_paras.append((p_num, p))

print(f"Total paragraphs from p213 to p229: {len(all_paras)}")

# Tìm vị trí các tiêu đề chương
markers = []
for idx, (p_num, text) in enumerate(all_paras):
    m = re.match(r'^(第\d+章.*)', text.strip())
    if m:
        markers.append((idx, p_num, text.strip()))
        print(f"Marker found at global index {idx} (page {p_num}): {text.strip()}")

# Các chương của chúng ta trong Batch 3:
# ch_103: từ marker thứ 0 (第102章 trên CZBooks) đến marker thứ 1 (第103章)
# ch_104: từ marker thứ 1 (第103章) đến marker thứ 2 (第104章)
# ch_105: từ marker thứ 2 (第104章) đến marker thứ 3 (第105章)
# ch_106: từ marker thứ 3 (第105章) đến marker thứ 4 (第106章)
# ch_107: từ marker thứ 4 (第106章) đến marker thứ 5 (第107章)
# ch_108: từ marker thứ 5 (第107章) đến marker thứ 6 (第108章)
# ch_109: từ marker thứ 6 (第108章) đến marker thứ 7 (第109章)
# ch_110: từ marker thứ 7 (第109章) đến marker thứ 8 (第110章)

print("\n--- Summary of boundaries ---")
for i in range(len(markers)):
    idx, p_num, title = markers[i]
    next_idx = markers[i+1][0] if i+1 < len(markers) else len(all_paras)
    ch_id = f"ch_{103+i:03d}"
    cnt = next_idx - idx - 1 # trừ đi dòng tiêu đề
    print(f"{ch_id}: start={idx+1}, end={next_idx}, count={cnt} paras, title_raw='{title}'")
