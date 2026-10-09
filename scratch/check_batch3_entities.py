import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

all_entities = {
    '陸阡': 'Lục Thiên',
    '楚月月': 'Sở Nguyệt Nguyệt',
    '李媛媛': 'Lý Viện Viện',
    '啤酒肚': 'Bụng Bia',
    '黃毛': 'Hoàng Mao',
    '密寶': 'Mật Bảo',
}

print("=== CHECKING ALL ARC 2 CHAPTERS (ch_031 -> ch_051) ===")
for ch in range(31, 52):
    s_path = f'novel_projects/phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương/chapters/ch_{ch:03d}/source.md'
    t_path = f'novel_projects/phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương/chapters/ch_{ch:03d}/translation.md'
    if not os.path.exists(s_path) or not os.path.exists(t_path):
        continue
    s_paras = [p.strip() for p in open(s_path, encoding='utf-8').read().split('\n\n') if p.strip()]
    t_paras = [p.strip() for p in open(t_path, encoding='utf-8').read().split('\n\n') if p.strip()]
    
    for idx, (sp, tp) in enumerate(zip(s_paras, t_paras)):
        for cn, vi in all_entities.items():
            if cn in sp and vi.lower() not in tp.lower():
                print(f'ch_{ch:03d} [P{idx+1}]: {cn} ({vi}) in raw, but "{vi}" not found in trans!')
                print(f'   RAW:   {sp}')
                print(f'   TRANS: {tp}\n')
                
        # Also check if 'Sở Niên Niên' appears >= 2 times in a single paragraph where raw has '楚年年' only <= 1 time
        raw_snn = sp.count('楚年年')
        tr_snn = tp.count('Sở Niên Niên')
        if tr_snn >= 2 and raw_snn < tr_snn:
            print(f'ch_{ch:03d} [P{idx+1}]: REPEATED NAME "Sở Niên Niên" ({tr_snn} times vs raw {raw_snn} times)')
            print(f'   RAW:   {sp}')
            print(f'   TRANS: {tp}\n')
