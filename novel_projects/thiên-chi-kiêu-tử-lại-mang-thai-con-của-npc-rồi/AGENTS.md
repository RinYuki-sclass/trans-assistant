# AGENT RULES: THIÊN CHI KIÊU TỬ LẠI MANG THAI CON CỦA NPC RỒI (天之骄子又怀了npc的崽[快穿])

Tài liệu này xác định các quy chuẩn nhân vật, bối cảnh, ma trận đại từ, văn phong và quy trình dịch thuật áp dụng riêng cho dự án **Thiên Chi Kiêu Tử Lại Mang Thai Con Của NPC Rồi**.

---

## ⛔ 1. QUY TẮC CỐT LÕI (MANDATORY ZERO GOOGLE API KEY & INTEGRITY RULES)

1. **Agent Tự Thân Dịch Thuật (Universal Zero Google API Key Mandate):**
   - Agent tự đọc nội dung raw `source.md`, tự phân tích ngữ cảnh nhân vật, tự sinh bản dịch tiếng Việt chuẩn xác, mượt mà và lưu trực tiếp vào file.
   - **TUYỆT ĐỐI CẤM** gọi bất kỳ script/tool/process bên ngoài dùng `GOOGLE_API_KEY` hay `GEMINI_API_KEY` (như thư viện `google.genai`, `google-generativeai`).
   - Mọi thao tác Pre-scan, Dịch, QC, Cập nhật Lore và Format đều do AI Code Agent trực tiếp đảm nhiệm trong workspace để tránh triệt để lỗi rate limit 429/503 và bảo vệ hạn mức của người dùng.
2. **Bảo Toàn 1:1 Đoạn Văn (1:1 Paragraph Alignment):**
   - Số đoạn văn tiếng Việt trong `translation.md` bắt buộc phải khớp tuyệt đối 1:1 với `source.md`.
   - Tuyệt đối không tự ý gộp đoạn, chẻ đoạn, không thêm bớt tình tiết ngoài nguyên tác.
3. **Quy Cách Ngắt Dòng Chuẩn `\n\n`:**
   - Mọi đoạn trần thuật và lời thoại bắt buộc phải có đúng 1 dòng trống (`\n\n`) ngăn cách. Tuyệt đối không để dính dòng (`\n`).
4. **Dấu Ngoặc Thoại Tiếng Việt Chuẩn:**
   - Sử dụng ngoặc kép cong tiếng Việt `“...”` cho toàn bộ lời thoại nhân vật. Không dùng gạch đầu dòng (`-`) hay ngoặc thẳng `""`.

---

## 👥 2. BẢNG NHÂN VẬT & MA TRẬN ĐẠI TỪ (THẾ GIỚI 1: MẠT THẾ)

> 💡 **Quy ước tuổi tác cốt lõi:**  
> • **Giản Ngọc:** **22 tuổi** (Công - lớn hơn 3 tuổi, cao hơn 1m87).  
> • **Giang Huyền:** **19 tuổi** (Thụ - nhỏ hơn 3 tuổi, cao 1m87).  
> Xưng hô đối thoại bắt buộc phản ánh đúng độ chênh lệch tuổi tác này.

| Tên nhân vật | Tên gốc | Ngôi 3 trần thuật | Vai trò / Thân phận | Quy chuẩn xưng hô theo tuổi tác & Tính cách |
| :--- | :--- | :---: | :--- | :--- |
| **Giản Ngọc** | 简玉 | **anh** | **Công chính Thế giới 1** (22 tuổi, Ký chủ Cục Xuyên Thư - Bộ phận NPC, xuyên thành phú nhị đại biến thái bắt cóc nam chính) | Ngoại hình cực phẩm, da trắng môi hồng, khuyên tai giọt máu hình hồ ly, hút thuốc lá Treasure. Tính lười biếng, độc miệng, tự luyến, thích trêu chọc đối phương.<br>• **Xưng hô với Giang Huyền (19 tuổi):**<br>- Xưng: **"tôi"** (bình thường) hoặc **"anh"** (khi trêu ghẹo, tỏ vẻ đàn anh, tán tỉnh, thân mật).<br>- Gọi Giang Huyền: **"cậu"**, **"Đội trưởng Giang / tiểu đội trưởng"**, **"nhóc"**, **"em"** (khi trêu ghẹo hoặc thân mật). *Tuyệt đối không gọi Giang Huyền là "anh".*<br>• Với Hệ thống: xưng **"tôi"**, gọi **"tiểu mật ong / Điệp Điệp"**. |
| **Giang Huyền** | 江玄 | **hắn** | **Thụ chính Thế giới 1** (19 tuổi, Thiên chi kiêu tử, Đội trưởng cứu thế chủ mạt thế, thành viên Hiệp hội 1 tổ chức FBO) | 19 tuổi, cao 1m87, cơ bắp săn chắc, đường nhân ngư rõ nét, võ lực đỉnh cao, ra tay quyết đoán lạnh lùng. Bề ngoài nghiêm nghị, ít nói nhưng thực chất nội tâm ngây thơ, rất dễ thẹn thùng và đỏ bừng vành tai trước đàn anh Giản Ngọc.<br>• **Xưng hô với Giản Ngọc (22 tuổi):**<br>- Xưng: **"tôi"** (nghiêm túc / giữ kẽ) hoặc **"em"** (khi đã mềm lòng / thân mật).<br>- Gọi Giản Ngọc: **"anh"** (đúng vai vế nhỏ hơn 3 tuổi) hoặc gọi thẳng tên **"Giản Ngọc"** (khi tức giận, cảnh giác hoặc bị chọc tức). *Tuyệt đối không gọi Giản Ngọc là "cậu".* |
| **Hệ thống Điệp Điệp (Tiểu Mật Ong)** | 系统小蜜蜂 (蝶蝶) | **nó / hệ thống** | **Hệ thống hỗ trợ của Giản Ngọc** | Hình tượng đầu người chibi Q-version gắn thân ong mật nhỏ bé, tính cách nhí nhảnh, nhiều chuyện, thích cổ vũ và mang đèn led. Quản lý **Nhiệt kế tình cảm** (mục tiêu 999 độ).<br>• Xưng: **"tôi / hệ thống"**, gọi Giản Ngọc là **"ký chủ"**. |
| **A Đại** | 阿大 | **gã / hắn** | Vệ sĩ của Giản Ngọc | Nịnh hót, ham ăn, uống nhầm bát canh rùa nhiễm độc nên hóa thành tang thi đầu tiên. |
| **A Nhị** | 阿二 | **gã / hắn** | Vệ sĩ đi theo Giản Ngọc | Tỉnh táo hơn, biết võ nghệ, bảo vệ Giản Ngọc trong khách sạn trước khi chạy trốn. |

