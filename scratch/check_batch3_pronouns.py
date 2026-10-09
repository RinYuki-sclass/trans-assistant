import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters"
cids = ['ch_045', 'ch_046', 'ch_047', 'ch_048', 'ch_049', 'ch_050', 'ch_051']

for cid in cids:
    trans_file = os.path.join(BASE_DIR, cid, "translation.md")
    with open(trans_file, 'r', encoding='utf-8') as f:
        content = f.read()

    body = content.split('---\n\n', 1)[1] if '---\n\n' in content else content
    paras = [p.strip() for p in body.split('\n\n') if p.strip()]

    print(f"\n--- Checking {cid} ({len(paras)} paras) ---")
    suspicious = []
    for i, p in enumerate(paras):
        narrative_parts = re.split(r'“[^”]*”', p)
        for n_part in narrative_parts:
            m1 = re.search(r'\b(Sở Niên Niên)\b[^.?!]{0,40}\b(anh ta|anh ấy|anh)\b', n_part)
            if m1:
                suspicious.append((i, "Sở Niên Niên followed by anh", n_part.strip()))
            m2 = re.search(r'\b(Cố Xuyên)\b[^.?!]{0,40}\b(cậu ta|cậu ấy|cậu)\b', n_part)
            if m2:
                suspicious.append((i, "Cố Xuyên followed by cậu", n_part.strip()))

    print(f"Suspicious count: {len(suspicious)}")
    for idx, reason, snippet in suspicious[:5]:
        print(f"  [Para {idx}] {reason}: {snippet[:90]}...")
