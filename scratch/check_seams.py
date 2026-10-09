import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scratch.extract_ch089 import p183_ch89, p184_ch89, p185_ch89, p186_ch89

print("=== End of p183 ===")
for p in p183_ch89[-3:]:
    print(p)

print("\n=== Start of p184 ===")
for p in p184_ch89[:3]:
    print(p)

print("\n=== End of p184 ===")
for p in p184_ch89[-3:]:
    print(p)

print("\n=== Start of p185 ===")
for p in p185_ch89[:3]:
    print(p)

print("\n=== End of p185 ===")
for p in p185_ch89[-3:]:
    print(p)

print("\n=== Start of p186 ===")
for p in p186_ch89[:3]:
    print(p)
