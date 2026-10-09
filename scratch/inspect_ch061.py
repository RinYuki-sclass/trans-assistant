import sys
sys.stdout.reconfigure(encoding='utf-8')

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_061/translation.md'
p_src = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_061/source.md'

with open(p_trans, 'r', encoding='utf-8') as f:
    t_paras = f.read().split('\n\n')

with open(p_src, 'r', encoding='utf-8') as f:
    s_paras = f.read().split('\n\n')

print(f'Total paras: {len(t_paras)}')
for i in range(len(t_paras)):
    t = t_paras[i]
    s = s_paras[i]
    alerts = []
    if 'shen' in t.lower(): alerts.append('shen')
    if 'ông tống' in t.lower(): alerts.append('ông tống')
    if 'anh ta' in t.lower(): alerts.append('anh ta')
    if 'cậu ta' in t.lower(): alerts.append('cậu ta')
    if '"' in t: alerts.append('straight_quote')
    if alerts:
        print(f'P{i} {alerts}:\n  SRC: {s[:90]}\n  TRN: {t[:120]}')
