import os
from google import genai

# Cấu hình Gemini
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("GEMINI_API_KEY not set")
else:
    client = genai.Client(api_key=api_key)
    print("Listing models with google-genai...")
    for m in client.models.list():
        print(f"{m.name} supported methods: {m.supported_generation_methods}")
