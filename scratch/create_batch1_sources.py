import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch1_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

p_ch2 = pages['4'][9:] + pages['5'][:34]
p_ch3 = pages['5'][34:] + pages['6'] + pages['7'] + pages['8'][:6]
p_ch4 = pages['8'][6:] + pages['9'][:16]
p_ch5 = pages['9'][16:] + pages['10'][:34]
p_ch6 = pages['10'][34:] + pages['11'][:36]
p_ch7 = pages['11'][36:] + pages['12'] + pages['13'][:31]

clean_chs = {
    'ch_002': ('Chương 2: Đến đấm cậu này', p_ch2[:66]),
    'ch_003': ('Chương 3: Tôi muốn theo đuổi cậu', p_ch3[:78]),
    'ch_004': ('Chương 4: Thiết lập nam thần học đường sụp đổ', p_ch4[:50]),
    'ch_005': ('Chương 5: Có thể tha thứ cho tôi không', p_ch5[:59]),
    'ch_006': ('Chương 6: Ngủ ở chỗ tôi', p_ch6[:49]),
    'ch_007': ('Chương 7: Là thủ đoạn dụ dỗ sao?', p_ch7[:70]),
}

base_dir = r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters'

for cid, (title, paras) in clean_chs.items():
    cdir = os.path.join(base_dir, cid)
    os.makedirs(cdir, exist_ok=True)
    source_path = os.path.join(cdir, 'source.md')
    header = f"---\ntitle: {title}\n---\n\n"
    content = header + '\n\n'.join(paras) + '\n'
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {source_path}: {len(paras)} paras")
