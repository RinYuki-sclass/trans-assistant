---
name: novel-orchestrator
description: >-
  Master coordinator for novel projects. It inspects the chapter state (source.md, QA status,
  translation.md, QC report, memory updates), routes tasks automatically to the appropriate novel
  skill (novel-prescan-extractor, novel-chunk-translator, novel-qc-auditor, novel-lorekeeper,
  novel-publisher-formatter), and seamlessly manages the end-to-end translation pipeline.
---

# Novel Pipeline Orchestrator Subagent

## Purpose
Acts as the central conductor for all novel translation projects in `novel_projects/`. Instead of requiring the user to remember and manually invoke individual subagents, the Orchestrator inspects the current progress of any given chapter, automatically coordinates the 4-Phase Translation Pipeline with Phrase-by-Phrase Scene Pronoun Locking, and seamlessly transitions between workflow stages.

---

## 🏛️ QUY TRÌNH DỊCH 4-PHASE TIÊU CHUẨN (ÁP DỤNG TOÀN BỘ NOVEL_PROJECTS)

Toàn bộ các bộ truyện thuộc `novel_projects/**` đều được xử lý theo 4 Phase chuẩn hóa nhằm phòng chống triệt để sai lệch đại từ và xưng hô giữa nhân vật chính và phụ:

```mermaid
graph TD
    subgraph PHASE 1: PRE-SCAN & SCENE PHRASE MAPPING
        Raw["source.md (Raw Text)"] --> Sub1["🕵️ Subagent 1: Scene & Speaker Mapper"]
        Sub1 --> QA["qa_clarifications.md\n(Bảng Xưng hô + Thuật ngữ mới)"]
        Sub1 --> SceneMap["phrase_scene_map.json\n(Bản đồ phân cảnh & Khóa xưng hô)"]
    end

    subgraph PHASE 2: PHRASE-LOCKED CHUNK TRANSLATION
        SceneMap --> Sub2["✍️ Subagent 2: Phrase Chunk Translator"]
        Raw --> Sub2
        Sub2 --> Chunk1["Phrase 1 (Scene A: Đoạn 1 - 35)"]
        Sub2 --> Chunk2["Phrase 2 (Scene B: Đoạn 36 - 70)"]
        Sub2 --> Chunk3["Phrase 3 (Scene C: Đoạn 71 - Hết)"]
        Chunk1 & Chunk2 & Chunk3 --> Draft["translation_draft.md\n(Khớp 1:1, chuẩn \\n\\n)"]
    end

    subgraph PHASE 3: PRONOUN GATEKEEPER & QC AUDIT
        Draft --> Sub3["🛡️ Subagent 3: Multi-Layer Pronoun QC Auditor"]
        Sub3 --> Patch["Tự động vá lỗi đại từ & lệch speaker"]
        Patch --> CleanTrans["translation.md (Bản dịch chuẩn 100%)"]
        Sub3 --> QCReport["qc_report.md"]
    end

    subgraph PHASE 4: LOREKEEPER & PUBLISHING
        CleanTrans --> Sub4["📦 Subagent 4: Lorekeeper & Publisher"]
        Sub4 --> MemSync["Cập nhật characters.json & timeline.json"]
        Sub4 --> PubReady["meta.json + Format sạch sẵn sàng đăng"]
    end
```

---

## 🧭 State Machine & Automatic Routing Decision Table

Khi được yêu cầu xử lý một chương (ví dụ `ch_xxx` trong dự án `<slug>`), Orchestrator kiểm tra các file trong `novel_projects/<slug>/chapters/ch_xxx/`:

| Hiện trạng thư mục chương (`ch_xxx`) | Trạng thái | Phase tương ứng | Kỹ năng kích hoạt | Hành động của Orchestrator |
| :--- | :--- | :--- | :--- | :--- |
| Thiếu `source.md` hoặc rỗng | `EMPTY_NEEDS_SOURCE` | Phase 0 | *(Không)* | Nhắc người dùng nạp file raw vào `chapters/ch_xxx/source.md`. |
| Có `source.md`, chưa có `qa_clarifications.md` | `NEEDS_PRESCAN` | **PHASE 1** | **`novel-prescan-extractor`** | 1. Quét raw, tạo Bảng A (xưng hô) & Bảng B (thuật ngữ).<br>2. Phân chia phrase/scene, bóc tách speaker và xuất `phrase_scene_map.json`. |
| Đã duyệt QA, chưa có `translation.md` | `NEEDS_TRANSLATION` | **PHASE 2** | **`novel-chunk-translator`** | Nạp `phrase_scene_map.json` và quy chuẩn `AGENTS.md`. Dịch tuần tự theo từng Phrase/Scene-Chunk để khóa cứng đại từ, ghép thành bản dịch 1:1 với khoảng cách `\n\n`. |
| Đã có `translation.md`, chưa có `qc_report.md` | `NEEDS_QC` | **PHASE 3** | **`novel-qc-auditor`** | Áp dụng Bộ quét 5 Lớp (5-Layer Pronoun Filter) đối soát nguyên tác, bắt lỗi trôi đại từ, speaker attribution và tự động áp bản vá (patch). |
| Đã duyệt QC, chưa cập nhật Memory | `NEEDS_POST_PROCESS` | **PHASE 4** | **`novel-lorekeeper`** & **`novel-publisher-formatter`** | Cập nhật `timeline.json`, đồng bộ `characters.json`, chuẩn hóa typography và xuất `meta.json`. |
| Đầy đủ tất cả files | `COMPLETED` | Đã xong | **`novel-publisher-formatter`** | Báo cáo chương đã hoàn thiện 100%, sẵn sàng xuất bản WordPress. |

