import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch3_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# ch16: Page 26 (19) -> Page 28 (4)
p_ch16 = pages['26'][19:] + pages['27'] + pages['28'][:4]
# ch17: Page 28 (4) -> Page 29 (29)
p_ch17 = pages['28'][4:] + pages['29'][:29]
# ch18: Page 29 (29) -> Page 31 (29)
p_ch18 = pages['29'][29:] + pages['30'] + pages['31'][:29]
# ch19: Page 31 (29) -> Page 32 (45)
p_ch19 = pages['31'][29:] + pages['32'][:45]
# ch20: Page 32 (45) -> Page 34 (51)
p_ch20 = pages['32'][45:] + pages['33'] + pages['34'][:51]
# ch21: Page 34 (51) -> Page 36 (25)
p_ch21 = pages['34'][51:] + pages['35'] + pages['36'][:25]
# ch22: Page 36 (25) -> Page 38 (14)
p_ch22 = pages['36'][25:] + pages['37'] + pages['38'][:14]
# ch23: Page 38 (14) -> Page 40 (4)
p_ch23 = pages['38'][14:] + pages['39'] + pages['40'][:4]

raw_chapters = {
    'ch_016': p_ch16,
    'ch_017': p_ch17,
    'ch_018': p_ch18,
    'ch_019': p_ch19,
    'ch_020': p_ch20,
    'ch_021': p_ch21,
    'ch_022': p_ch22,
    'ch_023': p_ch23,
}

cleaned_chapters = {}

for cid, paras in raw_chapters.items():
    print(f"=== {cid} ===")
    header = paras[0]
    print(f"Header: {header}")
    
    body = paras[1:]
    
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

# Save to scratch/cleaned_batch3.json
with open('scratch/cleaned_batch3.json', 'w', encoding='utf-8') as f:
    json.dump({cid: {'header': h, 'paras': p} for cid, (h, p) in cleaned_chapters.items()}, f, ensure_ascii=False, indent=2)

print("Saved scratch/cleaned_batch3.json successfully!")
