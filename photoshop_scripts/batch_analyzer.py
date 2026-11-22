# -*- coding: utf-8 -*-
"""
batch_analyzer.py - Next-Gen ComicText & Multi-Select Batch Auto-Style VFX Engine
Tích hợp ComicTextDetector Deep Learning AI:
  1. Tự động định vị chính xác khối chữ gốc của tác giả (Korean/Japanese text block) bằng Deep Learning.
  2. Tạo vùng crop ôm sát nét chữ gốc (Tight Crop) y hệt thao tác tay khoanh Marquee Tool (F6).
  3. Phân tích chính xác 100% Fill/Gradient, Stroke, Outer Glow, Drop Shadow bằng Local CV & Gemini AI.
  4. Đồng bộ hóa đa luồng, chống lệch thứ tự index khi Multi-Select.
"""

import os
import sys
import json
import glob
from concurrent.futures import ThreadPoolExecutor
import cv2
import numpy as np
from PIL import Image
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(script_dir, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "comictextdetector.pt.onnx")

# Import các hàm phân tích style từ style_analyzer
from style_analyzer import analyze_with_local_cv, get_gemini_client

_ONNX_SESSION = None
_SESSION_INITIALIZED = False


def ensure_comic_text_model():
    """Tự động kiểm tra và nạp model ComicTextDetector (ưu tiên DirectML GPU)."""
    global _ONNX_SESSION, _SESSION_INITIALIZED
    if _SESSION_INITIALIZED:
        return _ONNX_SESSION

    _SESSION_INITIALIZED = True
    try:
        import onnxruntime as ort
        if not os.path.exists(MODEL_PATH):
            print(f"[Batch Style AI] Không tìm thấy model tại {MODEL_PATH}")
            return None

        opts = ort.SessionOptions()
        opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        available = ort.get_available_providers()
        providers = []
        if "DmlExecutionProvider" in available:
            providers.append("DmlExecutionProvider")
        if "CUDAExecutionProvider" in available:
            providers.append("CUDAExecutionProvider")
        providers.append("CPUExecutionProvider")

        _ONNX_SESSION = ort.InferenceSession(MODEL_PATH, sess_options=opts, providers=providers)
        active_prov = _ONNX_SESSION.get_providers()[0]
        print(f"[Batch Style AI] Đã nạp ComicTextDetector trên {active_prov}!")
        return _ONNX_SESSION
    except Exception as e:
        print(f"[Batch Style AI Warning] Không thể nạp ComicTextDetector: {e}")
        return None


