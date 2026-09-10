# -*- coding: utf-8 -*-
with open('input/trans/354-en.md', 'r', encoding='utf-8') as f:
    en_paras = [p.strip() for p in f.read().split('\n\n') if p.strip()]
with open('scratch/354-vi.md', 'r', encoding='utf-8') as f:
    vi_paras = [p.strip() for p in f.read().split('\n\n') if p.strip()]

assert len(en_paras) == len(vi_paras), f'Mismatch: EN={len(en_paras)} vs VI={len(vi_paras)}'
print(f'SUCCESS: Exactly {len(en_paras)} paragraphs matched 1:1.')

mismatches = 0
for i in range(len(en_paras)):
    en_quote = en_paras[i].startswith(('“', '"', '‘', "'"))
    vi_quote = vi_paras[i].startswith(('“', '"', '‘', "'"))
    if en_quote != vi_quote:
        print(f'Warning at P{i+1}: EN quote={en_quote} vs VI quote={vi_quote}')
        mismatches += 1

if mismatches == 0:
    print("All quotes and paragraphs aligned perfectly 100%!")
