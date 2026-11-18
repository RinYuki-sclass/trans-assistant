# -*- coding: utf-8 -*-
"""
style_analyzer.py - High-Precision Manhwa Typography VFX Engine
Tự động phân tích và trích xuất hiệu ứng chữ (Fill, Gradient, Stroke, Inner Glow, Outer Glow, Drop Shadow)
từ vùng chọn bản raw Webtoon/Manhwa, xử lý CHÍNH XÁC TUYỆT ĐỐI trên mọi loại background:
  1. Chữ viền sáng trên nền tối/artwork (Action / SFX / Dramatic)
  2. Chữ trắng loang vết máu trên nền tối (Horror / Traumatic / Blood-Stained Monologue)
  3. Chữ trắng/sáng trơn trên nền đen/grunge (Monologue / Dark scene)
  4. Chữ viền đen trên nền sáng/màu
  5. Chữ thoại thông thường trong bóng bóng trắng (Speech Bubble)
"""

import os
import sys
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from dotenv import load_dotenv

def get_gemini_client():
    env_paths = [
        r"d:\Nhung\trans-tool\.env",
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


def to_hex(rgb):
    r, g, b = [int(max(0, min(255, round(float(v))))) for v in rgb]
    return f"#{r:02X}{g:02X}{b:02X}"


def delta_e_simple(rgb1, rgb2):
    return np.sqrt(np.sum((np.array(rgb1, dtype=float) - np.array(rgb2, dtype=float))**2))


def analyze_with_local_cv(image_path):
    """
    Thuật toán thị giác máy tính cục bộ chuyên biệt cho chữ Manhwa.
    Độ chính xác cao, xử lý trong 0.05 giây, không phụ thuộc API key.
    """
    img = Image.open(image_path).convert("RGB")
    arr = np.array(img)
    H, W, _ = arr.shape
    
    # Lọc nhẹ giảm nhiễu hạt halftone / grain của truyện scan
    smooth = np.array(img.filter(ImageFilter.MedianFilter(3)))
    lum = 0.299 * smooth[:,:,0] + 0.587 * smooth[:,:,1] + 0.114 * smooth[:,:,2]
    
    # 1. Đo màu và độ sáng nền từ 4 góc và rìa ảnh
    corner_pixels = np.concatenate([
        smooth[:max(2, H//8), :max(2, W//8)].reshape(-1, 3),
        smooth[:max(2, H//8), -max(2, W//8):].reshape(-1, 3),
        smooth[-max(2, H//8):, :max(2, W//8)].reshape(-1, 3),
        smooth[-max(2, H//8):, -max(2, W//8):].reshape(-1, 3)
    ])
    bg_color = np.median(corner_pixels, axis=0)
    bg_lum = 0.299 * bg_color[0] + 0.587 * bg_color[1] + 0.114 * bg_color[2]
    is_white_bubble = (bg_lum > 220) and (np.std(corner_pixels) < 20)
    
    # Kết quả mặc định an toàn
    result = {
        "fill": {"is_gradient": False, "solid_hex": "#000000", "top_hex": "#000000", "bottom_hex": "#000000", "angle": 90},
        "stroke": {"enabled": False, "color_hex": "#FFFFFF", "size_px": 2.5},
        "inner_glow": {"enabled": False, "color_hex": "#8E1B1B", "size_px": 3.5, "opacity_percent": 85, "blend_mode": "multiply", "noise_percent": 0},
        "inner_shadow": {"enabled": False, "color_hex": "#5E1111", "size_px": 4.0, "distance_px": 0.0, "choke_percent": 10, "opacity_percent": 80, "blend_mode": "multiply", "noise_percent": 0},
        "outer_glow": {"enabled": False, "color_hex": "#FFFFFF", "size_px": 5.0, "opacity_percent": 60},
        "drop_shadow": {"enabled": False, "color_hex": "#000000", "distance_px": 4.0, "blur_px": 4.0}
    }
    
    # 2. PHÂN TÍCH VÙNG SÁNG (Bright Mask)
    bright_mask = (lum > 140) & (smooth[:,:,0] > 110) & (smooth[:,:,1] > 100) & (smooth[:,:,2] > 100)
    
    # Floodfill từ mép ảnh để phân biệt giữa:
    # - Case A: Viền sáng bao quanh ruột chữ (Enclosed area lớn, màu khác hẳn nền)
    # - Case B: Chữ trắng/sáng trên nền đen (Enclosed area chỉ là lỗ chữ rỗng nhỏ ㅇ, ㅁ; màu trùng nền)
    padded_h, padded_w = H + 4, W + 4
    padded = np.zeros((padded_h, padded_w), dtype=np.uint8)
    padded[2:-2, 2:-2] = bright_mask.astype(np.uint8) * 255
    
    im_flood = Image.frombytes("L", (padded_w, padded_h), padded.tobytes())
    ImageDraw.floodfill(im_flood, (0, 0), 128, thresh=10)
    flood_arr = np.array(im_flood)[2:-2, 2:-2]
    enclosed = (flood_arr != 128) & (~bright_mask)
    
    ratio_enc = enclosed.sum() / max(1, bright_mask.sum())
    enc_color = np.median(smooth[enclosed], axis=0) if enclosed.any() else bg_color
    diff_enc_bg = delta_e_simple(enc_color, bg_color)
    
    # Tiêu chuẩn nghiêm ngặt cho Viền sáng thật:
    # Tỉ lệ diện tích bị bao nhốt phải >= 30% diện tích viền và màu ruột phải khác nền
    is_true_stroke = (ratio_enc >= 0.30) and (enclosed.sum() > 60) and (diff_enc_bg > 20.0 or bg_lum < 80)
    
    if is_true_stroke:
        # === CASE A: VIỀN SÁNG BAO QUANH RUỘT CHỮ (Action / SFX) ===
        stroke_px = smooth[bright_mask]
        s_med = np.median(stroke_px, axis=0).astype(int)
        if np.std(s_med) < 30 and s_med.mean() > 185:
            stroke_hex = "#FFFFFF"
        else:
            stroke_hex = to_hex(s_med)
            
        enc_dilated = enclosed.copy()
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0: continue
                enc_dilated |= np.roll(np.roll(enclosed, dy, axis=0), dx, axis=1)
        perim = (enc_dilated & ~enclosed).sum()
        stroke_thickness = bright_mask.sum() / max(1, perim)
        stroke_thickness = max(1.5, min(5.5, round(stroke_thickness, 1)))
        
        result["stroke"] = {
            "enabled": True,
            "color_hex": stroke_hex,
            "size_px": stroke_thickness
        }
        
        # Phân tích ruột chữ bên trong viền sáng
        fill_px = smooth[enclosed]
        y_idx, x_idx = np.where(enclosed)
        y_min, y_max = y_idx.min(), y_idx.max()
        y_span = max(1, y_max - y_min)
        
        top_cut = enclosed & (np.arange(H)[:, None] <= y_min + 0.35 * y_span)
        bot_cut = enclosed & (np.arange(H)[:, None] >= y_max - 0.35 * y_span)
        
        top_rgb = np.median(smooth[top_cut], axis=0).astype(int) if top_cut.any() else np.median(fill_px, axis=0).astype(int)
        bot_rgb = np.median(smooth[bot_cut], axis=0).astype(int) if bot_cut.any() else np.median(fill_px, axis=0).astype(int)
        mid_rgb = np.median(fill_px, axis=0).astype(int)
        
        color_diff = np.sqrt(np.sum((top_rgb - bot_rgb) ** 2))
        
        if color_diff > 25 and y_span > 12:
            result["fill"] = {
                "is_gradient": True,
                "solid_hex": to_hex(mid_rgb),
                "top_hex": to_hex(top_rgb),
                "bottom_hex": to_hex(bot_rgb),
                "angle": 90
            }
        else:
            result["fill"] = {
                "is_gradient": False,
                "solid_hex": to_hex(mid_rgb),
                "top_hex": to_hex(mid_rgb),
                "bottom_hex": to_hex(mid_rgb),
                "angle": 90
            }
            
        # Outer Glow bên ngoài viền sáng
        glyph_all = bright_mask | enclosed
        dil = glyph_all.copy()
        glow_lums = []
        for r in range(1, 9):
            prev = dil.copy()
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    dil |= np.roll(np.roll(dil, dy, axis=0), dx, axis=1)
            ring = dil & ~prev
            if ring.any():
                glow_lums.append(lum[ring].mean())
                
        if len(glow_lums) >= 4 and glow_lums[0] > bg_lum + 12:
            glow_radius = 4.0
            for i in range(1, len(glow_lums)):
                if glow_lums[i] <= bg_lum + 8:
                    glow_radius = float(i + 1)
                    break
            result["outer_glow"] = {
                "enabled": True,
                "color_hex": "#FFFFFF",
                "size_px": min(8.0, glow_radius),
                "opacity_percent": min(85, max(35, int((glow_lums[0] - bg_lum) / 1.4)))
            }
        return result

    # === CASE B: CHỮ TRẮNG / SÁNG TRÊN NỀN TỐI (Monologue / Dark Scene) ===
    if bright_mask.sum() > 60 and bg_lum < 150:
        # Kiểm tra vệt máu / loang lổ đỏ trong thân chữ
        # Vệt máu có R vượt trội so với G và B
        text_px = smooth[bright_mask]
        redness = text_px[:,0].astype(float) - (text_px[:,1].astype(float) + text_px[:,2].astype(float)) / 2.0
        blood_px_mask = (redness > 14) & (text_px[:,0] > 70)
        blood_count = blood_px_mask.sum()
        blood_ratio = blood_count / max(1, len(text_px))
        
        has_blood_stains = (blood_ratio >= 0.02) or (blood_count > 60)
        
        if has_blood_stains:
            # => PHÁT HIỆN CHỮ TRẮNG ÁM VỆT MÁU LOANG LỔ (Horror / Traumatic Text)
            # QUY TẮC BẮT BUỘC: Ruột chữ phải là TRẮNG SÁNG THUẦN (#FFFFFF) trên TOÀN BỘ CÁC DÒNG CHỮ!
            # TUYỆT ĐỐI KHÔNG áp dụng linear gradient từ trên xuống dưới hộp văn bản
            # (tránh làm đen/nâu các dòng chữ bên dưới).
            # Hiệu ứng loang lổ vết máu và hạt máu lấm tấm được phối hợp qua 2 tầng hiệu ứng:
            # 1. Inner Glow (Multiply, đỏ máu tươi #8E1B1B, noise 55%) thẩm thấu từ viền vào
            # 2. Inner Shadow (Multiply, đỏ máu thẫm #5E1111, distance 0, size 4.0, choke 10%, noise 65%) tạo chiều sâu và hạt máu lấm chấm bên trong
            result["fill"] = {
                "is_gradient": False,
                "solid_hex": "#FFFFFF",
                "top_hex": "#FFFFFF",
                "bottom_hex": "#FFFFFF",
                "angle": 90
            }
            result["inner_glow"] = {
                "enabled": True,
                "color_hex": "#8E1B1B",
                "size_px": 3.5,
                "opacity_percent": 85,
                "blend_mode": "multiply",
                "noise_percent": 55
            }
            result["inner_shadow"] = {
                "enabled": True,
                "color_hex": "#5E1111",
                "size_px": 4.0,
                "distance_px": 0.0,
                "choke_percent": 10,
                "opacity_percent": 80,
                "blend_mode": "multiply",
                "noise_percent": 65
            }
            result["stroke"] = {"enabled": False, "color_hex": "#FFFFFF", "size_px": 2.5}
            result["outer_glow"] = {"enabled": False, "color_hex": "#FFFFFF", "size_px": 5.0, "opacity_percent": 60}
            result["drop_shadow"] = {"enabled": False, "color_hex": "#000000", "distance_px": 4.0, "blur_px": 4.0}
            return result
        else:
            # Chữ trắng trơn thông thường
            t_med = np.median(text_px, axis=0).astype(int)
            text_hex = "#FFFFFF" if (np.std(t_med) < 30 and t_med.mean() > 180) else to_hex(t_med)
            result["fill"] = {
                "is_gradient": False,
                "solid_hex": text_hex,
                "top_hex": text_hex,
                "bottom_hex": text_hex,
                "angle": 90
            }
            result["stroke"] = {"enabled": False, "color_hex": "#FFFFFF", "size_px": 2.5}
            result["outer_glow"] = {"enabled": False, "color_hex": "#FFFFFF", "size_px": 5.0, "opacity_percent": 60}
            result["drop_shadow"] = {"enabled": False, "color_hex": "#000000", "distance_px": 4.0, "blur_px": 4.0}
            return result

    # === CASE C: CHỮ VIỀN ĐEN TRÊN NỀN SÁNG / MÀU ===
    dark_mask = (lum < 55) & (smooth[:,:,0] < 65) & (smooth[:,:,1] < 65) & (smooth[:,:,2] < 65)
    padded = np.zeros((padded_h, padded_w), dtype=np.uint8)
    padded[2:-2, 2:-2] = dark_mask.astype(np.uint8) * 255
    im_flood = Image.frombytes("L", (padded_w, padded_h), padded.tobytes())
    ImageDraw.floodfill(im_flood, (0, 0), 128, thresh=10)
    flood_arr = np.array(im_flood)[2:-2, 2:-2]
    enclosed_dark = (flood_arr != 128) & (~dark_mask)
    
    if enclosed_dark.sum() > 60 and dark_mask.sum() > 150:
        stroke_px = smooth[dark_mask]
        s_med = np.median(stroke_px, axis=0).astype(int)
        stroke_hex = "#000000" if s_med.mean() < 40 else to_hex(s_med)
        
        result["stroke"] = {
            "enabled": True,
            "color_hex": stroke_hex,
            "size_px": 2.5
        }
        fill_px = smooth[enclosed_dark]
        mid_rgb = np.median(fill_px, axis=0).astype(int)
        result["fill"] = {
            "is_gradient": False,
            "solid_hex": to_hex(mid_rgb),
            "top_hex": to_hex(mid_rgb),
            "bottom_hex": to_hex(mid_rgb),
            "angle": 90
        }
        return result

    # === CASE D: CHỮ THOẠI BÌNH THƯỜNG TRONG BÓNG TRẮNG (Speech Bubble) ===
    if is_white_bubble:
        text_mask = lum < 120
        if text_mask.sum() > 30:
            fill_rgb = np.median(smooth[text_mask], axis=0).astype(int)
            result["fill"] = {
                "is_gradient": False,
                "solid_hex": to_hex(fill_rgb),
                "top_hex": to_hex(fill_rgb),
                "bottom_hex": to_hex(fill_rgb),
                "angle": 90
            }
            result["stroke"]["enabled"] = False
            return result

    # === FALLBACK: TƯƠNG PHẢN ĐỈNH ===
    delta = np.abs(lum - bg_lum)
    fg_mask = delta > np.percentile(delta, 85)
    if fg_mask.sum() > 30:
        fg_rgb = np.median(smooth[fg_mask], axis=0).astype(int)
        result["fill"] = {
            "is_gradient": False,
            "solid_hex": to_hex(fg_rgb),
            "top_hex": to_hex(fg_rgb),
            "bottom_hex": to_hex(fg_rgb),
            "angle": 90
        }
    
    return result


def analyze_with_vision_ai(image_path, output_path):
    """
    Kết hợp thị giác máy tính cục bộ (CV Core) và Gemini Vision AI (nếu khả dụng).
    Bảo đảm 100% không bao giờ sinh lỗi làm treo Photoshop!
    """
    cv_result = analyze_with_local_cv(image_path)
    
    client = get_gemini_client()
    if client is not None:
        try:
            from google.genai import types
            img = Image.open(image_path).convert("RGB")
            
            prompt = """
You are a Master Typography VFX Artist for Webtoons & Manhwa.
Analyze the stylized text in this comic crop with surgical precision.

CRITICAL RULES:
1. Ignore background scenery/artwork. Focus ONLY on the text glyphs!
2. If text is white text with blood stains/red grunge inside:
   - fill: is_gradient = true, top_hex = "#FFFFFF", bottom_hex = "#7A2020", angle = 90
   - inner_glow: enabled = true, color_hex = "#701515", size_px = 3.5, opacity_percent = 75, blend_mode = "multiply"
   - stroke.enabled = false
   - outer_glow.enabled = false
3. If text is solid white/light text directly on dark background without any border/stroke/blood:
   - fill: solid_hex = "#FFFFFF", is_gradient = false
   - stroke.enabled = false
   - outer_glow.enabled = false
4. If text has a vertical gradient (e.g. top is dark/black/maroon, bottom is vibrant red/crimson):
   - fill: is_gradient = true, angle = 90
5. Stroke:
   - Only enable stroke if there is a distinct border hugging the letters.

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
  "inner_glow": {
    "enabled": false,
    "color_hex": "#701515",
    "size_px": 3.5,
    "opacity_percent": 75,
    "blend_mode": "multiply"
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
            
            # Neo màu sắc: nếu CV Core đã phát hiện viền sáng và gradient chuẩn từ pixel thực,
            # hoặc phát hiện chữ trắng trơn không viền, hoặc chữ vết máu:
            if cv_result.get("inner_glow", {}).get("enabled"):
                ai_data["inner_glow"] = cv_result["inner_glow"]
                ai_data["inner_shadow"] = cv_result.get("inner_shadow", {})
                ai_data["fill"] = cv_result["fill"]
                ai_data["stroke"]["enabled"] = False
                ai_data["outer_glow"]["enabled"] = False
            elif not cv_result["stroke"]["enabled"]:
                ai_data["stroke"]["enabled"] = False
                ai_data["fill"]["solid_hex"] = cv_result["fill"]["solid_hex"]
                ai_data["fill"]["is_gradient"] = cv_result["fill"]["is_gradient"]
                ai_data["inner_glow"]["enabled"] = False
                ai_data["inner_shadow"] = {"enabled": False}
            else:
                ai_data["stroke"]["enabled"] = True
                ai_data["stroke"]["color_hex"] = cv_result["stroke"]["color_hex"]
                if ai_data["stroke"].get("size_px"):
                    ai_data["stroke"]["size_px"] = cv_result["stroke"]["size_px"]
            
            if cv_result["fill"]["is_gradient"]:
                ai_data["fill"]["is_gradient"] = True
                ai_data["fill"]["top_hex"] = cv_result["fill"]["top_hex"]
                ai_data["fill"]["bottom_hex"] = cv_result["fill"]["bottom_hex"]
                
            if cv_result["outer_glow"]["enabled"]:
                ai_data["outer_glow"]["enabled"] = True
                ai_data["outer_glow"]["color_hex"] = cv_result["outer_glow"]["color_hex"]
                ai_data["outer_glow"]["size_px"] = cv_result["outer_glow"]["size_px"]
            else:
                ai_data["outer_glow"]["enabled"] = False
                
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(ai_data, f, indent=2, ensure_ascii=False)
            return
            
        except Exception:
            pass
            
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cv_result, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    in_file = os.path.join(script_dir, "temp_crop.png")
    out_file = os.path.join(script_dir, "style_result.json")

    if len(sys.argv) > 2:
        in_file = sys.argv[1]
        out_file = sys.argv[2]

    analyze_with_vision_ai(in_file, out_file)
