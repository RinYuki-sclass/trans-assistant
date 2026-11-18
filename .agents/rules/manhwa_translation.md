# Manhwa Translation Rules

## 1. Định dạng khối thoại (Default Tag Format)
- Định dạng chuẩn bắt buộc nhận diện người nói / người dẫn chuyện `[Người nói/narrator]`:
  ```text
  [Người nói/narrator]
  KR: <Nội dung tiếng Hàn trên 1 dòng>
  <Nội dung tiếng Việt trên 1 dòng>
  ```
- **Quy tắc gán nhãn người nói (Visual Speaker Attribution):**
  - Nhìn hướng đuôi bong bóng thoại và nhân vật đang nói trong tranh để gán tên tương ứng (ví dụ: `[Han Yoojin]`, `[Han Yoohyun]`, `[Sung Hyunjae]`, `[Park Yerim]`, v.v.).
  - Khung chữ nhật dẫn chuyện, thuyết minh bối cảnh, suy nghĩ độc thoại nền: `[Narrator]` hoặc `[Độc thoại]`.
  - Hiệu ứng âm thanh quan trọng tới cốt truyện: `[SFX]`.
  - Nhân vật phụ / quần chúng: `[Dân chúng]`, `[Thợ săn]` hoặc `[Người qua đường]`.
  - Trường hợp không rõ nguồn phát ngôn: để mặc định `[Bóng thoại]`.

## 2. Quy tắc Dấu câu (Tối thượng - Punctuation Matching)
- **Đảm bảo số lượng và vị trí các dấu câu** (`!`, `!!`, `?`, `?!`, `~`, `~!!`, `.`, `…`, `….`, `,`, ngoặc kép `' '`) ở câu dịch tiếng Việt khớp tuyệt đối với câu tiếng Hàn (KR).
- Nếu dòng KR không có dấu kết thúc câu (ví dụ câu lửng hoặc thoại hét không chấm) thì dòng VI cũng không đặt dấu kết thúc.

## 3. Quy tắc Kính ngữ & Tính Lịch sự (Honorifics & Politeness)
- **Đuôi `요`:** Không nhất thiết phải luôn chêm từ "ạ"; dùng câu văn tự nhiên, mượt mà và đúng ngữ cảnh.
- **Đuôi `했습니까`, `하십니까`, `하십시오`, `드리다`:** Thêm đầy đủ chủ ngữ - vị ngữ và sử dụng từ ngữ trang trọng, lịch thiệp (ví dụ: *xin mời, xin nhờ, kính chào, dùng bữa, có sao không, v.v.*) để thể hiện sự lịch sự thay vì chỉ thêm "ạ".

## 4. Hậu tố xưng hô sau tên riêng (Name Suffixes)
- Giữ nguyên các hậu tố xưng hô sau tên riêng:
  - `-아` / `-야` -> `-ah` / `-yah` (ví dụ: `유현아` -> `Yoohyun-ah`, `예림아` -> `Yerim-ah`, `유진아` -> `Yoojin-ah`).
  - `-씨` -> `-ssi` (ví dụ: `성현제 씨` -> `Sung Hyunjae-ssi`, `성모 씨` -> `Sungmo-ssi`, `한유진 씨` -> `Han Yoojin-ssi`).
  - `-군` -> `-gun` (ví dụ: `한유진 군` -> `Han Yoojin-gun`).
  - `-양` -> `-yang` (ví dụ: `리에트 양` -> `Liette-yang`).

## 5. Quy tắc Xưng hô (Pronouns & Nuances)
- **Từ `형` (Hyung):** Khi Han Yoohyun gọi Han Yoojin là `형`, giữ nguyên là `Hyung` (không dịch thành "anh").
- **Han Yoojin (YJ) ↔ Han Yoohyun (YH):** Anh – Em (*Yoohyun-ah / em trai của anh*). YH xưng với YJ: Em – Hyung / Anh.
- **Sung Hyunjae (HJ) ↔ Han Yoojin (YJ):**
  - HJ gọi YJ: Tôi – Cậu (*Han Yoojin-gun*).
  - YJ gọi HJ: Tôi – Anh (*Sung Hyunjae-ssi / Sungmo-ssi*).
