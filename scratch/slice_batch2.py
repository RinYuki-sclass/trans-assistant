import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch2_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# ch8: Page 13 from 31 to Page 15 at 20
p_ch8 = pages['13'][31:] + pages['14'] + pages['15'][:20]
# ch9: Page 15 from 20 to Page 16 at 32
p_ch9 = pages['15'][20:] + pages['16'][:32]
# ch10: Page 16 from 32 to Page 17 at 44
p_ch10 = pages['16'][32:] + pages['17'][:44]
# ch11: Page 17 from 44 to Page 19 at 47
p_ch11 = pages['17'][44:] + pages['18'] + pages['19'][:47]
# ch12: Page 19 from 47 to Page 21 at 11
p_ch12 = pages['19'][47:] + pages['20'] + pages['21'][:11]
# ch13: Page 21 from 11 to Page 22 at 48
p_ch13 = pages['21'][11:] + pages['22'][:48]
# ch14: Page 22 from 48 to Page 24 at 36
p_ch14 = pages['22'][48:] + pages['23'] + pages['24'][:36]
# ch15: Page 24 from 36 to Page 26 at 19
p_ch15 = pages['24'][36:] + pages['25'] + pages['26'][:19]

raw_chapters = {
    'ch_008': p_ch8,
    'ch_009': p_ch9,
    'ch_010': p_ch10,
    'ch_011': p_ch11,
    'ch_012': p_ch12,
    'ch_013': p_ch13,
    'ch_014': p_ch14,
    'ch_015': p_ch15,
}

cleaned_chapters = {}

for cid, paras in raw_chapters.items():
    print(f"=== {cid} ===")
    header = paras[0]
    print(f"Header: {header}")
    
    # Filter out header line if it is just 第X章
    body = paras[1:]
    
    # Check for author notes
    note_idx = None
    for idx, p in enumerate(body):
        if '作者有話說' in p or '作者有话说' in p:
            note_idx = idx
            break
            
    if note_idx is not None:
        print(f"Author note found at index {note_idx}: {body[note_idx][:50]}...")
        clean_body = body[:note_idx]
    else:
        clean_body = body
        
    print(f"Total paras after cleaning: {len(clean_body)}")
    print(f"First para: {clean_body[0][:60]}")
    print(f"Last para: {clean_body[-1][:60]}\n")
    cleaned_chapters[cid] = (header, clean_body)

# Save to scratch/cleaned_batch2.json
with open('scratch/cleaned_batch2.json', 'w', encoding='utf-8') as f:
    json.dump({cid: {'header': h, 'paras': p} for cid, (h, p) in cleaned_chapters.items()}, f, ensure_ascii=False, indent=2)

print("Saved scratch/cleaned_batch2.json successfully!")
