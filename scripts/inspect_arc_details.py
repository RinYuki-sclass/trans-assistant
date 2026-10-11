import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = os.path.join('novel_projects', 'tra-nam-này-không-đáng-được-tẩy-trắng', 'chapters')

arc_samples = {
    'Arc 1 (Công tử)': 'ch_001',
    'Arc 2 (Đại hiệp)': 'ch_019',
    'Arc 3 (Omega)': 'ch_031',
    'Arc 4 (Võng du)': 'ch_043',
    'Arc 5 (Phu lang)': 'ch_058',
    'Arc 6 (Mạt thế)': 'ch_075',
    'Arc 7 (Phú nhị đại)': 'ch_089',
    'Arc 8 (Chân thiếu gia)': 'ch_103',
    'Arc 9 (Cha dượng)': 'ch_116',
    'Arc 10 (Phủ doãn)': 'ch_128',
    'Arc 11 (Ảnh đế)': 'ch_143',
    'Arc 12 (Tu chân)': 'ch_155',
}

for arc_name, ch in arc_samples.items():
    sf = os.path.join(p, ch, 'source.md')
    with open(sf, 'r', encoding='utf-8') as f:
        text = f.read(3500)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    print(f"=== {arc_name} ({ch}) ===")
    for l in lines[:15]:
        print(" ", l)
    print()
