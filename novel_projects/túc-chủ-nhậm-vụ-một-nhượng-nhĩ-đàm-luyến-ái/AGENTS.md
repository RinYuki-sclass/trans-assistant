# AGENT RULES: TÚC CHỦ, NHẬM VỤ MỘT NHƯỢNG NHĨ ĐÀM LUYẾN ÁI (宿主，任务没让你谈恋爱)

> **Tên tác phẩm:** Túc Chủ, Nhậm Vụ Một Nhượng Nhĩ Đàm Luyến Ái (宿主，任务没让你谈恋爱)  
> **Tên dịch:** Ký Chủ, Nhiệm Vụ Đâu Có Bảo Ngươi Đi Yêu Đương  
> **Tác giả:** Mặc Ngư Bồ Đào (墨鱼葡萄)  
> **Slug dự án:** `túc-chủ-nhậm-vụ-một-nhượng-nhĩ-đàm-luyến-ái`  
> **Thể loại:** Đam mỹ, Cổ trang Tiên hiệp tu chân, Xuyên thư, Hệ thống, Chủ công, Hài hước sa điêu, Quần tượng, Song khiết, Nước chảy mây trôi, 1v1, HE.  
> **Cặp đôi chính:** Giản Tri (Chủ công / Xuyên thư pháo hôi) × Ân Trường Tư (Thụ chính / Phong lưu tà mị đại lão)

---

## ⛔ QUY TẮC TỐI THƯỢNG: TOÀN BỘ SOURCE KHÔNG DÙNG GOOGLE API KEY (ZERO GOOGLE API KEY MANDATE)

1. **AI Agent Tự Thân Thực Thi Trực Tiếp 100%:**
   - Đọc trực tiếp `source.md` bằng công cụ đọc file (`read_file`).
   - Tự phân tích ngữ cảnh, tra cứu đối chiếu thực thể trong `AGENTS.md` và `memory/`.
   - Trực tiếp biên dịch, chuẩn hóa đại từ ngôi 3, phân tầng đối thoại cổ phong tu chân pha sa điêu, bảo toàn khoảng cách `\n\n` và tỷ lệ đoạn 1:1.
   - Trực tiếp lưu trữ `translation.md`, `qc_report.md`, `meta.json` bằng công cụ ghi file (`write_file`).
2. **CẤM GỌI API NGOÀI:** Tuyệt đối không chạy script Python hoặc công cụ ngoài sử dụng Google API (`GEMINI_API_KEY`, `GOOGLE_API_KEY`, thư viện google-genai, v.v.) để tránh phát sinh lỗi **429 Resource Exhausted** và **503 High Demand**.

---

## 📖 1. MA TRẬN NHÂN VẬT & ĐẠI TỪ TRẦN THUẬT NGÔI THỨ BA

| Nhân vật | Hán tự | Vai trò / Thân phận | Đại từ trần thuật ngôi 3 | Quy chuẩn xưng hô & Nguyên tắc dịch |
| :--- | :--- | :--- | :--- | :--- |
| **Giản Tri** | 简知 | **Công chính / Chủ công (POV chính)** | **hắn** | Xuyên thư thành pháo hôi xuất hiện hai phút, bị Hệ thống 34 trói buộc đi làm bà mai. Tính cách lý trí, mặt dày, phản ứng nhanh, thích cà khịa. Đối thoại: xưng **"ta"**, gọi Ân Trường Tư là **"tiền bối"** (ban đầu) / **"ngươi"** / **"Trường Tư"**. |
| **Ân Trường Tư** | 殷长思 | **Thụ chính** | **y** | Đại lão tu chân phong lưu phóng khoáng, dựa cây hòe phe phẩy quạt, khóe mắt có nốt ruồi lệ câu hồn. **Bắt buộc dùng "y" trong trần thuật** để phân biệt rạch ròi với "hắn" (Giản Tri). Đối thoại: xưng **"ta"**, gọi Giản Tri là **"ngươi"** / **"nhóc con"** / **"tiểu khả liên"**. |
| **Hệ thống 34** | 系统34 | Hệ thống nhiệm vụ | **nó / Hệ thống 34** | Giao nhiệm vụ ngăn đồ đệ hắc hóa, thường xuyên gào thét vì ký chủ đi yêu đương. |
| **Giang Lâm Hề** | 江临兮 | Đồ đệ nguyên tác | **hắn / y** | Đồ đệ nhút nhát ban đầu, mục tiêu nhiệm vụ cần ngăn hắc hóa, thầm mến sư tôn. |
| **Lạc Thiên Sơn** | 落千山 | Sư tôn nguyên tác | **y** | Sư tôn lạnh lùng như băng tuyết trên đài cao. |

