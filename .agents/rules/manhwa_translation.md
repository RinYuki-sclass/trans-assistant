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

## 2. Quy tắc Dấu câu (Tối thượng - Punctuation Matching & Question Mark Mandate)
- **Đảm bảo số lượng và vị trí các dấu câu** (`!`, `!!`, `?`, `?!`, `~`, `~!!`, `.`, `…`, `….`, `,`, ngoặc kép `' '`) ở câu dịch tiếng Việt khớp với câu tiếng Hàn (KR).
- Nếu dòng KR không có dấu kết thúc câu (ví dụ câu lửng hoặc thoại hét không chấm) thì dòng VI cơ bản cũng không đặt dấu kết thúc.
- **QUY TẮC BỔ SUNG DẤU HỎI CHẤM CHO CÂU HỎI (QUESTION MARK MANDATE):**
  - Trong tiếng Hàn, rất nhiều câu thoại mang tính chất hỏi, nghi vấn, dò hỏi, thắc mắc (dùng đuôi `~나`, `~가`, `~ㄹ까`, `~냐`, `~니`, `~어/아`, `~죠`, `~는지`, `~할지`, v.v.) nhưng tác giả chỉ đặt dấu chấm `.`, dấu lửng `…` hoặc không đặt dấu.
  - **Quy tắc bắt buộc:** Nếu bản gốc (raw KR) không có dấu `?`, nhưng **câu dịch tiếng Việt mang nghĩa là một câu hỏi / câu nghi vấn thì BẮT BUỘC PHẢI KẾT THÚC ĐUÔI BẰNG DẤU `?`** (hoặc `?!` nếu mang sắc thái kinh ngạc / cảm thán). Tuyệt đối không để câu hỏi kết thúc bằng dấu chấm `.` hay câu trần thuật cụt lủn.

## 3. Quy tắc Kính ngữ & Tính Lịch sự (Honorifics & Politeness)
- **Đuôi `요`:** Không nhất thiết phải luôn chêm từ "ạ"; dùng câu văn tự nhiên, mượt mà và đúng ngữ cảnh.
- **Đuôi `했습니까`, `하십니까`, `하십시오`, `드리다`:** Thêm đầy đủ chủ ngữ - vị ngữ và sử dụng từ ngữ trang trọng, lịch thiệp (ví dụ: *xin mời, xin nhờ, kính chào, dùng bữa, có sao không, v.v.*) để thể hiện sự lịch sự thay vì chỉ thêm "ạ".

## 4. Hậu tố xưng hô sau tên riêng (Name Suffixes)
- **BẮT BUỘC giữ nguyên các hậu tố xưng hô sau tên riêng (TUYỆT ĐỐI KHÔNG VIỆT HÓA THÀNH "...à / ...ơi"):**
  - `-아` / `-야` -> `-ah` / `-yah`:
    - `유현아` -> **LUÔN CHỐT LÀ `Yoohyun-ah`** (CẤM dịch thành *"Yoohyun à"*, *"Yoohyun ơi"*).
    - `예림아` -> **LUÔN CHỐT LÀ `Yerim-ah`** (CẤM dịch thành *"Yerim à"*, *"Yerim ơi"*).
    - `유진아` -> **LUÔN CHỐT LÀ `Yoojin-ah`** (CẤM dịch thành *"Yoojin à"*, *"Yoojin ơi"*).
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
    - **Đại từ tự xưng của Yerim:** Yerim **BẮT BUỘC tự xưng là "Tôi"** (hoặc "Bọn mình" khi nói chung), **TUYỆT ĐỐI KHÔNG dùng "em" hay "cháu"** với Yoojin.
    - **Yoojin gọi Yerim:** Yoojin **BẮT BUỘC gọi Yerim là "nhóc"** (hoặc gọi tên *Yerim-ah*), **TUYỆT ĐỐI KHÔNG BAO GIỜ XÀI "em"**.
    - **Sắc thái lời thoại & Kính ngữ:** Khi nói chuyện với Yoojin, **bỏ hoàn toàn chữ "ạ"**, dùng ngữ điệu tự nhiên, thoải mái, thân mật ngang hàng (như bạn bè / người thân trong nhà: *"...à?", "...đấy", "...mà"*).
    - **Danh xưng gọi Yoojin (`아저씨`):** Dùng linh hoạt giữa **"Ahjussi"** và **"chú"**:
      - Khi gọi giật giọng, gọi như tên riêng / đứng đầu câu cảm thán gọi đích danh: dùng **"Ahjussi"** (ví dụ: `아저씨! 이거 봐요` -> *“Ahjussi! Nhìn cái này này”*).
      - Khi nằm ở giữa câu hoặc trong câu trần thuật: dùng **"chú"** (ví dụ: *“Tôi đã bảo với chú rồi mà”*).
      - **CHỈ DÙNG khi bản gốc KR có nhắc đến `아저씨`:** Tuyệt đối không tự ý thêm "chú" / "Ahjussi" nếu raw không có (ví dụ: `저기 봐요!` -> *“Nhìn đằng kia kìa!”*, KHÔNG dịch *“Xem kìa chú”*).
  - YR ↔ Han Yoohyun (YH): Tôi – Anh (*Hội trưởng / Han Yoohyun*). YH gọi YR: Tôi – Cô (*Park Yerim*).
  - YR ↔ Sung Hyunjae (HJ): Cháu – Chú (*chú Hội trưởng / ngài Hội trưởng*).
  - YR ↔ Iwahata Gakuto: Tôi – Anh (Yerim gọi Gakuto: *tôi - anh*). Gakuto gọi YR: Tôi – Cô (*Gakuto xưng tôi/ta, gọi Yerim là cô*).
