import httpx

headers = {'User-Agent': 'Mozilla/5.0'}
with httpx.Client(headers=headers, timeout=15) as client:
    r = client.get('https://cherrymist.cafe/wp-content/themes/fictioneer/js/chapter.min.js?ver=1786283304')
    print("chapter.min.js length:", len(r.text))
    
    with open('scratch/chapter_js.txt', 'w', encoding='utf-8') as f:
        f.write(r.text)
        
    # Search for action or fetch or ajax or b64
    for line in r.text.split(';'):
        if any(k in line for k in ['action', 'fetch', 'Post', 'ajax', 'chapter', 'b64', 'nonce', 'fcn_']):
            print("  -", line[:120].encode('ascii', 'ignore').decode())
