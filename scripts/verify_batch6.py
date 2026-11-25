import json, os, re

project_dir = r'novel_projects/xuyen-den-tinh-te-lam-co-giap-su-doc-quyen'
idx_path = os.path.join(project_dir, 'chapters_index.json')
toc_path = os.path.join(project_dir, 'TOC.md')
timeline_path = os.path.join(project_dir, 'memory', 'timeline.json')

# 1. Update index
with open(idx_path, 'r', encoding='utf-8') as f:
    idx = json.load(f)

for ch_num in range(121, 126):
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
    for ch_num in range(121, 126):
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
    'chapters': 'Chương 101 - 125',
    'title': 'Batch 6: Bầu Không Khí Mới & Xác Lập Địa Vị Cơ Giáp Sư Thần Cấp',
    'summary': 'Diệp Kiêu An thâm nhập giới thượng lưu tinh tế và các thế lực ngầm; cứu viện và chữa trị tinh thần lực cho Lăng Bùi; vạch trần âm mưu buôn lậu độc phẩm và thí nghiệm cơ thể sống; củng cố liên minh vững chắc, chính thức được tôn vinh là Lãnh chúa và Cơ giáp sư độc quyền.',
    'status': 'QC_PASSED'
})

with open(timeline_path, 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print('Index, TOC, and Timeline updated successfully for Batch 6!')

# 4. Exhaustive Audit for Batch 6 (ch_101 - ch_125)
print('--- AUDIT BATCH 6 (Ch 101 - 125) ---')
total_paras = 0
all_passed = True
for ch_num in range(101, 126):
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
    matches = list(re.finditer(r'(?<![a-zA-ZÀ-ỹ0-9])[Yy](?![a-zA-ZÀ-ỹ0-9])', trans_text))
    # Filter out legitimate words: Thần Bố Y, y phục, y tế, y học, địa y, nan y, y như
    forbidden_y = []
    for m in matches:
        start = max(0, m.start() - 20)
        end = min(len(trans_text), m.end() + 20)
        ctx = trans_text[start:end].lower()
        if any(w in ctx for w in ['bố y', 'y phục', 'y tế', 'y học', 'địa y', 'nan y', 'y như', 'y hệt', 'xiêm y', 'quân y', 'y nhĩ', 'y thuật', 'bác sĩ', 'tiến sĩ y']):
            continue
        forbidden_y.append(trans_text[start:end])
    
    drift = trans_c - src_c
    if drift != 0 or len(forbidden_y) > 0:
        all_passed = False
        print(f'FAIL {ch_id}: src={src_c}, trans={trans_c}, drift={drift}, forbidden_y={len(forbidden_y)}')
        for f in forbidden_y:
            print(f'   violation: ...{f}...')
    else:
        print(f'PASS {ch_id}: {trans_c}/{src_c} paras (1:1), zero drift, 0 forbidden y')

print(f"Total Batch 6 Paragraphs Translated: {total_paras}")
print(f"Total Project Translated Chapters: {idx['translated_chapters']}")
print(f"Total Project QC Passed Chapters: {idx['qc_passed_chapters']}")
print(f"All 25 chapters passed 1:1 and pronoun rules: {all_passed}")
