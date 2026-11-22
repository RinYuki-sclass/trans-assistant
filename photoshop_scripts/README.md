# 🎨 BỘ TOOL PHOTOSHOP AI TYPESET (VFX AUTO-STYLER)
> Giải pháp tự động hóa trích xuất hiệu ứng chữ (Gradient, Stroke, Outer Glow, Drop Shadow) từ bản raw Manhwa/Webtoon sang Text Layer tiếng Việt trong Photoshop bằng **Gemini Vision AI Engine**.

---

## 📁 1. Cấu trúc thư mục

Khi copy sang máy tính khác, bạn chỉ cần mang theo toàn bộ thư mục `photoshop_scripts/` gồm các file sau:

```text
photoshop_scripts/
├── install_to_photoshop.bat     # File cài đặt tự động 1-click cho Windows
├── install.ps1                  # Script PowerShell quét và copy file vào Photoshop
├── AutoStyleFromSelection.jsx   # Script gán phím F6: Xử lý 1 chữ/khung thoại đơn lẻ
├── BatchStyleFromSelection.jsx  # Script gán phím F7: Xử lý Multi-Select Style hàng loạt layer
├── BatchAutoCenterAndFit.jsx    # Script gán phím F8: Tự động canh giữa & fit Font Size theo raw
├── BatchAutoCenter.jsx          # Script: Tự động canh giữa hàng loạt (giữ nguyên cỡ chữ của user)
├── BatchCleanBubbles.jsx        # Script gán phím F9: Tự động Batch Clean bóng thoại, loại trừ 100% SFX
├── style_analyzer.py            # AI Engine phân tích đơn lẻ (F6)
├── batch_analyzer.py            # AI Engine phân tích hàng loạt song song (F7)
├── layout_analyzer.py           # ComicText & Typeset Engine (F8)
├── bubble_cleaner.py            # AI Speech Bubble Cleaner & SFX Filter (F9)
└── README.md                    # Hướng dẫn cài đặt và sử dụng
```

---

## ⚙️ 2. Yêu cầu môi trường trên PC mới

