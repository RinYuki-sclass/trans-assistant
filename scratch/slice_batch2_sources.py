import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch2_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

def get_paras(p_num):
    return pages[str(p_num)]['paragraphs']

titles = {
    'ch_096': 'Chương 96: Nghi ngờ và thăm dò',
    'ch_097': 'Chương 97: Nếu em đồng ý thì sao',
    'ch_098': 'Chương 98: Sân đấu thực chiến rực lửa',
    'ch_099': 'Chương 99: Cơn sốt tin tức tố bùng phát',
    'ch_100': 'Chương 100: Gõ cửa căn hộ áp mái',
    'ch_101': 'Chương 101: Tỉnh giấc chung giường',
    'ch_102': 'Chương 102: Giúp chị gái xử lý hoa đào'
}

chapters_raw = {}

# ch_096: P199[32:] + P200[:] + P201[:29]
ch_096_paras = get_paras(199)[32:] + get_paras(200) + get_paras(201)[:29]
chapters_raw['ch_096'] = [p.strip() for p in ch_096_paras if p.strip()]

# ch_097: P201[30:] + P202[:] + P203[:18]
ch_097_paras = get_paras(201)[30:] + get_paras(202) + get_paras(203)[:18]
chapters_raw['ch_097'] = [p.strip() for p in ch_097_paras if p.strip()]

# ch_098: P203[23:] + P204[:] + P205[:17]
ch_098_paras = get_paras(203)[23:] + get_paras(204) + get_paras(205)[:17]
chapters_raw['ch_098'] = [p.strip() for p in ch_098_paras if p.strip()]

# ch_099: P205[23:] + P206[:] + P207[:45]
ch_099_paras = get_paras(205)[23:] + get_paras(206) + get_paras(207)[:45]
chapters_raw['ch_099'] = [p.strip() for p in ch_099_paras if p.strip()]

# ch_100: P207[50:] + P208[:] + P209[:28]
ch_100_paras = get_paras(207)[50:] + get_paras(208) + get_paras(209)[:28]
chapters_raw['ch_100'] = [p.strip() for p in ch_100_paras if p.strip()]

# ch_101: P209[33:] + P210[:] + P211[:34]
ch_101_paras = get_paras(209)[33:] + get_paras(210) + get_paras(211)[:34]
chapters_raw['ch_101'] = [p.strip() for p in ch_101_paras if p.strip()]

# ch_102: P211[35:] + P212[:] + P213[:35]
ch_102_paras = get_paras(211)[35:] + get_paras(212) + get_paras(213)[:35]
chapters_raw['ch_102'] = [p.strip() for p in ch_102_paras if p.strip()]

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters"

for cid, paras in chapters_raw.items():
    cdir = os.path.join(base_dir, cid)
    os.makedirs(cdir, exist_ok=True)
    header = f"---\ntitle: {titles[cid]}\n---\n\n"
    content = header + "\n\n".join(paras) + "\n"
    source_file = os.path.join(cdir, "source.md")
    with open(source_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {cid} source.md: {len(paras)} paras")

with open('scratch/batch2_sliced.json', 'w', encoding='utf-8') as f:
    json.dump({cid: {'title': titles[cid], 'paras': paras} for cid, paras in chapters_raw.items()}, f, ensure_ascii=False, indent=2)

print("Batch 2 sources sliced and created successfully!")
