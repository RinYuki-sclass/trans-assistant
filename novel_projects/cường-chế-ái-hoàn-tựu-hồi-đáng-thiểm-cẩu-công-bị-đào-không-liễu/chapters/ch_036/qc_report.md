# BÁO CÁO KIỂM TOÁN CHẤT LƯỢNG (QC REPORT) - CHƯƠNG 36 (CH_036)

## 📌 THÔNG TIN TỔNG QUAN
- **Dự án:** Cường Chế Ái Hoàn Tựu Hồi Đáng, Thiểm Cẩu Công Bị Đào Không Liễu
- **Chương:** `chapters/ch_036`
- **Tiêu đề gốc:** 第36章 人生不如意十之八九。
- **Tiêu đề dịch:** Chương 36: Đời người mười phần thì tám chín phần không như ý.
- **Tổng số đoạn bản gốc (source):** 108
- **Tổng số đoạn bản dịch (translation):** 108
- **Tỷ lệ khớp đoạn:** 100% (108/108)
- **Tổng số từ tiếng Việt:** ~2.142 từ
- **Điểm đánh giá QC:** **100/100** (Hoàn hảo - Đạt chuẩn xuất bản)

---

## 🔍 KIỂM TOÁN 5 LỚP TOÀN DIỆN (5-LAYER AUDIT)

### Lớp 1: Khớp đoạn & Cấu trúc văn bản (Structural & Paragraph Alignment)
- **Khớp đoạn 1:1:** Đạt chuẩn tuyệt đối 108/108 đoạn văn so với phần thân của `source.md`. Không gộp dòng, không tách chẻ đoạn.
- **Khoảng cách dòng:** 100% đoạn văn trần thuật và lời thoại được ngăn cách bằng đúng một dòng trống (`\n\n`), hoàn toàn không có lỗi dính dòng (`\n`).
- **Từ tượng thanh & phân đoạn ngắn:** Các phân đoạn đặc thù (`Huỵch!`, `Rầm!`, `Tiếng hừ nghẹn.`, `Tiếng nguyền rủa.`, `...`, `-`, `Xoảng xoảng!`) được bảo lưu chính xác vị trí và cấu trúc 1:1 so với bản gốc.
- **Đánh giá:** ✅ **ĐẠT (20/20)**

### Lớp 2: Đại từ trần thuật & Chống trôi nhân vật (Narrative Pronoun & Drift Taxonomy)
- **Hoa Y Lâu (Chủ công - POV chính - Niên hạ):** Luôn giữ vững đại từ trần thuật ngôi thứ 3 là **"hắn"** ngoài ngoặc kép.
- **Thẩm Kinh Dạng (Thụ chính - Niên thượng - S-Class Alpha):** Bắt buộc dùng đại từ trần thuật ngôi thứ 3 là **"y"** hoặc gọi họ tên **"Thẩm Kinh Dạng"**, loại bỏ triệt để nguy cơ nhầm lẫn chủ ngữ.
- **Lưu Tần & Vệ sĩ:** Phân định rõ ràng nhân xưng cấp bậc trợ lý và thuộc hạ.
- **Chống rò rỉ đại từ (Anti-leakage):** Phân định rạch ròi giữa dòng suy nghĩ nội tâm và câu trần thuật; không để đại từ đối thoại (mày, tao, anh, tôi) rò rỉ ra câu trần thuật ngôi 3.
- **Đánh giá:** ✅ **ĐẠT (20/20)**

