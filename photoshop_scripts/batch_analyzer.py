import os
import sys
import glob
import json
from concurrent.futures import ThreadPoolExecutor
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

def analyze_single_crop(client, image_path):
    if not os.path.exists(image_path):
        return None

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
        return json.loads(response.text)
    except Exception as e:
        return {
            "fill": {"is_gradient": False, "solid_hex": "#000000", "top_hex": "#000000", "bottom_hex": "#000000", "angle": 90},
            "stroke": {"enabled": False, "color_hex": "#000000", "size_px": 2.0},
            "outer_glow": {"enabled": False, "color_hex": "#FFFFFF", "size_px": 5.0, "opacity_percent": 80},
            "drop_shadow": {"enabled": False, "color_hex": "#000000", "distance_px": 4.0, "blur_px": 4.0},
            "error": str(e)
        }

def run_batch(working_dir):
    client = get_gemini_client()
    crop_files = sorted(glob.glob(os.path.join(working_dir, "crop_*.png")))
    
    if not crop_files:
        return

    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_file = {executor.submit(analyze_single_crop, client, f): f for f in crop_files}
        for future in future_to_file:
            f = future_to_file[future]
            base_name = os.path.basename(f)
            try:
                data = future.result()
                results[base_name] = data
            except Exception as e:
                results[base_name] = {"error": str(e)}

    out_file = os.path.join(working_dir, "batch_result.json")
    with open(out_file, "w", encoding="utf-8") as out:
        json.dump(results, out, indent=2)

if __name__ == "__main__":
    work_dir = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) > 1:
        work_dir = sys.argv[1]
    run_batch(work_dir)
