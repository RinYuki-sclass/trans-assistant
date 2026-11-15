import os
import json

base_dir = r"d:\Nhung\trans-tool\novel_projects"

# Project 1: mat-the-chi-trung-khuyen-thoai-bien-ky
p1 = os.path.join(base_dir, "mat-the-chi-trung-khuyen-thoai-bien-ky")
os.makedirs(os.path.join(p1, "memory"), exist_ok=True)
os.makedirs(os.path.join(p1, "chapters"), exist_ok=True)

p1_config = {
    "title": "Mạt Thế Chi Trung Khuyển Thoái Biến Ký",
    "chinese_title": "末世之忠犬蜕变记",
    "author": "Đang cập nhật",
    "slug": "mat-the-chi-trung-khuyen-thoai-bien-ky",
    "source_lang": "Chinese",
    "target_lang": "Vietnamese",
    "genre": [
        "Đam mỹ",
        "Chủ công",
        "Trọng sinh",
        "Mạt thế tang thi",
        "Dị năng",
        "Cường cường",
        "Trung khuyển biến dị công x Lãnh khốc căn cứ trưởng thụ",
        "1v1",
        "HE"
    ],
    "description": "Tiểu thuyết đam mỹ mạt thế chủ công 1v1. Công kiếp trước là dị năng giả bình thường đi theo đội ngũ của thụ, chết vì cứu thụ. Trọng sinh về ngày đầu mạt thế, công thức tỉnh dị năng biến dị đỉnh phong, nhưng vẫn một lòng trung thành làm lá chắn bảo vệ thụ. Thụ là thủ lĩnh căn cứ Long Ngạo Thiên sắt đá, nhận ra sự tận tụy sủng ái của chú cún trung thành nên rung động và chủ động kéo công vào lòng.",
    "style_guide": "Chủ công, mạt thế dị năng, trung khuyển công x lãnh khốc cường thụ.\n1. Định dạng \\n\\n giữa các đoạn văn.\n2. Lời thoại ngoặc kép “...”.\n3. Đại từ: Công xưng anh/hắn, Thụ xưng cậu/hắn/y.",
    "confidence_threshold": 0.8,
    "chunk_size": 20,
    "created_at": "2026-11-15T16:48:00",
    "is_completed": False,
    "is_dropped": False
}

with open(os.path.join(p1, "config.json"), "w", encoding="utf-8") as f:
    json.dump(p1_config, f, ensure_ascii=False, indent=2)

# Project 2: mat-the-chi-tuyet-doi-phuc-tung
p2 = os.path.join(base_dir, "mat-the-chi-tuyet-doi-phuc-tung")
os.makedirs(os.path.join(p2, "memory"), exist_ok=True)
os.makedirs(os.path.join(p2, "chapters"), exist_ok=True)

p2_config = {
    "title": "Mạt Thế Chi Tuyệt Đối Phục Tùng",
    "chinese_title": "末世之绝对服从",
    "author": "Đang cập nhật",
    "slug": "mat-the-chi-tuyet-doi-phuc-tung",
    "source_lang": "Chinese",
    "target_lang": "Vietnamese",
    "genre": [
        "Đam mỹ",
        "Chủ công",
        "Dị năng quân sự",
        "Mạt thế phế thổ",
        "Hạ khắc thượng",
        "Thâm tình trung khuyển công x Bá đạo quân vương Long Ngạo Thiên thụ",
        "1v1",
        "HE"
    ],
    "description": "Tiểu thuyết mạt thế quân sự dị năng chủ công 1v1. Công là sĩ quan cận vệ kiêm chiến sĩ tiên phong trầm mặc kiên định, xem mệnh lệnh của thụ là thiên chỉ. Thụ là tư lệnh chiến khu, dị năng giả mạnh nhất thế giới, phong thái ngút trời nhưng bị bạo động tinh thần lực, chỉ có công mới xoa dịu được. Cảnh hạ khắc thượng, trước mặt người ngoài công quỳ gối xưng ngài, sau cánh cửa phòng kín lại ôm chặt dỗ dành và chiếm hữu.",
    "style_guide": "Chủ công, mạt thế quân sự, hạ khắc thượng, trung khuyển công x bá đạo vương giả thụ.\n1. Định dạng \\n\\n giữa các đoạn văn.\n2. Lời thoại ngoặc kép “...”.\n3. Đại từ: Công xưng anh/hắn, Thụ xưng cậu/hắn/ngài.",
    "confidence_threshold": 0.8,
    "chunk_size": 20,
    "created_at": "2026-11-15T16:48:00",
    "is_completed": False,
    "is_dropped": False
}

with open(os.path.join(p2, "config.json"), "w", encoding="utf-8") as f:
    json.dump(p2_config, f, ensure_ascii=False, indent=2)

# Memory files
for p, slug in [(p1, "mat-the-chi-trung-khuyen-thoai-bien-ky"), (p2, "mat-the-chi-tuyet-doi-phuc-tung")]:
    with open(os.path.join(p, "memory", "characters.json"), "w", encoding="utf-8") as f:
        json.dump({"project": slug, "characters": []}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(p, "memory", "glossary.json"), "w", encoding="utf-8") as f:
        json.dump({"project": slug, "terms": {}}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(p, "memory", "relationships.json"), "w", encoding="utf-8") as f:
        json.dump({"project": slug, "pairs": []}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(p, "memory", "timeline.json"), "w", encoding="utf-8") as f:
        json.dump({"project": slug, "events": [{"chapter": 0, "summary": "Khởi tạo cấu trúc dự án."}]}, f, ensure_ascii=False, indent=2)

print("All project files created.")