---

## 🧩 CHI TIẾT CƠ CHẾ PHRASE-BY-PHRASE SCENE LOCKING

Để loại bỏ hoàn toàn tình trạng trôi đại từ (Pronoun Drift) khi dịch một chương dài:
1. **Phân chia Phrase/Scene-Chunk:** Mỗi chương được chia thành các Phrase (25 - 40 đoạn) theo phân cảnh tự nhiên.
2. **Khóa cứng cặp xưng hô (Scene Pronoun Locking):** Mỗi Phrase có một bộ quy tắc xưng hô riêng biệt:
   - **Niên hạ (Đổi Thụ Arc 3):** Công nhỏ tuổi = `cậu` (xưng tôi/mày, gọi anh); Thụ lớn tuổi = `anh / hắn` (xưng tôi, gọi cậu/em).
   - **Hiện đại / Đô thị (Thụ Trà Xanh, Showbiz):** Công = `anh`; Thụ = `cậu`.
   - **Cổ trang / Tiên hiệp (Đại Ma Đầu):** Công = `hắn`; Thụ = `y` *(Tuyệt đối cấm dùng anh - cậu)*.
   - **Tinh tế / Cường-Cường (Khi Đại Lão):** Công = `anh`; Thụ = `hắn`.
   - **Phản diện / Trà xanh:** Luôn dùng `gã / tên đó / cậu ta`.
   - **Nhân vật phụ lớn tuổi:** Luôn dùng `ông / bà / bác`.
   - **Nhân vật phụ nữ:** Luôn dùng `cô ấy / nàng / thị`.

---

## 🛠️ Operating Modes

### 1. Smart Interactive Mode (Mặc định - Khuyên dùng)
Orchestrator tự động thực hiện từng bước, nhưng chủ động dừng lại ở **2 trạm kiểm soát then chốt (Checkpoints)**:
- **Trạm 1:** Dừng sau Phase 1 khi lập xong 2 bảng QA & Phân cảnh để người dùng duyệt xưng hô và thuật ngữ mới.
- **Trạm 2:** Dừng sau Phase 3 khi lập báo cáo QC để người dùng duyệt các điểm vá xưng hô trước khi ghi vào bộ nhớ dài hạn.

### 2. Fast Batch Mode (Chế độ tự động một chạm)
Khi người dùng ra lệnh: *"Dịch tự động chương 53 bộ khi-đại-lão từ đầu đến cuối"*:
- Orchestrator tự động áp dụng các quy chuẩn mặc định từ `AGENTS.md` và `memory/` sẵn có.
- Tuần tự chạy mượt mà qua cả 4 Phase mà không cần can thiệp thủ công.

---

## ⛔ QUY TẮC BẮT BUỘC (UNIVERSAL ZERO GOOGLE API KEY MANDATE)
- Toàn bộ 4 Phase đều do AI Code Agent tự thân đọc, phân tích, dịch, audit và ghi file trực tiếp trong workspace.
- Tuyệt đối KHÔNG chạy script ngoài gọi qua `GEMINI_API_KEY` hay `GOOGLE_API_KEY`.�� áp dụng patch tối thiểu ➔ Cập nhật Memory ➔ Trích xuất bản dịch sạch.

---

## How to Invoke the Orchestrator

Người dùng chỉ cần nhắn một câu tự nhiên:
- `"Orchestrator: tiếp tục xử lý chapter 53 bộ khi-đại-lão-phản-diện..."`
- `"Orchestrator: kiểm tra tiến độ và chạy tiếp các chương đang dở"`
- `"Orchestrator: chạy pipeline đầy đủ cho ch_053"`

Orchestrator sẽ tự kiểm tra trạng thái và tự động gọi đúng skill tương ứng mà bạn không cần phải chỉ định thủ công tên từng subagent.
