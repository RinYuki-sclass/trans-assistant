import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

base = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters'

chapters = [f'ch_{i:03d}' for i in range(1, 6)]

for ch in chapters:
    src_file = os.path.join(base, ch, 'source.md')
    if not os.path.exists(src_file):
        print(f"File not found: {src_file}")
        continue
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n==================== {ch} ====================")
    # Extract title
    title_match = re.search(r'title:\s*["\']?(.*?)["\']?\n', content)
    if title_match:
        print(f"Title: {title_match.group(1)}")
    
    # Check lines
    lines = [line.strip() for line in content.split('\n') if line.strip() and not line.startswith('---') and not line.startswith('title:') and not line.startswith('chapter_index:')]
    print(f"Total valid paragraphs: {len(lines)}")
    
    # Search for quotes / dialogues
    dialogues = [l for l in lines if '“' in l or '"' in l or '「' in l]
    print(f"Dialogues count: {len(dialogues)}")
    print("Sample dialogues (first 5):")
    for d in dialogues[:5]:
        print("  ", d[:120])
        
    # Search for potential proper names (e.g. 傅, 汪, 系統, etc.)
    # Let's extract Chinese characters or recurring names
