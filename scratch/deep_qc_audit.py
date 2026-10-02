import os, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'd:\Nhung\RIDI\trans-assistant\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters'

def audit_chapter(ch_num):
    ch_id = f'ch_{ch_num:03d}'
    ch_dir = os.path.join(base, ch_id)
    trans_file = os.path.join(ch_dir, 'translation.md')
    src_file = os.path.join(ch_dir, 'source.md')
    meta_file = os.path.join(ch_dir, 'meta.json')
    
    with open(trans_file, 'r', encoding='utf-8') as f:
        t_raw = f.read()
    with open(src_file, 'r', encoding='utf-8') as f:
        s_raw = f.read()
    with open(meta_file, 'r', encoding='utf-8') as f:
        meta = json.load(f)
        
    t_body = t_raw.split('---', 2)[2].strip()
    s_body = s_raw.split('---', 2)[2].strip()
    
    tp = [p.strip() for p in t_body.split('\n\n') if p.strip()]
    sp = [p.strip() for p in s_body.split('\n\n') if p.strip()]
    
    audit_results = {
        "chapter_id": ch_id,
        "n_source": len(sp),
        "n_trans": len(tp),
        "meta_target": meta['n_paragraphs'],
        "alignment_1_1": len(sp) == len(tp) == meta['n_paragraphs'],
        "issues": []
    }
    
    # Check forbidden terms
    forbidden = [
        'con thư trùng', 'con hùng trùng', 'con quân thư', 'Phí Lạc',
        'A Lợi Khắc Tư', 'Ngải Lợi Khắc Tư', 'Thụy An', 'Phật Đức Lý Hi',
        'Hải Đức Mạn', 'Ngải Lợi Âu', 'Tát Khắc Sâm', 'Khô Lâu'
    ]
    
    for i, p in enumerate(tp, 1):
        for term in forbidden:
            if term.lower() in p.lower():
                audit_results["issues"].append({
                    "para": i,
                    "type": "C1/C3: Thuật ngữ cấm",
                    "text": p[:60],
                    "forbidden_term": term
                })
                
        # Check Case A1: Does Lệ Yến Trạch get called 'anh' in narrative?
        # Check Case A2: Does Thẩm Từ get called 'cậu' in narrative?
        # Check Case A4: Does Chu Lạc Lạc get called 'cậu' in narrative?
        # Extract outside dialogue
        # Remove text in “...” and 【...】
        outside_dialogue = re.sub(r'“.*?”', '', p)
        outside_dialogue = re.sub(r'【.*?】', '', outside_dialogue)
        outside_dialogue = re.sub(r'".*?"', '', outside_dialogue)
        
        # Check if outside dialogue mentions Lệ Yến Trạch as 'anh'
        # e.g., 'anh [chỉ Lệ Yến Trạch]'
        if 'Lệ Yến Trạch' in outside_dialogue:
            # check if followed by 'anh'
            m = re.search(r'Lệ Yến Trạch[^\.\,\;]*?\banh\b', outside_dialogue)
            if m:
                audit_results["issues"].append({
                    "para": i,
                    "type": "Case A1: Lệ Yến Trạch bị gọi là anh?",
                    "text": m.group(0)
                })
        if 'Chu Lạc Lạc' in outside_dialogue:
            # check if followed by 'cậu' or 'cậu ta'
            m = re.search(r'Chu Lạc Lạc[^\.\,\;]*?\bcậu\b', outside_dialogue)
            if m:
                audit_results["issues"].append({
                    "para": i,
                    "type": "Case A4: Chu Lạc Lạc bị gọi là cậu?",
                    "text": m.group(0)
                })
                
    return audit_results

for ch in range(53, 64):
    res = audit_chapter(ch)
    print(f"[{res['chapter_id']}] 1:1={res['alignment_1_1']} ({res['n_trans']}/{res['n_source']}) Issues={len(res['issues'])}")
    if res['issues']:
        for iss in res['issues']:
            print("  ->", iss)
