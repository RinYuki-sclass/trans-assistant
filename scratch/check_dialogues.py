import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\Nhung\trans-tool\novel_projects\công-vai-chính-công\chapters'

for ch_num in range(109, 116):
    ch_path = os.path.join(base_dir, f'ch_{ch_num}', 'translation.md')
    with open(ch_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f"\n==================== CHAPTER {ch_num} ====================")
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if '“' in line or '”' in line:
            print(f"L{i+1}: {line}")
