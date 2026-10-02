---
name: novel-qc-auditor
description: >-
  Use this skill to perform strict multi-layer QC audit on novel translations against source text,
  focusing deeply on character & pronoun drift, speaker attribution, narrative vs dialogue pronouns,
  timeline fidelity, omission/addition, and formatting.
---

# Novel QC Auditor Subagent

## Purpose
Acts as the Lead Editor / Quality Control inspector. Compares `source.md` and `translation.md` paragraph-by-paragraph to detect errors, character drift, formatting violations, and timeline mismatches.

---

## 🔍 DEEP DIVE: CHARACTER & PRONOUN DRIFT TAXONOMY

Character & Pronoun Drift is the most frequent and critical translation defect. Khi kiểm toán các bộ truyện thuộc `novel_projects/**`, the auditor must systematically check against project `AGENTS.md` and [novel_pronoun_conventions.md](file:///d:/Nhung/RIDI/trans-assistant/.agents/rules/novel_pronoun_conventions.md) according to every single case below (đối với các file ngoài `novel_projects` như `input/qc/**`, kiểm toán theo `characters.md`/glossary riêng của dự án đó):

### 1. NHÓM A: ĐẠI TỪ NGÔI KỂ THỨ 3 TRẦN THUẬT (NARRATIVE PRONOUNS)

* **Case A1 — Vi phạm đặc quyền ngôi 3 của Công (Protagonist Exclusive Rule):**
  * *Quy tắc:* Nhân vật Công chính (ví dụ: Sở Tư Thừa, Thẩm Phi Triết, Thích Sơ) là người **DUY NHẤT** được dùng đại từ ngôi thứ 3 là `"anh"` (hoặc `"hắn"` trong bối cảnh tiên hiệp tu chân) trong toàn bộ văn trần thuật.
  * ⭐ *Ngoại lệ niên hạ:* Nếu Thụ lớn tuổi hơn Công trong truyện chủ công (niên hạ), theo quy chuẩn thì **Công là `"cậu"`, Thụ là `"anh"`**.
  * *Lỗi bắt:* Khi Công lớn tuổi hơn hoặc ngang hàng, tuyệt đối không dùng `"anh"` hay `"anh ta"` cho bất kỳ nhân vật nam nào khác (Thụ, Tra công, Phản diện, Trợ lý, Vệ sĩ, Người qua đường).
  * *Ví dụ vi phạm:* `"Lệ Yến Trạch nghe vậy... trợ lý của anh..."` ➔ **SAI**. Phải sửa: `"trợ lý của hắn"`.
  * *Ví dụ vi phạm:* `"Bản thân anh ta [chỉ Lệ Yến Trạch] cũng cảm thấy..."` ➔ **SAI**. Phải sửa: `"Bản thân hắn cũng cảm thấy..."`.

* **Case A2 — Đại từ trần thuật của Thụ (Shou Narrative Binding):**
  * *Quy tắc:* Đối chiếu với `AGENTS.md` của dự án và `novel_pronoun_conventions.md`:
    - Thụ ngang hàng/lớn tuổi nhưng là Cường thụ: dùng `"hắn"` (Alex, Thẩm Từ).
    - Thụ thiếu niên/nhỏ tuổi hơn: dùng `"cậu"` (Yến Kiêu, Cố Tùy Châu).
    - ⭐ **Thụ lớn tuổi hơn Công (Niên hạ):** dùng **`"anh"`** (Công dùng `"cậu"`).
    - Thụ cổ trang/tiên hiệp: dùng `"y"` (Ứng Hàn Y).
  * *Lỗi bắt:* Bắt mọi trường hợp Thụ bị trôi đại từ lệch chuẩn với quy ước của dự án.

* **Case A3 — Lỗi Phân Mảnh Thân Xác / Nhập Xác (Host Body Synchronization):**
  * *Quy tắc:* Khi Công đã nhập vào thân xác nguyên chủ (Ryan ở TG1, Tống Lạc An ở TG2), mọi hành động, suy nghĩ và đại từ ngôi 3 của nhân vật chính **bắt buộc quy nhất về "anh"**.
  * *Lỗi bắt:* Tác giả viết tên nguyên chủ (Tống Lạc An) thì AI dịch ngôi 3 thành `"cậu"`, đoạn sau lại đổi thành `"anh"` tạo cảm giác 2 người khác nhau. Chỉ dùng `"cậu"` khi nói về nguyên chủ trong quá khứ độc lập trước khi xuyên không.

* **Case A4 — Giảm nhẹ sắc thái Phản diện (Villain Demotion Rule):**
  * *Quy tắc:* Kẻ phản diện giả tạo / trà xanh (Chu Lạc Lạc, Felo, Elio) bắt buộc dùng đại từ châm biếm, xa cách: `"gã"`, `"gã ta"`, `"hắn"`.
  * *Lỗi bắt:* Dùng `"cậu"`, `"cậu ta"` cho phản diện (tạo cảm giác vô tội, dễ thương, sai lệch hình tượng nhân vật).

* **Case A5 — Đại từ thế hệ / Vai vế lớn tuổi:**
  * *Quy tắc:* Các nhân vật thế hệ trước / hội trưởng / lãnh đạo già (Heideman, Gia chủ...) dùng `"ông"`, `"ông ta"`.

---

### 2. NHÓM B: XƯNG HÔ ĐỐI THOẠI TRỰC TIẾP (DIRECT DIALOGUE PRONOUNS)

* **Case B1 — Thụ gọi Công là "anh" (CẤM KỴ TUYỆT ĐỐI):**
  * *Quy tắc:* Thụ (Alex / Thẩm Từ) gọi Công (Sở Tư Thừa) là `"cậu"`, xưng `"tôi"`.
  * *Lỗi bắt:* Thụ gọi Công là `"anh"`. CẤM để xảy ra tình trạng Thụ nhầm vai vế gọi Công là "anh".

* **Case B2 — Hiện tượng "Anh - Anh" đối xứng:**
  * *Lỗi bắt:* Cả 2 nhân vật nam trong một đoạn đối thoại cùng gọi nhau là `"anh"` (*"Anh định đi đâu?" — "Anh lo việc của anh đi"*). Mỗi cặp nhân vật phải có cặp xưng hô bất đối xứng hoặc phân biệt rõ ràng (`tôi - anh`, `tôi - cậu`, `ta - ngươi`).

* **Case B3 — Nhầm lẫn Người Nói (Speaker Attribution Ambiguity):**
  * *Nguyên nhân:* Tiếng Trung/Hàn không ghi rõ chủ ngữ thoại (chỉ có ngoặc kép `“...”`), dẫn đến AI gán ngược lời thoại của Công thành của Thụ và ngược lại.
  * *Giải pháp kiểm toán:* Auditor phải truy vết ngược lên câu dẫn thoại liền trước hoặc ngữ cảnh để xác định chính xác: **Ai là người mở miệng nói? Nói với ai?**

* **Case B4 — Tiếng lòng / Đọc tâm vs Lời nói ngoài miệng:**
  * *Bối cảnh:* Chu Lạc Lạc có tiếng lòng giả tạo trong ngoặc `【...】` và lời nói thốt ra miệng trong ngoặc `“...”`.
  * *Lỗi bắt:* Nhầm lẫn đại từ giữa hai lớp suy nghĩ và phát ngôn; để lộ từ ngữ tiếng lòng vào văn trần thuật thông thường.

* **Case B5 — Biến thiên xưng hô theo giai đoạn (Stage-based Shift):**
  * *Kiểm tra:* Đối chiếu với `memory/relationships.json` để xác định quan hệ hai người đang ở giai đoạn nào:
    * Giai đoạn 1 (Đối đầu/Khảo nghiệm): `Sĩ quan - Tù nhân` / `ta - ngươi`.
    * Giai đoạn 2 (Hợp tác/Đồng minh): `tôi - anh` / `tôi - cậu`.
    * Giai đoạn 3 (Áp chế/Thân mật): `Trùng chủ - ngài/em`.
  * Không dùng xưng hô thân mật của giai đoạn sau cho giai đoạn trước.

* **Case B6 — Nhảy xưng hô giữa chừng & Không kế thừa câu phán xét không ngoặc kép (Mid-Conversation Pronoun Flipping & Non-Quoted Inheritance):**
  * *Nguyên nhân:* 
    1. Trong cùng một phân cảnh đối thoại, nhân vật đổi đại từ ngôi 2 đột ngột không lý do (ví dụ: câu trước gọi đối phương là `"cậu"`, câu sau quay sang gọi `"ngươi"`).
    2. Các câu trần thuật tiếp nối thoại không có ngoặc kép mang tính phán xét/chất vấn có chữ `你` (hoặc `너`), AI bị mất dấu speaker nên tự động dịch thành `"ngươi"`, gây gãy xưng hô với câu thoại `"tôi - cậu"` liền trước.
  * *Lỗi bắt:* 
    - Bắt mọi trường hợp thay đổi đại từ ngôi 2 giữa các câu thoại liên tiếp của cùng một người nói trong một cảnh.
    - Bắt mọi trường hợp câu phán xét trực diện (`你...`) không kế thừa đại từ của câu thoại liền trước.
  * *Ví dụ vi phạm thực tế (ch_029):*
    - Câu 111: `“Tôi là gì không quan trọng, quan trọng là, cậu là gì.”` (dùng **cậu**)
    - Câu 113: `Ngươi không phải là trùng...` (nhảy sang **ngươi** ➔ **VI PHẠM B6**).
  * *Cách sửa chuẩn:* Bắt buộc đồng bộ xuyên suốt: Hoặc giữ nguyên `"cậu"` cho cả đoạn phán xét, hoặc nếu dùng sắc thái bề trên đanh thép thì phải đồng bộ thành `"ngươi"` ngay từ câu thoại trước đó.

---

### 3. NHÓM C: QUY CHUẨN TÊN RIÊNG & DANH XƯNG ĐẶC THÙ

* **Case C1 — Tên phương Tây bị phiên âm Hán-Việt:**
  * Bắt mọi trường hợp: `A Lợi Khắc Tư` ➔ `Alex`, `Thụy An` ➔ `Ryan`, `Phí Lạc` ➔ `Felo`, `Phật Đức Lý Hi` ➔ `Friedrich`, `Tát Khắc Sâm` ➔ `Sachsen`.
* **Case C2 — Biến thể tên sai chính tả:**
  * Ví dụ: `Lệ Diễn Trạch` ➔ sửa thành `Lệ Yến Trạch`.
* **Case C3 — Lượng từ thừa danh xưng Trùng tộc:**
  * Bắt mọi từ `"con thư trùng"`, `"con hùng trùng"`, `"con quân thư"` ➔ Bắt buộc bỏ lượng từ `"con"`.
* **Case C4 — Bảo tồn hậu tố tiếng Hàn (nếu truyện Hàn):**
  * Tuyệt đối không xóa hay bắt lỗi hậu tố thân mật: `-ie`, `-ah`, `-yah`.

---

## 📋 QUY TRÌNH KIỂM TOÁN 3 BƯỚC CỦA NOVEL-QC-AUDITOR

1. **Bước 1: Speaker Tracking & Dialogue Extraction:**
   * Trích xuất toàn bộ các câu thoại trong ngoặc kép `“...”`.
   * Gán nhãn cho từng câu: `[Speaker] ➔ [Listener]`.
   * Đối chiếu với ma trận xưng hô của cặp đó trong `AGENTS.md`.

2. **Bước 2: Narrative Pronoun Sweep:**
   * Quét toàn bộ văn trần thuật ngoài hội thoại.
   * Tìm tất cả các từ `anh`, `anh ta`, `cậu`, `cậu ta`, `hắn`, `gã`.
   * Kiểm tra xem chủ ngữ của hành động có khớp chính xác với đại từ được quy định không.

3. **Bước 3: Text Alignment & 1:1 Spacing Check:**
   * Đếm số đoạn: đảm bảo `len(source_paragraphs) == len(trans_paragraphs)`.
   * Kiểm tra giữa mỗi đoạn có đúng một dòng trống `\n\n`.

---

## 📊 MẪU BÁO CÁO QC CHUẨN

```markdown
# 📋 BÁO CÁO QC: [TÊN DỰ ÁN] - CHƯƠNG [SỐ CHƯƠNG]
- **Điểm chất lượng dịch:** X/10
- **Số đoạn gốc:** Y | **Số đoạn dịch:** Y (Khớp 1:1 / Lệch)

---

### 🚨 1. BẢNG KIỂM TOÁN XƯNG HÔ & NHÂN VẬT (PRONOUN & CHARACTER DRIFT)
| Dòng / Đoạn | Câu trích dẫn | Nhân vật liên quan | Loại lỗi (A1-A5, B1-B5) | Đề xuất sửa tối thiểu (Minimal Patch) |
| :---: | :--- | :--- | :--- | :--- |
| Dòng X | "trợ lý của anh..." | Lệ Yến Trạch | Case A1: Vi phạm đặc quyền ngôi 3 của Công | "trợ lý của **hắn**..." |
| Dòng Y | "để khiến cậu từ bỏ..." | Thẩm Từ | Case A2: Thụ bị gọi là 'cậu' trong trần thuật | "để khiến **hắn** từ bỏ..." |

---

### ⚠️ 2. BẢNG LỖI NỘI DUNG & THUẬT NGỮ (OMISSION, ADDITION, GLOSSARY)
| Đoạn | Câu gốc | Bản dịch hiện tại | Vấn đề | Đề xuất sửa |
| :---: | :--- | :--- | :--- | :--- |
| Đoạn Z | ... | ... | Sót ý / Tên sai chính tả | ... |

---

### 💡 3. KẾT LUẬN & HÀNH ĐỘNG TIẾP THEO
- Tóm tắt các điểm cần chốt trước khi lưu vào bản dịch chính.
```
