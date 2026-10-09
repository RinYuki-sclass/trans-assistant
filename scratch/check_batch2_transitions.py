import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch2_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

checks = [
    (199, 28, 35),
    (201, 26, 33),
    (203, 16, 25),
    (205, 15, 25),
    (207, 43, 52),
    (209, 26, 35),
    (211, 31, 38),
    (213, 33, 42)
]

for p_num, s, e in checks:
    paras = pages[str(p_num)]['paragraphs']
    print(f"\n--- Page {p_num} indices {s} to {e} ---")
    for i in range(max(0, s), min(len(paras), e)):
        print(f"[{i}] {paras[i][:60]}")
