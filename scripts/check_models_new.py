import os
from google import genai

# Cấu hình Gemini
api_key = "AIzaSyBLkkK6HOGu_B7HCR8O-uLPDHAI3waEzdg"
if not api_key:
    print("GEMINI_API_KEY not set")
else:
    client = genai.Client(api_key=api_key)
    print("Listing models...")
    with open('scripts/available_models.txt', 'w', encoding='utf-8') as f:
        for m in client.models.list():
            line = f"Name: {m.name} | Display Name: {m.display_name}\n"
            f.write(line)
            print(line.strip())
