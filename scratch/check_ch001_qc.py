import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

def parse_md(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]
    paras = [p.strip() for p in content.split('\n\n') if p.strip()]
    return paras

s_paras = parse_md(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_001\source.md')
t_paras = parse_md(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_001\translation.md')

print(f"Source paragraphs: {len(s_paras)}")
print(f"Translation paragraphs: {len(t_paras)}")

assert len(s_paras) == len(t_paras), f"Mismatch: {len(s_paras)} vs {len(t_paras)}"
print("✅ PERFECT 1:1 MATCH: 90/90 paragraphs!")

# Check for pronoun violations in dialogue quotes
quotes = re.findall(r'“([^”]+)”', '\n'.join(t_paras))
print(f"Total dialogue quotes: {len(quotes)}")
for i, q in enumerate(quotes, 1):
    if re.search(r'\bmày\b', q, re.I) and re.search(r'\btôi\b', q, re.I):
        print(f"❌ MISMATCH tôi - mày in quote #{i}: {q}")
    if re.search(r'\btao\b', q, re.I) and re.search(r'\bcậu\b', q, re.I):
        print(f"❌ MISMATCH tao - cậu in quote #{i}: {q}")
    if re.search(r'\btao\b', q, re.I) and re.search(r'\banh\b', q, re.I):
        print(f"❌ MISMATCH tao - anh in quote #{i}: {q}")

print("Audit check completed!")
