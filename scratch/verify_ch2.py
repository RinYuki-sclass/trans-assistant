# -*- coding: utf-8 -*-
with open(r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_002\source.md', 'r', encoding='utf-8') as f:
    s_lines = [l.strip() for l in f if l.strip() and not l.startswith('---') and not l.startswith('title:') and not l.startswith('chapter_index:')]

with open(r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_002\translation.md', 'r', encoding='utf-8') as f:
    t_lines = [l.strip() for l in f if l.strip() and not l.startswith('---') and not l.startswith('title:') and not l.startswith('chapter_index:')]

print(f"Source count: {len(s_lines)}, Translation count: {len(t_lines)}")
assert len(s_lines) == len(t_lines)

# Check forbidden pronouns:
for i, t in enumerate(t_lines):
    # Check if 'hắn' is mistakenly used for Pho Van Xuyen or Giang Minh Lang
    if " hắn " in f" {t} " or " hắn," in t or " hắn." in t:
        print(f"[Warning] Potential 'hắn' in line {i+1}: {t}")

print("Validation completed successfully.")
