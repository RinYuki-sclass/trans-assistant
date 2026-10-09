import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\Nhung\trans-tool\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters'

for ch_num in range(43, 59):
    ch_id = f'ch_{ch_num:03d}'
    t_path = os.path.join(base_dir, ch_id, 'translation.md')
    if not os.path.exists(t_path):
        continue
    with open(t_path, 'r', encoding='utf-8') as f:
        t_lines = f.readlines()
        
    print(f"\n==================== {ch_id} ====================")
    for i, line in enumerate(t_lines, 1):
        l = line.strip()
        # Look for dialogues with 'anh', 'em', 'cậu'
        if l.startswith("“") or l.startswith('"'):
            # check if line contains anh/em/cậu
            if any(w in l.lower() for w in ['anh', 'em', 'cậu']):
                # print dialogue and surrounding line if it gives context
                print(f"L{i}: {l}")
