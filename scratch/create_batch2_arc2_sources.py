import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/cleaned_batch2_arc2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

titles_vn = {
    'ch_038': 'Chương 38: Sống chung một phòng',
    'ch_039': 'Chương 39: Ngắm nhìn cơ bắp',
    'ch_040': 'Chương 40: Ngủ chung một giường',
    'ch_041': 'Chương 41: Hơi ấm đêm đông',
    'ch_042': 'Chương 42: Dạo quanh căn cứ',
    'ch_043': 'Chương 43: Bữa ăn ấm cúng',
    'ch_044': 'Chương 44: Rung động',
}

base_dir = r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters'

for cid, item in data.items():
    cdir = os.path.join(base_dir, cid)
    os.makedirs(cdir, exist_ok=True)
    title = titles_vn[cid]
    paras = item['paras']

    header = f"---\ntitle: {title}\n---\n\n"
    content = header + '\n\n'.join(paras) + '\n'

    source_path = os.path.join(cdir, 'source.md')
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created {source_path}: {len(paras)} paras")

print("All Batch 2 sources created successfully!")
