import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_089\translation.md", "r", encoding="utf-8") as f:
    text = f.read()

paras = text.split("---")[-1].strip().split("\n\n")

print(f"Total paragraphs to check: {len(paras)}")
pronoun_warnings = []

for i, p in enumerate(paras):
    # Remove dialogue parts to check only narration
    narration = re.sub(r'“.*?”', '', p)
    
    # Check if "anh" refers to Kỷ Cảnh in narration
    # e.g., "Kỷ Cảnh... anh..."
    if "Kỷ Cảnh" in narration and " anh " in narration:
        # Check context
        pronoun_warnings.append((i, "Kỷ Cảnh + anh in narration", p))

    # Check if "cậu" refers to Lục Tư Niên in narration
    # e.g., "Lục Tư Niên... cậu..."
    if "Lục Tư Niên" in narration and " cậu " in narration:
        pronoun_warnings.append((i, "Lục Tư Niên + cậu in narration", p))

print(f"Found {len(pronoun_warnings)} potential pronoun contexts:")
for idx, kind, p in pronoun_warnings:
    print(f"[{idx:03d}] {kind}:")
    print(f"     {p[:100]}...")