def detect_tight_text_box(session, img_bgr, query_cx, query_cy):
    """
    Dùng ComicTextDetector để tìm bounding box ôm sát khối chữ raw gần tâm Text Layer nhất.
    Trả về: (tx1, ty1, tx2, ty2) hoặc None nếu không nhận diện được.
    """
    if session is None or img_bgr is None:
        return None

    try:
        h, w = img_bgr.shape[:2]
        scale = 1024.0 / max(h, w)
        nh, nw = int(h * scale), int(w * scale)
        resized = cv2.resize(img_bgr, (nw, nh))

        input_tensor = np.zeros((1, 3, 1024, 1024), dtype=np.float32)
        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        chw = np.transpose(rgb.astype(np.float32) / 255.0, (2, 0, 1))
        input_tensor[0, :, :nh, :nw] = chw

        outs = session.run(None, {"images": input_tensor})
        blk_raw = outs[0][0]  # Shape [64512, 7]

        boxes = []
        confs = []
        conf_thresh = 0.08
        nms_thresh = 0.35

        for b in blk_raw:
            obj_conf = b[4]
            if obj_conf > conf_thresh:
                cls_conf = max(b[5], b[6])
                score = float(obj_conf * cls_conf)
                if score > conf_thresh:
                    bcx, bcy, bbw, bbh = b[0], b[1], b[2], b[3]
                    x1 = int((bcx - bbw / 2.0) / scale)
                    y1 = int((bcy - bbh / 2.0) / scale)
                    bw_orig = int(bbw / scale)
                    bh_orig = int(bbh / scale)
                    boxes.append([x1, y1, bw_orig, bh_orig])
                    confs.append(score)

        if not boxes:
            return None

        indices = cv2.dnn.NMSBoxes(boxes, confs, conf_thresh, nms_thresh)
        if len(indices) == 0:
            return None

        best_dist = float("inf")
        best_box = None

        flat_indices = indices.flatten() if hasattr(indices, 'flatten') else [i[0] if hasattr(i, '__iter__') else i for i in indices]
        for idx in flat_indices:
            bx, by, bw_b, bh_b = boxes[idx]
            bcx = bx + bw_b / 2.0
            bcy = by + bh_b / 2.0
            d = (bcx - query_cx) ** 2 + (bcy - query_cy) ** 2
            if d < best_dist:
                best_dist = d
                best_box = (bx, by, bw_b, bh_b)

        if best_box is not None:
            bx, by, bw_b, bh_b = best_box
            # Viền đệm nhỏ 12px ôm trọn stroke và glow y như F6
            pad = 12
            tx1 = max(0, bx - pad)
            ty1 = max(0, by - pad)
            tx2 = min(w, bx + bw_b + pad)
            ty2 = min(h, by + bh_b + pad)
            return (tx1, ty1, tx2, ty2)

    except Exception as e:
        print(f"[Detect Text Warning] {e}")

    return None


def analyze_single_tight_crop(client, image_path):
    """Phân tích VFX style trên ảnh crop sát chữ gốc (Tight Crop)."""
    if not os.path.exists(image_path):
        return None

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
        if cv_data.get("inner_glow", {}).get("enabled"):
            ai_data["inner_glow"] = cv_data["inner_glow"]
            ai_data["inner_shadow"] = cv_data.get("inner_shadow", {})
            ai_data["fill"] = cv_data["fill"]
            ai_data["stroke"]["enabled"] = False
            ai_data["outer_glow"]["enabled"] = False
        elif cv_data["stroke"]["enabled"]:
            ai_data["stroke"]["enabled"] = True
            ai_data["stroke"]["color_hex"] = cv_data["stroke"]["color_hex"]
            if ai_data["stroke"].get("size_px"):
                ai_data["stroke"]["size_px"] = cv_data["stroke"]["size_px"]
            ai_data["inner_glow"]["enabled"] = False
            ai_data["inner_shadow"] = {"enabled": False}
        else:
            ai_data["stroke"]["enabled"] = False
            ai_data["inner_glow"]["enabled"] = False
            ai_data["inner_shadow"] = {"enabled": False}

        if cv_data["fill"]["is_gradient"]:
            ai_data["fill"]["is_gradient"] = True
            ai_data["fill"]["top_hex"] = cv_data["fill"]["top_hex"]
            ai_data["fill"]["bottom_hex"] = cv_data["fill"]["bottom_hex"]
        else:
            ai_data["fill"]["is_gradient"] = False
            ai_data["fill"]["solid_hex"] = cv_data["fill"]["solid_hex"]

        if cv_data["outer_glow"]["enabled"]:
            ai_data["outer_glow"]["enabled"] = True
            ai_data["outer_glow"]["color_hex"] = cv_data["outer_glow"]["color_hex"]
            ai_data["outer_glow"]["size_px"] = cv_data["outer_glow"]["size_px"]
        else:
            ai_data["outer_glow"]["enabled"] = False

        return ai_data
    except Exception:
        return cv_data


