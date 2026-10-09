# -*- coding: utf-8 -*-
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch4_sliced.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

titles = {
    'ch_111': 'Chương 111: Rời đi sau cơn mẫn cảm',
    'ch_112': 'Chương 112: Cơ hội tuyển quân đợt hai',
    'ch_113': 'Chương 113: Tân binh gia nhập Đệ tam quân đoàn',
    'ch_114': 'Chương 114: Thăm dò và ghen tuông',
    'ch_115': 'Chương 115: Gián cách ngàn dặm và hoa hồng',
    'ch_116': 'Chương 116: Khắc ghi dấu ấn trọn đời',
    'ch_117': 'Chương 117: Lời cầu hôn và chiếc nhẫn kim cương',
    'ch_118': 'Chương 118: Đồng phục thỏ nữ lang và Đại kết cục'
}

base_dir = 'novel_projects/phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương/chapters'

for ch_id, title in titles.items():
    paras = data[ch_id]
    ch_dir = os.path.join(base_dir, ch_id)
    os.makedirs(ch_dir, exist_ok=True)
    source_path = os.path.join(ch_dir, 'source.md')
    
    content = f"---\ntitle: {title}\n---\n\n" + "\n\n".join(paras) + "\n"
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {source_path}: {len(paras)} paragraphs")

print("Done creating batch 4 sources.")
