from bs4 import BeautifulSoup

with open('scratch/cherrymist_ch1.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('All elements with text > 200 chars:')
for el in soup.find_all(True):
    txt = el.get_text(strip=True)
    if len(txt) > 200:
        cls = ' '.join(el.get('class') or [])
        eid = el.get('id') or ''
        # check if this element is a leaf-ish container (doesn't contain huge children that are body/html)
        if el.name not in ['html', 'body', 'div', 'main']:
            print(f"  <{el.name} id='{eid}' class='{cls}'> ({len(txt)} chars)")
        elif any(k in f"{eid} {cls}".lower() for k in ['chapter', 'content', 'story', 'entry', 'text', 'fictioneer']):
            print(f"  Container <{el.name} id='{eid}' class='{cls}'> ({len(txt)} chars)")
