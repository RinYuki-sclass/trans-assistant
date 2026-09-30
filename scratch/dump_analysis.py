import json
import glob
import os

files = sorted(glob.glob('d:/Nhung/RIDI/trans-assistant/novel_projects/*khi*/chapters/*/analysis.json'))

out_lines = []

for p in files:
    ch = os.path.basename(os.path.dirname(p))
    out_lines.append(f"\n==================== {ch} ====================")
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    out_lines.append(f"--- SUMMARY ---:\n{data.get('chapter_summary', '')}\n")
    
    out_lines.append("--- CHARACTERS ---:")
    for c in data.get('new_characters', []):
        out_lines.append(f"  {c.get('original')} -> {c.get('suggested')} (Hán-Việt: {c.get('hanviet')}) | Vai trò: {c.get('role')} | Giới tính: {c.get('gender')} | Xưng hô: {c.get('pronoun')} | Mô tả: {c.get('description')}")
        
    out_lines.append("--- LOCATIONS ---:")
    for loc in data.get('new_locations', []):
        out_lines.append(f"  {loc.get('original')} -> {loc.get('suggested')} (Hán-Việt: {loc.get('hanviet')}) | Loại: {loc.get('category')}")
        
    out_lines.append("--- TERMS ---:")
    for t in data.get('new_terms', []):
        out_lines.append(f"  {t.get('original')} -> {t.get('suggested')} (Hán-Việt: {t.get('hanviet')}) | Loại: {t.get('category')}")

    out_lines.append("--- AMBIGUOUS ---:")
    for amb in data.get('ambiguous', []):
        out_lines.append(f"  [{amb.get('id')}] {amb.get('original')} -> {amb.get('suggested')} | Hỏi: {amb.get('question')} | Options: {amb.get('options')}")

with open('d:/Nhung/RIDI/trans-assistant/scratch/full_analysis_dump.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))

print("Dumped successfully, total lines:", len(out_lines))
