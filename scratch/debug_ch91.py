import os
import sys
import json
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
load_dotenv('.env')

from google import genai
from google.genai import types

k = os.environ.get("GEMINI_API_KEY_2") or os.environ.get("GEMINI_API_KEY")
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

resp = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT_ARC4,
        temperature=0.15,
    )
)

print("Finish reason:", resp.candidates[0].finish_reason if resp.candidates else "No candidates")
text = resp.text
print("Text length:", len(text) if text else 0)
if text:
    print("First 300 chars:\n", text[:300])
