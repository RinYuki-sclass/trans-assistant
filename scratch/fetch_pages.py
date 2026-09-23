import subprocess
import time
import json
import urllib.request
import asyncio
import websockets

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
user_data = r'C:\Users\Innotech\AppData\Local\Temp\edge_cdp_profile'

cmd = [
    edge_path,
    f'--user-data-dir={user_data}',
    '--remote-debugging-port=9222',
    '--window-size=1280,800',
    'https://www.novelupdates.com/viewlist/141600/?st=1&pg=2'
]

proc = subprocess.Popen(cmd)

async def send_cmd(ws, method, params=None, msg_id=1):
    payload = {'id': msg_id, 'method': method}
    if params:
        payload['params'] = params
    await ws.send(json.dumps(payload))
    while True:
        resp = json.loads(await ws.recv())
        if resp.get('id') == msg_id:
            return resp

async def fetch_page(ws, url, filename, msg_id):
    # navigate
    await send_cmd(ws, 'Page.navigate', {'url': url}, msg_id)
    msg_id += 1
    await asyncio.sleep(3)
    
    # check title
    for i in range(15):
        resp = await send_cmd(ws, 'Runtime.evaluate', {'expression': 'document.title'}, msg_id)
        msg_id += 1
        title = resp.get('result', {}).get('result', {}).get('value', '')
        if 'Just a moment' not in title and title != '':
            print(f'Loaded {url}: {title}')
            break
        await asyncio.sleep(1)
        
    html_resp = await send_cmd(ws, 'Runtime.evaluate', {'expression': 'document.documentElement.outerHTML'}, msg_id)
    msg_id += 1
    html = html_resp.get('result', {}).get('result', {}).get('value', '')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Saved {filename} ({len(html)} bytes)')
    return msg_id

async def main():
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
        print('Target not found')
        return

    async with websockets.connect(ws_url) as ws:
        msg_id = 1
        await asyncio.sleep(2)
        # Fetch page 2
        msg_id = await fetch_page(ws, 'https://www.novelupdates.com/viewlist/141600/?st=1&pg=2', 'scratch/page2.html', msg_id)
        # Fetch page 3
        msg_id = await fetch_page(ws, 'https://www.novelupdates.com/viewlist/141600/?st=1&pg=3', 'scratch/page3.html', msg_id)

try:
    asyncio.run(main())
finally:
    proc.terminate()
