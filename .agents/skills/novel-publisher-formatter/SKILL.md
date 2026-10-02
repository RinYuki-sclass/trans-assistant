---
name: novel-publisher-formatter
description: >-
  Use this skill to clean, format, and prepare the final Vietnamese novel chapter for publishing
  (removing raw tags, normalizing typography and spacing '\n\n', generating meta.json and social post templates).
---

# Novel Publisher & Formatter Subagent

## Purpose
Post-processes the finalized translation, stripping raw foreign text if present, standardizing typography, creating chapter metadata (`meta.json`), and formulating social media release announcements.

## Procedures

1. **Clean Vietnamese Extraction**:
   - If the file is interlinear (`KR: ...` / `VI: ...` or `CN: ...` / `VI: ...`), remove all foreign language tags and keep only the refined Vietnamese lines.
   - Ensure every paragraph has exactly one intervening blank line (`\n\n`).
   - Clean up leading/trailing spaces and normalize dialogue dashes (`-` or `—`).

2. **Generate Chapter Metadata (`meta.json`)**:
   - Write to `novel_projects/<slug>/chapters/ch_xxx/meta.json`:
     ```json
     {
       "chapter_id": "ch_xxx",
       "word_count": 2450,
       "paragraph_count": 86,
       "status": "published",
       "updated_at": "YYYY-MM-DDTHH:mm:ss"
     }
     ```

3. **Generate Social Post Template**:
   - Create a ready-to-copy social post template for Facebook/Discord:
     ```text
     [Tên Truyện] — Chương [X]: [Tên Chương nếu có]
     Link đọc: https://...
     ________________________________________
     Bản dịch thuộc về nhóm dịch. Vui lòng không reup! (´｡• ᵕ •｡`)
     ```
