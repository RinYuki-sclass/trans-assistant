import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/cleaned_batch4_arc2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

base_dir = 'novel_projects/phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương/chapters'

for cid, cdata in data.items():
    cdir = os.path.join(base_dir, cid)
    os.makedirs(cdir, exist_ok=True)
    source_path = os.path.join(cdir, 'source.md')

    content = "\n\n".join(cdata['paras'])
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created {source_path}: {len(cdata['paras'])} paras")

print("All Batch 4 source.md files created successfully.")
