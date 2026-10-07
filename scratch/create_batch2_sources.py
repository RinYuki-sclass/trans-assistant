import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/cleaned_batch2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

titles_vn = {
    'ch_008': 'Chương 8: Cho cậu đấy',
    'ch_009': 'Chương 9: Cậu ta muốn tỏ tình',
    'ch_010': 'Chương 10: Đã sống chung rồi',
    'ch_011': 'Chương 11: Tiểu thuyết ngôn tình Mary Sue',
    'ch_012': 'Chương 12: Tôi đến từ vùng núi',
    'ch_013': 'Chương 13: Ngoài ý muốn',
    'ch_014': 'Chương 14: Cậu thật kỳ lạ',
    'ch_015': 'Chương 15: Chơi thật đấy à',
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