---

## 🌌 3. THIẾT LẬP THẾ GIỚI & ĐỊNH DẠNG HỆ THỐNG

1. **Bối cảnh Thế giới 1 (Mạt thế tang thi bùng phát):**
   - Bắt đầu vào dịp Giáng sinh 2025, virus tang thi số 1 đột biến lan tràn từ các cơ sở phúc lợi và nguồn nước.
   - Tang thi trong truyện có đặc điểm: giữ lại tàn dư tri giác và trí thông minh, có thể giả chết mai phục, tốc độ trao đổi chất gấp vạn lần, chỉ có dùng **lửa thiêu** mới tiêu diệt triệt để.
   - Bối cảnh hành trình: Khách sạn trung tâm thành phố Z -> Cao tốc -> Khu tị nạn Khu Công nghiệp.
2. **Quy chuẩn hiển thị Giao diện Hệ thống:**
   - **Thông báo Hệ thống:** Đặt trong ngoặc vuông đậm `【...】`.
     - *Ví dụ:* `【Hệ thống: Nhiệm vụ chính tuyến — Khiến thiên chi kiêu tử Giang Huyền mang thai con của NPC.】`
     - *Ví dụ:* `【Cảnh báo: Nhiệt kế tình cảm hiện tại: 0°C. Cần đạt 999°C để kích hoạt điều kiện hoài thai!】`
3. **Cấu trúc Đơn nguyên văn (Khoái xuyên - Các thế giới tiếp theo):**
   - **Thế giới 1 (Mạt thế):** Phú nhị đại tang thi công (Giản Ngọc) × Đội trưởng cứu thế chủ cường thụ (Giang Huyền).
   - **Thế giới 2 (Esports):** Tiền bối hết thời lười biếng công × Tân binh ngôi sao ngoài lạnh trong cuồng si thụ.
   - **Thế giới 3 (Vô hạn lưu):** Tân sinh viên gà mờ sợ chết công × Hội trưởng sinh viên trường kinh dị thụ.

---

## 🎭 4. PHÂN ĐỊNH TUYỆT ĐỐI GIỮA THOẠI VÀ TRẦN THUẬT

1. **Văn trần thuật ngôi 3 ngoài ngoặc kép:**
   - Tuyệt đối nghiêm túc, gãy gọn, bảo toàn góc nhìn thứ ba khách quan kết hợp tính châm biếm hài hước tao nhã.
   - Giản Ngọc trong ngôi 3 luôn là **"anh"**.
   - Giang Huyền trong ngôi 3 luôn là **"hắn"**.
   - **NGHIÊM CẤM:** Không được đưa đại từ khẩu ngữ ngôi 1/ngôi 2 (`mày`, `tao`, `ngươi`) vào trong các câu trần thuật hoặc suy nghĩ nội tâm ngôi 3.
2. **Lời thoại trực tiếp trong `“...”`:**
   - Khắc họa sống động sự ranh mãnh, tao nhã, châm chọc của Giản Ngọc và vẻ ngoài nghiêm cẩn nhưng dễ ngượng ngùng của Giang Huyền.
   - Giữ trọn sự dí dỏm, phản sáo lộ đặc trưng của thể loại sinh tử văn / hài hước ngọt sủng.

---

## 🛠️ 5. TIÊU CHUẨN THỰC THI PIPELINE 5 BƯỚC

1. **Pre-scan (`novel-prescan-extractor`):** Rà soát thực thể mới, danh xưng, địa danh trước khi dịch từng chương/batch.
2. **Translation (`novel-chunk-translator`):** Agent tự thân dịch trực tiếp 1:1, kiểm soát chuẩn `\n\n` và thoại `“...”`.
3. **QC Audit (`novel-qc-auditor`):** Rà soát đối chiếu dòng-dòng, đảm bảo không lệch đại từ, không rớt đoạn.
4. **Lorekeeper (`novel-lorekeeper`):** Cập nhật dữ liệu vào `memory/characters.json`, `memory/glossary.json`, `memory/timeline.json`.
5. **Publisher Formatter (`novel-publisher-formatter`):** Chuẩn hóa file xuất bản, đồng bộ `TOC.md` và `chapters_index.json`.
