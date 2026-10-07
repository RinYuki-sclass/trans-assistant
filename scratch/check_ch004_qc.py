import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_md(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]
    return [p.strip() for p in content.split('\n\n') if p.strip()]

s_paras = parse_md(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_004\source.md')
t_paras = parse_md(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_004\translation.md')

print(f"Source paras: {len(s_paras)} | Translation paras: {len(t_paras)}")
assert len(s_paras) == len(t_paras), f"Mismatch: {len(s_paras)} vs {len(t_paras)}"
print("✅ EXACT 1:1 MATCH!")

# Check dialogue quote mismatches
quotes = re.findall(r'“([^”]+)”', '\n'.join(t_paras))
print(f"Total dialogue quotes: {len(quotes)}")
errors = 0
for i, q in enumerate(quotes, 1):
    if re.search(r'\bmày\b', q, re.I) and re.search(r'\btôi\b', q, re.I):
        print(f"❌ MISMATCH tôi - mày #{i}: {q}")
        errors += 1
    if re.search(r'\btao\b', q, re.I) and re.search(r'\bcậu\b', q, re.I):
        print(f"❌ MISMATCH tao - cậu #{i}: {q}")
        errors += 1
    if re.search(r'\btao\b', q, re.I) and re.search(r'\banh\b', q, re.I):
        print(f"❌ MISMATCH tao - anh #{i}: {q}")
        errors += 1

print(f"Total errors: {errors}")
