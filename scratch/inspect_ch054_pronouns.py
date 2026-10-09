import sys
sys.stdout.reconfigure(encoding='utf-8')

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_054/translation.md'
p_src = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_054/source.md'

with open(p_trans, 'r', encoding='utf-8') as f:
    t_paras = f.read().split('\n\n')

with open(p_src, 'r', encoding='utf-8') as f:
    s_paras = f.read().split('\n\n')

for i in range(len(t_paras)):
    t = t_paras[i]
    s = s_paras[i]
    # Check if 'hắn' is in t
    if 'hắn' in t:
        print(f'P{i} [HẮN]: {t}')
    # Check if 'Chu Lạc Lạc' is referred as anything
    if 'chu lạc lạc' in t.lower() or 'lạc lạc' in t.lower():
        print(f'P{i} [CHU LAC LAC]: {t}')
