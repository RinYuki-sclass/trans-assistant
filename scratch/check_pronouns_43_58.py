import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\Nhung\trans-tool\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters'

for ch_num in range(43, 59):
    ch_id = f'ch_{ch_num:03d}'
    t_path = os.path.join(base_dir, ch_id, 'translation.md')
    if not os.path.exists(t_path):
        continue
    with open(t_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    issues = []
    for idx, line in enumerate(lines, 1):
        line_s = line.strip()
        if not line_s:
            continue
        
        # Narration: Sở Niên Niên should be 'cậu', Cố Xuyên should be 'anh'
        # Check if line has both or references them
        # Check for dialogue quotes
        if line_s.startswith(('“', '"')):
            # dialogue
            continue
        
        # Look for suspicious narration
        if 'Sở Niên Niên' in line_s and re.search(r'\b(anh|anh ta)\b', line_s):
            # check if 'anh' refers to Sở Niên Niên or Cố Xuyên
            issues.append((idx, 'NN_narration', line_s))
        if 'Cố Xuyên' in line_s and re.search(r'\b(cậu|cậu ta)\b', line_s):
            issues.append((idx, 'CX_narration', line_s))

    print(f'=== {ch_id}: {len(issues)} narration checks ===')
    for idx, tag, text in issues[:10]:
        print(f'  [{tag}] L{idx}: {text[:100]}...')
