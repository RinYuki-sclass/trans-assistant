# -*- coding: utf-8 -*-
import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch3_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

all_paras = []
for p_num in range(213, 230):
    k = str(p_num)
    if k in pages:
        p_list = pages[k].get('paragraphs', [])
        for p in p_list:
            all_paras.append(p)

markers = []
for idx, text in enumerate(all_paras):
    m = re.match(r'^(第\d+章.*)', text.strip())
    if m:
        markers.append((idx, text.strip()))

titles = {
    "ch_103": "Chương 103: Trừng trị Alpha theo đuổi",
    "ch_104": "Chương 104: Lịch sử phân hóa và lời thổ lộ",
    "ch_105": "Chương 105: Bữa tiệc nguyên soái và ghen tuông",
    "ch_106": "Chương 106: Phòng nghỉ say rượu",
    "ch_107": "Chương 107: Mềm lòng và làm lành",
    "ch_108": "Chương 108: Quyết định trở lại quân đoàn",
    "ch_109": "Chương 109: Kỳ nhạy cảm bùng phát",
    "ch_110": "Chương 110: Lần đánh dấu đầu tiên"
}

proj = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương"
batch3_data = {}

for i in range(8):
    ch_id = f"ch_{103+i:03d}"
    idx = markers[i][0]
    next_idx = markers[i+1][0]
    # paragraphs bỏ dòng tiêu đề
    paras = [p.strip() for p in all_paras[idx+1:next_idx] if p.strip()]
    batch3_data[ch_id] = paras

    ch_dir = os.path.join(proj, "chapters", ch_id)
    os.makedirs(ch_dir, exist_ok=True)
    src_file = os.path.join(ch_dir, "source.md")

    frontmatter = f"---\ntitle: {titles[ch_id]}\n---\n\n"
    content = frontmatter + "\n\n".join(paras) + "\n"

    with open(src_file, "w", encoding="utf-8") as f:
        f.write(content)

    # Xuất file paras txt vào scratch
    txt_file = f"scratch/{ch_id}_paras.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(f"Total paras: {len(paras)}\n")
        for p_i, p in enumerate(paras):
            f.write(f"[{p_i:03d}] {p}\n")

    print(f"Created {src_file} with {len(paras)} paras (Frontmatter: 1 block -> Total {len(paras)+1} blocks)")

with open("scratch/batch3_sliced.json", "w", encoding="utf-8") as f:
    json.dump(batch3_data, f, ensure_ascii=False, indent=2)

print("Batch 3 sources created successfully!")
