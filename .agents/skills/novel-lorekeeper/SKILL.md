---
name: novel-lorekeeper
description: >-
  Use this skill to update and maintain the novel project's long-term memory: characters.json,
  glossary.json, relationships.json, and timeline.json after a chapter translation has been QC approved.
---

# Novel Lorekeeper Subagent

## Purpose
Maintains the persistent long-term memory in `novel_projects/<slug>/memory/`. Ensures that character evolutions, new relationships, chapter timelines, and validated glossary entries are accurately appended without duplicate entities.

## File Targets
- `novel_projects/<slug>/memory/characters.json`
- `novel_projects/<slug>/memory/glossary.json`
- `novel_projects/<slug>/memory/relationships.json`
- `novel_projects/<slug>/memory/timeline.json`

## Actions to Perform

1. **Chapter Timeline Summary**:
   - Extract a 2-3 sentence core plot summary of the approved chapter (Who did what? Where are they? Any major injury/power awakening/item acquired?).
   - Append to `timeline.json` with chapter ID and key status tags.

2. **Deduplicated Character Merge**:
   - If a new character appeared or a character gained an alias/title:
   - Check existing names, Sino-Vietnamese names, and aliases in `characters.json` (case-insensitive).
   - Merge rather than duplicate: append new aliases to the existing character record.

3. **Relationship Progress**:
   - If two characters established a new relationship or changed forms of address (e.g. from formal to lovers), record the updated relationship in `relationships.json`.

4. **Glossary Lock**:
   - Mark terms verified in the chapter as locked (`confirmed: true`) in `glossary.json`.
