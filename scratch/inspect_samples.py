import json

with open('scratch/novels_with_synopsis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Loaded {len(data)} items")
for item in data[:5]:
    print("---")
    print(item['rank'], item['title'])
    print("Associated:", item.get('associated'))
    print("Genres:", ", ".join(item.get('genres', [])))
    print("Synopsis snippet:", item.get('synopsis', '')[:200].replace('\n', ' '))
