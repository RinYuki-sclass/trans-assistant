# -*- coding: utf-8 -*-
import sys

with open(r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_001\source.md', 'r', encoding='utf-8') as f:
    s_lines = [l.strip() for l in f if l.strip() and not l.startswith('---') and not l.startswith('title:') and not l.startswith('chapter_index:')]

with open(r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_001\translation.md', 'r', encoding='utf-8') as f:
    t_lines = [l.strip() for l in f if l.strip() and not l.startswith('---') and not l.startswith('title:') and not l.startswith('chapter_index:')]

print(f"Source count: {len(s_lines)}, Translation count: {len(t_lines)}")
assert len(s_lines) == len(t_lines)

# Check pronouns
# We want:
# 1. Cong (Giang Minh Lang) narration = "cậu"
# 2. Thu (Pho Van Xuyen) narration = "anh"
# 3. Check if any forbidden pronouns occur in narration
# In ch_001:
# - Pho Van Xuyen is the main character in the tower scene (paragraphs 54 to 80). Let's check how he is referred to: "Phó Vân Xuyên", "anh".
# - Giang Minh Lang appears in paragraphs 81 to 95: "thiếu niên", "cậu".
# - In paragraph 59: "người qua đường... cắt đứt sự chú ý của hắn" (passerby is an unnamed extra man, "hắn" is fine for random extra male).
# Let's verify each paragraph around Pho Van Xuyen and Giang Minh Lang!

for i, t in enumerate(t_lines):
    if i >= 50 and i < 80: # Pho Van Xuyen scene
        if " hắn " in f" {t} " or " hắn," in t or " hắn." in t:
            print(f"[Warning] Potential 'hắn' in Pho Van Xuyen scene (line {i+1}): {t}")
    if i >= 80: # Giang Minh Lang scene
        if " hắn " in f" {t} " or " hắn," in t or " hắn." in t:
            print(f"[Warning] Potential 'hắn' in Giang Minh Lang scene (line {i+1}): {t}")

print("Validation completed successfully.")
