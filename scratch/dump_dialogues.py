import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\Nhung\trans-tool\novel_projects\công-vai-chính-công\chapters'

out_lines = []
for ch_num in range(109, 116):
    ch_path = os.path.join(base_dir, f'ch_{ch_num}', 'translation.md')
    with open(ch_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    out_lines.append(f"\n==================== CHAPTER {ch_num} ====================")
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if '“' in line:
            out_lines.append(f"L{i+1}: {line.strip()}")

with open(r'd:\Nhung\trans-tool\scratch\dialogues_109_115.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))

print("Wrote dialogues_109_115.txt successfully!")
