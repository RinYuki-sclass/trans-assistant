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
        
    # Check for occurrences where Sở Niên Niên calls Cố Xuyên 'cậu' in dialogue
    # or Cố Xuyên calls Sở Niên Niên 'anh'
    # or Sở Niên Niên is called 'anh ta'
    # or Cố Xuyên is called 'cậu ta'
    inconsistencies = []
    for i, line in enumerate(lines, 1):
        l = line.strip()
        # Look for dialogue lines with “...cậu...” where speaker is likely Sở Niên Niên talking to Cố Xuyên
        # Let's inspect context
        if '“' in l:
            # If line has 'cậu' and mentions Cố Xuyên or in conversation with Cố Xuyên
            if i > 1 and ('Cố Xuyên' in lines[i-2] or (i < len(lines) and 'Cố Xuyên' in lines[i])):
                if ' cậu ' in l or ' cậu?' in l or ' cậu.' in l or ' cậu!' in l:
                    inconsistencies.append((i, "Dialogue 'cậu' near Cố Xuyên", l))
                    
    if inconsistencies:
        print(f"\n{ch_id}:")
        for inc in inconsistencies:
            print(f"  L{inc[0]} [{inc[1]}]: {inc[2]}")
