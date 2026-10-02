---
name: novel-prescan-extractor
description: >-
  Use this skill to inspect and pre-scan a new raw novel chapter in source.md before translation.
  It extracts new characters, proper nouns, locations, skills, and dialogue pairs, checks against
  memory/ and project AGENTS.md, and produces 2 clean QA clarification tables for user approval.
---

# Novel Pre-Scan & Term Extractor Subagent

## Purpose
Pre-scans the raw chapter (`chapters/ch_xxx/source.md`) before any translation starts. It cross-checks with `memory/characters.json`, `memory/glossary.json`, and project `AGENTS.md` to identify:
1. Unregistered entities (characters, places, skills, terms).
2. Western/English names that must **NOT** be transliterated into Sino-Vietnamese (Hán Việt).
3. Conversational pairs and contextual pronouns.

## Step-by-Step Procedure

1. **Locate Target Chapter & Project Lore**:
   - Chapter source: `novel_projects/<slug>/chapters/ch_xxx/source.md`
   - Memory: `novel_projects/<slug>/memory/characters.json` and `glossary.json`
   - Specific Rules: `novel_projects/<slug>/AGENTS.md` and `config.json`

2. **Entity & Western Name Detection**:
   - Extract all recurring named entities in `source.md`.
   - Check if any entity is a Western/English name (e.g., Alex, Ryan, Friedrich, Felo, Heideman). If yes, mark strictly as **KEEP ENGLISH**.
   - Filter out entities that are already finalized in `memory/glossary.json` or `memory/characters.json`.

3. **Dialogue & Relationship Scan**:
   - Identify interacting character pairs in the chapter.
   - Retrieve current relationship & pronouns from `memory/characters.json` or `memory/relationships.json`.
   - If there is a new relationship or an ambiguous tone (formal vs. casual, intimate vs. hostile), flag it.

4. **Generate QA Clarification Report**:
   Output strictly two tables:

   ### 📋 BẢNG A: Thống nhất Xưng hô & Đối thoại trong chương
   | STT | Cặp nhân vật | Ngữ cảnh trong chương | Đề xuất xưng hô (Tôi - anh / Tôi - cậu...) | Trạng thái / Lựa chọn |
   | :---: | :--- | :--- | :--- | :---: |

   ### 📋 BẢNG B: Thuật ngữ / Thực thể mới xuất hiện
   | STT | Thuật ngữ gốc | Phân loại | Ngữ cảnh xuất hiện | Đề xuất dịch chuẩn | Ghi chú quy tắc |
   | :---: | :--- | :---: | :--- | :--- | :--- |

5. **Stop & Await User Confirmation**:
   - Do NOT begin full translation until the user has confirmed or modified the QA tables.