- **Song Taewon (TW) ↔ Han Yoojin (YJ):** Tôi – Cậu (TW gọi YJ: *Han Yoojin-ssi*) & Tôi – Anh (YJ gọi TW).
- **Yoo Myungwoo (YMW):** Độc thoại tự xưng "Tôi".
- **Shishio (Amaterasu):**
  - Gọi nhóm Yoojin là **“các cậu”** (TUYỆT ĐỐI KHÔNG dùng *"các ngươi"*).
  - Cấp dưới thuộc hạ (Iwahata Gakuto, Quân sư...) gọi Shishio: **“Shishio đại nhân”** (`시시오 님` -> **Shishio đại nhân**, không dùng "ngài Shishio" hay "Shishio-sama").

## 6. Quy chuẩn Thứ tự Text nhỏ & Ngữ điệu Đối thoại Manhwa
- **Thứ tự Text nhỏ / Viết tay (Floating & Handwritten Texts):**
  - Luôn quét và xếp thứ tự đọc hợp lý theo bố cục khung tranh (từ trên xuống dưới, theo ngữ cảnh hội thoại).
  - Text nhỏ phụ họa, lẩm bẩm (ví dụ: `그래서 사자왕인가?`, `형 괜찮아?`) phải đặt đúng diễn biến trước/sau bóng thoại chính, không ngắt đôi luồng suy nghĩ độc thoại của nhân vật khác.
- **Quy tắc chống lặp đuôi cảm thán:**
  - Hạn chế tối đa việc lặp lại các đuôi cảm thán như *"sao"*, *"hả"*, *"mà"*, *"á"*.
  - **Cấm kỵ:** Không dùng cùng 1 đuôi cảm thán trong 2 câu liên tiếp. Đa dạng hóa câu thoại tự nhiên (*...thế nào?*, *...chứ!*, *...chăng?!*, *...đấy à?*, *...phải không?*).
- **Quy tắc chống lặp từ `참다` (Đa dạng hóa vốn từ nhẫn nại / chịu đựng):**
  - Khi bản gốc tiếng Hàn dùng lặp lại nhiều biến thể của động từ `참다` (`참으며`, `참고`, `참지 않아도`, `참는`...) trong cùng một phân cảnh tâm lý, **TUYỆT ĐỐI KHÔNG dịch rập khuôn thành một từ "chịu đựng" liên tục**.
  - Bắt buộc khai thác vốn từ phong phú, giàu cảm xúc của tiếng Việt theo từng sắc thái:
    - Sự hy sinh, gánh vác: *“cắn răng cam chịu biết bao thiệt thòi”*.
    - Nội tâm dồn nén, u uất: *“cứ nén lòng, cứ nhẫn nhịn, cắn răng nuốt bao cay đắng”*.
    - Lời an ủi xoa dịu, giải phóng gánh nặng: *“không cần phải gồng mình nén nhịn nữa đâu”*.
    - Sự chờ đợi kiên nhẫn: *“kiên nhẫn chờ đợi / nhẫn nại”*.
- **Văn phong tự nhiên & Sắc thái biểu cảm:**
  - Chuyển ngữ mượt mà theo văn nói, tránh dịch thô hoặc làm trầm trọng hóa cảm xúc (ví dụ: `당황스럽네` thể hiện sự bối rối, dở khóc dở cười $\rightarrow$ dịch nhẹ nhàng *“Bối rối thật đấy...”*, không dịch gay gắt như *"Đúng là cạn lời với tên..."*).
  - Cảnh tương tác anh em Yoojin - Yoohyun mang sắc thái cưng chiều, bất lực đời thường hài hước, không dịch gắt gỏng căng thẳng.
- **Chuẩn hóa Thuật ngữ:**
  - `화염뿔사자` (Linh thú sư tử lửa 1 sừng của Yoojin / Shishio) $\rightarrow$ Chốt thống nhất duy nhất là **“Độc Giác Hỏa Sư”** (không dùng Hỏa Giác Sư hay Hỏa Sư).
  - `경기장` (Sân đấu / Đấu trường trong giải đấu Thợ săn) $\rightarrow$ Chốt thống nhất là **“võ đài”** (không dùng sân đấu, sân thi đấu hay sân vận động).
  - `던전` (Dungeon) $\rightarrow$ Chốt thống nhất là **“ngục tối”** (không dùng hầm ngục).
  - `물의 지배자` (Danh hiệu của Park Yerim) $\rightarrow$ Chốt thống nhất là **“Kẻ Trị Thủy”** (không dùng Thống Trị Làn Nước hay Chúa Tể Của Nước).
  - `게이트석` (Gate Stone) $\rightarrow$ Chốt thống nhất là **“Môn thạch”** (theo glossary.md dòng 478, không dùng đá cổng hay đá cổng dịch chuyển).
  - `그림자 없는 낮` (Shadowless Day - Kỹ năng cấp SS của Yerim) $\rightarrow$ Chốt thống nhất là **“Vô Ảnh Nhật”** (theo glossary.md dòng 583, không dùng Bạch Nhật Vô Ảnh).
