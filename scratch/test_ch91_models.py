import os
import sys
import json
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
load_dotenv('.env')

from google import genai
from google.genai import types

# Use key 3 or key 4
k = os.environ.get("GEMINI_API_KEY_3") or os.environ.get("GEMINI_API_KEY_4")
client = genai.Client(api_key=k)

with open('scratch/batch1_sliced.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
chunk_paras = d['ch_091']['paras'][:20]

n = len(chunk_paras)
numbered_input = [f"[{i+1:02d}] {p}" for i, p in enumerate(chunk_paras)]
input_text = "\n\n".join(numbered_input)

from scratch.translate_arc4_batch1 import SYSTEM_PROMPT_ARC4

prompt = f"""Chương: Chương 91: Tuyến thể ngứa ngáy
Dịch đoạn sau (gồm đúng {n} đoạn, từ [{1:02d}] đến [{n:02d}]):
{input_text}
"""

models = ["gemini-3.1-flash-lite", "gemini-3.5-flash", "gemini-flash-lite-latest"]

safety = [
    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
]

for m in models:
    try:
        resp = client.models.generate_content(
            model=m,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT_ARC4,
                temperature=0.15,
                safety_settings=safety
            )
        )
        if resp.text:
            print(f"Model {m}: SUCCESS! Output length {len(resp.text)}")
            print("First 200 chars:", resp.text[:200])
            break
        else:
            print(f"Model {m}: Empty response (candidates: {resp.candidates})")
    except Exception as e:
        print(f"Model {m}: Exception -> {e}")
