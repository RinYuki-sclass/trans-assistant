import subprocess
import time
import json
import os
import sys
import urllib.request
import asyncio
import websockets
from bs4 import BeautifulSoup
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
user_data = r'C:\Users\Innotech\AppData\Local\Temp\edge_cdp_profile'

async def send_cmd(ws, method, params=None, msg_id=1):
    payload = {'id': msg_id, 'method': method}
    if params:
        payload['params'] = params
    await ws.send(json.dumps(payload))
    while True:
        resp = json.loads(await ws.recv())
        if resp.get('id') == msg_id:
            return resp

async def get_fresh_cookie():
    cmd = [
        edge_path,
        f'--user-data-dir={user_data}',
        '--remote-debugging-port=9222',
        '--window-size=1280,800',
        'https://www.novelupdates.com/series/i-became-the-main-top-in-a-reverse-harem-novel/'
    ]
    proc = subprocess.Popen(cmd)
    try:
        ws_url = None
        for _ in range(15):
            try:
                with urllib.request.urlopen('http://127.0.0.1:9222/json') as resp:
                    targets = json.loads(resp.read().decode())
                    for t in targets:
                        if 'novelupdates.com' in t.get('url', ''):
                            ws_url = t.get('webSocketDebuggerUrl')
                            break
                if ws_url:
                    break
            except Exception:
                pass
            await asyncio.sleep(1)

        if not ws_url:
            print('Edge target not found')
            return {}, ''

        async with websockets.connect(ws_url) as ws:
            msg_id = 1
            await asyncio.sleep(3)
            # check and solve Turnstile if needed
            for _ in range(15):
                resp = await send_cmd(ws, 'Runtime.evaluate', {'expression': 'document.title'}, msg_id)
                msg_id += 1
                title = resp.get('result', {}).get('result', {}).get('value', '')
                if 'Just a moment' in title or title == '':
                    resp_rect = await send_cmd(ws, 'Runtime.evaluate', {
                        'expression': '''
                            (() => {
                                const el = document.querySelector("div[id^='lVJB5']") || document.querySelector("div.main-content") || document.querySelector("div[id*='turnstile']");
                                if (el) {
                                    const r = el.getBoundingClientRect();
                                    return { x: r.x, y: r.y, w: r.width, h: r.height };
                                }
                                return null;
                            })()
                        ''',
                        'returnByValue': True
                    }, msg_id)
                    msg_id += 1
                    rect = resp_rect.get('result', {}).get('result', {}).get('value')
                    if rect:
                        cx = rect['x'] + 30
                        cy = rect['y'] + 32
                        await send_cmd(ws, 'Input.dispatchMouseEvent', {'type': 'mouseMoved', 'x': cx, 'y': cy}, msg_id)
                        msg_id += 1
                        await asyncio.sleep(0.2)
                        await send_cmd(ws, 'Input.dispatchMouseEvent', {'type': 'mousePressed', 'x': cx, 'y': cy, 'button': 'left', 'clickCount': 1}, msg_id)
                        msg_id += 1
                        await asyncio.sleep(0.1)
                        await send_cmd(ws, 'Input.dispatchMouseEvent', {'type': 'mouseReleased', 'x': cx, 'y': cy, 'button': 'left', 'clickCount': 1}, msg_id)
                        msg_id += 1
                    await asyncio.sleep(2)
                else:
                    print('Passed Cloudflare on Edge:', title)
                    break

            cookie_resp = await send_cmd(ws, 'Network.getCookies', msg_id=msg_id)
            msg_id += 1
            cookies = cookie_resp.get('result', {}).get('cookies', [])
            cookie_dict = {c['name']: c['value'] for c in cookies if 'novelupdates.com' in c.get('domain', '')}

            ua_resp = await send_cmd(ws, 'Runtime.evaluate', {'expression': 'navigator.userAgent'}, msg_id)
            ua = ua_resp.get('result', {}).get('result', {}).get('value')
            return cookie_dict, ua
    finally:
        proc.terminate()

def run():
    with open('scratch/all_novels.json', 'r', encoding='utf-8') as f:
        novels = json.load(f)

    out_file = 'scratch/novels_with_synopsis.json'
    results = {}
    if os.path.exists(out_file):
        try:
            with open(out_file, 'r', encoding='utf-8') as f:
                for item in json.load(f):
                    results[item['url']] = item
        except Exception as e:
            pass

    print(f"Total novels: {len(novels)}, already fetched: {len(results)}")

    cookie_dict, ua = asyncio.run(get_fresh_cookie())
    print("Got cookies:", list(cookie_dict.keys()))

    session = requests.Session()
    session.cookies.update(cookie_dict)
    session.headers.update({
        'User-Agent': ua or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0",
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.novelupdates.com/'
    })

    success_count = 0
    for i, novel in enumerate(novels):
        url = novel['url']
        if url in results and results[url].get('synopsis'):
            continue

        print(f"[{i+1}/{len(novels)}] Fetching {novel['title']}...")
        try:
            resp = session.get(url, impersonate='edge101', timeout=15)
            if resp.status_code != 200 or 'Just a moment' in resp.text:
                print(f"  Failed (status {resp.status_code}, Turnstile: {'Just a moment' in resp.text})")
                print("  Refreshing cookie...")
                cookie_dict, ua = asyncio.run(get_fresh_cookie())
                session.cookies.update(cookie_dict)
                resp = session.get(url, impersonate='edge101', timeout=15)
                if resp.status_code != 200 or 'Just a moment' in resp.text:
                    print("  Still failed, skipping for now...")
                    continue

            soup = BeautifulSoup(resp.text, 'html.parser')
            desc_div = soup.find('div', id='editdescription')
            synopsis = desc_div.get_text(separator='\n', strip=True) if desc_div else ''
            
            assoc_div = soup.find('div', id='editassociated')
            associated = assoc_div.get_text(separator=' / ', strip=True) if assoc_div else ''
            
            type_span = soup.find('a', class_='genre type')
            novel_type = type_span.get_text(strip=True) if type_span else ''

            tags_div = soup.find('div', id='showtags')
            tags = [t.get_text(strip=True) for t in tags_div.find_all('a')] if tags_div else []

            novel_data = dict(novel)
            novel_data['associated'] = associated
            novel_data['type'] = novel_type
            novel_data['synopsis'] = synopsis
            novel_data['tags'] = tags

            results[url] = novel_data
            success_count += 1

            if success_count % 5 == 0:
                with open(out_file, 'w', encoding='utf-8') as f:
                    json.dump(list(results.values()), f, ensure_ascii=False, indent=2)
                print(f"  Saved progress ({len(results)} items)")

            time.sleep(0.35)
        except Exception as e:
            print(f"  Error on {url}: {e}")
            time.sleep(1)

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(list(results.values()), f, ensure_ascii=False, indent=2)

    print(f"\nCOMPLETED: {len(results)}/{len(novels)} fetched!")

if __name__ == '__main__':
    run()
