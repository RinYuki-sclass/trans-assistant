import glob
import json
import os

dir_path = glob.glob('d:/Nhung/RIDI/trans-assistant/novel_projects/*khi*')[0]

characters = [
    {
        "name": "Sở Tư Thừa",
        "hanviet_name": "Sở Tư Thừa",
        "original_name": "楚司承",
        "pinyin": "Chǔ Sīchéng",
        "gender": "Nam",
        "third_person_pronoun": "hắn",
        "role": "Nhân vật chính, cựu Trưởng nhóm Phản diện của Cục Quản lý Thời Không",
        "notes": "Bình tĩnh, cơ trí, thâm độc, phong thái đại lão phản diện. Xuyên vào các vai chính bị ngược để đoạt lại hào quang."
    },
    {
        "name": "Ryan",
        "hanviet_name": "Thụy An",
        "original_name": "瑞安",
        "pinyin": "Ruì'ān",
        "gender": "Nam",
        "third_person_pronoun": "cậu",
        "role": "Thân xác hùng trùng nguyên tác tại thế giới Trùng tộc (Sở Tư Thừa nhập vào)",
        "notes": "Hùng trùng cấp F (tiềm năng cấp S), bị Felo gài bẫy vu oan mưu hại đồng loại."
    },
    {
        "name": "Alex Sachsen",
        "hanviet_name": "Ngải Lợi Khắc Tư · Tát Khắc Sâm",
        "original_name": "艾利克斯·萨克森",
        "pinyin": "Àilìkèsī Sàkèsēn",
        "gender": "Nam (Quân thư)",
        "third_person_pronoun": "hắn",
        "role": "Tướng quân quân thư cấp SS, người hành hình",
        "notes": "Khinh ghét hùng trùng, cao ngạo, lạnh lùng, gặp vấn đề tinh thần lực bạo động dễ trùng hóa."
    },
    {
        "name": "Friedrich",
        "hanviet_name": "Phật Đức Lý Hi",
        "original_name": "弗德里希",
        "pinyin": "Fúdélǐxī",
        "gender": "Nam (Quân thư)",
        "third_person_pronoun": "hắn",
        "role": "Quân thư cấp tướng, quan phối nguyên tác của Ryan",
        "notes": "Bị kẻ xuyên không Felo tiếp cận và muốn cướp đoạt."
    },
    {
        "name": "Felo",
        "hanviet_name": "Phí Lạc",
        "original_name": "费洛",
        "pinyin": "Fèiluò",
        "gender": "Nam (Hùng trùng)",
        "third_person_pronoun": "gã",
        "role": "Kẻ xuyên không (Bug), hùng trùng cấp A hám danh",
        "notes": "Biết trước cốt truyện, vu khống hãm hại Ryan để chiếm đoạt hào quang."
    },
    {
        "name": "Heideman",
        "hanviet_name": "Hải Đức Mạn",
        "original_name": "海德曼",
        "pinyin": "Hǎidémàn",
        "gender": "Nam (Hùng trùng)",
        "third_person_pronoun": "ông ta",
        "role": "Hội trưởng Hiệp hội Bảo vệ Hùng trùng",
        "notes": "Bảo thủ, tức giận khi phát hiện sai phạm nghiêm trọng trong việc giam cầm và xét xử tù nhân 0101."
    },
    {
        "name": "Hệ thống",
        "hanviet_name": "Hệ thống",
        "original_name": "系统",
        "gender": "Vô tính",
        "third_person_pronoun": "nó",
        "role": "Hệ thống hỗ trợ của Sở Tư Thừa",
        "notes": "Trợ thủ đắc lực, theo dõi chỉ số hào quang và nhiệm vụ."
    },
    {
        "name": "Hư ảnh đầu lâu",
        "hanviet_name": "Khô Lâu / Hắc vụ khô lâu",
        "original_name": "骷髅 / 骷髅头虚影",
        "gender": "Không rõ",
        "third_person_pronoun": "nó",
        "role": "Thực thể tà ác bí ẩn cấu kết với Felo",
        "notes": "Xuất hiện trong sương đen hứa hẹn giúp Felo lật kèo khi cốt truyện bị phá vỡ."
    }
]

