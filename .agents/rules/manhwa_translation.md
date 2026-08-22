# Manhwa Translation Rules

## 1. Định dạng khối thoại (Default Tag Format)
- Mặc định sử dụng `[]` (thay vì `[Khung thoại]` hay `[TAG]`):
  ```text
  []
  KR: <Nội dung tiếng Hàn trên 1 dòng>
  <Nội dung tiếng Việt trên 1 dòng>
  ```

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
  - YR ↔ Han Yoojin (YJ): Tôi/Bọn mình – Chú/Ahjussi.
  - YR ↔ Han Yoohyun (YH): Tôi – Anh (*Hội trưởng / Han Yoohyun*). YH gọi YR: Tôi – Cô (*Park Yerim*).
  - YR ↔ Sung Hyunjae (HJ): Cháu – Chú (*chú Hội trưởng / ngài Hội trưởng*).
- **Song Taewon (TW) ↔ Han Yoojin (YJ):** Tôi – Cậu (TW gọi YJ: *Han Yoojin-ssi*) & Tôi – Anh (YJ gọi TW).
- **Yoo Myungwoo (YMW):** Độc thoại tự xưng "Tôi".
