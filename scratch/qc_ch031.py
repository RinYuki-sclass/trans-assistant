import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

cdir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_031"
with open(os.path.join(cdir, "source.md"), "r", encoding="utf-8") as f:
    src_content = f.read()

with open(os.path.join(cdir, "translation.md"), "r", encoding="utf-8") as f:
    trans_content = f.read()

src_body = src_content.split("---\n\n", 1)[1] if "---\n\n" in src_content else src_content
trans_body = trans_content.split("---\n\n", 1)[1] if "---\n\n" in trans_content else trans_content

src_paras = [p.strip() for p in src_body.split("\n\n") if p.strip()]
trans_paras = [p.strip() for p in trans_body.split("\n\n") if p.strip()]

print(f"Source paras: {len(src_paras)}")
print(f"Translation paras: {len(trans_paras)}")

assert len(src_paras) == len(trans_paras), f"Count mismatch: {len(src_paras)} vs {len(trans_paras)}"

errors = []
for i, (sp, tp) in enumerate(zip(src_paras, trans_paras)):
    # Check internal newlines
    if "\n" in tp:
        errors.append(f"Para {i}: internal newline detected")
    # Check straight double quotes
    if '"' in tp:
        errors.append(f"Para {i}: straight double quotes detected: {tp}")
    # Check if raw had dialogue quotes but translation doesn't
    if ("“" in sp or "”" in sp) and not ("“" in tp or "”" in tp or "【" in tp):
        errors.append(f"Para {i}: Raw had quotes but translation missing quotes: {sp} vs {tp}")

print(f"Errors found: {len(errors)}")
for e in errors:
    print(e)

if not errors:
    print("ALL QC AUDIT CHECKS PASSED PERFECTLY!")
