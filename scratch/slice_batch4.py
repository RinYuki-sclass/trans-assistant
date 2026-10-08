import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch4_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# ch24: Page 40 (4) -> Page 41 (42)
p_ch24 = pages['40'][4:] + pages['41'][:42]

# ch25: Page 41 (42) -> Page 44 (8)
p_ch25 = pages['41'][42:] + pages['42'] + pages['43'] + pages['44'][:8]

# ch26: Page 44 (8) -> Page 49 (13)
p_ch26 = pages['44'][8:] + pages['45'] + pages['46'] + pages['47'] + pages['48'] + pages['49'][:13]

# ch27: Page 49 (13) -> Page 54 (35)
p_ch27 = pages['49'][13:] + pages['50'] + pages['51'] + pages['52'] + pages['53'] + pages['54'][:35]

# ch28: Page 54 (35) -> Page 57 (30)
p_ch28 = pages['54'][35:] + pages['55'] + pages['56'] + pages['57'][:30]

# ch29: Page 57 (30) -> Page 61 (47)
p_ch29 = pages['57'][30:] + pages['58'] + pages['59'] + pages['60'] + pages['61'][:47]

# ch30: Page 61 (47) -> Page 64 (45)
p_ch30 = pages['61'][47:] + pages['62'] + pages['63'] + pages['64'][:45]

raw_chs = {
    'ch_024': p_ch24,
    'ch_025': p_ch25,
    'ch_026': p_ch26,
    'ch_027': p_ch27,
    'ch_028': p_ch28,
    'ch_029': p_ch29,
    'ch_030': p_ch30,
}

cleaned = {}

for cid, paras in raw_chs.items():
    header = paras[0]
    body = paras[1:]
    
    note_idx = None
    for idx, p in enumerate(body):
        if '作者有話說' in p or '作者有话说' in p:
            note_idx = idx
            break
            
    if note_idx is not None:
        print(f"[{cid}] Author note found at index {note_idx}: {body[note_idx][:50]}...")
        clean_body = body[:note_idx]
    else:
        clean_body = body
        
    print(f"[{cid}] Header: {header} | Paras: {len(clean_body)}")
    print(f"      First: {clean_body[0][:60]}")
    print(f"      Last:  {clean_body[-1][:60]}\n")
    cleaned[cid] = {'header': header, 'paras': clean_body}

with open('scratch/cleaned_batch4.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned, f, ensure_ascii=False, indent=2)

print("Saved scratch/cleaned_batch4.json successfully!")
