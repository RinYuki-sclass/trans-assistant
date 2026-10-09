import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/cleaned_batch3_arc2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

titles_vn = {
    'ch_045': 'Chương 45: Tang thi triều tập kích',
    'ch_046': 'Chương 46: Phòng thủ tiền tuyến',
    'ch_047': 'Chương 47: Hy sinh anh dũng',
    'ch_048': 'Chương 48: Nỗi đau và an ủi',
    'ch_049': 'Chương 49: Điểm yếu duy nhất',
    'ch_050': 'Chương 50: Quyết không chạy trốn',
    'ch_051': 'Chương 51: Nụ hôn giữa khói lửa',
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

print("All Batch 3 sources created successfully!")
