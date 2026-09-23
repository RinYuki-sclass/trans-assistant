import json
import sys

with open('scratch/novels_with_synopsis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = []
for i, item in enumerate(data):
    title = item['title']
    rank = item['rank']
    url = item['url']
    assoc = item.get('associated', '').replace('\n', ' ')
    genres = ', '.join(item.get('genres', []))
    synopsis = item.get('synopsis', '').strip()
    
    lines.append(f"### {rank}. [{title}]({url})")
    if assoc:
        lines.append(f"- **Tên gốc / Tên khác:** {assoc}")
    lines.append(f"- **Thể loại:** {genres}")
    lines.append(f"- **Văn án:** {synopsis[:400]}...")
    lines.append("")

with open('scratch/preview_utf8.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Wrote preview_utf8.md successfully")
