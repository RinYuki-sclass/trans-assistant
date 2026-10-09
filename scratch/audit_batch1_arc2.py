import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters"
cids = ['ch_032', 'ch_033', 'ch_034', 'ch_035', 'ch_036', 'ch_037']

overall_errors = {}

for cid in cids:
    cdir = os.path.join(BASE_DIR, cid)
    src_file = os.path.join(cdir, "source.md")
    trans_file = os.path.join(cdir, "translation.md")

    with open(src_file, 'r', encoding='utf-8') as f:
        src_raw = f.read()
    with open(trans_file, 'r', encoding='utf-8') as f:
        trans_raw = f.read()

    s_body = src_raw.split('---\n\n', 1)[1] if '---\n\n' in src_raw else src_raw
    t_body = trans_raw.split('---\n\n', 1)[1] if '---\n\n' in trans_raw else trans_raw

    s_paras = [p.strip() for p in s_body.split('\n\n') if p.strip()]
    t_paras = [p.strip() for p in t_body.split('\n\n') if p.strip()]

    errors = []
    if len(s_paras) != len(t_paras):
        errors.append(f"Paragraph count mismatch: source={len(s_paras)} vs trans={len(t_paras)}")

    # Audit individual paragraphs
    fixed_paras = []
    changed = False
    for i, (sp, tp) in enumerate(zip(s_paras, t_paras)):
        cur_p = tp

        # 1. Check straight quotes
        if '"' in cur_p:
            cur_p = re.sub(r'\"([^\"]+)\"', r'“\1”', cur_p)
            cur_p = cur_p.replace('"', '”')
            changed = True

        # 2. Check quotes presence
        if ('“' in sp or '”' in sp) and not ('“' in cur_p or '”' in cur_p or '【' in cur_p or '-' == cur_p):
            errors.append(f"Para {i}: Raw had quotes but translation missing quotes:\n  RAW: {sp}\n  TRN: {cur_p}")

        fixed_paras.append(cur_p)

    if changed:
        header = f"---\ntitle: {trans_raw.split('---')[1].strip().split('title:')[1].strip()}\n---\n\n"
        with open(trans_file, 'w', encoding='utf-8') as f:
            f.write(header + "\n\n".join(fixed_paras) + "\n")
        print(f"[{cid}] Standardized quotes in translation.md")

    overall_errors[cid] = errors
    print(f"[{cid}] Checked {len(t_paras)} paras. Errors: {len(errors)}")
    for e in errors:
        print(f"   ! {e}")

print("\nAudit finished.")
