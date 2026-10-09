import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch1_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

checks = [
    (188, 43, 49),
    (190, 36, 42),
    (192, 40, 47),
    (194, 38, 44),
    (196, 40, 48),
    (199, 25, 33)
]

for p_num, s, e in checks:
    paras = pages[str(p_num)]['paragraphs']
    print(f"\n--- Page {p_num} indices {s} to {e} ---")
    for i in range(max(0, s), min(len(paras), e)):
        print(f"[{i}] {paras[i][:60]}")
