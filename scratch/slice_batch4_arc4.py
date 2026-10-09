# -*- coding: utf-8 -*-
import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch4_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

# Flatten paragraphs in order from page 229 to 245
all_paras = []
for p in range(229, 246):
    sp = str(p)
    if sp in raw:
        for idx, line in enumerate(raw[sp]['paragraphs']):
            all_paras.append((p, idx, line))

# Find the marker indices
markers = [
    '第110章',
    '第111章',
    '第112章',
    '第113章',
    '第114章',
    '第115章',
    '第116章'
]

indices = []
for m in markers:
    for i, (p, idx, line) in enumerate(all_paras):
        if m in line:
            indices.append((m, i))
            break

print("Found markers:", indices)

# Now, let's carve out the slices
# Section 1 (ch_111): from 第110章 marker to 第111章 marker
# Section 2 (ch_112): from 第111章 marker to 第112章 marker
# Section 3 (ch_113): from 第112章 marker to 第113章 marker
# Section 4 (ch_114): from 第113章 marker to 第114章 marker
# Section 5 (ch_115): from 第114章 marker to 第115章 marker
# Section 6 (ch_116): from 第115章 marker to 第116章 marker
# Section 7 (ch_117 & ch_118): from 第116章 marker to end

raw_sections = {}
for k in range(len(indices)-1):
    m_name, start_i = indices[k]
    _, end_i = indices[k+1]
    # paragraphs between start_i+1 and end_i
    paras = [all_paras[x][2].strip() for x in range(start_i+1, end_i)]
    # filter out empty
    paras = [p for p in paras if p]
    raw_sections[f'sec_{k+1}'] = paras

# For Section 7 onwards:
sec7_all = [all_paras[x][2].strip() for x in range(indices[-1][1]+1, len(all_paras))]
sec7_all = [p for p in sec7_all if p]

# Find split point in sec7_all for ch_117 and ch_118:
# Around paragraph with 【叮咚，恭喜宿主完成100的任務進度！】
split_idx = None
for i, p in enumerate(sec7_all):
    if '叮咚，恭喜宿主完成100的任務進度' in p:
        split_idx = i
        break

print(f"Sec7 total paras: {len(sec7_all)}, split_idx: {split_idx}")
# If there is a "…" right before split_idx, we can let ch_117 end at the proposal ("我願意。") or include the "…"
# Let's inspect around split_idx
print("Around split_idx:")
for offset in range(-3, 3):
    idx = split_idx + offset
    if 0 <= idx < len(sec7_all):
        print(f"  {idx}: {sec7_all[idx]}")

raw_sections['ch_111'] = raw_sections['sec_1']
raw_sections['ch_112'] = raw_sections['sec_2']
raw_sections['ch_113'] = raw_sections['sec_3']
raw_sections['ch_114'] = raw_sections['sec_4']
raw_sections['ch_115'] = raw_sections['sec_5']
raw_sections['ch_116'] = raw_sections['sec_6']
raw_sections['ch_117'] = sec7_all[:split_idx]
raw_sections['ch_118'] = sec7_all[split_idx:]

for ch_id in ['ch_111', 'ch_112', 'ch_113', 'ch_114', 'ch_115', 'ch_116', 'ch_117', 'ch_118']:
    print(f"{ch_id}: {len(raw_sections[ch_id])} paragraphs")

with open('scratch/batch4_sliced.json', 'w', encoding='utf-8') as f:
    json.dump({k: raw_sections[k] for k in ['ch_111', 'ch_112', 'ch_113', 'ch_114', 'ch_115', 'ch_116', 'ch_117', 'ch_118']}, f, ensure_ascii=False, indent=2)

print("Saved scratch/batch4_sliced.json")
