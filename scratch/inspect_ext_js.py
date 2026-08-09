import httpx

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://cherrymist.cafe/wp-content/plugins/fictioneer-extended/public/build/assets/app-BV97l_1z.js?ver=2.0.0-beta6'
with httpx.Client(headers=headers, timeout=15) as client:
    r = client.get(url)
    print("app-BV97l_1z.js length:", len(r.text))
    
    with open('scratch/ext_app_js.txt', 'w', encoding='utf-8') as f:
        f.write(r.text)
        
    for line in r.text.split(';'):
        if any(k in line for k in ['action', 'fetch', 'Post', 'ajax', 'chapter', 'b64', 'nonce', 'fcn_']):
            print("  -", line[:120].encode('ascii', 'ignore').decode())
