import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\Nhung\trans-tool\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters'

for ch_num in range(43, 59):
    ch_id = f'ch_{ch_num:03d}'
    t_path = os.path.join(base_dir, ch_id, 'translation.md')
    s_path = os.path.join(base_dir, ch_id, 'source.md')
    if not os.path.exists(t_path):
        continue
    with open(t_path, 'r', encoding='utf-8') as f:
        t_lines = f.readlines()
    with open(s_path, 'r', encoding='utf-8') as f:
        s_lines = f.readlines()
        
    print(f"\n==================== {ch_id} ====================")
    # Check lines where dialogue might mix up
    for i in range(len(t_lines)):
        t_line = t_lines[i].strip()
        s_line = s_lines[i].strip() if i < len(s_lines) else ""
        if not t_line:
            continue
        # Check if Cố Xuyên uses 'em' or Sở Niên Niên uses 'anh' for himself
        # Or Sở Niên Niên calls Cố Xuyên 'cậu'
        # Or Cố Xuyên calls Sở Niên Niên 'anh'
        # Or third person: Sở Niên Niên is called 'anh ta'
        # Or Cố Xuyên is called 'cậu ta'
        
        suspicious = False
        reason = []
        
        if ("Sở Niên Niên" in t_line or "Niên Niên" in t_line) and "anh ta" in t_line:
            suspicious = True
            reason.append("NN + anh ta")
            
        if ("Cố Xuyên" in t_line) and "cậu ta" in t_line:
            suspicious = True
            reason.append("CX + cậu ta")
            
        if t_line.startswith("“") or t_line.startswith('"'):
            # Check dialogue:
            # If line mentions 'cậu' when talking between CX & NN
            # Let's see context
            pass
            
        if suspicious:
            print(f"L{i+1} [{', '.join(reason)}]:")
            print(f"  RAW:   {s_line}")
            print(f"  TRANS: {t_line}")
