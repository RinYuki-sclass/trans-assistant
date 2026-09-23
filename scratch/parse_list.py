import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/novelupdates_page.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('Title:', soup.title.string if soup.title else '')

# Find all links containing /series/
series_links = soup.find_all('a', href=lambda h: h and 'novelupdates.com/series/' in h)
print('Total series links:', len(series_links))

novels = []
seen = set()
for a in series_links:
    href = a['href']
    if href in seen:
        continue
    seen.add(href)
    title = a.get_text(strip=True)
    if not title:
        # maybe an image inside
        title = a.get('title', '')
    novels.append((title, href, a.parent))

print(f'Unique series count: {len(novels)}')
for i, (title, href, parent) in enumerate(novels):
    print(f'{i+1}. {title} -> {href}')
    # Print parent structure / description
    p_text = parent.get_text(separator=' | ', strip=True)
    print(f'   Parent text: {p_text[:200]}')

pagination = soup.find('div', class_='pagination') or soup.find('div', class_='digg_pagination')
if pagination:
    for a in pagination.find_all('a'):
        print('Page:', a.get('href'), a.get_text(strip=True))
