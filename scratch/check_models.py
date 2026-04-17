import os
from dotenv import load_dotenv
from google import genai

# Load API Key từ .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY_1") or os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in .env")
else:
    print(f"Checking models for Key: {api_key[:10]}...")
    client = genai.Client(api_key=api_key)
    
    try:
        print("\n--- AVAILABLE MODELS ---")
        # List models
        for model in client.models.list():
            print(f"- {model.name}")
    except Exception as e:
        print(f"Error calling ListModels: {e}")
