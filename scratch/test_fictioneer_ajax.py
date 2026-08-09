import httpx
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

post_id = '365934' # Post ID of chapter uh-1

actions_to_test = [
    {'action': 'fictioneer_load_chapter', 'post_id': post_id},
    {'action': 'fcn_load_chapter', 'post_id': post_id},
    {'action': 'fcn_fetch_chapter', 'post_id': post_id},
    {'action': 'get_chapter_content', 'post_id': post_id},
    {'action': 'fictioneer_get_chapter', 'post_id': post_id},
    {'action': 'fcn_chapter_content', 'id': post_id},
    {'action': 'fictioneer_load_chapter_content', 'chapter_id': post_id},
]

with httpx.Client(headers=headers, timeout=15, follow_redirects=True) as client:
    for data in actions_to_test:
        r = client.post('https://cherrymist.cafe/wp-admin/admin-ajax.php', data=data)
        print(f"Action {data.get('action')}: Status {r.status_code}, Length {len(r.text)}")
        if r.status_code == 200 and len(r.text) > 50:
            print("   Response text preview:", r.text[:200].encode('ascii', 'ignore').decode())
