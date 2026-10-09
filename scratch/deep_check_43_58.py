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
        
    print(f"\n==================== {ch_id} ====================")
    # Check lines where Sở Niên Niên talks to Cố Xuyên or vice versa
    for idx, line in enumerate(lines, 1):
        l = line.strip()
        # Look for dialogue where someone calls someone else 'cậu' or 'anh'
        # specifically if Sở Niên Niên calls Cố Xuyên 'cậu'
        # or Cố Xuyên calls Sở Niên Niên 'anh'
        # or Sở Niên Niên refers to himself as 'anh'
        # or Cố Xuyên refers to himself as 'em'
        if any(target in l for target in [
            '“Tối qua cậu', 'tỏ tình với cậu', 'Cậu có đồng ý', 'với cậu không', 
            'anh ta có tỏ tình', 'khóe miệng anh ta cong'
        ]):
            print(f"L{idx}: {l}")
        
        # Narration where Sở Niên Niên is called 'anh ta'
        # or Cố Xuyên is called 'cậu ta'
        if re.search(r'\bSở Niên Niên\b.*?\b(anh ta)\b', l) or re.search(r'\b(anh ta)\b.*?\bSở Niên Niên\b', l):
            print(f"L{idx} [NN as anh ta]: {l}")
        if re.search(r'\bCố Xuyên\b.*?\b(cậu ta)\b', l) or re.search(r'\b(cậu ta)\b.*?\bCố Xuyên\b', l):
            print(f"L{idx} [CX as cậu ta]: {l}")
