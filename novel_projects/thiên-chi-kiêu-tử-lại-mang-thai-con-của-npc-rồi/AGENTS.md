# AGENT RULES: THIÊN CHI KIÊU TỬ LẠI MANG THAI CON CỦA NPC RỒI (天之骄子又怀了npc的崽[快穿])

Tài liệu này xác định các quy chuẩn nhân vật, bối cảnh, ma trận đại từ, văn phong và quy trình dịch thuật áp dụng riêng cho dự án **Thiên Chi Kiêu Tử Lại Mang Thai Con Của NPC Rồi**.

---

## ⛔ 1. QUY TẮC CỐT LÕI (MANDATORY ZERO API KEY & INTEGRITY RULES)

1. **Agent Tự Thân Dịch Thuật (Zero Google API Key Mandate):**
   - Agent tự đọc nội dung file raw `source.md`, tự phân tích ngữ cảnh nhân vật, tự sinh bản dịch tiếng Việt chuẩn xác, mượt mà và lưu trực tiếp vào file.
   - **Tuyệt đối cấm** gọi script/tool bên ngoài dùng `GOOGLE_API_KEY` hay `GEMINI_API_KEY`.
2. **Bảo Toàn 1:1 Đoạn Văn (1:1 Paragraph Alignment):**
   - Số đoạn tiếng Việt trong `translation.md` phải khớp tuyệt đối 1:1 với `source.md`. Không tự ý gộp đoạn, chẻ đoạn, không thêm bớt tình tiết.
3. **Quy Cách Ngắt Dòng Chuẩn `\n\n`:**
   - Mọi đoạn trần thuật và lời thoại bắt buộc phải có đúng 1 dòng trống (`\n\n`) ngăn cách. Tuyệt đối không để dính dòng (`\n`).
4. **Dấu Ngoặc Thoại:**
   - Sử dụng ngoặc kép cong tiếng Việt `“...”` cho toàn bộ lời thoại nhân vật. Không dùng gạch đầu dòng (`-`).

---

## 2. BẢNG NHÂN VẬT CHÍNH & MA TRẬN ĐẠI TỪ (THẾ GIỚI 1: MẠT THẾ)

| Tên nhân vật | Tên gốc | Đại từ ngôi 3 | Vai trò / Thân phận | Quy chuẩn xưng hô & Ghi chú |
| :--- | :--- | :--- | :--- | :--- |
| **Giản Ngọc** | 简玉 | **anh** | **Công chính Thế giới 1** (Phú nhị đại xinh đẹp tao nhã, mở màn biến thành tang thi nhưng giữ nguyên lý trí, mang nhiệm vụ khiến nam chính mang bầu) | Ngoại hình cực kỳ xinh đẹp như chim công kiêu kỳ, tính cách vừa lịch thiệp vừa phúc hắc chiếm hữu cao. Xưng **"tôi"** (hoặc **"anh"** khi trêu ghẹo), gọi Giang Huyền là **"Đội trưởng Giang / tiểu đội trưởng / anh"**. |
| **Giang Huyền** | 江玄 | **hắn** | **Thụ chính Thế giới 1** (Thiên chi kiêu tử, nam chính cứu thế chủ mạt thế, Đội trưởng tiểu đội dị năng) | Trầm mặc, tuấn mỹ, cơ bắp săn chắc, võ lực đỉnh cao. Bề ngoài nghiêm túc lạnh lùng nhưng thực chất rất dễ mềm lòng và đỏ tai trước Giản Ngọc. Xưng **"tôi"**, gọi Giản Ngọc là **"cậu / Giản Ngọc"**. |

---

## 3. THIẾT LẬP CÁC THẾ GIỚI (ĐƠN NGUYÊN VĂN) & ĐỊNH DẠNG HỆ THỐNG

1. **Cấu trúc Đơn nguyên văn (Từng thế giới độc lập):**
   - **Thế giới 1 (Mạt thế):** Phú nhị đại biến thành tang thi (Giản Ngọc - Công) × Đội trưởng cứu thế chủ trầm mặc tuấn mỹ (Giang Huyền - Cường thụ).
   - **Thế giới 2 (Esports):** Tiền bối Esports hết thời nằm thẳng (Công) × Ngôi sao mới nổi ngoài lạnh trong fan cuồng (Thụ).
   - **Thế giới 3 (Vô hạn lưu):** Tân sinh viên gà mờ sợ chết nhưng đẹp trai (Công) × Đại diện sinh viên trường đại học kinh dị ngầu lòi (Thụ).
2. **Thông báo Hệ thống:**
   - Đặt trong ngoặc vuông đậm `【...】`.
   - *Ví dụ:* `【Hệ thống: Nhiệm vụ chính tuyến — Khiến nam chính Giang Huyền mang thai con của NPC.】`

---

## 4. PHÂN BIỆT RÕ RÀNG GIỮA THOẠI VÀ TRẦN THUẬT

- **Lời thoại trong `“...”`:** Tự nhiên, sống động, thể hiện rõ nét quyến rũ, ranh mãnh của Giản Ngọc và sự nghiêm nghị nhưng hay ngượng ngùng của Giang Huyền.
- **Văn trần thuật ngôi 3 ngoài ngoặc:** Mượt mà, sắc nét, hài hước duyên dáng. Ở Thế giới 1, Giản Ngọc luôn là **"anh"**, Giang Huyền luôn là **"hắn"**. Tuyệt đối không đem đại từ ngôi 1/ngôi 2 (`mày`, `tao`) vào câu trần thuật ngôi 3.
