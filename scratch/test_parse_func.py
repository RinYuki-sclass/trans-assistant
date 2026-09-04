import os, re

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant"

def _nw_parse_novel_file(text):
    if not text:
        return {"headers": [], "body": [], "footers": [], "has_dense_spacing": False, "normalized_text": ""}
    raw_lines = text.splitlines()
    non_empty = [l.strip() for l in raw_lines if l.strip()]
    
    blank_line_count = sum(1 for l in raw_lines if not l.strip())
    has_dense_spacing = (blank_line_count < len(non_empty) * 0.4) and len(non_empty) > 10

    headers = []
    header_indices = set()
    for idx in range(min(8, len(non_empty))):
        l = non_empty[idx]
        if re.match(r'^(Trans|Beta|Edit|Editor|Dịch|Nguồn|Tác giả|Author)\s*[:\-]', l, re.I):
            headers.append(l)
            header_indices.add(idx)

    content_lines = [l for idx, l in enumerate(non_empty) if idx not in header_indices]

    footers = []
    end_idx = len(content_lines)
    while end_idx > 0:
        l = content_lines[end_idx - 1]
        if re.match(r'^\[\d+\]\s+', l):
            footers.insert(0, l)
            end_idx -= 1
        else:
            break

    body = content_lines[:end_idx]
    
    parts = []
    if headers:
        parts.append("\n".join(headers))
    parts.extend(body)
    if footers:
        parts.append("\n".join(footers))
    normalized_text = "\n\n".join(parts) + "\n"

    return {
        "headers": headers,
        "body": body,
        "footers": footers,
        "has_dense_spacing": has_dense_spacing,
        "normalized_text": normalized_text
    }

with open(os.path.join(BASE_DIR, 'input', '336-en.md'), 'r', encoding='utf-8') as f:
    en_res = _nw_parse_novel_file(f.read())

with open(os.path.join(BASE_DIR, 'input', '336-vi.md'), 'r', encoding='utf-8') as f:
    vi_res = _nw_parse_novel_file(f.read())

print("EN body count:", len(en_res["body"]), "Footers:", len(en_res["footers"]), "Dense:", en_res["has_dense_spacing"])
print("VI body count:", len(vi_res["body"]), "Headers:", vi_res["headers"], "Dense:", vi_res["has_dense_spacing"])
