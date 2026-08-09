from bs4 import BeautifulSoup

with open('scratch/cherrymist_ch1.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("All elements in main / article:")
main = soup.select_one('main, article, #main, #primary, #content')
if main:
    print(f"Main element: <{main.name} class='{main.get('class')}' id='{main.get('id')}'>")
    for child in main.find_all(True):
        txt = child.get_text(strip=True)
        if len(txt) > 0 and child.name not in ['script', 'style']:
            print(f"  <{child.name} id='{child.get('id')}' class='{child.get('class')}'>: {txt[:80].encode('ascii', 'ignore').decode()}")
else:
    print("No main/article element found!")
