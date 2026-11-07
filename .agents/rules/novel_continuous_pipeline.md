---
description: "QUY CHUẨN TỰ HÀNH LIÊN HOÀN (AUTONOMOUS CONTINUOUS PIPELINE) - Không dừng chờ duyệt giữa các batch / phrase trong novel projects"
globs: "novel_projects/**"
alwaysApply: true
---

# 🚀 QUY CHUẨN WORKFLOW TỰ HÀNH LIÊN HOÀN (AUTONOMOUS NOVEL TRANSLATION PIPELINE)

Quy tắc này áp dụng cho toàn bộ hoạt động dịch thuật, kiểm toán và xử lý tiểu thuyết trong `novel_projects/**`.

---

## 1. NGUYÊN TẮC VẬN HÀNH "ZERO-WAIT" (KHÔNG DỪNG CHỜ DUYỆT THỦ CÔNG)

Khi người dùng ra lệnh dịch truyện (*"dịch tiếp", "chạy đi", "chạy batch", "dịch liên hoàn từ ch_X đến ch_Y", "tiếp tục"*):
1. **Tuyệt đối không dừng lại giữa chừng:**
   - ❌ **CẤM:** Không dừng lại sau Phase 1 để bắt người dùng duyệt bảng `qa_clarifications.md`.
   - ❌ **CẤM:** Không dừng lại sau mỗi Phrase trong chương để hỏi *"Có dịch tiếp phrase 2 không?"*.
   - ❌ **CẤM:** Không dừng lại sau Phase 3 để bắt người dùng bấm duyệt `qc_report.md`.
   - ❌ **CẤM:** Không dừng lại giữa các chương trong cùng một Batch.

2. **Cơ chế Tự Động Hóa Toàn Trình:**
   - **Auto Pre-scan:** Tự động đối chiếu `memory/characters.json` và quy chuẩn `AGENTS.md`. Nếu phát hiện nhân vật hoặc thuật ngữ mới, Agent **tự động nội suy (Auto-Inference)** theo bối cảnh truyện, ghi vào `qa_clarifications.md` với cờ `[AUTO-INFERRED]` và chuyển ngay sang Phase 2.
   - **Continuous Translation:** Dịch tuần tự các Phrase (Phrase 1 $\rightarrow$ N) trong một lượt xử lý, khóa cứng xưng hô phân cảnh, bảo toàn 1:1 số đoạn văn, chuẩn khoảng cách dòng `\n\n`, lưu trực tiếp vào `chapters/ch_xxx/translation.md`.
   - **Auto-QC & Self-Healing:** Tự động chạy kiểm toán 5 lớp. Nếu phát hiện lệch đại từ trôi hoặc định dạng, **tự động áp bản vá (Self-Healing)** trực tiếp vào `translation.md`, cập nhật `meta.json` (`qc_approved: true`) và tạo `qc_report.md`.
   - **Lorekeeper & Auto-Advance:** Tự động cập nhật `timeline.json`, đồng bộ `chapters_index.json` và `TOC.md`. Ngay sau khi xong một chương, **tự động nạp chương kế tiếp** trong dải batch mà không dừng lại chờ người dùng gõ lệnh.

---

## 2. CIRCUIT BREAKER (CHỈ DỪNG DUY NHẤT KHI GẶP LỖI BẤT THƯỜNG CHÍ MẠNG)

Agent CHỈ ĐƯỢC PHÉP tạm dừng quy trình tự hành và báo cáo người dùng trong 3 tình huống bất khả kháng sau:
1. **Lệch số đoạn nghiêm trọng:** Sau khi tự kiểm tra và cân chỉnh, `abs(len(source) - len(trans)) > 3` đoạn.
2. **Hỏng file nguồn:** File `chapters/ch_xxx/source.md` bị thiếu hoặc hoàn toàn rỗng (0 bytes).
3. **Mâu thuẫn định danh nhân vật chí mạng:** Nhân vật phản diện trùng 100% tên nhân vật chính trong cùng bối cảnh mà Agent không thể suy luận được chủ thể phát ngôn/hành động.

---

## 3. QUẢN LÝ CONTEXT WINDOW & TIẾN ĐỘ TINH GỌN (TOKEN-EFFICIENT LOGGING)

Để duy trì hiệu suất context lớn mà không bị nghẽn token khi dịch liên tục nhiều chương:
- Sau mỗi chương hoàn thành, chỉ ghi log 1 dòng tóm tắt:
  ```text
  ✅ [PASS] ch_xxx: 120/120 đoạn (1:1) | QC 100% | Timeline Updated
  🚀 [NEXT] Bắt đầu xử lý ch_xxx+1...
  ```
- Không in toàn bộ văn bản dịch dài dòng ra màn hình chat; toàn bộ bản dịch sạch được ghi trực tiếp vào file `translation.md`.
