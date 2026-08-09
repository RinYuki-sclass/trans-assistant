from bs4 import BeautifulSoup
import httpx
import re

with open('scratch/uh1_60s.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

js_urls = []
for s in soup.find_all('script', src=True):
    src = s['src']
    if 'fictioneer' in src or 'theme' in src or 'plugin' in src:
        js_urls.append(src)

print(f"Found {len(js_urls)} relevant JS script files:")
for u in js_urls:
    print("  -", u)

headers = {'User-Agent': 'Mozilla/5.0'}
with httpx.Client(headers=headers, timeout=15, follow_redirects=True) as client:
    for u in js_urls[:10]:
        try:
            r = client.get(u)
            if r.status_code == 200:
                actions = re.findall(r'action\s*:\s*[\"\']([^\"\']+)[\"\']', r.text)
                if actions:
                    print(f"JS [{u.split('/')[-1]}] actions found: {set(actions)}")
                
                # Search for fetch or $.ajax in JS file
                ajax_matches = re.findall(r'(?:ajax|fetch|post)\s*\([^)]*\)', r.text, re.IGNORECASE)
                if ajax_matches:
                    print(f"JS [{u.split('/')[-1]}] ajax calls count: {len(ajax_matches)}")
                    for m in ajax_matches[:5]:
                        print("    -", m[:100].encode('ascii', 'ignore').decode())
        except Exception as e:
            print(f"Error fetching {u}: {e}")
