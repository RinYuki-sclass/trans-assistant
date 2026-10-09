import os
import sys
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
load_dotenv('.env')

from google import genai

k = os.environ.get("GEMINI_API_KEY_2") or os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=k)

for m in ["gemini-2.5-flash-lite", "gemini-flash-lite-latest", "gemini-3.1-flash-lite"]:
    try:
        resp = client.models.generate_content(
            model=m,
            contents="Dịch sang tiếng Việt: 'Hello world!'"
        )
        print(f"Model {m}: SUCCESS -> {resp.text.strip()}")
    except Exception as e:
        print(f"Model {m}: ERROR -> {str(e)[:100]}")
