from bs4 import BeautifulSoup
import re

with open('scratch/cherrymist_ch1.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("1. Searching for all elements with class or id containing chapter, content, story, text, entry, fictioneer:")
matching_tags = []
for tag in soup.find_all(['div', 'article', 'section', 'main']):
    id_str = tag.get('id') or ''
    cls_str = ' '.join(tag.get('class') or [])
    combined = f"{id_str} {cls_str}".lower()
    txt = tag.get_text(strip=True)
    if any(k in combined for k in ['chapter', 'content', 'story', 'text', 'entry', 'fictioneer', 'post', 'main', 'body', 'formatting']):
        matching_tags.append((tag.name, id_str, cls_str, len(txt), txt[:80].encode('ascii', 'ignore').decode()))

# Sort by length of text inside container descending
matching_tags.sort(key=lambda x: x[3], reverse=True)

for name, eid, cls, length, preview in matching_tags[:25]:
    print(f"  <{name} id='{eid}' class='{cls}'> ({length} chars) -> {preview}")
