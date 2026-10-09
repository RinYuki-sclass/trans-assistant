import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch1_arc4_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

def get_paras(p_num):
    return pages[str(p_num)]['paragraphs']

chapters_raw = {}

# ch_090: P186[28:] + P187[:] + P188[:43]
ch_090_paras = get_paras(186)[28:] + get_paras(187) + get_paras(188)[:43]
chapters_raw['ch_090'] = {
    'title': 'Chương 90: Bị Lục giáo sư hớp hồn',
    'paras': [p.strip() for p in ch_090_paras if p.strip()]
}

# ch_091: P188[49:] + P189[:] + P190[:36]
ch_091_paras = get_paras(188)[49:] + get_paras(189) + get_paras(190)[:36]
chapters_raw['ch_091'] = {
    'title': 'Chương 91: Tuyến thể ngứa ngáy',
    'paras': [p.strip() for p in ch_091_paras if p.strip()]
}

# ch_092: P190[42:] + P191[:] + P192[:46]
ch_092_paras = get_paras(190)[42:] + get_paras(191) + get_paras(192)[:46]
chapters_raw['ch_092'] = {
    'title': 'Chương 92: Dịch Nam trà trộn',
    'paras': [p.strip() for p in ch_092_paras if p.strip()]
}

# ch_093: P192[47:] + P193[:] + P194[:43]
ch_093_paras = get_paras(192)[47:] + get_paras(193) + get_paras(194)[:43]
chapters_raw['ch_093'] = {
    'title': 'Chương 93: Cảnh cáo và nghi ngờ',
    'paras': [p.strip() for p in ch_093_paras if p.strip()]
}

# ch_094: P194[44:] + P195[:] + P196[:47]
ch_094_paras = get_paras(194)[44:] + get_paras(195) + get_paras(196)[:47]
chapters_raw['ch_094'] = {
    'title': 'Chương 94: Khám bệnh và lời tỏ tình',
    'paras': [p.strip() for p in ch_094_paras if p.strip()]
}

# ch_095: P196[48:] + P197[:] + P198[:] + P199[:31]
ch_095_paras = get_paras(196)[48:] + get_paras(197) + get_paras(198) + get_paras(199)[:31]
chapters_raw['ch_095'] = {
    'title': 'Chương 95: Vạt váy tung bay dưới trăng',
    'paras': [p.strip() for p in ch_095_paras if p.strip()]
}

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters"

for cid, item in chapters_raw.items():
    cdir = os.path.join(base_dir, cid)
    os.makedirs(cdir, exist_ok=True)
    header = f"---\ntitle: {item['title']}\n---\n\n"
    content = header + "\n\n".join(item['paras']) + "\n"
    source_file = os.path.join(cdir, "source.md")
    with open(source_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {cid} source.md: {len(item['paras'])} paras")

with open('scratch/batch1_sliced.json', 'w', encoding='utf-8') as f:
    json.dump(chapters_raw, f, ensure_ascii=False, indent=2)

print("Batch 1 sources sliced and created successfully!")
