import json, os, re

project_dir = r'novel_projects/xuyen-den-tinh-te-lam-co-giap-su-doc-quyen'
idx_path = os.path.join(project_dir, 'chapters_index.json')
toc_path = os.path.join(project_dir, 'TOC.md')
timeline_path = os.path.join(project_dir, 'memory', 'timeline.json')

# 1. Update index
with open(idx_path, 'r', encoding='utf-8') as f:
    idx = json.load(f)

for ch_num in range(97, 101):
    ch_id = f'ch_{ch_num:03d}'
    ch_dir = os.path.join(project_dir, 'chapters', ch_id)
    trans_p = os.path.join(ch_dir, 'translation.md')
    p_count = len(open(trans_p, encoding='utf-8').read().strip().split('\n\n'))
    
    for ch in idx['chapters']:
        if ch['id'] == ch_id:
            ch['status'] = 'QC_PASSED'
            ch['translation_exists'] = True
            ch['qc_exists'] = True
            ch['paragraphs'] = p_count

idx['translated_chapters'] = sum(1 for ch in idx['chapters'] if ch.get('translation_exists'))
idx['qc_passed_chapters'] = sum(1 for ch in idx['chapters'] if ch.get('status') == 'QC_PASSED')

with open(idx_path, 'w', encoding='utf-8') as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)

# 2. Update TOC.md
with open(toc_path, 'r', encoding='utf-8') as f:
    toc_lines = f.readlines()

new_toc = []
for line in toc_lines:
    updated = False
    for ch_num in range(97, 101):
        ch_id = f'ch_{ch_num:03d}'
        if f'[{ch_id}]' in line:
            ch_dir = os.path.join(project_dir, 'chapters', ch_id)
            trans_p = os.path.join(ch_dir, 'translation.md')
            p_count = len(open(trans_p, encoding='utf-8').read().strip().split('\n\n'))
            parts = line.split('|')
            if len(parts) >= 6:
                parts[3] = f' {p_count} '
                parts[4] = ' QC_PASSED '
                new_toc.append('|'.join(parts))
                updated = True
                break
    if not updated:
        new_toc.append(line)

with open(toc_path, 'w', encoding='utf-8') as f:
    f.writelines(new_toc)

# 3. Update timeline.json
with open(timeline_path, 'r', encoding='utf-8') as f:
    timeline = json.load(f)

timeline['events'].append({
    'chapters': 'Chương 074 - 100',
    'title': 'Batch 5: Chiến Tranh Tinh Cầu & Đột Phá Thí Nghiệm',
    'summary': 'Diệp Kiêu An giải cứu An Lê, bẻ khóa bí mật virus Hương Giới và thực nghiệm thể S-589; đánh lui Trùng Đế trên chiến trường tinh tế; đối mặt với biến cố tình cảm và vết thương tinh thần lực của Lăng Bùi, chính thức xác lập ấn ký tinh thần lực trọn đời.',
    'status': 'QC_PASSED'
})

with open(timeline_path, 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print('Index, TOC, and Timeline updated successfully!')

# 4. Exhaustive Audit for Batch 5 (ch_074 - ch_100)
print('--- AUDIT BATCH 5 (Ch 074 - 100) ---')
total_paras = 0
all_passed = True
for ch_num in range(74, 101):
    ch_id = f'ch_{ch_num:03d}'
    ch_dir = os.path.join(project_dir, 'chapters', ch_id)
    src_p = os.path.join(ch_dir, 'source.md')
    trans_p = os.path.join(ch_dir, 'translation.md')
    
    src_lines = open(src_p, encoding='utf-8').read().strip().split('\n\n')
    trans_lines = open(trans_p, encoding='utf-8').read().strip().split('\n\n')
    
    src_c = len(src_lines)
    trans_c = len(trans_lines)
    total_paras += trans_c
    
    # Check forbidden 'y' as standalone pronoun
    trans_text = '\n\n'.join(trans_lines)
    y_matches = re.findall(r'(?<![a-zA-ZÀ-ỹ0-9])[Yy](?![a-zA-ZÀ-ỹ0-9])', trans_text)
    
    drift = trans_c - src_c
    if drift != 0 or len(y_matches) > 0:
        all_passed = False
        print(f'FAIL {ch_id}: src={src_c}, trans={trans_c}, drift={drift}, y_matches={len(y_matches)}')
    else:
        print(f'PASS {ch_id}: {trans_c}/{src_c} paras (1:1), zero drift, 0 y-matches')

print(f'Total Batch 5 Paragraphs Translated: {total_paras}')
print(f'All 27 chapters passed 1:1 and pronoun rules: {all_passed}')
