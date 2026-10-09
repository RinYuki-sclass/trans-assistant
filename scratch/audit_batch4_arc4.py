# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters"
chapters = [f"ch_{i:03d}" for i in range(111, 119)]

print("=== AUDIT BATCH 4 (CH_111 -> CH_118) ===")

all_passed = True

for ch_id in chapters:
    ch_dir = os.path.join(base_dir, ch_id)
    s_path = os.path.join(ch_dir, "source.md")
    t_path = os.path.join(ch_dir, "translation.md")
    
    if not os.path.exists(s_path) or not os.path.exists(t_path):
        print(f"[{ch_id}] Missing files!")
        all_passed = False
        continue
        
    with open(s_path, 'r', encoding='utf-8') as f:
        s_raw = f.read().strip()
    with open(t_path, 'r', encoding='utf-8') as f:
        t_raw = f.read().strip()
        
    s_blocks = s_raw.split('\n\n')
    t_blocks = t_raw.split('\n\n')
    
    # Header check
    s_has_front = s_blocks[0].startswith('---')
    t_has_front = t_blocks[0].startswith('---')
    
    s_paras = s_blocks[1:] if s_has_front else s_blocks
    t_paras = t_blocks[1:] if t_has_front else t_blocks
    
    match_count = len(s_paras) == len(t_paras)
    
    # Pronoun audit
    # Narrative: "Kỷ Cảnh ... anh" -> check if Kỷ Cảnh is wrongly addressed as "anh" in narration
    # "Lục Tư Niên ... cậu" -> check if Lục Tư Niên is wrongly addressed as "cậu" in narration
    drift_errors = []
    for idx, p in enumerate(t_paras):
        # Check if outside quotes there's a drift
        # Strip dialogue inside quotes
        narrative = re.sub(r'“.*?”', '', p)
        # Check if Kỷ Cảnh is followed by 'anh' in narration
        if re.search(r'Kỷ Cảnh (?:đang|đã|liền|vẫn|lại|nghĩ|thầm|nói|cười|nhìn)\s+anh\b', narrative):
            drift_errors.append(f"Para {idx}: potential pronoun drift Kỷ Cảnh -> anh: {p[:70]}")
        # Check if Lục Tư Niên is followed by 'cậu' in narration
        if re.search(r'Lục Tư Niên (?:đang|đã|liền|vẫn|lại|nghĩ|thầm|nói|cười|nhìn)\s+cậu\b', narrative):
            drift_errors.append(f"Para {idx}: potential pronoun drift Lục Tư Niên -> cậu: {p[:70]}")
            
    print(f"[{ch_id}] Source paras: {len(s_paras)} | Trans paras: {len(t_paras)} | 1:1 Match: {match_count} | Drift warnings: {len(drift_errors)}")
    if drift_errors:
        for e in drift_errors[:3]:
            print(f"   -> {e}")
            
    if not match_count:
        all_passed = False

print(f"\nOverall Audit Result: {'ALL PASSED' if all_passed else 'FAILED'}")
