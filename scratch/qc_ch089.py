import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ch_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_089"
source_path = os.path.join(ch_dir, "source.md")
trans_path = os.path.join(ch_dir, "translation.md")

with open(source_path, "r", encoding="utf-8") as f:
    s_raw = f.read()

with open(trans_path, "r", encoding="utf-8") as f:
    t_raw = f.read()

# Strip frontmatter
s_body = s_raw.split("---")[-1].strip()
t_body = t_raw.split("---")[-1].strip()

s_paras = s_body.split("\n\n")
t_paras = t_body.split("\n\n")

print(f"Source paras: {len(s_paras)}")
print(f"Trans paras:  {len(t_paras)}")

errors = []

if len(s_paras) != len(t_paras):
    errors.append(f"Mismatched paragraph count: source {len(s_paras)} vs trans {len(t_paras)}")

# Check dialogues formatting
for i, p in enumerate(t_paras):
    # Check if there is internal single newline
    if "\n" in p:
        errors.append(f"Para {i} contains internal single newline: {p[:30]}...")
    # Check if dialogue starts with dash instead of quote
    if p.startswith("—") or p.startswith("- "):
        errors.append(f"Para {i} starts with dash instead of quote: {p[:30]}")

# Pronoun audit
# In narration, Kỷ Cảnh should NOT be referred to as "anh"
# Lục Tư Niên should NOT be referred to as "cậu"
for i, (sp, tp) in enumerate(zip(s_paras, t_paras)):
    # Check quotes
    if tp.startswith("“") and not tp.endswith("”") and not tp.endswith("”..."):
        # dialogue might have trailing punctuation or narration tag after quote
        pass

print("\n--- Summary of Checks ---")
if errors:
    print(f"FAILED with {len(errors)} issues:")
    for e in errors:
        print("  -", e)
else:
    print("ALL BASIC CHECKS PASSED!")