glossary = [
    {"original": "楚司承", "translation": "Sở Tư Thừa", "hanviet": "Sở Tư Thừa", "category": "character", "confidence": 1.0, "approved": True, "notes": "Nhân vật chính"},
    {"original": "瑞安", "translation": "Ryan", "hanviet": "Thụy An", "category": "character", "confidence": 1.0, "approved": True, "notes": "Thân xác thế giới trùng tộc"},
    {"original": "艾利克斯", "translation": "Alex", "hanviet": "Ngải Lợi Khắc Tư", "category": "character", "confidence": 1.0, "approved": True, "notes": "Tướng quân quân thư"},
    {"original": "萨克森", "translation": "Sachsen", "hanviet": "Tát Khắc Sâm", "category": "character", "confidence": 1.0, "approved": True, "notes": "Họ của Alex"},
    {"original": "弗德里希", "translation": "Friedrich", "hanviet": "Phật Đức Lý Hi", "category": "character", "confidence": 1.0, "approved": True, "notes": "Quân thư quan phối"},
    {"original": "费洛", "translation": "Felo", "hanviet": "Phí Lạc", "category": "character", "confidence": 1.0, "approved": True, "notes": "Bug xuyên không"},
    {"original": "海德曼", "translation": "Heideman", "hanviet": "Hải Đức Mạn", "category": "character", "confidence": 1.0, "approved": True, "notes": "Hội trưởng Hiệp hội Bảo vệ Hùng trùng"},
    {"original": "雄虫", "translation": "Hùng trùng", "hanviet": "Hùng trùng", "category": "faction", "confidence": 1.0, "approved": True, "notes": "Giống đực"},
    {"original": "雌虫", "translation": "Thư trùng", "hanviet": "Thư trùng", "category": "faction", "confidence": 1.0, "approved": True, "notes": "Giống cái"},
    {"original": "军雌", "translation": "Quân thư", "hanviet": "Quân thư", "category": "faction", "confidence": 1.0, "approved": True, "notes": "Thư trùng quân sự"},
    {"original": "亚雌", "translation": "Á thư", "hanviet": "Á thư", "category": "faction", "confidence": 1.0, "approved": True, "notes": "Á thư trùng"},
    {"original": "信息素", "translation": "Pheromone", "hanviet": "Tín tức tố", "category": "skill", "confidence": 1.0, "approved": True, "notes": "Pheromone của trùng tộc"},
    {"original": "精神力", "translation": "Tinh thần lực", "hanviet": "Tinh thần lực", "category": "skill", "confidence": 1.0, "approved": True, "notes": ""},
    {"original": "二次蜕化", "translation": "Lột xác lần hai", "hanviet": "Nhị thứ thuế hóa", "category": "concept", "confidence": 1.0, "approved": True, "notes": "Giai đoạn thức tỉnh sức mạnh"},
    {"original": "狂暴期", "translation": "Kỳ cuồng bạo", "hanviet": "Cuồng bạo kỳ", "category": "concept", "confidence": 1.0, "approved": True, "notes": "Giai đoạn mất kiểm soát của quân thư"},
    {"original": "暴躁期", "translation": "Kỳ cuồng bạo", "hanviet": "Bạo táo kỳ", "category": "concept", "confidence": 1.0, "approved": True, "notes": ""},
    {"original": "虫化", "translation": "Trùng hóa", "hanviet": "Trùng hóa", "category": "concept", "confidence": 1.0, "approved": True, "notes": "Biến hình dạng trùng"},
    {"original": "抑制剂", "translation": "Thuốc ức chế", "hanviet": "Ức chế tễ", "category": "item", "confidence": 1.0, "approved": True, "notes": ""},
    {"original": "纹刀", "translation": "Văn đao", "hanviet": "Văn đao", "category": "item", "confidence": 1.0, "approved": True, "notes": "Dao khắc hoa văn hình cụ"},
    {"original": "光脑", "translation": "Quang não", "hanviet": "Quang não", "category": "item", "confidence": 1.0, "approved": True, "notes": "Thiết bị đầu cuối AI"},
    {"original": "雄虫保护协会", "translation": "Hiệp hội Bảo vệ Hùng trùng", "hanviet": "Hùng trùng bảo hộ hiệp hội", "category": "faction", "confidence": 1.0, "approved": True, "notes": ""},
    {"original": "雄虫保护中心", "translation": "Trung tâm Bảo vệ Hùng trùng", "hanviet": "Hùng trùng bảo hộ trung tâm", "category": "faction", "confidence": 1.0, "approved": True, "notes": ""},
    {"original": "帝星最高法院", "translation": "Tòa án Tối cao Đế tinh", "hanviet": "Đế tinh tối cao pháp viện", "category": "faction", "confidence": 1.0, "approved": True, "notes": ""},
    {"original": "莫格拉斯监狱", "translation": "Nhà tù Mogelas", "hanviet": "Mạc Cách Lạp tư giam ngục", "category": "location", "confidence": 1.0, "approved": True, "notes": ""},
    {"original": "死遁", "translation": "Giả chết thoát thân", "hanviet": "Tử độn", "category": "concept", "confidence": 1.0, "approved": True, "notes": ""},
    {"original": "主角光环", "translation": "Hào quang nhân vật chính", "hanviet": "Chủ giác quang hoàn", "category": "concept", "confidence": 1.0, "approved": True, "notes": ""},
    {"original": "气运光环", "translation": "Hào quang khí vận", "hanviet": "Khí vận quang hoàn", "category": "concept", "confidence": 1.0, "approved": True, "notes": ""}
]

with open(f'{dir_path}/memory/characters.json', 'w', encoding='utf-8') as f:
    json.dump(characters, f, ensure_ascii=False, indent=2)

with open(f'{dir_path}/memory/glossary.json', 'w', encoding='utf-8') as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

print("Saved characters.json and glossary.json successfully!")
