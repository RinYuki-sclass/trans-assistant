import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters'

chapters = [f'ch_{i:03d}' for i in range(1, 6)]

for ch in chapters:
    src_file = os.path.join(base, ch, 'source.md')
    with open(src_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f"\n==================== {ch} ====================")
    # find lines with mentions of names or dialogue
    for line in text.split('\n'):
        line = line.strip()
        if not line or line.startswith('---') or line.startswith('title:') or line.startswith('chapter_index:'):
            continue
        # search for any character interactions or names
        if any(k in line for k in ['白', '李', '張', '叔', '媽', '統', '指揮官', '傅', '江明朗', '小朗', '經理', '特助']):
            # print matching sentences or snippet
            print(f"[{ch}] {line}")

