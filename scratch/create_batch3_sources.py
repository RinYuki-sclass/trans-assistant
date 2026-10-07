import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/cleaned_batch3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

titles_vn = {
    'ch_016': 'Chương 16: Tặng cậu đấy',
    'ch_017': 'Chương 17: Tôi đang theo đuổi Tần thiếu',
    'ch_018': 'Chương 18: Cậu ta khá cưng chiều cậu',
    'ch_019': 'Chương 19: Nụ hôn',
    'ch_020': 'Chương 20: Chơi đùa với cậu ta',
    'ch_021': 'Chương 21: Vậy thì chơi đùa chút',
    'ch_022': 'Chương 22: Không được gọi đàn anh',
    'ch_023': 'Chương 23: Ngủ chung',
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
