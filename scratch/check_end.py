import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Nhung\RIDI\trans-assistant\scratch\talebed_cache\page_110.html", "r", encoding="utf-8") as f:
    h110 = f.read()

with open(r"d:\Nhung\RIDI\trans-assistant\scratch\talebed_cache\page_111.html", "r", encoding="utf-8") as f:
    h111 = f.read()

m110 = re.search(r'<div class="read-content">(.*?)</div>\s*</div>\s*<div class="px-6', h110, re.DOTALL)
m111 = re.search(r'<div class="read-content">(.*?)</div>\s*</div>\s*<div class="px-6', h111, re.DOTALL)

p110 = re.findall(r'<p>(.*?)</p>', m110.group(1))
p111 = re.findall(r'<p>(.*?)</p>', m111.group(1))

print("=== Page 110 Headers / Paras ===")
for p in p110:
    if "第" in p and "章" in p:
        print("  H110:", p)
print("P110 last 5:")
for p in p110[-5:]:
    print(" ", p)

print("=== Page 111 Headers / Paras ===")
for p in p111:
    if "第" in p and "章" in p:
        print("  H111:", p)
print("P111 first 10:")
for p in p111[:10]:
    print(" ", p)
