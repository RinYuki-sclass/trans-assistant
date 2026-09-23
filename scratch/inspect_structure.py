import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/novelupdates_page.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find the main container of reading list
container = soup.find('div', class_='w-blog-content') or soup.find('div', class_='l-content')
print('Container tag:', container.name if container else 'None')

# Look for items with class or table
items = soup.find_all('div', class_=lambda c: c and ('rl_item' in c or 'reading_list' in c or 'my-list' in c or 'search_main_box_nu' in c or 'search_body_nu' in c))
print('Items by class count:', len(items))

# Let's inspect elements containing '# |'
hash_spans = soup.find_all(lambda el: el.string and el.string.strip() == '#' or (el.get_text() and '# |' in el.get_text()))
print('Hash elements count:', len(hash_spans))

# Let's inspect the exact HTML around the first item
first_a = soup.find('a', href=lambda h: h and 'i-became-the-main-top' in h)
if first_a:
    curr = first_a
    for _ in range(5):
        curr = curr.parent
        print('--- PARENT LEVEL ---', curr.name, curr.get('class'))
    print('Parent HTML snippet:\n', curr.prettify()[:1000])
