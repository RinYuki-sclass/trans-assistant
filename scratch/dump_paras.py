import sys

with open(r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_089\source.md", "r", encoding="utf-8") as f:
    text = f.read()

paras = text.split("---")[-1].strip().split("\n\n")

with open(r"d:\Nhung\RIDI\trans-assistant\scratch\paras_ch089.txt", "w", encoding="utf-8") as f:
    f.write(f"Total paras: {len(paras)}\n")
    for i, p in enumerate(paras):
        f.write(f"[{i:03d}] {p}\n")

print(f"Wrote {len(paras)} paras to paras_ch089.txt in utf-8")
