import httpx

headers = {'User-Agent': 'Mozilla/5.0'}

api_urls = [
    'https://cherrymist.cafe/wp-json/wp/v2/fcn_chapter?slug=uh-1',
    'https://cherrymist.cafe/wp-json/wp/v2/posts?slug=uh-1',
    'https://cherrymist.cafe/wp-json/fictioneer/v1/chapters?slug=uh-1',
]

with httpx.Client(headers=headers, timeout=20, follow_redirects=True) as client:
    for url in api_urls:
        try:
            r = client.get(url)
            print(f"API: {url} -> Status: {r.status_code}")
            if r.status_code == 200:
                data = r.json()
                print(f"   Data type: {type(data)}, len: {len(data) if isinstance(data, list) else len(data.keys())}")
                if isinstance(data, list) and data:
                    item = data[0]
                    print(f"   Keys: {list(item.keys())}")
                    if 'content' in item:
                        c_rendered = item['content'].get('rendered', '')
                        print(f"   Content rendered len: {len(c_rendered)}")
        except Exception as e:
            print(f"API Error {url}: {e}")
