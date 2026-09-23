import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/novels_with_synopsis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, item in enumerate(data):
    title = item['title']
    rank = item['rank']
    url = item['url']
    assoc = item.get('associated', '').replace('\n', ' ')
    genres = ', '.join(item.get('genres', []))
    synopsis = item.get('synopsis', '').strip()
    
    print(f"### {rank}. [{title}]({url})")
    if assoc:
        print(f"- **Tên gốc / Tên khác:** {assoc}")
    print(f"- **Thể loại:** {genres}")
    print(f"- **Văn án:** {synopsis[:300]}...")
    print()
