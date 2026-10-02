import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Nhung\RIDI\trans-assistant\scratch\talebed_cache\page_111.html", "r", encoding="utf-8") as f:
    h111 = f.read()

m111 = re.search(r'<div class="read-content">(.*?)</div>\s*</div>\s*<div class="px-6', h111, re.DOTALL)
p111 = re.findall(r'<p>(.*?)</p>', m111.group(1))

lock_idx = -1
for idx, p in enumerate(p111):
    if "第80章" in p:
        lock_idx = idx
        break

print(f"Lock index: {lock_idx} / {len(p111)}")
print("Paras before lock:")
for p in p111[max(0, lock_idx-10):lock_idx]:
    print(" ", p)

print("Paras after lock:")
for p in p111[lock_idx:]:
    print(" ", p)
