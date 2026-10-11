# Manhwa Character Visual Recognition Guide (Visual Grounding)

> **Mục đích:** Cung cấp nguồn nhận diện thị giác (Visual Grounding Source) và dấu hiệu nhận dạng lời thoại để AI Vision Model Pro xác định chính xác người nói trong khung tranh `[Người nói/narrator]`.

---

## 1. BẢNG ĐẶC ĐIỂM NHẬN DẠNG NGOẠI HÌNH (VISUAL PROFILES)

| Nhân vật | Đặc điểm khuôn mặt & Tóc | Vóc dáng & Trang phục đặc trưng | Dấu hiệu nhận biết khác |
| :--- | :--- | :--- | :--- |
| **Han Yoojin (한유진)** | Tóc đen ngắn tự nhiên, mái rẽ nhẹ hoặc tự nhiên; mắt nâu ấm áp, khuôn mặt thanh tú, hiền lành nhưng ánh mắt kiên định. | Dáng người mảnh khảnh, thấp hơn các Hunter cấp S. Thường mặc áo len dệt kim rộng (knit sweater), áo sơ mi đơn giản, áo khoác cardigan, hoặc âu phục công vụ đơn sắc của Haeyeon. | Thường bế hoặc đi cùng ma thú con: **Peace** (sư tử nhỏ lông đỏ cam, có sừng nhọn) hoặc **Chirpie** (chim tròn lông vàng, có lá mầm trên đỉnh đầu). |
| **Han Yoohyun (한유현)** | Tóc đen cắt ngắn vuốt gọn gàng; đôi mắt xám/đen sắc lạnh, ánh nhìn nghiêm nghị, sắc bén. Trước mặt Yoojin ánh mắt dịu dàng, ngoan ngoãn. | Cao lớn (~1m86), bờ vai rộng, cơ bắp săn chắc. Luôn mặc âu phục đen/xám cao cấp của Hội trưởng Haeyeon hoặc áo giáp chiến đấu đen tuyền. | Kỹ năng lửa rực cháy quanh người hoặc trên vũ khí. Luôn có xu hướng đứng chắn phía trước Yoojin. |
| **Sung Hyunjae (성현제)** | **Tóc vàng kim sáng (blonde) vuốt ngược ra sau gọn gàng**, vài sợi rủ nhẹ; **đôi mắt màu hổ phách/vàng cam**, đuôi mắt dài quyến rũ, nụ cười nửa miệng trêu chọc/sâu cay. | Vóc dáng cao lớn vượt trội (~1m90), phong thái quý tộc xa hoa. Mặc âu phục ba mảnh đắt tiền, áo khoác choàng dài, có thể có chuỗi xích vàng trang trí. | Kỹ năng sấm sét/dây xích điện màu vàng bao quanh. Thường cầm tách trà hoặc chống cằm mỉm cười nhìn Yoojin. |
| **Park Yerim (박예림)** | Tóc đen hoặc xanh đen dài, **thường buộc đuôi ngựa cao (high ponytail)**; đôi mắt to tròn màu xanh nước biển hoặc đen, nét mặt bướng bỉnh, lanh lợi. | Nữ sinh 15 tuổi, dáng người nhanh nhẹn. Mặc đồng phục học sinh cấp 3, áo khoác thể thao năng động, hoặc đồ chiến đấu thợ săn gọn nhẹ. | Hiệu ứng nước hoặc băng tuyết bao quanh khi chiến đấu. Thường làm biểu cảm chu môi, phồng má hoặc tạo dáng tự tin. |
| **Song Taewon (송태원)** | Tóc đen cắt ngắn kiểu nhà binh (crew cut); đôi mắt đen sâu thẳm, **quầng thâm mắt rõ rệt vì thiếu ngủ và làm việc quá sức**, khuôn mặt vuông vức nghiêm nghị. | Thể hình đồ sộ, cơ bắp cuồn cuộn như tảng đá. Luôn mặc âu phục công vụ đen, sơ mi trắng cài kín cổ, thắt cà vạt nghiêm chỉnh, tác phong chuẩn mực. | Thường xuất hiện với vẻ mặt mệt mỏi, bất lực trước sự quậy phá của các thợ săn cấp S. |
| **Noah Rugir (노아 루기르)** | **Tóc vàng nhạt gợn sóng dài ngang vai**, khuôn mặt lai phương Tây thanh thoát, **đôi mắt xanh lam trong veo**, biểu cảm rụt rè, bẽn lẽn, hay đỏ mặt. | Dáng người dong dỏng, gầy nhẹ. Thường mặc trang phục đơn giản, áo choàng kín đáo. | Có thể biến thân thành **Rồng nhỏ màu vàng kim** có cánh bay lơ lửng, hoặc nửa người nửa rồng (mọc sừng, cánh vàng). |
| **Moon Hyuna (문현아)** | Tóc đỏ tía/hồng đậm cắt ngắn cá tính hoặc vuốt ngược; mắt sắc sảo, nụ cười lớn sảng khoái, răng khểnh. | Nữ, cao lớn, cơ bắp săn chắc, phong thái chị đại phóng khoáng. Thường mặc áo khoác da, áo sát nách khoe cơ bắp, mang thương kích lớn. | Hội trưởng Breaker, tính cách bộc trực, hay khoác vai đùa cợt với Yoojin. |
| **Yoo Myungwoo (유명우)** | Tóc nâu/đen bù xù, đeo kính cận tròn dày; ban đầu rụt rè tự ti, sau khi thức dũng mãnh và tự tin hơn. | Mặc trang phục thợ rèn, đeo tạp dề da chống nhiệt, tay áo xắn cao, mang búa thợ rèn ma thuật. | Bạn thân cùng tuổi của Yoojin, luôn lo lắng Yoojin không biết quý trọng bản thân. |
| **Park Hayool (박하율)** | Nam, 20 tuổi, khuôn mặt thư sinh, nụ cười ngây thơ ngọt ngào kiểu thần tượng/diễn viên. | Mặc đồ thời trang trẻ trung, vẻ ngoài ngoan ngoãn dễ thương. | Kỹ năng tinh thần mê hoặc (tâm cơ ngầm, giả vờ làm em trai ngoan để thao túng). |

