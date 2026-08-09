with open('scratch/soup_ch1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in soup_ch1.txt: {len(lines)}")
for i, line in enumerate(lines):
    l = line.strip()
    if len(l) > 30 and not l.startswith('<') and not l.startswith('var ') and not l.startswith('/*') and not l.startswith('//') and not l.startswith('function') and not l.startswith('}') and not l.startswith('{'):
        clean = l[:100].encode('ascii', 'ignore').decode()
        print(f"L{i+1}: {clean}")
