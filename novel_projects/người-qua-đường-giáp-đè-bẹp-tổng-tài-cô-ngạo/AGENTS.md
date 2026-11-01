# AGENT RULES: NGƯỜI QUA ĐƯỜNG GIÁP ĐÈ BẸP TỔNG TÀI CÔ NGẠO (路人甲压倒孤傲总裁)

Tài liệu này xác định các quy chuẩn nhân vật, bối cảnh, ma trận đại từ, văn phong và quy trình dịch thuật áp dụng riêng cho dự án **Người Qua Đường Giáp Đè Bẹp Tổng Tài Cô Ngạo**.

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

## 2. BẢNG NHÂN VẬT CHÍNH & MA TRẬN ĐẠI TỪ

| Tên nhân vật | Tên gốc | Đại từ ngôi 3 | Vai trò / Thân phận | Quy chuẩn xưng hô & Ghi chú |
| :--- | :--- | :--- | :--- | :--- |
| **Thẩm Khinh Vân** | 沈轻云 | **anh** | **Công chính** ("Thần chi tý bàng", huyền thoại Cục Xuyên Thư, đóng vai người qua đường Giáp si tình trong giới giải trí) | Bề ngoài diễn vai pháo hôi si tình nhường tài nguyên cho vạn nhân mê để lĩnh tiền thưởng từ hệ thống; thực chất là đại lão phúc hắc, mê sắc đẹp cô ngạo của Tần Tư Niên. Xưng **"tôi"** (hoặc **"anh"** khi dỗ dành/thân mật), gọi Tần Tư Niên là **"Tần tổng / anh / em"**. |
| **Tần Tư Niên** | 秦斯年 | **hắn** | **Thụ chính** (Tổng tài bá đạo cô ngạo nguyên tác) | Âu phục giày da chỉnh tề, khí chất lạnh lùng kiêu ngạo, nhưng lại bị Thẩm Khinh Vân đè bẹp và chinh phục hoàn toàn. Xưng **"tôi"** (hoặc **"em"** khi mềm lòng), gọi Thẩm Khinh Vân là **"cậu / anh / Thẩm Khinh Vân"**. |
| **Tô Thiếu Âm** | 苏少音 | **cậu ta** | **Thụ chính nguyên tác** (Kẻ xuyên sách tự phụ, đóng vai tiểu gay vạn nhân mê) | Kẻ xuyên sách tự cho rằng mình nắm rõ sở thích của Tần Tư Niên và Thẩm Khinh Vân, thích tận hưởng cảm giác được hai người tranh giành, được Thẩm Khinh Vân "nhường" tài nguyên để cày tiền thưởng hệ thống. |

---

## 3. THIẾT LẬP HỆ THỐNG & ĐỊNH DẠNG ĐẶC THÙ

1. **Thông báo Hệ thống:**
   - Đặt trong ngoặc vuông đậm `【...】`.
   - *Ví dụ:* `【Hệ thống: Cảnh báo OOC! Ký chủ đang lệch khỏi thiết lập người qua đường Giáp!】`
2. **Hot Search Weibo & Bình luận mạng (Giới giải trí):**
   - Hashtag Weibo giữ nguyên cấu trúc `#...#`, kèm nhãn `[Bạo]`, `[Hot]`, `[Mới]`.
   - Bình luận cư dân mạng để trong ngoặc kép cong `“...”` hoặc tiền tố `[Cư dân mạng]:` rõ ràng, văn phong trẻ trung, bắt trend showbiz.

---

## 4. PHÂN BIỆT RÕ RÀNG GIỮA THOẠI VÀ TRẦN THUẬT

- **Lời thoại trong `“...”`:** Hiện đại, sắc sảo, thể hiện rõ sự tương phản giữa lúc Thẩm Khinh Vân "diễn kịch" và lúc anh bộc lộ bản tính áp đảo Tần Tư Niên.
- **Văn trần thuật ngôi 3 ngoài ngoặc:** Mượt mà, hiện đại, sang trọng nhưng pha nét hài hước tinh tế. Thẩm Khinh Vân luôn là **"anh"**, Tần Tư Niên luôn là **"hắn"**. Tuyệt đối không đem đại từ ngôi 1/ngôi 2 (`mày`, `tao`) vào câu trần thuật ngôi 3.
