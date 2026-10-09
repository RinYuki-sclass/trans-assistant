import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters"
cids = ['ch_032', 'ch_033', 'ch_034', 'ch_035', 'ch_036', 'ch_037']

for cid in cids:
    trans_file = os.path.join(BASE_DIR, cid, "translation.md")
    with open(trans_file, 'r', encoding='utf-8') as f:
        content = f.read()

    body = content.split('---\n\n', 1)[1] if '---\n\n' in content else content
    paras = [p.strip() for p in body.split('\n\n') if p.strip()]

    print(f"\n--- Checking {cid} ({len(paras)} paras) ---")
    suspicious = []
    for i, p in enumerate(paras):
        # Look for dialogue parts vs narrative parts
        narrative_parts = re.split(r'“[^”]*”', p)
        for n_part in narrative_parts:
            # Check if Sở Niên Niên is followed by 'anh' in narration
            if re.search(r'Sở Niên Niên[^.?!]*\banh\b', n_part, re.IGNORECASE):
                suspicious.append((i, "Sở Niên Niên associated with 'anh' in narration", n_part.strip()))
            # Check if Cố Xuyên is followed by 'cậu' in narration
            if re.search(r'Cố Xuyên[^.?!]*\bcậu\b', n_part, re.IGNORECASE):
                suspicious.append((i, "Cố Xuyên associated with 'cậu' in narration", n_part.strip()))

    print(f"Suspicious count: {len(suspicious)}")
    for idx, reason, snippet in suspicious[:5]:
        print(f"  [Para {idx}] {reason}: {snippet[:100]}...")

