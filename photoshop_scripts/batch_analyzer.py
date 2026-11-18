# -*- coding: utf-8 -*-
"""
batch_analyzer.py - Multi-Select Batch Auto-Style VFX Engine
Xử lý hàng loạt các vùng chọn crop_0.png, crop_1.png... song song.
Áp dụng cùng kiến trúc Hybrid thông minh với style_analyzer.py.
"""

import os
import sys
import glob
import json
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from dotenv import load_dotenv

# Import trực tiếp thuật toán từ style_analyzer
from style_analyzer import analyze_with_local_cv, get_gemini_client

def analyze_single_crop(client, image_path):
    if not os.path.exists(image_path):
        return None

    # Luôn có kết quả CV Core chuẩn xác làm nền tảng
    cv_data = analyze_with_local_cv(image_path)
    
    if client is None:
        return cv_data

    try:
        from google.genai import types
        img = Image.open(image_path).convert("RGB")

        prompt = """
You are a Master Typography VFX Artist for Webtoons & Manhwa.
Analyze the stylized text in this comic crop with surgical precision.

CRITICAL RULES:
1. Ignore background scenery/artwork. Focus ONLY on the text glyphs!
2. Fill: Check for vertical gradient (e.g. dark top, vibrant red bottom).
3. Stroke: Look for a crisp solid border hugging the letters.
4. Outer Glow: Look for a soft glowing aura around the letters/stroke.

Output ONLY valid JSON:
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
    "opacity_percent": 60
  },
  "drop_shadow": {
    "enabled": false,
    "color_hex": "#000000",
    "distance_px": 4.0,
    "blur_px": 4.0
  }
}
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[img, prompt],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.1
            )
        )
        ai_data = json.loads(response.text)
        
        # Neo màu từ CV Core
        if cv_data["stroke"]["enabled"]:
            ai_data["stroke"]["enabled"] = True
            ai_data["stroke"]["color_hex"] = cv_data["stroke"]["color_hex"]
            if ai_data["stroke"].get("size_px"):
                ai_data["stroke"]["size_px"] = cv_data["stroke"]["size_px"]
        
        if cv_data["fill"]["is_gradient"]:
            ai_data["fill"]["is_gradient"] = True
            ai_data["fill"]["top_hex"] = cv_data["fill"]["top_hex"]
            ai_data["fill"]["bottom_hex"] = cv_data["fill"]["bottom_hex"]
            
        if cv_data["outer_glow"]["enabled"]:
            ai_data["outer_glow"]["enabled"] = True
            ai_data["outer_glow"]["color_hex"] = cv_data["outer_glow"]["color_hex"]
            ai_data["outer_glow"]["size_px"] = cv_data["outer_glow"]["size_px"]

        return ai_data
    except Exception:
        return cv_data


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
        json.dump(results, out, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    work_dir = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) > 1:
        work_dir = sys.argv[1]
    run_batch(work_dir)
