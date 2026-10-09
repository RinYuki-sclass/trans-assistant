import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\Nhung\trans-tool\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters'

def check_chapter(ch_num):
    ch_id = f'ch_{ch_num:03d}'
    t_path = os.path.join(base_dir, ch_id, 'translation.md')
    if not os.path.exists(t_path):
        return
    with open(t_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    findings = []
    
    # We want to identify:
    # 1. Dialogues where Sở Niên Niên talks to Cố Xuyên with 'cậu' instead of 'anh'
    # 2. Third person pronoun issues: Sở Niên Niên as 'anh ta' or 'anh'
    # 3. Third person pronoun issues: Cố Xuyên as 'cậu ta' or 'cậu'
    for i, line in enumerate(lines, 1):
        l = line.strip()
        if not l:
            continue
            
        # Check dialogue
        if l.startswith('“') or l.startswith('"'):
            # check if Sở Niên Niên talks to Cố Xuyên with 'cậu'
            # let's look for known patterns
            if any(k in l for k in ['tỏ tình với cậu', 'Cậu có đồng ý', 'Tối qua cậu và Lục Thiên']):
                findings.append((i, 'Dialogue NN calling CX cậu', l))
                
        # Check narration
        # If line refers to Sở Niên Niên as 'anh ta'
        # e.g. "khóe miệng anh ta cong thành một đường thẳng, nói." (when NN speaks)
        # e.g. "anh ta vẫn không nhận được câu trả lời của Cố Xuyên" (NN)
        # e.g. "Anh ta cúi đầu, từ từ ngồi xổm xuống" (NN)
        # e.g. "Đầu lưỡi anh ta lăn lộn" (NN)
        if any(pat in l for pat in [
            'khóe miệng anh ta cong thành một đường thẳng',
            'anh ta vẫn không nhận được câu trả lời của Cố Xuyên',
            'Anh ta cúi đầu, từ từ ngồi xổm xuống',
            'Đầu lưỡi anh ta lăn lộn',
            'tiếng bước chân của Cố Xuyên ngày càng đến gần.\n\n“Vậy còn tôi thì sao?” Đầu lưỡi anh ta'
        ]):
            findings.append((i, 'NN narrated as anh ta', l))
            
        if 'Sở Niên Niên' in l and 'anh ta' in l:
            # could be Đại Hải / Lục Thiên / Trần Khiêm / Triệu Doãn etc as 'anh ta'
            # let's check if 'anh ta' is NN
            pass

    return ch_id, findings

print("=== CHECKING CH 43 - 58 ===")
for ch in range(43, 59):
    res = check_chapter(ch)
    if res and res[1]:
        print(f"\n{res[0]}:")
        for f in res[1]:
            print(f"  L{f[0]} [{f[1]}]: {f[2]}")
