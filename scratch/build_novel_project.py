import os
import sys
import json
import re
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')

def now_gmt7():
    return datetime.now(timezone(timedelta(hours=7)))

PROJECT_DIR = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình"
SLUG = "đấng-cứu-thế-trả-nợ-tình"
CZBOOKS_URL = "https://czbooks.net/n/skdfi4kimel"
CHUNK_SZ = 20

# 1. Load crawled raw pages
with open('scratch/raw_pages_skdfi4kimel.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Flatten all paragraphs
all_paras = []
for p in pages:
    page_num = p['page_num']
    for idx, text in enumerate(p['paragraphs']):
        all_paras.append({
            'page_num': page_num,
            'para_idx': idx,
            'text': text
        })

# Define chapter titles and mapping
CHAPTER_DEFS = [
    {"num": 1, "orig": "第一章 咚，您的債主已上線", "vi": "Chương 1: Đinh, chủ nợ của bạn đã online"},
    {"num": 2, "orig": "第二章 褲子穿上", "vi": "Chương 2: Mặc quần vào"},
    {"num": 3, "orig": "第三章 陽哥，你親過嗎？", "vi": "Chương 3: Dương ca, anh hôn qua chưa?"},
    {"num": 4, "orig": "第四章 哥哥，我錯了", "vi": "Chương 4: Ca ca, em sai rồi"},
    {"num": 5, "orig": "第五章 你身上怎麽會有香水味？", "vi": "Chương 5: Trên người anh sao lại có mùi nước hoa?"},
    {"num": 6, "orig": "第六章 你在跟蹤我？", "vi": "Chương 6: Anh đang theo dõi em à?"},
    {"num": 7, "orig": "第七章 不起！", "vi": "Chương 7: Không dậy!"},
    {"num": 8, "orig": "第八章 什麽怪物", "vi": "Chương 8: Quái vật gì thế"},
    {"num": 9, "orig": "第九章 像小狗", "vi": "Chương 9: Giống cún con"},
    {"num": 10, "orig": "第十章 那你幹嘛親我！", "vi": "Chương 10: Thế sao anh lại hôn em!"},
    {"num": 11, "orig": "第十一章 請將它打開", "vi": "Chương 11: Hãy mở nó ra"},
    {"num": 12, "orig": "第十二章 他瘋了", "vi": "Chương 12: Hắn điên rồi"},
    {"num": 13, "orig": "第十三章 我想你", "vi": "Chương 13: Em nhớ anh"},
    {"num": 14, "orig": "第十四章 隻給你看", "vi": "Chương 14: Chỉ cho anh xem"},
    {"num": 15, "orig": "第十五章 男護工", "vi": "Chương 15: Nam hộ lý"},
    {"num": 16, "orig": "第十六章 他和我一樣", "vi": "Chương 16: Hắn cũng giống như em"},
    {"num": 17, "orig": "第十七章 你做了什麽", "vi": "Chương 17: Anh đã làm gì"},
    {"num": 18, "orig": "第十八章 頂樓", "vi": "Chương 18: Tầng thượng"},
    {"num": 19, "orig": "第十九章 帶他走", "vi": "Chương 19: Đưa cậu ấy đi"},
    {"num": 20, "orig": "第二十章 你又親我了", "vi": "Chương 20: Anh lại hôn em rồi"},
    {"num": 21, "orig": "第二十一章 談戀愛", "vi": "Chương 21: Yêu đương"},
    {"num": 22, "orig": "第二十二章 關著什麽人", "vi": "Chương 22: Nhốt người nào"},
    {"num": 23, "orig": "第二十三章 摸摸", "vi": "Chương 23: Sờ sờ"},
    {"num": 24, "orig": "第二十四章 小可憐蛋", "vi": "Chương 24: Nhóc đáng thương"},
    {"num": 25, "orig": "第二十五章 哥哥，好帥", "vi": "Chương 25: Ca ca, đẹp trai quá"},
    {"num": 26, "orig": "第二十六章 帶我回去，蔣先生", "vi": "Chương 26: Đưa tôi về, Tưởng tiên sinh"},
    {"num": 27, "orig": "第二十七章 宿主清白不保", "vi": "Chương 27: Ký chủ trong sạch khó giữ"},
    {"num": 28, "orig": "第二十八章 我也喜歡你", "vi": "Chương 28: Em cũng thích anh"},
    {"num": 29, "orig": "第二十九章 我很乖的", "vi": "Chương 29: Em ngoan lắm mà"},
    {"num": 30, "orig": "第三十章 別哭了", "vi": "Chương 30: Đừng khóc nữa"},
    {"num": 31, "orig": "第三十一章 417年落雪節", "vi": "Chương 31: Tiết rơi tuyết năm 417"},
    {"num": 32, "orig": "第三十二章 只有你（完結章）", "vi": "Chương 32: Chỉ có em [Hoàn]"},
    {"num": 33, "orig": "第一章 關於上輩子", "vi": "Phiên ngoại 1: Về kiếp trước"},
    {"num": 34, "orig": "第二章 關於這輩子", "vi": "Phiên ngoại 2: Về kiếp này"},
    {"num": 35, "orig": "第三章 關於易緣是什麽時候摘下乖巧面具的。", "vi": "Phiên ngoại 3: Về thời điểm Dịch Duyên tháo xuống mặt nạ ngoan ngoãn"},
]

# Find start index of each chapter
chapter_indices = []
for c_def in CHAPTER_DEFS:
    target = c_def["orig"]
    found_idx = None
    for i, item in enumerate(all_paras):
        if item['text'].strip() == target.strip():
            found_idx = i
            break
    if found_idx is None:
        raise ValueError(f"Could not find start for {target}")
    chapter_indices.append(found_idx)

# Build chapters slicing
chapters_data = []
for i in range(len(CHAPTER_DEFS)):
    start_idx = chapter_indices[i]
    end_idx = chapter_indices[i+1] if i + 1 < len(chapter_indices) else len(all_paras)
    
    # Exclude the header itself from body paragraphs, or keep it in source.md
    c_info = CHAPTER_DEFS[i]
    body_items = all_paras[start_idx:end_idx]
    
    # Filter out empty or header line if needed
    paras_text = [item['text'] for item in body_items]
    
    # If first paragraph is the header, remove it from paras_text so title isn't duplicated
    if paras_text and paras_text[0].strip() == c_info["orig"].strip():
        paras_text = paras_text[1:]
        
    # Also filter out '番外123' banner if it appears
    paras_text = [p for p in paras_text if p.strip() != '番外123']
    
    chapters_data.append({
        "num": c_info["num"],
        "id": f"ch_{c_info['num']:03d}",
        "orig_title": c_info["orig"],
        "vi_title": c_info["vi"],
        "full_title": f"{c_info['vi']} ({c_info['orig']})",
        "paragraphs": paras_text,
        "start_page": body_items[0]['page_num'],
        "end_page": body_items[-1]['page_num']
    })

print(f"Prepared {len(chapters_data)} chapters.")
for c in chapters_data:
    print(f"{c['id']}: {c['vi_title']} | Pages {c['start_page']}-{c['end_page']} | Paras: {len(c['paragraphs'])}")

# Setup directories
chapters_dir = os.path.join(PROJECT_DIR, "chapters")
memory_dir = os.path.join(PROJECT_DIR, "memory")
os.makedirs(chapters_dir, exist_ok=True)
os.makedirs(memory_dir, exist_ok=True)

# 1. config.json
config_data = {
    "title": "Đấng Cứu Thế Trả Nợ Tình [Hệ Thống]",
    "original_title": "还情债的救世主（系统）",
    "author": "什司 (Thập Ty)",
    "description": "Lâu Hỉ Dương là một đấng cứu thế tiêu chuẩn, thân thế bất phàm, vận mệnh long đong lận đận, trải qua nghìn trùng sóng gió cuối cùng bước lên đỉnh cao nhân sinh cô độc.\nNào ngờ ngoài ý muốn trọng sinh, bị một hệ thống trói định, buộc phải yêu đương với kẻ thù kiếp trước.\nLâu Hỉ Dương một lòng cứu thế: Không yêu! Tuyệt đối không yêu! Huống chi còn là kẻ thù!\nHệ thống: Không yêu là chết đó nhen...\nVì để sống sót bảo vệ thế giới, Lâu Hỉ Dương bất đắc dĩ phải nuôi dưỡng kẻ thù phiên bản ấu trùng, dốc lòng dạy dỗ cậu thành một thanh niên đoan chính, phẩm hạnh tốt đẹp.\nChỉ là tiểu cẩu tể tử này lớn lên, ánh mắt nhìn anh sao mà kỳ lạ thế? Nhơm nhớp, khắc chế, thỉnh thoảng lại làm da đầu anh tê rần.\nHệ thống: Đã bảo rồi, nó thích anh đấy! Anh còn không tin!\n\n(Ôn nhu dịu dàng thẳng nam cứu thế chủ công x Bệnh thái giả ngoan cẩu điên em trai nhà bên thụ)\nThiết lập: Đam mỹ, Trọng sinh, Mạt thế, Hệ thống, Tinh tế nhẹ Cyberpunk, Điềm văn hỗ sủng, HE.",
    "slug": SLUG,
    "source_lang": "Chinese",
    "target_lang": "Vietnamese",
    "raw_links": {
        "czbooks_overview": CZBOOKS_URL,
        "czbooks_first_page": f"{CZBOOKS_URL}/sk2e5?chapterNumber=0",
        "jjwxc": "https://www.jjwxc.net/onebook.php?novelid=6396956"
    },
    "style_guide": "Truyện đam mỹ mạt thế tương lai/tinh tế, hệ thống trả nợ tình, hỗ sủng điềm văn, 1v1, HE.\n\nQUY TẮC BẮT BUỘC:\n1. Văn phong: Mạch lạc, tự nhiên, đậm chất mạt thế tương lai/cyberpunk nhẹ nhàng nhưng giàu cảm xúc ngọt ngào. Lời thoại đặt trong dấu ngoặc kép “...”.\n2. Xưng hô đối thoại:\n   - Công (Lâu Hỉ Dương): Gọi thụ là 'Dịch Duyên' hoặc xưng 'anh - em'.\n   - Thụ (Dịch Duyên): Gọi công là 'Dương ca' (阳哥) hoặc 'ca ca / anh' (哥哥), xưng 'em - anh'. Ngoan ngoãn giả vờ trước mặt công nhưng nội tâm điên cuồng độc chiếm.\n3. Ngôi kể thứ 3 (Tự sự):\n   - Công (Lâu Hỉ Dương): Dùng 'hắn' hoặc 'anh' hoặc tên riêng 'Lâu Hỉ Dương'.\n   - Thụ (Dịch Duyên): Dùng 'cậu' hoặc 'y' hoặc tên riêng 'Dịch Duyên'.\n   - Tuyệt đối không nhầm lẫn đại từ giữa 2 nhân vật nam trong cùng một câu văn.\n4. Bảo toàn 1:1: Giữ nguyên số lượng đoạn văn, cách dòng chuẩn \\n\\n, không thêm bớt tình tiết.",
    "confidence_threshold": 0.8,
    "chunk_size": CHUNK_SZ,
    "created_at": now_gmt7().isoformat(),
    "chapters_count": len(chapters_data),
    "czbooks_pages_count": len(pages)
}
with open(os.path.join(PROJECT_DIR, "config.json"), "w", encoding="utf-8") as f:
    json.dump(config_data, f, ensure_ascii=False, indent=2)

# 2. AGENTS.md
agents_content = """# AGENT RULES: ĐẤNG CỨU THẾ TRẢ NỢ TÌNH [HỆ THỐNG] (还情债的救世主（系统）)

## 1. THÔNG TIN DỰ ÁN & BỐI CẢNH
- **Tên truyện:** Đấng Cứu Thế Trả Nợ Tình [Hệ Thống] (还情债的救世主（系统） / 還情債的救世主（系統）).
- **Tác giả:** 什司 (Thập Ty / Thập Tư).
- **Slug dự án:** `đấng-cứu-thế-trả-nợ-tình`.
- **Thể loại:** Đam mỹ, Trọng sinh, Mạt thế, Viễn tưởng tương lai, Hệ thống, Cyberpunk nhẹ, Điềm văn, Hỗ sủng, Niên hạ, HE.
- **Góc nhìn chính:** Chủ công (Lâu Hỉ Dương).
- **Quy mô:** 32 chương chính văn + 3 chương phiên ngoại (Tổng cộng 35 chương hoàn chỉnh).
- **Liên kết Raw:**
  - 📖 **CZBooks:** [czbooks.net/n/skdfi4kimel](https://czbooks.net/n/skdfi4kimel)
  - 🏛️ **Bản quyền Tấn Giang (JJWXC):** [jjwxc.net/onebook.php?novelid=6396956](https://www.jjwxc.net/onebook.php?novelid=6396956)

---

## 2. THIẾT LẬP NHÂN VẬT CHÍNH
### 🌟 Công: 娄禧阳 / 婁禧陽 (Lâu Hỉ Dương - Lou Xiyang)
* **Hình tượng:** Cứu thế chủ kiếp trước, dịu dàng thẳng nam. Vóc người cao ráo, cơ bắp rắn rỏi, xăm mình phong trần, bên ngoài nhìn như lưu manh bất cần đời nhưng bản chất bên trong là "lão hảo nhân", tràn đầy tinh thần trách nhiệm và lòng trắc ẩn.
* **Thân phận:** Kiếp trước giải cứu M tinh cầu, kiếp này trọng sinh về năm 17 tuổi lúc cha bị bắt, gia đình sa sút.
* **Ngôi kể thứ 3:** Dùng **"anh"** hoặc **"hắn"** hoặc tên riêng **"Lâu Hỉ Dương"**.

### 🖤 Thụ: 易缘 / 易緣 (Dịch Duyên - Yi Yuan)
* **Hình tượng:** Kẻ thù kiếp trước của Lâu Hỉ Dương. Kiếp này lúc đầu là cậu bé hàng xóm đáng thương được Lâu Hỉ Dương bảo bọc, nuôi nấng. Lớn lên thành tuyệt sắc mỹ thiếu niên, bên ngoài giả vờ ngoan ngoãn dịu dàng gọi "ca ca", bên trong là con chó điên bệnh kiều, cố chấp, sẵn sàng xé xác kẻ thù nhưng chỉ dịu dàng mềm mại trước Lâu Hỉ Dương.
* **Xưng hô đối thoại:** Gọi Lâu Hỉ Dương là **"Dương ca" (阳哥)** hoặc **"ca ca / anh" (哥哥)**, xưng **"em" (我)**.
* **Ngôi kể thứ 3:** Dùng **"cậu"** hoặc **"y"** hoặc tên riêng **"Dịch Duyên"**.

### 🤖 Hệ Thống Trả Nợ Tình (情债系统)
* Hệ thống thúc giục Lâu Hỉ Dương hoàn thành nhiệm vụ "trả nợ tình", tính cách hoạt bát, hay cà khịa, nhắc nhở túc chủ phải yêu đương để sống sót.

---

## 3. THUẬT NGỮ & ĐỊA DANH QUAN TRỌNG
- **M星球 (M Tinh cầu):** Hành tinh quê hương đang đối mặt với thảm họa mạt thế.
- **天梯计划 (Kế hoạch Thang Trời):** Dự án xây dựng thế giới mới trên không trung của Liên bang.
- **paradise (Thiên đường):** Trạm không gian / pháo đài sinh tồn trên cao dành cho giới thượng lưu.
- **星船 (Tinh thuyền / Tàu vũ trụ):** Phương tiện di cư giữa các hành tinh.
- **机甲 (Cơ giáp):** Robot chiến đấu chuyên dụng.
- **联邦管理局 (Cục Quản lý Liên bang):** Chính quyền tối cao.

---

## 4. QUY TẮC DỊCH THUẬT & QC BẮT BUỘC
1. **Bảo toàn 1:1 tuyệt đối:** Mỗi đoạn văn tiếng Trung tương ứng chính xác 1 đoạn tiếng Việt. Không gộp đoạn, không tách đoạn.
2. **Cách dòng chuẩn:** Giữa các đoạn luôn cách nhau 1 dòng trống (`\\n\\n`).
3. **Dấu ngoặc thoại:** Dùng ngoặc kép tiếng Việt `“...”`, không dùng gạch đầu dòng (`— ...`).
4. **Không bỏ sót, không phóng tác (Zero Omission, Zero Addition).**
"""
with open(os.path.join(PROJECT_DIR, "AGENTS.md"), "w", encoding="utf-8") as f:
    f.write(agents_content)

# 3. memory files
characters_data = [
    {
        "name": "Lou Xiyang",
        "hanviet_name": "Lâu Hỉ Dương",
        "original_name": "娄禧阳 / 婁禧陽",
        "gender": "Nam",
        "role": "Công (Nhân vật chính / Cứu thế chủ)",
        "aliases": ["Dương ca", "Lâu ca", "cứu thế chủ"],
        "honorifics": "anh - em / tôi",
        "speech_style": "Trầm ổn, dịu dàng, thẳng thắn, bao dung và trách nhiệm",
        "notes": "Đấng cứu thế kiếp trước trọng sinh, ngoài lạnh trong nóng"
    },
    {
        "name": "Yi Yuan",
        "hanviet_name": "Dịch Duyên",
        "original_name": "易缘 / 易緣",
        "gender": "Nam",
        "role": "Thụ (Chủ nợ tình / Em trai nhà bên)",
        "aliases": ["tiểu Duyên", "chó điên nhỏ", "tiểu cẩu tể tử"],
        "honorifics": "em - Dương ca / ca ca",
        "speech_style": "Ngoan ngoãn, mềm mỏng khi ở trước mặt Lâu Hỉ Dương; lạnh lùng tàn nhẫn với kẻ khác",
        "notes": "Kẻ thù kiếp trước, kiếp này được nuôi lớn, thâm tình si luyến bệnh kiều"
    },
    {
        "name": "System",
        "hanviet_name": "Hệ Thống",
        "original_name": "系统 / 系統",
        "gender": "Vô tính",
        "role": "Hệ thống phụ trợ",
        "aliases": ["Hệ thống trả nợ tình"],
        "honorifics": "tôi - ký chủ",
        "speech_style": "Nhí nhảnh, cảnh báo, nhắc nhở tình cảm",
        "notes": "Trói định với Lâu Hỉ Dương ép anh yêu đương"
    }
]
with open(os.path.join(memory_dir, "characters.json"), "w", encoding="utf-8") as f:
    json.dump(characters_data, f, ensure_ascii=False, indent=2)

glossary_data = [
    {"original": "娄禧阳", "translation": "Lâu Hỉ Dương", "hanviet": "Lâu Hỉ Dương", "category": "character", "confidence": 1.0, "approved": True, "notes": "Công chính"},
    {"original": "易缘", "translation": "Dịch Duyên", "hanviet": "Dịch Duyên", "category": "character", "confidence": 1.0, "approved": True, "notes": "Thụ chính"},
    {"original": "M星球", "translation": "hành tinh M", "hanviet": "M tinh cầu", "category": "location", "confidence": 1.0, "approved": True, "notes": "Hành tinh quê hương"},
    {"original": "天梯计划", "translation": "Kế hoạch Thang Trời", "hanviet": "Thiên thê kế hoạch", "category": "term", "confidence": 1.0, "approved": True, "notes": "Dự án cứu sinh"},
    {"original": "paradise", "translation": "Paradise", "hanviet": "Thiên đường", "category": "location", "confidence": 1.0, "approved": True, "notes": "Trạm không gian cho giới giàu"},
    {"original": "星船", "translation": "tinh thuyền", "hanviet": "tinh thuyền", "category": "term", "confidence": 1.0, "approved": True, "notes": "Tàu vũ trụ"},
    {"original": "机甲", "translation": "cơ giáp", "hanviet": "cơ giáp", "category": "term", "confidence": 1.0, "approved": True, "notes": "Robot chiến đấu"},
    {"original": "联邦管理局", "translation": "Cục Quản lý Liên bang", "hanviet": "Liên bang Quản lý cục", "category": "organization", "confidence": 1.0, "approved": True, "notes": "Chính quyền tối cao"}
]
with open(os.path.join(memory_dir, "glossary.json"), "w", encoding="utf-8") as f:
    json.dump(glossary_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(memory_dir, "relationships.json"), "w", encoding="utf-8") as f:
    json.dump([], f, ensure_ascii=False, indent=2)

with open(os.path.join(memory_dir, "timeline.json"), "w", encoding="utf-8") as f:
    json.dump([], f, ensure_ascii=False, indent=2)

# 4. Generate all chapters with source.md, chunks, and meta.json
full_raw_accumulator = []

for c in chapters_data:
    ch_dir = os.path.join(chapters_dir, c["id"])
    chunks_dir = os.path.join(ch_dir, "chunks")
    os.makedirs(chunks_dir, exist_ok=True)
    
    paras = c["paragraphs"]
    n_chunks = (len(paras) + CHUNK_SZ - 1) // CHUNK_SZ if paras else 1
    
    # Write source.md
    source_path = os.path.join(ch_dir, "source.md")
    source_body = "\n\n".join(paras)
    source_content = f"---\ntitle: {c['full_title']}\n---\n\n{source_body}\n"
    with open(source_path, "w", encoding="utf-8") as f:
        f.write(source_content)
        
    # Write chunks
    for ci in range(n_chunks):
        s, e = ci * CHUNK_SZ, (ci + 1) * CHUNK_SZ
        chunk_paras = paras[s:e]
        chunk_content = f"---\ntitle: {c['vi_title']} — Chunk {ci+1}/{n_chunks}\n---\n\n" + "\n\n".join(chunk_paras) + "\n"
        with open(os.path.join(chunks_dir, f"chunk_{ci+1:03d}.md"), "w", encoding="utf-8") as f:
            f.write(chunk_content)
            
    # Write meta.json
    meta_path = os.path.join(ch_dir, "meta.json")
    meta_data = {
        "chapter_id": c["id"],
        "chapter_number": c["num"],
        "title": c["vi_title"],
        "original_title": c["orig_title"],
        "imported_at": now_gmt7().isoformat(),
        "n_paragraphs": len(paras),
        "n_chunks": n_chunks,
        "chunk_size": CHUNK_SZ,
        "start_page": c["start_page"],
        "end_page": c["end_page"],
        "czbooks_url": f"{CZBOOKS_URL}/?chapterNumber={c['start_page']-1}",
        "status": "imported"
    }
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta_data, f, ensure_ascii=False, indent=2)
        
    full_raw_accumulator.append(f"## {c['orig_title']}\n\n{source_body}\n")

# Write raw_full.txt in project root
with open(os.path.join(PROJECT_DIR, "raw_full.txt"), "w", encoding="utf-8") as f:
    f.write(f"# 《還情債的救世主（系統）》 什司 全文 RAW\n\n" + "\n\n".join(full_raw_accumulator))

# Chapters README
with open(os.path.join(chapters_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(f"# Chapters Directory\nTotal {len(chapters_data)} chapters imported and chunked.\n")

print("\nAll 35 chapters created successfully!")
