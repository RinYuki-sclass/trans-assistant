import os
import sys
import json
from PIL import Image
from dotenv import load_dotenv

def get_gemini_client():
    env_paths = [
        r"d:\Nhung\RIDI\trans-assistant\.env",
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    ]
    for p in env_paths:
        if os.path.exists(p):
            load_dotenv(p)
            break

    keys = []
    for k in ["GEMINI_API_KEY_1", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3", "GEMINI_API_KEY_4", "GEMINI_API_KEY", "GOOGLE_API_KEY"]:
        val = os.environ.get(k)
        if val and val not in keys:
            keys.append(val)

    if not keys:
        return None

    try:
        from google import genai
        return genai.Client(api_key=keys[0])
    except Exception:
        return None

VFX_PROMPT = """
You are a Master Typography VFX Artist for Webtoons & Manhwa.
Analyze the stylized text in this comic crop with high precision.

Look closely at the artistic details:
1. Fill / Gradient:
   - Does the text have a dramatic color shift from top to bottom?
   - For example: Top line is deep black/dark charcoal, while the bottom line shifts into blood red/crimson. Or top is bright yellow, bottom is deep orange.
   - Do NOT blend them into a dull average color! Capture the true high-contrast drama!
   - If plain/solid single color, set is_gradient = false.

2. Outline vs Glow:
   - Is it a hard drawn border/stroke, OR a soft glowing halo/aura (Outer Glow) separating the text from the background?
   - If it is a soft white/colored halo, set outer_glow.enabled = true, and stroke.enabled = false.
   - Only enable stroke if there is an actual crisp/sharp solid border.

Output ONLY a valid JSON:
{
  "fill": {
    "is_gradient": true/false,
    "solid_hex": "#RRGGBB",
    "top_hex": "#RRGGBB",
    "bottom_hex": "#RRGGBB",
    "angle": 90
  },
  "stroke": {
    "enabled": true/false,
    "color_hex": "#RRGGBB",
    "size_px": 2.5
  },
  "outer_glow": {
    "enabled": true/false,
    "color_hex": "#FFFFFF",
    "size_px": 5.0,
    "opacity_percent": 80
  },
  "drop_shadow": {
    "enabled": true/false,
    "color_hex": "#000000",
    "distance_px": 4.0,
    "blur_px": 4.0
  }
}
"""

def analyze_with_vision_ai(image_path, output_path):
    client = get_gemini_client()
    
    if client is None:
        fallback_analyze(image_path, output_path)
        return

    try:
        from google.genai import types
        img = Image.open(image_path).convert("RGB")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[img, VFX_PROMPT],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.1
            )
        )
        
        data = json.loads(response.text)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    except Exception:
        fallback_analyze(image_path, output_path)

def fallback_analyze(image_path, output_path):
    default_data = {
        "fill": {"is_gradient": False, "solid_hex": "#000000", "top_hex": "#000000", "bottom_hex": "#000000", "angle": 90},
        "stroke": {"enabled": False, "color_hex": "#000000", "size_px": 2.0},
        "outer_glow": {"enabled": False, "color_hex": "#FFFFFF", "size_px": 5.0, "opacity_percent": 80},
        "drop_shadow": {"enabled": False, "color_hex": "#000000", "distance_px": 4.0, "blur_px": 4.0}
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(default_data, f, indent=2)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    in_file = os.path.join(script_dir, "temp_crop.png")
    out_file = os.path.join(script_dir, "style_result.json")

    if len(sys.argv) > 2:
        in_file = sys.argv[1]
        out_file = sys.argv[2]

    analyze_with_vision_ai(in_file, out_file)
