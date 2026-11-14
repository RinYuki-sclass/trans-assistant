# BẢNG PHÂN TÍCH TIỀN TRẢM & LÀM RÕ NGỮ CẢNH (QA CLARIFICATIONS) - CHƯƠNG 37

## 1. THÔNG TIN CHUNG
- **Chương:** 37 (第37章)
- **Dự án:** Pháo Hôi Đặc Trợ Chích Tưởng Nã Tiền Bào Lộ (《炮灰特助只想拿钱跑路》)
- **Số đoạn văn gốc:** 72 đoạn.
- **Bối cảnh phân cảnh:**
  - Phân cảnh 1: Tùy Ứng ngồi trên tinh hạm, đáp trả tin nhắn quấy rối của Cố Thiên Diệp. Tinh hạm hạ cánh, Tùy Thịnh lái xe đón Tùy Ứng cùng chú cún Tưu Tưu (啾啾).
  - Phân cảnh 2: Hai anh em đưa Tưu Tưu đi tiệm thú cưng tắm rửa và mua đồ chơi. Mẹ kế Lý Tình gọi điện hối thúc ăn cơm.
  - Phân cảnh 3: Chuyển cảnh sang Bùi Tiềm và Phó Dận An. Phó Dận An âm thầm đi theo Tùy Ứng, ngồi lật hồ sơ uống rượu và ngượng ngùng hỏi Bùi Tiềm nên mua quà gì khi gặp mặt.
  - Phân cảnh 4: Tùy Ứng và Tùy Thịnh tới nhà hàng sang trọng của khách sạn liên sao gặp mẹ kế Lý Tình. Lý Tình tỏ vẻ thân thiết nhưng giả tạo xót tiền, than vãn về người cha Tùy Văn Hàn bị kẹt xe và mưu toan mai mối cho Tùy Ứng. Tùy Thịnh dằn mạnh cốc nước cắt ngang.

---

## 2. BẢNG THỰC THỂ & DANH TỪ RIÊNG (ENTITY MAPPING)

| Thực thể gốc | Hán Việt | Bản dịch chuẩn | Thể loại | Ghi chú ngữ cảnh |
| :--- | :--- | :--- | :--- | :--- |
| 隋应 | Tùy Ứng | Tùy Ứng | Nhân vật (Alpha) | Công chính, trần thuật ngôi 3 là "hắn". |
| 傅胤安 | Phó Dận An | Phó Dận An | Nhân vật (Alpha đỉnh cấp) | Thụ chính, trần thuật ngôi 3 là "anh". |
| 顾天烨 | Cố Thiên Diệp | Cố Thiên Diệp | Nhân vật | Kẻ bám đuôi gửi tin nhắn quấy rối. |
| 隋晟 | Tùy Thịnh | Tùy Thịnh | Nhân vật | Em trai cùng cha khác mẹ, gọi Tùy Ứng là "anh" (哥). |
| 啾啾 | Tưu Tưu | Tưu Tưu | Thú cưng | Chú cún giống Lang Thanh do Tùy Thịnh nuôi. |
| 裴潜 | Bùi Tiềm | Bùi Tiềm | Nhân vật | Bạn thân của Phó Dận An. |
| 李晴 | Lý Tình | Lý Tình | Nhân vật | Mẹ kế của Tùy Ứng, mẹ ruột Tùy Thịnh. |
| 隋文翰 | Tùy Văn Hàn | Tùy Văn Hàn | Nhân vật | Cha ruột của Tùy Ứng. |
| 首都星 | Thủ đô tinh | Tinh cầu thủ đô | Địa danh | Trung tâm tinh tế. |
| 星舰 | Tinh hạm | Tinh hạm | Phương tiện | Tàu vũ trụ liên sao. |
| 悬浮车 | Huyền phù xa | Xe bay | Phương tiện | Xe lơ lửng / xe bay. |
| 绿洲港 | Lục Châu Cảng | Cảng Lục Châu | Địa danh | Nơi có sơn trang suối nước nóng ở chương trước. |

---

## 3. MA TRẬN ĐẠI TỪ & QUY CHUẨN XƯNG HÔ ĐỐI THOẠI

| Cặp nhân vật | Người nói | Người nghe | Xưng | Gọi | Sắc thái & Quy chuẩn |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Tùy Ứng - Cố Thiên Diệp | Tùy Ứng | Cố Thiên Diệp | tôi | anh | Lạnh lùng, vạch rõ giới hạn qua tin nhắn. |
| Tùy Thịnh - Tùy Ứng | Tùy Thịnh | Tùy Ứng | em | anh | Nhiệt tình, bám người, mở miệng là "anh". |
| Tùy Ứng - Tùy Thịnh | Tùy Ứng | Tùy Thịnh | tôi | cậu | Giữ khoảng cách vừa phải, lý trí, điềm đạm. |
| Bùi Tiềm - Phó Dận An | Bùi Tiềm | Phó Dận An | tôi | cậu | Bạn bè thân thiết, trêu chọc chuyện tình cảm. |
| Phó Dận An - Bùi Tiềm | Phó Dận An | Bùi Tiềm | tôi | cậu | Lạnh lùng, ngượng ngùng khi bị chọc trúng tim đen. |
| Lý Tình - Tùy Ứng | Lý Tình | Tùy Ứng | dì | con / Tiểu Ứng | Giả lả, ngọt ngào bên ngoài, toan tính bên trong. |
| Tùy Ứng - Lý Tình | Tùy Ứng | Lý Tình | tôi / con | dì | Lịch sự xã giao, khách khí xa cách. |
| Tùy Thịnh - Lý Tình | Tùy Thịnh | Lý Tình | con | mẹ | Cộc lốc, bực bội vì biết rõ mưu tính của mẹ mình. |
