import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/cleaned_batch4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

titles_vn = {
    'ch_024': 'Chương 24: Hai người đang yêu nhau sao?',
    'ch_025': 'Chương 25: Cậu rõ ràng thích anh ấy',
    'ch_026': 'Chương 26: Xin lỗi, kết thúc thôi',
    'ch_027': 'Chương 27: Chân tướng lộ diện',
    'ch_028': 'Chương 28: Nhà kho đối chất',
    'ch_029': 'Chương 29: Kịch bản hoàn thành',
    'ch_030': 'Chương 30: Bên nhau trọn đời',
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

print("All Batch 4 sources created successfully!")
