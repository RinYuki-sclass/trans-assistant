import os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'd:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters'
for ch_num in range(16, 24):
    ch_id = f'ch_{ch_num:03d}'
    p = os.path.join(base, ch_id, 'source.md')
    with open(p, 'r', encoding='utf-8') as f:
        paras = [x for x in f.read().split('\n\n') if x.strip()]
    first_clean = paras[0].replace('\n', ' ')[:50]
    p1 = paras[1][:25] if len(paras) > 1 else ''
    last_clean = paras[-1].replace('\n', ' ')[:50]
    print(f'{ch_id}: total {len(paras)} | p[0]="{first_clean}" | p[1]="{p1}" | p[-1]="{last_clean}"')
