import re

def parse_and_normalize_novel_text(raw_text):
    """
    Chuẩn hóa văn bản tiểu thuyết:
    1. Bóc tách Header metadata (Trans, Beta, Nguồn, Tác giả...)
    2. Bóc tách Footnotes cuối bài ([1], [2]...)
    3. Tách các đoạn văn nội dung và đảm bảo cách dòng chuẩn (\n\n)
    """
    lines = [l.strip() for l in raw_text.split('\n') if l.strip()]
    
    headers = []
    footers = []
    body = []
    
    # 1. Bóc tách header (quét trong 6 dòng đầu)
    header_indices = set()
    for idx in range(min(6, len(lines))):
        l = lines[idx]
        if re.match(r'^(Trans|Beta|Edit|Editor|Dịch|Nguồn|Tác giả)\s*[:\-]', l, re.I):
            headers.append(l)
            header_indices.add(idx)

    # Lọc body loại bỏ các dòng header
    content_lines = [l for idx, l in enumerate(lines) if idx not in header_indices]

    # 2. Bóc tách footnotes ở cuối
    end_idx = len(content_lines)
    while end_idx > 0:
        l = content_lines[end_idx - 1]
        if re.match(r'^\[\d+\]\s+', l):
            footers.insert(0, l)
            end_idx -= 1
        else:
            break

    body = content_lines[:end_idx]
    
    # Chuẩn hóa văn bản có cách dòng chuẩn \n\n
    normalized_body = "\n\n".join(body)
    
    return {
        "headers": headers,
        "body_paragraphs": body,
        "footers": footers,
        "normalized_text": normalized_body
    }

# Test with 336-vi.md
with open('input/336-vi.md', 'r', encoding='utf-8') as f:
    vi_parsed = parse_and_normalize_novel_text(f.read())

# Test with 336-en.md
with open('input/336-en.md', 'r', encoding='utf-8') as f:
    en_parsed = parse_and_normalize_novel_text(f.read())

print("VI Headers:", vi_parsed["headers"])
print("VI Body count:", len(vi_parsed["body_paragraphs"]))
print("VI Footers:", vi_parsed["footers"])

print("EN Headers:", en_parsed["headers"])
print("EN Body count:", len(en_parsed["body_paragraphs"]))
print("EN Footers count:", len(en_parsed["footers"]))
