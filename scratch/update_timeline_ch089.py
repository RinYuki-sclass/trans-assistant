import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

timeline_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"

with open(timeline_path, "r", encoding="utf-8") as f:
    tl = json.load(f)

# Check if ch_089 already exists
for item in tl:
    if item.get("chapter") == "ch_089":
        print("ch_089 already in timeline, skipping duplicate.")
        sys.exit(0)

new_entry = {
    "chapter": "ch_089",
    "arc": "arc_04",
    "title": "Chương 89: Hương rượu Tequila đột ngột",
    "summary": "Mở đầu Thế giới 4 (ABO). Kỷ Cảnh cùng bè lũ Alpha chặn đường Lục Tư Niên - cựu chỉ huy trưởng Đệ tam quân đoàn vừa giải ngũ về làm giáo sư. Kỷ Cảnh dùng tin tức tố rượu Tequila uy hiếp vị giáo sư vừa phân hóa muộn thành Omega. Ngay trước khi bi kịch xảy ra, Hệ thống Yêu Đương (bướm Mật Bảo) thức tỉnh ý thức phản diện của Kỷ Cảnh và truyền kịch bản 《Omega Đệ Nhất Đế Quốc》. Để thoát khỏi kết cục thảm khốc bị đào tuyến thể, Kỷ Cảnh thực hiện nhiệm vụ cưỡng hôn Lục Tư Niên và bị anh đấm cảnh cáo.",
    "key_events": [
        "Kỷ Cảnh cùng đàn em chặn đường Lục Tư Niên; đám Alpha bỏ chạy vì sợ chiến lực của giáo sư",
        "Lục Tư Niên xuất hiện nghiêm nghị, dễ dàng bẻ tay ghì chặt Kỷ Cảnh lên tường",
        "Kỷ Cảnh phơi bày bí mật Lục Tư Niên là Omega và giải phóng tin tức tố rượu Tequila nồng nặc",
        "Lục Tư Niên bị kích thích mẫn cảm tuyến thể, mềm nhũn dựa vào tường",
        "Hệ thống Yêu Đương (Mật Bảo) xuất hiện thức tỉnh ý thức phản diện của Kỷ Cảnh",
        "Kỷ Cảnh cưỡng hôn Lục Tư Niên theo kịch bản tình cảm và bị anh tung đấm cảnh cáo"
    ]
}

tl.append(new_entry)

with open(timeline_path, "w", encoding="utf-8") as f:
    json.dump(tl, f, ensure_ascii=False, indent=2)

print("Successfully added ch_089 to timeline.json!")
