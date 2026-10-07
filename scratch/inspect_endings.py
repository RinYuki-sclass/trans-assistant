import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch1_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

chs = {
    'ch_002': pages['4'][9:] + pages['5'][:34],
    'ch_003': pages['5'][34:] + pages['6'] + pages['7'] + pages['8'][:6],
    'ch_004': pages['8'][6:] + pages['9'][:16],
    'ch_005': pages['9'][16:] + pages['10'][:34],
    'ch_006': pages['10'][34:] + pages['11'][:36],
    'ch_007': pages['11'][36:] + pages['12'] + pages['13'][:31],
}

for ch_id, paras in chs.items():
    print(f"\n=== {ch_id} (Total {len(paras)} paras) ===")
    for i in range(len(paras)-7, len(paras)):
        print(f"  [{i}] {paras[i][:80]}")