---

## ⚔️ 2. QUY CHUẨN XƯNG HÔ ĐỐI THOẠI & VĂN PHONG TIÊN HIỆP SA ĐIÊU

1. **Phân định rạch ròi cặp đại từ ngôi thứ 3 (Narrative POV):**
   - **Giản Tri:** Luôn là **"hắn"**.
   - **Ân Trường Tư:** Luôn là **"y"** (hoặc gọi thẳng họ tên "Ân Trường Tư").
   - ⚠️ **TUYỆT ĐỐI CẤM:** Không dùng **"anh - cậu"** trong lời kể trần thuật hay đối thoại của truyện cổ phong tiên hiệp.
2. **Xưng hô đối thoại cổ phong:**
   - Giữa Giản Tri và Ân Trường Tư: Xưng **"ta - ngươi"**, xưng hô tiền bối - vãn bối lúc đầu, về sau gọi tên riêng thân mật.
   - Với sư môn: Xưng **"sư tôn - đồ nhi"**, **"sư huynh - sư đệ"**.
   - ⚠️ **CẤM DÙNG "mày - tao":** Dù châm chọc, sa điêu đến đâu vẫn giữ chuẩn ngữ khí tu chân hài hước.
3. **Phân định Thoại trực tiếp `“...”` vs Trần thuật / Suy nghĩ nội tâm:**
   - **Thoại trực tiếp trong ngoặc kép `“...”`:** Tự do thể hiện tính sa điêu, bựa, hài hước của nhân vật.
   - **Trần thuật / Độc thoại không ngoặc kép:** Bắt buộc tuân thủ ngôi thứ 3 chuẩn xác. Tuyệt đối cấm mang đại từ đối thoại (ta, tôi, ngươi, mày) vào làm chủ ngữ trần thuật (hiện tượng đá ngôi).

---

## 💎 3. THUẬT NGỮ TU CHÂN & HỆ THỐNG

- **Cảnh giới / Môn phái:** Tông môn tu tiên, sư đồ, bái sư, môn hạ, đại điển bái sư.
- **Hệ thống:** Ký chủ (túc chủ), hệ thống, tích phân, hắc hóa, thiết lập nhân vật (nhân thiết), pháo hôi.
- **Pháp bảo / Đạo cụ:** Quạt xếp phong lưu, nốt ruồi lệ, phi kiếm, trận pháp.

---

## 📏 4. QUY CHUẨN ĐỊNH DẠNG & KỸ THUẬT TRÌNH BÀY BẮT BUỘC

1. **Khoảng cách đoạn chuẩn `\n\n`:**
   - Mọi đoạn văn trần thuật hoặc lời thoại bắt buộc phải cách nhau đúng 1 dòng trống (`\n\n`). Cấm dính dòng (`\n`).
2. **Dấu ngoặc kép chuẩn `“...”`:**
   - Lời thoại sử dụng ngoặc kép cong tiếng Việt `“...”`, không dùng gạch ngang đầu câu (`— ...`).
3. **Bảo toàn 100% nguyên tác (1:1 Paragraph Alignment):**
   - Số đoạn văn tiếng Việt trong `translation.md` phải khớp chính xác 1:1 với số đoạn văn gốc trong `source.md`.
4. **Nguyên tắc Tự Hành Liên Hoàn - Cấm Bẫy Dừng Hội Thoại (Zero Conversational Pause):**
   - Khi chạy chế độ liên hoàn hoặc batch, Agent tự động nạp chương, dịch, soát QC, đồng bộ memory và chuyển tiếp mượt mà, không dừng giữa chừng để chờ người dùng gõ lệnh "tiếp tục".

---

## ⚡ 5. QUY TRÌNH 4 GIAI ĐOẠN CHO MỖI CHƯƠNG (4-PHASE PIPELINE)

- **Phase 1: Pre-scan & Tra cứu Thực thể:** Đọc `source.md`, quét nhân vật mới, thuật ngữ tu tiên, lời thoại hệ thống.
- **Phase 2: Translation (Biên dịch chính thức):** Dịch trung thành 1:1, áp ma trận đại từ "hắn" (Giản Tri) vs "y" (Ân Trường Tư), ngoặc kép `“...”`, khoảng cách `\n\n`.
- **Phase 3: Strict QC Audit (Kiểm thử đa tầng):** Kiểm tra 1:1 paragraph count, soát lỗi đá ngôi, soát văn phong cổ phong sa điêu, xuất `qc_report.md`.
- **Phase 4: Lorekeeper & Publishing:** Cập nhật `characters.json`, `glossary.json`, `timeline.json`, ghi nhận vào `chapters_index.json` và `TOC.md`.
