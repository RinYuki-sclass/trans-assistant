# QUY TẮC BỔ SUNG VĂN ÁN & SIÊU DỮ LIỆU ĐẦY ĐỦ TỪ RIDIBOOKS CHO NOVEL PROJECT

Quy chuẩn này bắt buộc áp dụng khi khởi tạo, cập nhật hoặc bổ sung thông tin cho các tiểu thuyết có nguồn từ **RIDI (Ridibooks)** hoặc Webnovel Hàn Quốc vào workspace `trans-assistant`.

---

## 1. CẤU TRÚC VĂN ÁN TIÊU CHUẨN RIDI (RIDI STANDARD METADATA SCHEMA)
Mỗi tác phẩm trên RIDI luôn sở hữu cấu trúc thông tin giới thiệu độc quyền gồm 5 phần cốt lõi:
1. **Từ khóa tác phẩm (키워드 / Keywords):**
   - Bối cảnh/Thể loại (서양풍, 판타지물, 궁정물, 회귀물, 복수물...)
   - Thiết lập Công (황자공, 미인공, 다정공, 헌신공, 사랑꾼공, 짝사랑공...)
   - Thiết lập Thụ (기사수, 미남수, 단정수, 계략수, 능력수, 회귀수, 도망수...)
2. **Khi nào nên đọc (이럴 때 보세요 / Recommendation Hook):**
   - Câu gợi ý cảm xúc chủ đạo của tác phẩm cho độc giả.
3. **Giới thiệu nhân vật chính (등장인물 / Character Profiles):**
   - Công: Tên, thân phận, tính cách, vai trò và tình cảm dành cho Thụ.
   - Thụ: Tên, thân phận, biến cố tiền kiếp, mục tiêu trùng sinh/trả thù và sự thay đổi tâm lý.
4. **Văn án & Tóm tắt cốt truyện (작품 소개 / 줄거리 / Synopsis):**
   - Mở đầu bằng câu hook đặc trưng của truyện (thường là câu nói ấn tượng nhất).
   - Nội dung xung đột then chốt, bi kịch kiếp trước và hành trình định mệnh kiếp này.
5. **Trích đoạn tâm đắc (공감 글귀 / Highlight Quote):**
   - Đoạn hội thoại hoặc trích dẫn đắt giá nhất giữa hai nhân vật chính.

---

## 2. NGUYÊN TẮC LƯU TRỮ VÀO DỰ ÁN (STORAGE MAPPING)

Khi cào hoặc thu thập từ link RIDI (hoặc qua search/user cung cấp):

### A. Trong `config.json`:
- **`title`**: Tên truyện dịch thuần Việt mượt mà (tuân thủ Pure Vietnamese Novel Titling Mandate).
- **`korean_title`**: Tên gốc tiếng Hàn (ví dụ: `사냥개는 도망쳤다`).
- **`author`**: Tên tác giả nguyên bản tiếng Hàn kèm phiên âm / RIDI (ví dụ: `리튼 (liteun) / RIDI`).
- **`source_lang`**: `"Korean"`.
- **`ridi_url`**: Lưu đường link gốc RIDI để tiện đối chiếu (ví dụ: `https://ridibooks.com/books/1632014329`).
- **`cover_url`**: **BẮT BUỘC lưu link ảnh bìa gốc chất lượng cao từ CDN của RIDI**:
  - Trích xuất Book ID từ `ridi_url` (ví dụ: `1632014329`).
  - Cấu trúc URL ảnh bìa CDN chuẩn RIDI: `https://img.ridicdn.net/cover/<book_id>/xxlarge` (chất lượng sắc nét nhất).
  - Hoặc nếu người dùng tải ảnh offline: lưu file ảnh đặt tên là `cover.jpg` / `cover.png` / `cover.webp` đặt trực tiếp tại `novel_projects/<slug>/cover.<ext>`.
- **`keywords`**: Mảng danh sách các từ khóa chính dịch sang tiếng Việt kèm từ gốc.
- **`is_completed`**: Luôn mặc định là `false` khi khởi tạo mới (để truyện xuất hiện ngay trong tab chính **"📚 Đang Theo Dõi"**, tuyệt đối không tự ý set `true` làm ẩn vào tab Đã Đọc Xong).
- **`is_dropped`**: Luôn mặc định là `false`.
- **`description`**: **BẮT BUỘC lưu đầy đủ định dạng văn án hoàn chỉnh** (bao gồm Từ khóa, Giới thiệu nhân vật, Tóm tắt tác phẩm và Trích đoạn tâm đắc) theo đúng cấu trúc chuẩn bên dưới để hiển thị trọn vẹn trong Popup Dialog Văn Án của Streamlit.

### B. Trong `AGENTS.md`:
- Cập nhật mục **1. THÔNG TIN CƠ BẢN**: Thêm đầy đủ Tên, Link RIDI, Thể loại, Từ khóa.
- Cập nhật mục **2. THIẾT LẬP NHÂN VẬT & MA TRẬN XƯNG HÔ**: Điền thông tin chi tiết của Công và Thụ từ phần `등장인물`, cố định đại từ xưng hô chuẩn mực.
- Cập nhật mục **3. VĂN ÁN & TRÍCH ĐOẠN ĐẶC SẮC**: Trình bày song ngữ Hàn - Việt (hoặc bản dịch tiếng Việt chau chuốt).

### C. Trong `memory/characters.json` & `memory/relationships.json`:
- Tự động nạp sẵn hồ sơ 2 nhân vật chính (Công & Thụ) được trích xuất từ phần Giới thiệu nhân vật (tên phiên âm, từ khóa tính cách, thân phận, mối quan hệ).

---

## 3. MẪU TRÌNH BÀY VĂN ÁN HOÀN CHỈNH CHO `description` (TEMPLATE)

```text
【TỪ KHÓA TÁC PHẨM】
• Thể loại: [Tây phương huyễn tưởng, Cung đình hầu tước, Trọng sinh phục thù...]
• Công: [Tên Công] - [Đặc điểm, tính cách (ví dụ: Hoàng tử công, Dịu dàng thâm tình công, Yêu thầm công)]
• Thụ: [Tên Thụ] - [Đặc điểm, tính cách (ví dụ: Kỵ sĩ thụ, Mỹ nam thụ, Cơ trí trầm tĩnh thụ, Trùng sinh thụ)]

【GỢI Ý THƯỞNG THỨC】
[Câu trích dẫn 이럴 때 보세요 dịch mượt mà sang tiếng Việt]

【GIỚI THIỆU NHÂN VẬT】
• Công - [Tên Công]: [Mô tả chi tiết xuất thân, thân phận, năng lực và tình cảm dành cho thụ]
• Thụ - [Tên Thụ]: [Mô tả chi tiết quá khứ bi thảm kiếp trước, kế hoạch kiếp này và biến chuyển tình cảm]

【NỘI DUNG TÁC PHẨM】
“[Câu mở đầu ấn tượng của truyện]”

[Đoạn văn trần thuật tóm tắt cốt truyện hoàn chỉnh, giàu cảm xúc, không cắt xén]

【TRÍCH ĐOẠN ĐẮT GIÁ】
“[Trích đoạn hội thoại đặc sắc nhất giữa Công và Thụ]”
```
