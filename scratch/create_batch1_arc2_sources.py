import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/cleaned_batch1_arc2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

titles_vn = {
    'ch_032': 'Chương 32: Ôm đùi làm nũng',
    'ch_033': 'Chương 33: Dọn sạch tang thi',
    'ch_034': 'Chương 34: Lên xe đại lão',
    'ch_035': 'Chương 35: Cõng em',
    'ch_036': 'Chương 36: Đột phá vòng vây',
    'ch_037': 'Chương 37: Làn sóng tang thi ập đến',
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

print("All Batch 1 sources created successfully!")
