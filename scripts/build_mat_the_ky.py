import os
import re
import json
import time
import urllib.request
import html
from concurrent.futures import ThreadPoolExecutor, as_completed

project_dir = r"d:\Nhung\trans-tool\novel_projects\mat-the-ky"
os.makedirs(os.path.join(project_dir, "chapters"), exist_ok=True)
os.makedirs(os.path.join(project_dir, "memory"), exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_text(t):
    t = html.unescape(t)
    t = t.replace('&nbsp;', ' ').replace('&hellip;', '…').replace('&mdash;', '—').replace('&ldquo;', '“').replace('&rdquo;', '”')
    return t.strip()

def fetch_page(page_idx):
    url = f"https://www.52shuku.net/xiandaidushi/9065_{page_idx}.html"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
                p_tags = re.findall(r'<p>(.*?)</p>', content, re.DOTALL)
                clean_lines = []
                for p in p_tags:
                    cl = re.sub(r'<[^>]+>', '', p)
                    cl = clean_text(cl)
                    if not cl:
                        continue
                    if any(k in cl for k in ['52书库', '传送门：', '目录 上一页', '阅读记录', '上一页 下一页', '尾页', '哦豁，小伙伴们如果觉得52书库不错']):
                        continue
                    clean_lines.append(cl)
                return page_idx, clean_lines
        except Exception as e:
            time.sleep(1)
    return page_idx, []

print("Crawling all 305 pages...")
pages_data = {}
with ThreadPoolExecutor(max_workers=20) as executor:
    futures = {executor.submit(fetch_page, p): p for p in range(2, 307)}
    for f in as_completed(futures):
        pidx, lines = f.result()
        pages_data[pidx] = lines

all_lines = []
for pidx in range(2, 307):
    all_lines.extend(pages_data.get(pidx, []))

print(f"Total lines: {len(all_lines)}")

# Save full raw
raw_full_path = os.path.join(project_dir, "raw_full.md")
with open(raw_full_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(all_lines))
print(f"Saved raw_full.md ({len(all_lines)} paragraphs)")

# Identify chapter headings
ch_pattern = re.compile(r'^(第\s*[0-9零一二三四五六七八九十百千万]+\s*[章回节]|番外)')
chapter_splits = []

for idx, line in enumerate(all_lines):
    if ch_pattern.match(line) and len(line) < 60:
        chapter_splits.append((idx, line))

print(f"Found {len(chapter_splits)} chapter headings.")

chapters_index = []
toc_lines = [
    "# MỤC LỤC: Mạt Thế Kỷ (末世纪)",
    "",
    "- **Tác giả:** Tạ Dịch (谢亦)",
    "- **Slug:** `mat-the-ky`",
    "- **Thể loại:** Đam mỹ, Chủ công, Mạt thế dị năng, Thăng cấp lưu, Cường cường, Tang thi vương công x Binh bĩ thiết huyết quân nhân thụ, 1v1, HE.",
    f"- **Tổng số chương:** {len(chapter_splits)} chương",
    "- **Nguồn:** 52shuku (Full Raw)",
    "",
    "---",
    "",
    "### Danh sách chương:",
    ""
]

# Write chapters
for i in range(len(chapter_splits)):
    ch_num = i + 1
    ch_id = f"ch_{ch_num:03d}"
    start_idx, heading = chapter_splits[i]
    if i + 1 < len(chapter_splits):
        end_idx = chapter_splits[i+1][0]
    else:
        end_idx = len(all_lines)
    
    ch_lines = all_lines[start_idx:end_idx]
    ch_folder = os.path.join(project_dir, "chapters", ch_id)
    os.makedirs(ch_folder, exist_ok=True)
    
    source_path = os.path.join(ch_folder, "source.md")
    with open(source_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(ch_lines))
    
    chapters_index.append({
        "chapter_id": ch_id,
        "chapter_number": ch_num,
        "title": heading,
        "paragraphs_count": len(ch_lines),
        "has_source": True,
        "has_translation": False,
        "status": "raw_ready"
    })
    
    toc_lines.append(f"- **Chương {ch_num}:** {heading} | *{len(ch_lines)} đoạn* | *Sẵn sàng dịch*")

# Write chapters_index.json
with open(os.path.join(project_dir, "chapters_index.json"), "w", encoding="utf-8") as f:
    json.dump(chapters_index, f, ensure_ascii=False, indent=2)

# Write TOC.md
with open(os.path.join(project_dir, "TOC.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(toc_lines))

# Write config.json
config = {
    "title": "Mạt Thế Kỷ",
    "chinese_title": "末世纪",
    "author": "Tạ Dịch (谢亦)",
    "slug": "mat-the-ky",
    "source_lang": "Chinese",
    "target_lang": "Vietnamese",
    "genre": [
        "Đam mỹ",
        "Chủ công",
        "Mạt thế dị năng",
        "Thăng cấp lưu",
        "Cường cường",
        "Tang thi vương công x Binh bĩ thiết huyết quân nhân thụ",
        "1v1",
        "HE"
    ],
    "description": "Tiểu thuyết mạt thế thăng cấp lưu chủ công 1v1. Hầu Dĩnh thời bình là bạch lĩnh cao cấp, bạn trai lực MAX, tinh thần trách nhiệm và bộ não thông minh kiệt xuất. Mạt thế giáng lâm, anh mất đi ký ức 2 ngày đầu, trên đường truy tìm chân tướng anh gặp gỡ và câu dẫn chàng binh bĩ thiết huyết Lý Hiên Viên. Cả hai cùng lập nên chiến đội mạnh nhất mạt thế, dẫn dắt nhân loại vượt qua vô vàn tử kiếp. Sau đó Hầu Dĩnh mới phát hiện, bản thân mình thế mà lại chính là Tang Thi Vương đại BOSS tối thượng của cả thế giới.",
    "style_guide": "Chủ công, mạt thế thăng cấp lưu, chiến đội sinh tồn, thiết huyết cường thụ.\n1. Định dạng \\n\\n giữa các đoạn văn.\n2. Lời thoại ngoặc kép “...”.\n3. Đại từ: Hầu Dĩnh xưng anh/hắn, Lý Hiên Viên xưng hắn/cậu.",
    "confidence_threshold": 0.8,
    "chunk_size": 20,
    "created_at": "2026-11-15T17:08:00",
    "chapters_count": len(chapter_splits),
    "is_completed": False,
    "is_dropped": False
}
with open(os.path.join(project_dir, "config.json"), "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

# Memory files
characters = {
    "project": "mat-the-ky",
    "characters": [
        {
            "name": "Hầu Dĩnh",
            "chinese_name": "侯颖",
            "role": "Công",
            "aliases": ["Hầu ca", "Đại ca", "Tang Thi Vương"],
            "description": "Bạch lĩnh cao cấp thời bình, trầm ổn phúc hắc, IQ đỉnh cao, dị năng biến dị đặc thù, sau tiến hóa thành Tang Thi Vương đại BOSS tối thượng."
        },
        {
            "name": "Lý Hiên Viên",
            "chinese_name": "李轩辕",
            "role": "Thụ",
            "aliases": ["Lý đội", "Hiên Viên"],
            "description": "Binh bĩ thiết huyết, nguyên là đặc chủng binh, chiến thần vũ lực MAX của chiến đội, tính tình cộc lốc nam tính nhưng cực kỳ sủng công, giao trọn sinh mạng cho Hầu Dĩnh."
        }
    ]
}
with open(os.path.join(project_dir, "memory", "characters.json"), "w", encoding="utf-8") as f:
    json.dump(characters, f, ensure_ascii=False, indent=2)

with open(os.path.join(project_dir, "memory", "glossary.json"), "w", encoding="utf-8") as f:
    json.dump({"project": "mat-the-ky", "terms": {}}, f, ensure_ascii=False, indent=2)

with open(os.path.join(project_dir, "memory", "relationships.json"), "w", encoding="utf-8") as f:
    json.dump({"project": "mat-the-ky", "pairs": [
        {
            "characters": ["Hầu Dĩnh", "Lý Hiên Viên"],
            "relation": "Người yêu / Chiến hữu sinh tử (Công x Thụ)",
            "pronouns": {"Hầu Dĩnh": "anh/tôi", "Lý Hiên Viên": "cậu/tôi"}
        }
    ]}, f, ensure_ascii=False, indent=2)

with open(os.path.join(project_dir, "memory", "timeline.json"), "w", encoding="utf-8") as f:
    json.dump({"project": "mat-the-ky", "events": [
        {"chapter": 0, "summary": "Khởi tạo dự án, cào toàn bộ 353 chương Full Raw từ 52shuku."}
    ]}, f, ensure_ascii=False, indent=2)

print("Build complete!")
