import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

def check_batch4():
    base_dir = 'novel_projects/phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương/chapters'
    all_ok = True

    for ch in range(52, 59):
        cid = f"ch_{ch:03d}"
        s_path = os.path.join(base_dir, cid, 'source.md')
        t_path = os.path.join(base_dir, cid, 'translation.md')

        if not os.path.exists(t_path):
            print(f"[{cid}] translation.md NOT ready.")
            all_ok = False
            continue

        s_paras = [p.strip() for p in open(s_path, encoding='utf-8').read().split('\n\n') if p.strip()]
        t_paras = [p.strip() for p in open(t_path, encoding='utf-8').read().split('\n\n') if p.strip()]

        print(f"\n=== Checking {cid} (source: {len(s_paras)}, trans: {len(t_paras)}) ===")
        if len(s_paras) != len(t_paras):
            print(f"  ❌ MISMATCH in paragraph count! raw={len(s_paras)}, trans={len(t_paras)}")
            all_ok = False

        # Entity verification
        entities = {
            '陸阡': 'Lục Thiên',
            '楚月月': 'Sở Nguyệt Nguyệt',
            '李媛媛': 'Lý Viện Viện',
            '啤酒肚': 'Bụng Bia',
            '大海': 'Đại Hải',
            '趙昀': 'Triệu Doãn',
            '陳騫': 'Trần Khiêm',
            '趙哲': 'Triệu Triết',
        }

        for idx, (sp, tp) in enumerate(zip(s_paras, t_paras)):
            # Check dialogue formatting
            if tp.startswith('-') or tp.startswith('–'):
                print(f"  ❌ [P{idx+1}] Dash at beginning of dialogue: {tp[:40]}")
                all_ok = False

            # Check entity presence
            for cn, vi in entities.items():
                if cn in sp and vi.lower() not in tp.lower():
                    print(f"  ⚠️ [P{idx+1}] {cn} ({vi}) in source but not in trans!")
                    print(f"     RAW:   {sp[:60]}")
                    print(f"     TRANS: {tp[:60]}")
                    all_ok = False

            # Check repeated Sở Niên Niên
            raw_snn = sp.count('楚年年')
            tr_snn = tp.count('Sở Niên Niên')
            if tr_snn >= 2 and raw_snn < tr_snn:
                print(f"  ⚠️ [P{idx+1}] Repeated name 'Sở Niên Niên' ({tr_snn} vs raw {raw_snn}): {tp[:60]}")
                all_ok = False

    return all_ok

if __name__ == '__main__':
    check_batch4()
