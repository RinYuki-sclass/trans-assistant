import os

with open('input/336-vi.md', 'r', encoding='utf-8') as f:
    vi_raw = f.read()

with open('input/336-en.md', 'r', encoding='utf-8') as f:
    en_raw = f.read()

vi_paras = [p.strip() for p in vi_raw.split('\n') if p.strip()]
en_paras = [p.strip() for p in en_raw.split('\n') if p.strip()]

print(f"VI total non-empty lines: {len(vi_paras)}")
print(f"EN total non-empty lines: {len(en_paras)}")

# Check first few lines of VI
with open('scratch/alignment_debug.txt', 'w', encoding='utf-8') as f:
    f.write(f"VI lines: {len(vi_paras)} | EN lines: {len(en_paras)}\n\n")
    for i in range(min(len(vi_paras), len(en_paras))):
        f.write(f"--- PARAGRAPH {i+1} ---\n")
        f.write(f"VI: {vi_paras[i]}\n")
        f.write(f"EN: {en_paras[i]}\n\n")

print("Written alignment debug to scratch/alignment_debug.txt")
