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

async def wait_and_solve_turnstile(ws, msg_id):
    for attempt in range(25):
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
            print(f'Ready: {title}')
            break
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
        await asyncio.sleep(3)
        msg_id = await wait_and_solve_turnstile(ws, msg_id)

        # Check what page is loaded
        eval_resp = await send_cmd(ws, 'Runtime.evaluate', {
            'expression': 'window.location.href'
        }, msg_id)
        msg_id += 1
        print('Current URL:', eval_resp.get('result', {}).get('result', {}).get('value'))

        html_resp = await send_cmd(ws, 'Runtime.evaluate', {'expression': 'document.documentElement.outerHTML'}, msg_id)
        msg_id += 1
        with open('scratch/page2.html', 'w', encoding='utf-8') as f:
            f.write(html_resp.get('result', {}).get('result', {}).get('value', ''))
        print('Saved scratch/page2.html')

try:
    asyncio.run(main())
finally:
    proc.terminate()
