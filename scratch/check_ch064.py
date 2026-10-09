import sys

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_064/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    text = f.read()

paras = text.split('\n\n')
print(f'Total paragraphs: {len(paras)}')
straight_count = text.count('"')
print(f'Straight quotes count: {straight_count}')

for i, p in enumerate(paras):
    if 'shen' in p.lower():
        print(f'Alert shen at P{i}: {p}')
    if 'ông tống' in p.lower():
        print(f'Alert ong tong at P{i}: {p}')