### A. Cài đặt Python & Thư viện
1. Máy tính cần cài sẵn **Python 3.9 trở lên** (Tải tại [python.org](https://www.python.org/) - nhớ tích chọn `"Add python.exe to PATH"` khi cài).
2. Mở Command Prompt (`cmd`) hoặc PowerShell trên máy mới và chạy lệnh cài đặt thư viện cần thiết:
   ```bash
   pip install pillow numpy python-dotenv google-genai
   ```

### B. Cấu hình Gemini API Key (Miễn phí 100%)
1. Mở file `.env` nằm ở thư mục gốc của project (hoặc tạo file `.env` cùng cấp với script).
2. Điền API Key của Google Gemini vào:
   ```ini
   GEMINI_API_KEY_1="AIzaSyYourKeyHere..."
   ```
   > 💡 *Nếu chưa có API Key, truy cập [aistudio.google.com](https://aistudio.google.com/) $\rightarrow$ Bấm **Get API key** $\rightarrow$ **Create API key** (Miễn phí vĩnh viễn, không cần thẻ tín dụng, hạn mức 1.500 lượt/ngày).*

---

## 🚀 3. Hướng dẫn Cài đặt vào Photoshop trên PC mới

### Cách 1: Cài đặt tự động 1-Click (Khuyến nghị)
1. Nhấp đúp chuột vào file **`install_to_photoshop.bat`**.
2. Công cụ sẽ tự động quét Registry và các ổ đĩa `C:`, `D:` để tìm tất cả phiên bản Photoshop (CC 2020 $\rightarrow$ 2027) và copy trọn bộ script vào thư mục `Presets\Scripts\` của Photoshop.
3. Khi màn hình hiện thông báo xanh `[V] ĐÃ CÀI ĐẶT THÀNH CÔNG!` là xong.

### Cách 2: Cài đặt thủ công (Nếu file bat không tìm thấy đường dẫn)
Copy toàn bộ 4 file:
- `AutoStyleFromSelection.jsx`
- `BatchStyleFromSelection.jsx`
- `style_analyzer.py`
- `batch_analyzer.py`

Dán vào thư mục Scripts của Photoshop:
* `C:\Program Files\Adobe\Adobe Photoshop [Phiên bản]\Presets\Scripts\`
* *(Hoặc đường dẫn tùy chỉnh của máy bạn, ví dụ: `D:\Creative cloud\Adobe Photoshop [Phiên bản]\Presets\Scripts\`)*

---

## ⌨️ 4. Gán phím tắt F6, F7 và F8 trong Photoshop (Chỉ làm 1 lần)

1. **Khởi động lại Photoshop** (để Photoshop nạp các script mới).
2. Nhấn tổ hợp phím: **`Ctrl + Alt + Shift + K`** (Keyboard Shortcuts).
3. Tại dòng **Shortcuts For**, chọn: **Application Menus**.
4. Mở rộng mục **File** $\rightarrow$ mở rộng tiếp mục **Scripts**:
   * Tìm dòng **`AutoStyleFromSelection`** $\rightarrow$ Bấm phím **`F6`** $\rightarrow$ Bấm **Accept**.
   * Tìm dòng **`BatchStyleFromSelection`** $\rightarrow$ Bấm phím **`F7`** $\rightarrow$ Bấm **Accept**.
   * Tìm dòng **`BatchAutoCenterAndFit`** $\rightarrow$ Bấm phím **`F8`** $\rightarrow$ Bấm **Accept**.
   * Tìm dòng **`BatchCleanBubbles`** $\rightarrow$ Bấm phím **`F9`** $\rightarrow$ Bấm **Accept**.
5. Nhấn **OK** để lưu lại.

---

## 📖 5. Bố cục file PSD chuẩn khi Typeset

Để tool nhận diện chính xác 100% layer chữ và bản raw, bảng Layers của bạn nên tuân thủ bố cục 3 lớp tiêu chuẩn:

* **`Group 1`** *(Thư mục trên cùng)*: Chứa toàn bộ các Text Layer tiếng Việt do bạn gõ.
* **`raw`** *(Layer ở giữa)*: Bản scan gốc tiếng Hàn (chứa chữ raw để AI lấy mẫu).
* **`Background`** *(Layer dưới cùng)*: Bản tranh đã được redraw/clean sạch chữ.

---

## 🎯 6. Hướng dẫn sử dụng thực tế

### 📌 Phím `F6`: Xử lý 1 khung thoại / SFX đơn lẻ
* **Khi nào dùng?** Khi bạn đang gõ từng câu và muốn xem kết quả ngay.
* **Thao tác**:
  1. Gõ text tiếng Việt đặt vào vị trí.
  2. Bấm phím **`M`** (Marquee Tool) hoặc **`L`** (Lasso) khoanh 1 chữ tiếng Hàn trên bản raw.
  3. Bấm **`F6`** $\rightarrow$ Xong trong 0.8 giây!

---

### 📌 Phím `F7`: Multi-Select Batch hàng loạt (Nhiều Style khác nhau)
* **Khi nào dùng?** Khi trên trang tranh có nhiều khung thoại với các style khác nhau (câu chữ Vàng phát sáng Glow, câu chữ Đỏ rượu, câu chữ Tím viền trắng...).
* **Thao tác**:
  1. Bạn cứ gõ xong tất cả các câu thoại tiếng Việt trên trang và đặt vào đúng vị trí của nó.
  2. Trên bảng Layers, bạn **giữ phím `Ctrl` click chọn nhiều Text Layer** (hoặc chọn thẳng cả thư mục `Group 1`).
  3. Bấm **`F7`** *(Không cần dùng chuột khoanh)*:
     - Script tự động đo vị trí từng câu tiếng Việt $\rightarrow$ Tự soi xuống bản raw bên dưới.
     - AI Vision chạy đa luồng phân tích song song toàn bộ các vùng crop.
     - Tự động áp riêng biệt từng style tương ứng vào từng layer!

### 📌 Phím `F8`: Tự động Canh Giữa & Fit Cỡ Chữ (Batch Auto-Center & Fit)
* **Khi nào dùng?** Sau khi bạn gõ xong các câu thoại tiếng Việt, câu thì quá dài tràn bóng thoại, câu thì bị lệch khỏi tâm bóng thoại, cần căn giữa và thu phóng vừa vặn toàn bộ.
* **Thao tác**:
  1. Trên bảng Layers, bạn **giữ phím `Ctrl` click chọn nhiều Text Layer** (hoặc chọn thẳng cả thư mục `Group 1`).
  2. Bấm **`F8`**:
     - Script tự động đo vị trí và chụp vùng bóng thoại trên layer `raw` bên dưới.
     - **Gemini Vision AI Engine** trực tiếp soi tranh, phán đoán chính xác tâm thị giác đối xứng (Center X, Y) và nhận diện các bóng thoại kép/liên hoàn.
     - Tự động:
       1. Set **Center Justification** (căn giữa từng dòng).
       2. Tự điều chỉnh **Font Size** chuẩn tỷ lệ vàng theo chữ Raw của tác giả.
       3. Tự động **dịch chuyển Text Layer** về khớp 100% tâm bóng thoại!

---

## 🛠️ 7. Xử lý sự cố thường gặp (Troubleshooting)

1. **Bấm F6/F7 không thấy phản hồi hoặc báo lỗi python**:
   - Kiểm tra xem máy mới đã cài Python chưa bằng lệnh `python --version` trong cmd.
   - Đảm bảo đã chạy lệnh `pip install pillow numpy python-dotenv google-genai`.
2. **Không thấy script trong menu Keyboard Shortcuts**:
   - Hãy tắt hẳn Photoshop và mở lại để Photoshop nạp lại danh sách script mới từ thư mục `Presets\Scripts`.
3. **Chữ bị đè viền đen sai lệch**:
   - Đảm bảo text tiếng Việt của bạn nằm bên trong thư mục có tên là **`Group 1`** để script tự động ẩn tạm thời khi lấy mẫu.
