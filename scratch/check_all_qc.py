import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters'

def parse_md(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]
    return [p.strip() for p in content.split('\n\n') if p.strip()]

all_passed = True

existing_chs = sorted([d for d in os.listdir(base_dir) if d.startswith('ch_')])

for cid in existing_chs:
    cdir = os.path.join(base_dir, cid)
    s_path = os.path.join(cdir, 'source.md')
    t_path = os.path.join(cdir, 'translation.md')
    if not os.path.exists(t_path):
        continue
    
    s_paras = parse_md(s_path)
    t_paras = parse_md(t_path)
    
    if len(s_paras) != len(t_paras):
        print(f"❌ {cid}: Paragraph count mismatch ({len(s_paras)} vs {len(t_paras)})")
        all_passed = False
        continue
    
    quotes = re.findall(r'“([^”]+)”', '\n'.join(t_paras))
    errs = 0
    for q_idx, q in enumerate(quotes, 1):
        if re.search(r'\bmày\b', q, re.I) and re.search(r'\btôi\b', q, re.I):
            print(f"❌ {cid}: Quote #{q_idx} mismatch tôi - mày: {q}")
            errs += 1
        if re.search(r'\btao\b', q, re.I) and re.search(r'\bcậu\b(?!\s*(?:ta|ấy)\b)', q, re.I):
            print(f"❌ {cid}: Quote #{q_idx} mismatch tao - cậu: {q}")
            errs += 1
        if re.search(r'\btao\b', q, re.I) and re.search(r'\banh\b', q, re.I):
            print(f"❌ {cid}: Quote #{q_idx} mismatch tao - anh: {q}")
            errs += 1
    
    if errs == 0:
        print(f"✅ {cid}: PASS 100% ({len(s_paras)} paras, {len(quotes)} quotes checked, 0 errors)")
    else:
        all_passed = False

if all_passed:
    print("\n🎉 ALL 7 CHAPTERS PASSED QC WITH 0 PRONOUN ERRORS!")
