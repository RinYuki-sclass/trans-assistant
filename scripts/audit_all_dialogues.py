import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
p = 'd:/Nhung/trans-tool/novel_projects/cường-chế-ái-hoàn-tựu-hồi-đáng-thiểm-cẩu-công-bị-đào-không-liễu/chapters'

for i in range(1, 21):
    cid = f"ch_{i:03d}"
    tfile = os.path.join(p, cid, 'translation.md')
    if not os.path.exists(tfile):
        continue
    lines = open(tfile, encoding='utf-8').read().splitlines()
    found = []
    for idx, l in enumerate(lines):
        # Look for dialogues with anh / em / tôi / cậu / chú / Thẩm Kinh Dạng / Y Lâu
        if ('“' in l or '”' in l) and any(w in l for w in ['Thẩm Kinh Dạng', 'Kinh Dạng', 'Y Lâu', 'ông xã', 'chồng', 'anh', 'em', 'cậu', 'chú']):
            found.append((idx+1, l.strip()))
    if found:
        print(f"=== {cid} ===")
        for line_num, f in found:
            print(f"  [{line_num}] {f}")
