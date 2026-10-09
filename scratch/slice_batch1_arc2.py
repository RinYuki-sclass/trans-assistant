import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch1_arc2_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Combine paras:
# ch32: Page 67 (13:) -> Page 69 (:16)
# ch33: Page 69 (17:) -> Page 71 (:21)
# ch34: Page 71 (22:) -> Page 73 (:23)
# ch35: Page 73 (24:) -> Page 75 (:21)
# ch36: Page 75 (22:) -> Page 77 (:11)
# ch37: Page 77 (12:) -> Page 79 (:47)

headers = {
    'ch_032': (67, 12, 69, 16),
    'ch_033': (69, 16, 71, 21),
    'ch_034': (71, 21, 73, 23),
    'ch_035': (73, 23, 75, 21),
    'ch_036': (75, 21, 77, 11),
    'ch_037': (77, 11, 79, 47),
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

with open('scratch/cleaned_batch1_arc2.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Batch 1 slicing and cleaning complete!")
