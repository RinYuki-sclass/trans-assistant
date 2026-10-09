import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

def scan_batch4():
    raw_path = 'scratch/batch4_arc2_raw_pages.json'
    if not os.path.exists(raw_path):
        print(f"{raw_path} does not exist yet.")
        return

    data = json.load(open(raw_path, 'r', encoding='utf-8'))
    print(f"Total pages in raw: {len(data)}")

    # Sort pages numerically
    sorted_pages = sorted(data.keys(), key=lambda x: int(x))
    print(f"Pages: {sorted_pages[0]} -> {sorted_pages[-1]}")

    pattern = re.compile(r'^\s*第\s*([0-9一二三四五六七八九十百]+)\s*章.*')

    found_headers = []
    for p_str in sorted_pages:
        p_num = int(p_str)
        paras = data[p_str].get('paragraphs', [])
        for idx, para in enumerate(paras):
            m = pattern.match(para.strip())
            if m:
                found_headers.append({
                    'page': p_num,
                    'p_idx': p_num - 1,
                    'para_idx': idx,
                    'header': para.strip(),
                    'raw_num': m.group(1)
                })
                print(f"Page {p_num}, Para {idx}: {para.strip()}")

    out_file = 'scratch/batch4_arc2_headers.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(found_headers, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(found_headers)} headers to {out_file}")

if __name__ == '__main__':
    scan_batch4()
