import sys
from bs4 import BeautifulSoup
import json

sys.stdout.reconfigure(encoding='utf-8')

pages = [
    'scratch/novelupdates_page.html',
    'scratch/page2.html',
    'scratch/page3.html'
]

all_novels = []
seen = set()

for page_idx, path in enumerate(pages):
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    boxes = soup.find_all('div', class_='search_main_box_nu')
    print(f'Page {page_idx+1}: {len(boxes)} boxes')

    for box in boxes:
        title_div = box.find('div', class_='search_title')
        if not title_div:
            continue
        a = title_div.find('a')
        if not a:
            continue
        url = a.get('href', '').strip()
        title = a.get_text(strip=True)
        rank_span = title_div.find('span', class_='genre_rank')
        rank = rank_span.get_text(strip=True) if rank_span else ''

        # genres
        genre_div = box.find('div', class_='search_genre')
        genres = [g.get_text(strip=True) for g in genre_div.find_all('a')] if genre_div else []

        # stats
        stats_div = box.find('div', class_='search_stats')
        stats = [s.get_text(strip=True) for s in stats_div.find_all('span')] if stats_div else []

        # ratings & country
        rating_div = box.find('div', class_='search_ratings')
        rating = rating_div.get_text(strip=True) if rating_div else ''

        # user note if any
        note_div = box.find('div', class_=lambda c: c and 'ecuclp' in c)
        note = note_div.get_text(strip=True) if note_div else ''

        if url not in seen:
            seen.add(url)
            all_novels.append({
                'rank': rank,
                'title': title,
                'url': url,
                'rating': rating,
                'genres': genres,
                'stats': stats,
                'note': note
            })

print(f'\nTotal unique novels found: {len(all_novels)}')
with open('scratch/all_novels.json', 'w', encoding='utf-8') as f:
    json.dump(all_novels, f, ensure_ascii=False, indent=2)

for n in all_novels:
    print(f"{n['rank']} {n['title']} -> {n['url']}")
