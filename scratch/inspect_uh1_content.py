from bs4 import BeautifulSoup
import re

with open('scratch/uh1_60s.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("1. Searching for all div/article/section/p in uh1_60s.html...")
all_p = soup.find_all('p')
print(f"Total <p> tags: {len(all_p)}")

for i, p in enumerate(all_p):
    txt = p.get_text(strip=True)
    parent_cls = ' '.join(p.parent.get('class') or [])
    parent_id = p.parent.get('id') or ''
    clean_txt = txt[:120].encode('ascii', 'ignore').decode()
    print(f"P[{i}] parent=<{p.parent.name} id='{parent_id}' class='{parent_cls}'> -> {clean_txt}")

print("\n2. Searching for any element containing 'chapter' or 'fictioneer' in id/class:")
for el in soup.find_all(True):
    eid = el.get('id') or ''
    ecls = ' '.join(el.get('class') or [])
    comb = f"{eid} {ecls}".lower()
    if 'chapter' in comb or 'fictioneer' in comb:
        txt = el.get_text(strip=True)
        clean_txt = txt[:100].encode('ascii', 'ignore').decode()
        if len(txt) > 0:
            print(f"  <{el.name} id='{eid}' class='{ecls}'> ({len(txt)} chars) -> {clean_txt}")