- **Park Yerim (YR):**
  - **YR ↔ Han Yoojin (YJ):**
    - **Đại từ tự xưng:** Yerim **BẮT BUỘC tự xưng là "Tôi"** (hoặc "Bọn mình" khi nói chung), **TUYỆT ĐỐI KHÔNG dùng "cháu"** với Yoojin.
    - **Danh xưng gọi Yoojin (`아저씨`):** Dùng linh hoạt giữa **"Ahjussi"** và **"chú"**:
      - Khi gọi giật giọng, gọi như tên riêng / đứng đầu câu cảm thán gọi đích danh: dùng **"Ahjussi"** (ví dụ: `아저씨! 이거 봐요` -> *“Ahjussi! Nhìn cái này này”*).
      - Khi nằm ở giữa câu hoặc trong câu trần thuật: dùng **"chú"** (ví dụ: *“Tôi đã bảo với chú rồi mà”*).
      - **CHỈ DÙNG khi bản gốc KR có nhắc đến `아저씨`:** Tuyệt đối không tự ý thêm "chú" / "Ahjussi" nếu raw không có (ví dụ: `저기 봐요!` -> *“Nhìn đằng kia kìa!”*, KHÔNG dịch *“Xem kìa chú”*).
  - YR ↔ Han Yoohyun (YH): Tôi – Anh (*Hội trưởng / Han Yoohyun*). YH gọi YR: Tôi – Cô (*Park Yerim*).
  - YR ↔ Sung Hyunjae (HJ): Cháu – Chú (*chú Hội trưởng / ngài Hội trưởng*).
- **Song Taewon (TW) ↔ Han Yoojin (YJ):** Tôi – Cậu (TW gọi YJ: *Han Yoojin-ssi*) & Tôi – Anh (YJ gọi TW).
- **Yoo Myungwoo (YMW):** Độc thoại tự xưng "Tôi".
- **Shishio (Amaterasu):** Gọi nhóm Yoojin là **“các cậu”** (TUYỆT ĐỐI KHÔNG dùng *"các ngươi"*).

## 6. Quy chuẩn Thứ tự Text nhỏ & Ngữ điệu Đối thoại Manhwa
- **Thứ tự Text nhỏ / Viết tay (Floating & Handwritten Texts):**
  - Luôn quét và xếp thứ tự đọc hợp lý theo bố cục khung tranh (từ trên xuống dưới, theo ngữ cảnh hội thoại).
  - Text nhỏ phụ họa, lẩm bẩm (ví dụ: `그래서 사자왕인가?`, `형 괜찮아?`) phải đặt đúng diễn biến trước/sau bóng thoại chính, không ngắt đôi luồng suy nghĩ độc thoại của nhân vật khác.
- **Quy tắc chống lặp đuôi cảm thán:**
  - Hạn chế tối đa việc lặp lại các đuôi cảm thán như *"sao"*, *"hả"*, *"mà"*, *"á"*.
  - **Cấm kỵ:** Không dùng cùng 1 đuôi cảm thán trong 2 câu liên tiếp. Đa dạng hóa câu thoại tự nhiên (*...thế nào?*, *...chứ!*, *...chăng?!*, *...đấy à?*, *...phải không?*).
- **Văn phong tự nhiên & Sắc thái biểu cảm:**
  - Chuyển ngữ mượt mà theo văn nói, tránh dịch thô hoặc làm trầm trọng hóa cảm xúc (ví dụ: `당황스럽네` thể hiện sự bối rối, dở khóc dở cười $\rightarrow$ dịch nhẹ nhàng *“Bối rối thật đấy...”*, không dịch gay gắt như *"Đúng là cạn lời với tên..."*).
  - Cảnh tương tác anh em Yoojin - Yoohyun mang sắc thái cưng chiều, bất lực đời thường hài hước, không dịch gắt gỏng căng thẳng.
- **Chuẩn hóa Thuật ngữ:**
  - `화염뿔사자` (Linh thú sư tử lửa 1 sừng của Yoojin / Shishio) $\rightarrow$ Chốt thống nhất duy nhất là **“Độc Giác Hỏa Sư”** (không dùng Hỏa Giác Sư hay Hỏa Sư).
- **Đối chiếu người nói qua thị giác (Speaker Attribution):**
  - Luôn quan sát kỹ nhân vật mở miệng, cử chỉ và phụ kiện trong khung hình để không nhầm lẫn nhân vật (chú ý phân biệt: Noah tóc vàng nhút nhát $\neq$ Kang Soyoung; Han Yoojin chủ trì $\neq$ Moon Hyuna nâng ly rượu).

## 7. Quy tắc thực thi từ Coding Agent (Zero Google API Key Mandate)
- **Tự thân OCR & Dịch trực tiếp:** Khi người dùng yêu cầu Coding Agent xử lý ảnh manhwa, Agent tự đọc ảnh và dịch trực tiếp bằng năng lực multimodal in-context.
- **Nghiêm cấm gọi Google API Key:** Tuyệt đối không chạy script Python trung gian gọi API ngoài qua `GEMINI_API_KEY` hay Google GenAI để tránh lỗi 429 quota và 503 high demand.