- **Quy chuẩn Danh từ Chuẩn Xác & Chống Ghép Từ Ngô Nghê (Natural Noun Mandate):**
  - **Tuyệt đối cấm dịch ghép từ máy móc (Morpheme-by-morpheme):** Không tự tiện ghép từng chữ tiếng Hàn tạo ra các danh từ không có trong tiếng Việt đời thường.
  - **Kiến trúc & Nhà cửa:**
    - `가벽` (假壁): BẮT BUỘC dịch là **“vách ngăn”** hoặc **“bức vách”** (vách ngăn phòng/thạch cao). TUYỆT ĐỐI KHÔNG dịch là *"tường ngăn"* hay *"tường giả"*.
    - `지지대` (trong ngữ cảnh chịu lực/chống sụp đổ tâm lý): Dịch chuẩn xác là **“trụ đỡ”** hoặc **“điểm tựa vững chắc”** (không dùng *"chỗ dựa"* chung chung hay *"giá đỡ"* cơ học).
  - **Trang phục & Đời sống:**
    - `옷 깃 방향` (Yukata/Kimono): Dịch thoát ý chuẩn văn hóa **“vạt áo bị cài ngược bên”** (khép vạt trái đè lên vạt phải). TUYỆT ĐỐI KHÔNG dịch *"hướng vạt áo"*.
    - `허리끈` (Yukata/đồ truyền thống): Dịch là **“đai lưng”** hoặc **“thắt lưng”**. TUYỆT ĐỐI KHÔNG dịch là *"dây đai áo"*.
    - `양복`: Ưu tiên dịch tự nhiên là **“bộ vest”** thay vì lạm dụng từ cổ cứng nhắc *"bộ âu phục"*.
  - **Kinh tế & Giao thương Thợ săn:**
    - `길드` (Guild): BẮT BUỘC chốt thống nhất thành **“công hội”** hoặc **“hội”** (TUYỆT ĐỐI CẤM dùng *"bang hội"*).
    - `길드 독점`: Dịch là **“các hội lớn độc quyền”** (không dùng *"bang hội độc chiếm"*).
    - `던전을 걸고`: Dịch là **“đặt cược các ngục tối”** (không dịch thành *"tiền cược là các ngục tối"* vì dungeon không phải tiền tệ).
  - **Quy tắc Bỏ Toàn Bộ SFX (Zero SFX Mandate):**
    - Trong kịch bản dịch manhwa (`script.txt`), **LƯỢC BỎ HOÀN TOÀN TẤT CẢ KHỐI SFX** (không đưa các tiếng động như `콰앙`, `챙`, `쿵`, `촥`, `덜컥`, `슈우우` vào script). File kịch bản chỉ lưu trữ lời thoại nhân vật, dẫn chuyện/thuyết minh và độc thoại nội tâm để phục vụ trực tiếp cho Photoshop Type Tool và Web Streamlit.
  - **Kiểm duyệt & Meta gag (Phá vỡ bức tường thứ 4):**
    - `심의` (審議 - trong các cảnh che chắn nhân vật nhạy cảm): Nhận diện đúng **`심의`** là **“quy chuẩn kiểm duyệt”** (hoặc *tiêu chuẩn kiểm duyệt / thuần phong mỹ tục*). TUYỆT ĐỐI KHÔNG nhầm OCR thành `샘의` (*suối nguồn*).
- **Đối chiếu người nói qua thị giác (Speaker Attribution):**
  - Luôn quan sát kỹ nhân vật mở miệng, cử chỉ và phụ kiện trong khung hình để không nhầm lẫn nhân vật (chú ý phân biệt: Noah tóc vàng nhút nhát $\neq$ Kang Soyoung; Han Yoojin chủ trì $\neq$ Moon Hyuna nâng ly rượu).

## 7. Quy tắc thực thi từ Coding Agent (Zero Google API Key Mandate)
- **Tự thân OCR & Dịch trực tiếp:** Khi người dùng yêu cầu Coding Agent xử lý ảnh manhwa, Agent tự đọc ảnh và dịch trực tiếp bằng năng lực multimodal in-context.
- **Nghiêm cấm gọi Google API Key:** Tuyệt đối không chạy script Python trung gian gọi API ngoài qua `GEMINI_API_KEY` hay Google GenAI để tránh lỗi 429 quota và 503 high demand.
