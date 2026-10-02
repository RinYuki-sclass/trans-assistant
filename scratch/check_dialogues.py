import os, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'd:\Nhung\RIDI\trans-assistant\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters'

for ch in range(53, 64):
    ch_id = f'ch_{ch:03d}'
    trans_file = os.path.join(base, ch_id, 'translation.md')
    with open(trans_file, 'r', encoding='utf-8') as f:
        text = f.read()
        
    for bad in ['con thư trùng', 'con hùng trùng', 'con quân thư', 'con á thư', 'Phí Lạc', 'Khô Lâu', 'Thụy An']:
        if bad.lower() in text.lower():
            print(f'[{ch_id}] Found forbidden: {bad}')
            
    lines = text.split('\n\n')
    for idx, l in enumerate(lines, 1):
        if 'Thẩm Từ' in l and '“' in l:
            dialogues = re.findall(r'“([^”]+)”', l)
            for d in dialogues:
                if re.search(r'\banh\b', d, re.IGNORECASE):
                    print(f'[{ch_id}] L{idx} Thẩm Từ dialogue has "anh": {d}')
