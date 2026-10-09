import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch1_sliced.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for cid in ['ch_091', 'ch_092', 'ch_093', 'ch_094', 'ch_095']:
    paras = d[cid]['paras']
    with open(f'scratch/{cid}_paras.txt', 'w', encoding='utf-8') as f:
        f.write(f"Total paras: {len(paras)}\n")
        for i, p in enumerate(paras):
            f.write(f"[{i:03d}] {p}\n")
    print(f"Wrote {cid} paras: {len(paras)}")
