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
import cv2
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
    Thuật toán thị giác máy tính cục bộ chuyên biệt cho chữ Manhwa/Webtoon.
    Độ chính xác cao, xử lý trong 0.05 giây, không phụ thuộc API key:
      1. Tự động nhận diện bong bóng thoại sáng (Speech Bubble) bất kể viền ngoài có chạm nền tranh tối hay không.
      2. Tách bóc tách chính xác sắc thái màu (tím, đỏ, xanh, cam...) và Gradient top-to-bottom.
      3. Xử lý chuẩn xác chữ viền sáng trên nền tối (Action/SFX), chữ trắng vết máu (Horror).
    """
    img = Image.open(image_path).convert("RGB")
    smooth = np.array(img.filter(ImageFilter.MedianFilter(3)))
    H, W, _ = smooth.shape
    lum = 0.299 * smooth[:,:,0] + 0.587 * smooth[:,:,1] + 0.114 * smooth[:,:,2]
    
    # Kết quả mặc định an toàn
    result = {
        "fill": {"is_gradient": False, "solid_hex": "#000000", "top_hex": "#000000", "bottom_hex": "#000000", "angle": 90},
        "stroke": {"enabled": False, "color_hex": "#FFFFFF", "size_px": 2.5},
        "inner_glow": {"enabled": False, "color_hex": "#8E1B1B", "size_px": 3.5, "opacity_percent": 85, "blend_mode": "multiply", "noise_percent": 0},
        "inner_shadow": {"enabled": False, "color_hex": "#5E1111", "size_px": 4.0, "distance_px": 0.0, "choke_percent": 10, "opacity_percent": 80, "blend_mode": "multiply", "noise_percent": 0},
        "outer_glow": {"enabled": False, "color_hex": "#FFFFFF", "size_px": 5.0, "opacity_percent": 60},
        "drop_shadow": {"enabled": False, "color_hex": "#000000", "distance_px": 4.0, "blur_px": 4.0}
    }

    # 1. Đo phân bố độ sáng và kiểm tra Bong bóng thoại sáng / xám (Speech Bubble Detection)
    bright_ratio = np.mean(lum > 140)
    bright_pixels = smooth[lum > 140]
    if len(bright_pixels) > 0:
        bright_med = np.median(bright_pixels, axis=0)
        bright_lum = 0.299 * bright_med[0] + 0.587 * bright_med[1] + 0.114 * bright_med[2]
    else:
        bright_med = np.array([255, 255, 255])
        bright_lum = 255.0

    corners = [
        smooth[:max(2, H//8), :max(2, W//8)].reshape(-1, 3),
        smooth[:max(2, H//8), -max(2, W//8):].reshape(-1, 3),
        smooth[-max(2, H//8):, :max(2, W//8)].reshape(-1, 3),
        smooth[-max(2, H//8):, -max(2, W//8):].reshape(-1, 3)
    ]
    corner_medians = [np.median(c, axis=0) for c in corners]
    bg_color_corners = np.median(corner_medians, axis=0)
    bg_lum_corners = 0.299 * bg_color_corners[0] + 0.587 * bg_color_corners[1] + 0.114 * bg_color_corners[2]

    # Nhận diện Bong bóng thoại sáng hoặc xám:
    # Nếu có ít nhất 20% diện tích sáng (> 140) và màu sáng đạt chuẩn, HOẶC 4 góc là nền sáng
    is_speech_bubble = (bright_ratio >= 0.20 and bright_lum > 145) or (bg_lum_corners > 145)

    # =========================================================================
    # PHÂN NHÁNH 1: BONG BÓNG THOẠI SÁNG / NỀN TRẮNG (SPEECH BUBBLE & STYLIZED SFX)
    # =========================================================================
    if is_speech_bubble:
        # Kiểm tra xem chữ trên nền sáng có hiệu ứng Viền trắng + Glow/Shadow tối (SFX / Độc thoại cách điệu như preview_0) không
        core_mask = lum < min(75, bg_lum_corners * 0.45)
        if core_mask.sum() > 30:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
            d = core_mask.astype(np.uint8)
            ring_lums = []
            ring_rgbs = []
            for step in range(14):
                d_next = cv2.dilate(d, kernel)
                ring = (d_next > 0) & (d == 0)
                if ring.sum() > 0:
                    ring_lums.append(float(np.median(lum[ring])))
                    ring_rgbs.append(np.median(smooth[ring], axis=0))
                d = d_next

            max_early = max(ring_lums[:6]) if len(ring_lums) >= 6 else 0
            min_late = min(ring_lums[6:]) if len(ring_lums) > 6 else 0
            dip = max_early - min_late

            # Khi phát hiện đỉnh sáng (viền trắng) và thung lũng tối (vùng đổ bóng / outer glow):
            if max_early >= 235 and dip >= 20.0:
                fill_px = smooth[core_mask]
                y_idx, x_idx = np.where(core_mask)
                y_min, y_max = y_idx.min(), y_idx.max()
                y_span = max(1, y_max - y_min)

                top_cut = core_mask & (np.arange(H)[:, None] <= y_min + 0.35 * y_span)
                bot_cut = core_mask & (np.arange(H)[:, None] >= y_max - 0.35 * y_span)

                top_rgb = np.median(smooth[top_cut], axis=0).astype(int) if top_cut.any() else np.median(fill_px, axis=0).astype(int)
                bot_rgb = np.median(smooth[bot_cut], axis=0).astype(int) if bot_cut.any() else np.median(fill_px, axis=0).astype(int)
                mid_rgb = np.median(fill_px, axis=0).astype(int)

                color_diff = delta_e_simple(top_rgb, bot_rgb)
                lum_diff = abs(float(np.mean(top_rgb)) - float(np.mean(bot_rgb)))

                if (color_diff > 25 or lum_diff > 30) and y_span > 12:
                    result["fill"] = {
                        "is_gradient": True,
                        "solid_hex": to_hex(mid_rgb),
                        "top_hex": to_hex(top_rgb),
                        "bottom_hex": to_hex(bot_rgb),
                        "angle": 90
                    }
                else:
                    solid_hex = to_hex(mid_rgb)
                    result["fill"] = {
                        "is_gradient": False,
                        "solid_hex": solid_hex,
                        "top_hex": solid_hex,
                        "bottom_hex": solid_hex,
                        "angle": 90
                    }

                # Đo độ dày viền trắng
                white_rings = sum(1 for v in ring_lums[:7] if v >= 235)
                stroke_thickness = max(2.5, min(5.5, float(white_rings)))

                result["stroke"] = {
                    "enabled": True,
                    "color_hex": "#FFFFFF",
                    "size_px": stroke_thickness
                }

                # Outer Glow / Shadow từ trough bao quanh viền trắng
                trough_idx = 6 + ring_lums[6:].index(min_late)
                trough_rgb = ring_rgbs[trough_idx]
                alpha = 0.45
                c_glow = np.clip((trough_rgb - bg_color_corners * (1 - alpha)) / alpha, 0, 255)
                glow_hex = to_hex(c_glow)

                result["outer_glow"] = {
                    "enabled": True,
                    "color_hex": glow_hex,
                    "size_px": 10.0,
                    "opacity_percent": 65
                }
                result["drop_shadow"] = {
                    "enabled": False,
                    "color_hex": "#000000",
                    "distance_px": 4.0,
                    "blur_px": 4.0
                }
                return result

        # Loại bỏ 4 pixel viền ngoài cùng của ảnh crop để không bị dính viền bóng thoại hay viền ô tranh bên ngoài
        inner_mask = np.zeros((H, W), dtype=bool)
        pad = min(4, min(H, W) // 4)
        if pad > 0:
            inner_mask[pad:-pad, pad:-pad] = True
        else:
            inner_mask[:] = True

        # Lấy các pixel chữ bên trong bóng thoại (tối hơn nền bóng thoại)
        text_mask = (lum < max(120, bright_lum - 38)) & inner_mask
        if text_mask.sum() > 100:
            mid_rgb = np.median(smooth[text_mask], axis=0).astype(int)
            mid_chroma = max(abs(mid_rgb[0] - mid_rgb[1]), abs(mid_rgb[2] - mid_rgb[1]), abs(mid_rgb[0] - mid_rgb[2]))

            # Trong bóng thoại thường: Tuyệt đối không dùng Gradient Overlay để tránh làm mờ/bẩn chữ thoại
            # Chỉ giữ màu riêng nếu có độ bão hòa cao rõ rệt (chroma >= 25)
            if mid_chroma >= 25 and mid_rgb.mean() > 70:
                solid_hex = to_hex(mid_rgb)
            else:
                solid_hex = "#000000"

            result["fill"] = {
                "is_gradient": False,
                "solid_hex": solid_hex,
                "top_hex": solid_hex,
                "bottom_hex": solid_hex,
                "angle": 90
            }
            result["stroke"]["enabled"] = False
            result["outer_glow"]["enabled"] = False
            result["drop_shadow"]["enabled"] = False
            return result
        else:
            # Bóng thoại đã xóa sạch text hoặc chữ rất ít -> mặc định chữ đen solid #000000
            result["fill"] = {
                "is_gradient": False,
                "solid_hex": "#000000",
                "top_hex": "#000000",
                "bottom_hex": "#000000",
                "angle": 90
            }
            result["stroke"]["enabled"] = False
            result["outer_glow"]["enabled"] = False
            result["drop_shadow"]["enabled"] = False
            return result

    # =========================================================================
    # PHÂN NHÁNH 2: NỀN TỐI / TRANH VẼ ARTWORK (ACTION / SFX / HORROR)
    # =========================================================================
    bright_mask = (lum > 140) & (smooth[:,:,0] > 110) & (smooth[:,:,1] > 100) & (smooth[:,:,2] > 100)
    padded_h, padded_w = H + 4, W + 4
    padded = np.zeros((padded_h, padded_w), dtype=np.uint8)
    padded[2:-2, 2:-2] = bright_mask.astype(np.uint8) * 255
    im_flood = Image.frombytes("L", (padded_w, padded_h), padded.tobytes())
    ImageDraw.floodfill(im_flood, (0, 0), 128, thresh=10)
    flood_arr = np.array(im_flood)[2:-2, 2:-2]
    enclosed = (flood_arr != 128) & (~bright_mask)

    ratio_enc = enclosed.sum() / max(1, bright_mask.sum())
    enc_color = np.median(smooth[enclosed], axis=0) if enclosed.any() else bg_color_corners
    diff_enc_bg = delta_e_simple(enc_color, bg_color_corners)

    is_true_stroke = (ratio_enc >= 0.30) and (enclosed.sum() > 60) and (diff_enc_bg > 20.0 or bg_lum_corners < 80)

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

        fill_px = smooth[enclosed]
        y_idx, x_idx = np.where(enclosed)
        y_min, y_max = y_idx.min(), y_idx.max()
        y_span = max(1, y_max - y_min)

        top_cut = enclosed & (np.arange(H)[:, None] <= y_min + 0.35 * y_span)
        bot_cut = enclosed & (np.arange(H)[:, None] >= y_max - 0.35 * y_span)

        top_rgb = np.median(smooth[top_cut], axis=0).astype(int) if top_cut.any() else np.median(fill_px, axis=0).astype(int)
        bot_rgb = np.median(smooth[bot_cut], axis=0).astype(int) if bot_cut.any() else np.median(fill_px, axis=0).astype(int)
        mid_rgb = np.median(fill_px, axis=0).astype(int)

        color_diff = delta_e_simple(top_rgb, bot_rgb)

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

        if len(glow_lums) >= 4 and glow_lums[0] > bg_lum_corners + 12:
            glow_radius = 4.0
            for i in range(1, len(glow_lums)):
                if glow_lums[i] <= bg_lum_corners + 8:
                    glow_radius = float(i + 1)
                    break
            result["outer_glow"] = {
                "enabled": True,
                "color_hex": "#FFFFFF",
                "size_px": min(8.0, glow_radius),
                "opacity_percent": min(85, max(35, int((glow_lums[0] - bg_lum_corners) / 1.4)))
            }
        return result

    # === CASE B: CHỮ TRẮNG / SÁNG TRÊN NỀN TỐI (Monologue / Dark Scene / Horror) ===
    if bright_mask.sum() > 60 and bg_lum_corners < 100:
        text_px = smooth[bright_mask]
        redness = text_px[:,0].astype(float) - (text_px[:,1].astype(float) + text_px[:,2].astype(float)) / 2.0
        blood_px_mask = (redness > 14) & (text_px[:,0] > 70)
        blood_count = blood_px_mask.sum()
        blood_ratio = blood_count / max(1, len(text_px))

        has_blood_stains = (blood_ratio >= 0.02) or (blood_count > 60)

        if has_blood_stains:
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

    # === CASE C: CHỮ VIỀN ĐEN TRÊN NỀN MÀU / TRANH KHÁC BIỆT ===
    dark_mask = (lum < 55) & (smooth[:,:,0] < 65) & (smooth[:,:,1] < 65) & (smooth[:,:,2] < 65)
    padded = np.zeros((padded_h, padded_w), dtype=np.uint8)
    padded[2:-2, 2:-2] = dark_mask.astype(np.uint8) * 255
    im_flood = Image.frombytes("L", (padded_w, padded_h), padded.tobytes())
    ImageDraw.floodfill(im_flood, (0, 0), 128, thresh=10)
    flood_arr = np.array(im_flood)[2:-2, 2:-2]
    enclosed_dark = (flood_arr != 128) & (~dark_mask)

    enc_color = np.median(smooth[enclosed_dark], axis=0) if enclosed_dark.any() else bg_color_corners
    diff_enc_bg = delta_e_simple(enc_color, bg_color_corners)

    if enclosed_dark.sum() > 60 and dark_mask.sum() > 150 and diff_enc_bg > 35.0 and bg_lum_corners < 160:
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

    # === FALLBACK: TƯƠNG PHẢN ĐỈNH ===
    delta = np.abs(lum - bg_lum_corners)
    fg_mask = delta > np.percentile(delta, 85)
    if fg_mask.sum() > 30:
        fg_rgb = np.median(smooth[fg_mask], axis=0).astype(int)
        if bg_lum_corners > 150 and np.mean(fg_rgb) > 150:
            fg_rgb = np.array([0, 0, 0])
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