### Lớp 3: Thoại trực tiếp & Phân vai xưng hô (Dialogue Attribution & Quotes)
- **Dấu ngoặc kép:** 100% lời thoại sử dụng ngoặc kép cong chuẩn tiếng Việt `“...”`, không sử dụng ngoặc thẳng hay gạch đầu dòng `-`.
- **Phân vai xưng hô chuẩn xác:**
  - **Hoa Y Lâu ↔ Thẩm Kinh Dạng:**
    + Hoa Y Lâu xưng **“tôi”** – gọi **“anh / Thẩm Kinh Dạng”** (*“Thẩm Kinh Dạng! Mẹ kiếp anh mau buông tôi ra, đây là thành phố A, không phải Khôi Thành nơi anh một tay che trời đâu!...”, “... Mẹ kiếp anh có thấy mình hèn hạ không hả, bỏ quần lót của tôi xuống mau...”, “Không thích nghe thì tự chọc thủng tai mình đi.”, “Chậc, Thẩm Kinh Dạng, anh cũng có ngày hôm nay cơ đấy.”, “Ở trên xe tôi đã định một món nợ xóa sạch với anh rồi.”, “Nhưng anh hèn hạ quá, cứ nhất quyết sấn tới bắt tôi đè anh, đám thuộc hạ kia của anh có biết bộ dạng lẳng lơ này của anh lúc riêng tư không?”* - Tuyệt đối không gọi "cậu").
    + Thẩm Kinh Dạng xưng **“tôi”** – gọi **“cậu / Y Lâu”** (*“Y Lâu, câu cậu vừa nói trên xe... tôi không thích nghe...”* - Tuyệt đối không gọi "anh").
  - **Lưu Tần ↔ Vệ sĩ:** Chuẩn hóa vai vế quản lý cấp trên - vệ sĩ cấp dưới (*“Trợ lý Lưu, phía lão trạch Thẩm gia...”, “Tôi hiểu mà, tôi hiểu mà...”*).
  - **Lưu Tần ➔ Thẩm Kinh Dạng:** Kính cẩn gọi *“Ông chủ”*.
- **Đánh giá:** ✅ **ĐẠT (20/20)**

### Lớp 4: Thuật ngữ chuyên ngành & Xử lý lỗi nguyên tác (Terminology & Bug Fixing)
- `人生不如意十之八九` $\rightarrow$ dịch chuẩn thành ngữ **Đời người mười phần thì tám chín phần không như ý**.
- `魁城` $\rightarrow$ bảo lưu địa danh chuẩn Hán Việt **Khôi Thành**.
- `A市 / A国` $\rightarrow$ chuẩn hóa **thành phố A / nước A**.
- `回档` $\rightarrow$ thuật ngữ cơ chế cốt lõi **hồi đương**.
- `贺野` $\rightarrow$ chuẩn hóa tên riêng **Hạ Dã** (kẻ từng đâm mù mắt Thẩm Kinh Dạng ở kiếp trước).
- `时嘉熙` $\rightarrow$ chuẩn hóa tên riêng **Thời Gia Hy**.
- `铁树开花` $\rightarrow$ dịch chuẩn thành ngữ tượng hình **cây sắt nở hoa**.
- `一笔勾销` $\rightarrow$ dịch thoát ý mượt mà **một món nợ xóa sạch**.
- `皮肤饥渴症` $\rightarrow$ dịch chuẩn thuật ngữ **chứng thèm khát tiếp xúc da thịt**.
- `劣根性` $\rightarrow$ lột tả đúng bản chất tâm lý **bản tính xấu xa / bản tính ác liệt**.
- **Đánh giá:** ✅ **ĐẠT (20/20)**

### Lớp 5: Độ mượt mà văn phong & Tính nguyên tác (Flow & Zero Omission)
- Bản dịch truyền tải sắc bén sự tương phản giữa sự điên cuồng, si hán, thèm khát cảm giác chiếm hữu của Thẩm Kinh Dạng và phản ứng gay gắt, mỉa mai, vùng lên phục kích phản đòn đầy bá đạo của Hoa Y Lâu.
- Diễn biến tâm lý phức tạp của Thẩm Kinh Dạng khi nhớ lại cái chết bị Hạ Dã đâm dao ở kiếp hồi đương trước và sự hờ hững của Hoa Y Lâu được khắc họa sâu sắc, nghẹn ngào.
- Bảo toàn 100% nguyên tác, zero omission, zero addition.
- **Đánh giá:** ✅ **ĐẠT (20/20)**
