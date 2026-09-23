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
    'https://www.novelupdates.com/viewlist/141600/'
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

    print('Connecting...')
    async with websockets.connect(ws_url) as ws:
        msg_id = 1
        # Wait 4s for widget
        await asyncio.sleep(4)

        # Get rect of div#lVJB5 or turnstile
        resp = await send_cmd(ws, 'Runtime.evaluate', {
            'expression': '''
                (() => {
                    const el = document.querySelector('div#lVJB5') || document.querySelector('div.main-content');
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
        rect = resp.get('result', {}).get('result', {}).get('value')
        print('Rect:', rect)

        if rect:
            # Turnstile checkbox is usually ~30px inside from top-left of the widget box
            target_x = rect['x'] + 30
            target_y = rect['y'] + 32
            print(f'Clicking at ({target_x}, {target_y})')

            # Move mouse
            await send_cmd(ws, 'Input.dispatchMouseEvent', {
                'type': 'mouseMoved',
                'x': target_x,
                'y': target_y
            }, msg_id)
            msg_id += 1
            await asyncio.sleep(0.3)

            # Click
            await send_cmd(ws, 'Input.dispatchMouseEvent', {
                'type': 'mousePressed',
                'x': target_x,
                'y': target_y,
                'button': 'left',
                'clickCount': 1
            }, msg_id)
            msg_id += 1
            await asyncio.sleep(0.15)
            await send_cmd(ws, 'Input.dispatchMouseEvent', {
                'type': 'mouseReleased',
                'x': target_x,
                'y': target_y,
                'button': 'left',
                'clickCount': 1
            }, msg_id)
            msg_id += 1

        # Now watch for title changes
        for i in range(25):
            eval_req = await send_cmd(ws, 'Runtime.evaluate', {
                'expression': 'JSON.stringify({title: document.title, url: window.location.href})',
                'returnByValue': True
            }, msg_id)
            msg_id += 1
            val = json.loads(eval_req.get('result', {}).get('result', {}).get('value', '{}'))
            print(f'[{i}s] Title: {val.get("title")}')
            if val.get('title') and 'Just a moment' not in val.get('title'):
                print('SUCCESS!')
                html_resp = await send_cmd(ws, 'Runtime.evaluate', {
                    'expression': 'document.documentElement.outerHTML',
                    'returnByValue': True
                }, msg_id)
                msg_id += 1
                html = html_resp.get('result', {}).get('result', {}).get('value', '')
                with open('scratch/novelupdates_page.html', 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f'Saved {len(html)} bytes to scratch/novelupdates_page.html')
                break
            await asyncio.sleep(1)

try:
    asyncio.run(main())
finally:
    proc.terminate()
