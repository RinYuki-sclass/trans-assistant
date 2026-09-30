import os, requests, time
from dotenv import load_dotenv
load_dotenv()

KEYS = [os.getenv('GEMINI_API_KEY_1'), os.getenv('GEMINI_API_KEY_2'), os.getenv('GEMINI_API_KEY_3')]
MODELS = [
    "gemini-2.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-3-flash-preview",
    "gemini-2.0-flash",
    "gemini-1.5-flash"
]

for m in MODELS:
    for ki, k in enumerate(KEYS):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={k}"
        t0 = time.time()
        try:
            r = requests.post(url, json={"contents": [{"parts": [{"text": "hi"}]}]}, timeout=6)
            dur = time.time() - t0
            print(f"{m} (key {ki}): status {r.status_code} in {dur:.2f}s")
            if r.status_code == 200:
                print(f"  SUCCESS! Sample: {r.json().get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')[:30]}")
                break
        except Exception as e:
            print(f"{m} (key {ki}): error {e}")
