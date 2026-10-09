import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\Nhung\trans-tool\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters'

for ch_num in range(43, 59):
    ch_id = f'ch_{ch_num:03d}'
    t_path = os.path.join(base_dir, ch_id, 'translation.md')
    if not os.path.exists(t_path):
        continue
    with open(t_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]
        
    non_empty = [(idx+1, l) for idx, l in enumerate(lines) if l]
    
    inconsistencies = []
    for p_idx, (line_no, text) in enumerate(non_empty):
        if text.startswith('“'):
            prev_p = non_empty[p_idx-1][1] if p_idx > 0 else ""
            next_p = non_empty[p_idx+1][1] if p_idx < len(non_empty)-1 else ""
            
            # Check if this dialogue is between NN and CX
            # Case 1: NN talking to CX using 'cậu'
            if ('Sở Niên Niên' in prev_p or 'Sở Niên Niên' in next_p) and ('Cố Xuyên' in prev_p or 'Cố Xuyên' in next_p):
                inconsistencies.append((line_no, "Context NN & CX", text, prev_p, next_p))
                
    if inconsistencies:
        print(f"\n==================== {ch_id} ====================")
        for inc in inconsistencies:
            print(f"L{inc[0]}: {inc[2]}")
            print(f"   PREV: {inc[3][:80]}")
            print(f"   NEXT: {inc[4][:80]}")
