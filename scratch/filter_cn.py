import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/novels_with_synopsis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

han_regex = re.compile(r'[\u4e00-\u9fff]')
korean_regex = re.compile(r'[\uac00-\ud7af]')

cn_novels = []

for item in data:
    assoc = item.get('associated', '')
    rating_str = item.get('rating', '')
    has_han = bool(han_regex.search(assoc))
    has_kr = bool(korean_regex.search(assoc))

    # In NovelUpdates rating_div: span with class "orgcn" or "orgkr"
    # Or in associated names containing Chinese characters
    if has_han or 'CN' in rating_str:
        # Also check if it's purely Korean that happened to have some hanja, but in novelupdates Chinese novels have CN
        if not has_kr or 'CN' in rating_str:
            cn_novels.append(item)

print(f"Total: {len(data)}, Chinese novels: {len(cn_novels)}")

for n in cn_novels:
    print(f"{n['rank']}: {n['title']} --> {n.get('associated', '')}")