---

## 2. DẤU HIỆU LỜI THOẠI QUY CHIẾU (CONTEXTUAL DIALOGUE GROUNDING)

Khi nhân vật quay lưng, bị che khuất hoặc bóng đen, hãy nhận diện người nói qua các từ khóa xưng hô sau:

- Nếu người nói gọi **`Hyung` (형)**:
  - ➔ Chắc chắn là **Han Yoohyun** (hoặc Park Hayool / Choi Suryeon tùy phân cảnh).
- Nếu người nói gọi **`Han Yoojin-gun` (한유진 군)** hoặc trêu ghẹo cợt nhả:
  - ➔ Chắc chắn là **Sung Hyunjae**.
- Nếu người nói gọi **`Ahjussi` (아저씨)** hoặc **`Chú`**:
  - ➔ Chắc chắn là **Park Yerim**.
- Nếu người nói gọi **`Yoohyun-ah` (유현아)** hoặc **`em trai của anh`**:
  - ➔ Chắc chắn là **Han Yoojin**.
- Nếu người nói xưng hô mang tính hành chính công vụ, gọi **`Thợ săn Han Yoojin` (한유진 헌터)** với giọng nghiêm túc:
  - ➔ Là **Song Taewon**.
- Nếu người nói dùng kính ngữ rụt rè, gọi **`Ngài / Anh` (형님 / 소장님)**:
  - ➔ Thường là **Noah Rugir**.

---

## 3. QUY TẮC NHẬN DIỆN KHUNG ĐẶC BIỆT

- **Hộp thoại hình chữ nhật màu đen/trắng (không có đuôi bóng thoại trỏ vào ai)**:
  - Đây là lời thuyết minh bối cảnh hoặc suy nghĩ dẫn chuyện ➔ Gán `[Narrator]`.
  - Nếu là dòng suy nghĩ nội tâm của nhân vật chính ➔ Gán `[Han Yoojin - Độc thoại]`.
- **Bóng thoại có gai nhọn, viền răng cưa rung lắc**:
  - Tiếng hét to, kinh ngạc hoặc ra lệnh khẩn cấp ➔ Kiểm tra nhân vật đang mở miệng hét lớn trong khung.
- **Bóng thoại nét đứt (dashed/dotted border)**:
  - Tiếng nói thầm hoặc thì thầm trong miệng.
- **Chữ vẽ trực tiếp vào cảnh vật (Sound Effects)**:
  - Nếu là âm thanh va chạm, sấm sét, nổ lớn có ảnh hưởng mạch truyện ➔ Gán `[SFX]`.
