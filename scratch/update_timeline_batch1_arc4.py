import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

timeline_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"

with open(timeline_path, "r", encoding="utf-8") as f:
    tl = json.load(f)

existing_cids = {x.get("chapter") for x in tl}

from scratch.audit_batch1_arc4 import titles, key_events_map

summaries = {
    'ch_090': "Huấn luyện viên Vương Bằng phạt Kỷ Cảnh cùng đám bạn học trốn học vào khoang ảo chạy 10km. Kỷ Cảnh thể hiện thực lực ấn tượng. Đám học sinh mê đắm vẻ ngoài cấm dục của Lục giáo sư; Kỷ Cảnh nổi hứng tò mò lên kế hoạch tiếp cận.",
    'ch_091': "Kỷ Cảnh nảy ra ý định giả trang thành nữ Beta Dịch Nam để tiếp cận Lục Tư Niên. Chị gái Kỷ Vân Hy hỗ trợ Kỷ Cảnh trang điểm thanh thuần và chọn váy trắng tóc giả dài đen. Lục Tư Niên đến ngõ hẻm mua thuốc kháng chế vì tuyến thể ngứa ngáy sau khi ngửi tin tức tố rượu Tequila của Kỷ Cảnh. Kỷ Cảnh giả gái ra phố bị đám Alpha bám đuôi gạ gẫm; Lục Tư Niên bất ngờ xuất hiện giải vây.",
    'ch_092': "Lục Tư Niên ra tay đánh gục đám Alpha giải cứu Kỷ Cảnh; Kỷ Cảnh nhận mình là Dịch Nam, em gái Kỷ Cảnh. Kỷ Cảnh mặc váy ngắn đến lớp phòng ngự bốn của Lục Tư Niên dự thính, giơ tay trả lời câu hỏi khó được Lục giáo sư khen ngợi. Lục Tư Niên phát hiện vết thương bầm tím trên đùi Kỷ Cảnh và vạch trần cô không phải học sinh của trường.",
    'ch_093': "Kỷ Cảnh giả vờ khóc lóc bịa chuyện là con gái riêng của Kỷ Trình với cô lao công để lấy lòng thương cảm của Lục Tư Niên. Lục Tư Niên mềm lòng cho phương thức liên lạc. Kỷ Cảnh gửi ảnh đôi chân dài đầy vết bầm tím trên giường xám than đau khiến Lục Tư Niên khô nóng bứt rứt, phải tiêm thuốc kháng chế vào tuyến thể.",
    'ch_094': "Kỷ Cảnh mặc đồ nữ đến muộn trong lớp của Lục Tư Niên khiến cả phòng học xôn xao. Lục Tư Niên gọi Kỷ Cảnh vào văn phòng và đưa tuýp thuốc mỡ nội bộ quân đội để bôi vết bầm trên chân. Kỷ Cảnh rủ Lục Tư Niên đi ăn trưa tại nhà ăn giáo viên; Kỷ Cảnh gạt hạt cơm trên môi Lục Tư Niên khiến anh đỏ bừng tai. Đêm đến, Kỷ Cảnh ngả bài tỏ tình; Lục Tư Niên thức đến 2 giờ sáng nhắn tin từ chối.",
    'ch_095': "Kỷ Cảnh chất vấn lý do Lục Tư Niên từ chối; Lục Tư Niên che chở kéo cậu vào lòng tránh quả bóng rổ va phải. Tiệc sinh nhật thái tử gia Lục Đảo Phong diễn ra, học sinh bàn tán mỉa mai thân thế con riêng của Lục giáo sư. Lục Tư Niên tâm trạng u tối đến phòng giác đấu bật cấp 5 điên cuồng trút giận; Kỷ Cảnh bấm dừng máy và ôm eo Lục giáo sư vỗ về. Dưới trăng đêm xuân, Kỷ Cảnh cài hoa đỗ quyên đỏ lên vành tai hỏi 'Đẹp không?'; Lục Tư Niên ngơ ngẩn khen đẹp và ngửi thấy thoang thoảng mùi rượu Tequila quen thuộc."
}

for cid in ['ch_090', 'ch_091', 'ch_092', 'ch_093', 'ch_094', 'ch_095']:
    if cid in existing_cids:
        print(f"{cid} already in timeline, skipping.")
        continue
    entry = {
        "chapter": cid,
        "arc": "arc_04",
        "title": titles[cid],
        "summary": summaries[cid],
        "key_events": key_events_map[cid]
    }
    tl.append(entry)
    print(f"Added {cid} to timeline.")

with open(timeline_path, "w", encoding="utf-8") as f:
    json.dump(tl, f, ensure_ascii=False, indent=2)

print("Updated timeline.json successfully!")
