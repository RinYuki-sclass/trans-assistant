import os
import re
import sys
import json
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

base = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters'

all_text = ""
ch_data = {}
for i in range(1, 6):
    ch = f'ch_{i:03d}'
    src_file = os.path.join(base, ch, 'source.md')
    with open(src_file, 'r', encoding='utf-8') as f:
        c = f.read()
        ch_data[ch] = c
        all_text += "\n" + c

# Let's inspect all dialogue lines with context
print("=== SCANNING ENTITIES & NAMES ===")
# Find names ending in 先生, 總, 哥, 少爺, 媽, etc., or standard names
patterns = [
    r'[\u4e00-\u9fa5]{2,4}(?:先生|總|少爺|夫人|特助|秘書|隊長|指揮官|阿姨|叔叔|醫生|管家)',
    r'“([^”]+)”',
    r'「([^」]+)」'
]

for pat in patterns[:1]:
    matches = re.findall(pat, all_text)
    print(Counter(matches).most_common(30))

print("\n=== SCANNING CHARACTERS MENTIONED ===")
# Look for common surnames and 2-3 char sequences
# Let's dump all occurrences of 2-3 character proper names
# We know Jiang Minglang 江明朗, Fu Yunchuan 傅雲川 / 傅云川
test_names = ['傅雲川', '傅云川', '江明朗', '白', '林', '陳', '沈', '顧', '李', '張', '王', '宋', '陸', '程', '系統', '汪汪', '阿拉斯加']
for tn in test_names:
    c = all_text.count(tn)
    if c > 0:
        print(f"{tn}: {c} times")

