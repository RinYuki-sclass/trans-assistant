import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch3_arc2_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

headers = {
    'ch_045': (94, 12, 96, 21),
    'ch_046': (96, 21, 98, 11),
    'ch_047': (98, 11, 100, 19),
    'ch_048': (100, 19, 102, 21),
    'ch_049': (102, 21, 104, 35),
    'ch_050': (104, 35, 108, 13),
    'ch_051': (108, 13, 110, 8),
}

results = {}

for cid, (p_start, idx_start, p_end, idx_end) in headers.items():
    raw_paras = []
    for p in range(p_start, p_end + 1):
        p_paras = pages[str(p)]['paragraphs']
        if p == p_start and p == p_end:
            raw_paras.extend(p_paras[idx_start:idx_end])
        elif p == p_start:
            raw_paras.extend(p_paras[idx_start:])
        elif p == p_end:
            raw_paras.extend(p_paras[:idx_end])
        else:
            raw_paras.extend(p_paras)

    header = raw_paras[0]
    body = raw_paras[1:]

    # Remove author notes if present at the end
    author_note_idx = None
    for idx, para in enumerate(body):
        if '作者有話說' in para or '作者有话说' in para:
            author_note_idx = idx
            break

    if author_note_idx is not None:
        print(f"[{cid}] Author note found at index {author_note_idx}: {body[author_note_idx][:40]}")
        clean_body = body[:author_note_idx]
    else:
        clean_body = body

    # Clean watermarks from paragraphs
    cleaned_paras = []
    for p in clean_body:
        p_clean = p.replace('遖鳯獨傢', '').replace('南风独家', '').strip()
        if p_clean:
            cleaned_paras.append(p_clean)

    results[cid] = {
        'header': header,
        'paras': cleaned_paras,
        'count': len(cleaned_paras)
    }

    print(f"[{cid}] Header: {header} | Total paras: {len(cleaned_paras)}")
    print(f"       First: {cleaned_paras[0][:50]}")
    print(f"       Last:  {cleaned_paras[-1][:50]}\n")

with open('scratch/cleaned_batch3_arc2.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Batch 3 slicing and cleaning complete!")
