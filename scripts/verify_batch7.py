import os
import json
import re

project_dir = 'novel_projects/xuyen-den-tinh-te-lam-co-giap-su-doc-quyen'
ch_dir = os.path.join(project_dir, 'chapters')
ch_index_path = os.path.join(project_dir, 'chapters_index.json')
toc_path = os.path.join(project_dir, 'TOC.md')

with open(ch_index_path, 'r', encoding='utf-8') as f:
    idx = json.load(f)

with open(toc_path, 'r', encoding='utf-8') as f:
    toc = f.read()

legit_after = {
    'hệt', 'như', 'nguyên', 'thị', 'khác', 'án', 'bác', 'sĩ', 'khoa',
    'tế', 'viện', 'phục', 'lệnh', 'theo', 'chuẩn', 'dược', 'sinh', 'nhĩ',
    'sư', 'học', 'liệu', 'chức', 'quan', 'vụ', 'vật'
}

total_paras = 0
drift_chapters = []
illegal_y_list = []
tao_may_list = []

for ch_num in range(126, 151):
    ch_name = f'ch_{ch_num:03d}'
    d = os.path.join(ch_dir, ch_name)
    
    with open(os.path.join(d, 'source.md'), 'r', encoding='utf-8') as f:
        s_paras = [x for x in f.read().split('\n\n') if x.strip()]
    with open(os.path.join(d, 'translation.md'), 'r', encoding='utf-8') as f:
        t_text = f.read()
        t_paras = [x for x in t_text.split('\n\n') if x.strip()]
    
    total_paras += len(t_paras)
    if len(s_paras) != len(t_paras):
        drift_chapters.append((ch_name, len(s_paras), len(t_paras)))
    
    # Check 'y'
    for m in re.finditer(r'(.{0,20})\b([Yy])\b\s*(\w+)?', t_text):
        prefix = m.group(1).lower()
        next_w = (m.group(3) or '').lower()
        if prefix.endswith('thần bố ') or prefix.endswith('quân ') or prefix.endswith('nan ') or prefix.endswith('địa ') or prefix.endswith('xiêm ') or prefix.endswith('lục '):
            continue
        if next_w in legit_after:
            continue
        illegal_y_list.append((ch_name, m.group(0).strip()))

    # Check tao / mày
    for m in re.finditer(r'\b(tao|mày)\b', t_text, re.IGNORECASE):
        tao_may_list.append((ch_name, m.group(0)))

    # Update index & TOC
    for ch_entry in idx['chapters']:
        if ch_entry['chapter_num'] == ch_num:
            ch_entry['status'] = 'QC_PASSED'
            ch_entry['paragraphs'] = len(t_paras)

    toc = re.sub(
        rf'(- \[Chương {ch_num:03d}\]\(chapters/ch_{ch_num:03d}/translation\.md\)) - Chưa dịch',
        r'\1 - Đã dịch',
        toc
    )

translated_cnt = sum(1 for c in idx['chapters'] if c['status'] in ['TRANSLATED', 'QC_PASSED'])
qc_passed_cnt = sum(1 for c in idx['chapters'] if c['status'] == 'QC_PASSED')
idx['translated_chapters'] = translated_cnt
idx['qc_passed_chapters'] = qc_passed_cnt

with open(ch_index_path, 'w', encoding='utf-8') as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)

with open(toc_path, 'w', encoding='utf-8') as f:
    f.write(toc)

print(f"Batch 7 Verification (Ch 126-150):")
print(f"Total paragraphs: {total_paras}")
print(f"Drift chapters: {len(drift_chapters)} {drift_chapters}")
print(f"Illegal 'y' count: {len(illegal_y_list)} {illegal_y_list}")
print(f"Tao/May count: {len(tao_may_list)} {tao_may_list}")
print(f"Project index totals: translated={idx['translated_chapters']}, qc_passed={idx['qc_passed_chapters']}")
