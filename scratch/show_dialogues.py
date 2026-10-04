import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Nhung\trans-tool\scratch\analysis_ch1_5.txt', 'r', encoding='utf-8') as f:
    text = f.read()

chapters = text.split("==================== CHAPTER: ")
for c in chapters[1:]:
    lines = c.split('\n')
    ch_name = lines[0].split()[0]
    print(f"\n*** CHAPTER {ch_name} ***")
    for l in lines:
        if l.startswith("P"):
            print("  " + l[:140])