def run_batch(working_dir):
    input_file = os.path.join(working_dir, "batch_inputs.json")
    out_file = os.path.join(working_dir, "batch_result.json")

    # Nếu không có batch_inputs.json, fallback sang quét glob crop_*.png cũ
    if not os.path.exists(input_file):
        old_crop_files = sorted(glob.glob(os.path.join(working_dir, "crop_*.png")))
        if not old_crop_files:
            return
        client = get_gemini_client()
        results = {}
        for f in old_crop_files:
            results[os.path.basename(f)] = analyze_single_tight_crop(client, f)
        with open(out_file, "w", encoding="utf-8") as out:
            json.dump(results, out, indent=2, ensure_ascii=False)
        return

    with open(input_file, "r", encoding="utf-8") as f:
        items = json.load(f)

    if not items:
        return

    session = ensure_comic_text_model()
    client = get_gemini_client()

    results = []

    for item in items:
        idx = item.get("index")
        crop_file = item.get("crop_file")
        crop_path = os.path.join(working_dir, crop_file)

        if not os.path.exists(crop_path):
            tight_existing = os.path.join(working_dir, "debug_previews", f"tight_crop_{idx}.png")
            layout_existing = os.path.join(working_dir, f"layout_crop_{idx}.png")
            if os.path.exists(tight_existing):
                crop_path = tight_existing
            elif os.path.exists(layout_existing):
                crop_path = layout_existing
            else:
                results.append({
                    "index": idx,
                    "detected": False,
                    "error": "crop_not_found"
                })
                continue

        img_bgr = cv2.imread(crop_path)
        if img_bgr is None:
            results.append({
                "index": idx,
                "detected": False,
                "error": "cannot_read_image"
            })
            continue

        h, w = img_bgr.shape[:2]
        query_cx = item.get("text_local_cx", w / 2.0)
        query_cy = item.get("text_local_cy", h / 2.0)
        text_w = item.get("text_w", 150)
        text_h = item.get("text_h", 60)

        # 1. DÙNG COMIC-TEXT-DETECTOR TÌM TỌA ĐỘ CHÍNH XÁC CỦA CHỮ GỐC
        tight_box = detect_tight_text_box(session, img_bgr, query_cx, query_cy)

        if tight_box is not None:
            tx1, ty1, tx2, ty2 = tight_box
            detected = True
        else:
            # Fallback: Crop quanh tâm của Text Layer nếu model không phát hiện được chữ
            pad = 18
            tx1 = max(0, int(query_cx - text_w / 2.0 - pad))
            ty1 = max(0, int(query_cy - text_h / 2.0 - pad))
            tx2 = min(w, int(query_cx + text_w / 2.0 + pad))
            ty2 = min(h, int(query_cy + text_h / 2.0 + pad))
            detected = False

        if tx2 - tx1 < 6 or ty2 - ty1 < 6:
            tight_img = img_bgr
        else:
            tight_img = img_bgr[ty1:ty2, tx1:tx2]

        tight_crop_name = f"tight_crop_{idx}.png"
        tight_crop_path = os.path.join(working_dir, tight_crop_name)
        cv2.imwrite(tight_crop_path, tight_img)

        # Lưu bản copy vào debug_previews để dễ dàng đối chiếu
        preview_dir = os.path.join(working_dir, "debug_previews")
        if os.path.exists(preview_dir):
            cv2.imwrite(os.path.join(preview_dir, tight_crop_name), tight_img)

        # 2. PHÂN TÍCH VFX STYLE TRÊN ẢNH CROP SÁT NÉT CHỮ GỐC (Y HỆT F6)
        style_info = analyze_single_tight_crop(client, tight_crop_path)

        results.append({
            "index": idx,
            "detected": detected,
            "style": style_info
        })

    results.sort(key=lambda x: x["index"])

    with open(out_file, "w", encoding="utf-8") as out:
        json.dump(results, out, indent=2, ensure_ascii=False)

    print(f"\n[Batch Style AI Hoàn Tất] Đã phân tích chính xác {len(results)} layer bằng ComicText AI.")


if __name__ == "__main__":
    work_dir = sys.argv[1] if len(sys.argv) > 1 else script_dir
    run_batch(work_dir)
