import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scratch.extract_ch089 import all_paras

# Clean whitespace
cleaned_paras = [p.strip() for p in all_paras if p.strip()]
print(f"Total cleaned paras: {len(cleaned_paras)}")

out_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_089"
os.makedirs(out_dir, exist_ok=True)

header = "---\ntitle: Chương 89: Hương rượu Tequila đột ngột\n---\n\n"
content = header + "\n\n".join(cleaned_paras) + "\n"

with open(os.path.join(out_dir, "source.md"), "w", encoding="utf-8") as f:
    f.write(content)

print(f"Saved source.md with {len(cleaned_paras)} paragraphs.")
