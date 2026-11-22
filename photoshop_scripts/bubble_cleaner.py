# -*- coding: utf-8 -*-
"""
bubble_cleaner.py - AI Speech Bubble Cleaner & SFX Eliminator
Tích hợp ComicTextDetector (Deep Learning ONNX) & Thuật toán Computer Vision:
  1. Tự động nhận diện bong bóng thoại (Speech/Thought Bubbles) và loại trừ 100% SFX.
  2. Phân tích độ thuần màu của nền (Background Variance & Brightness).
  3. Clean triệt để chữ raw bằng cv2.inpaint (Telea) & Pure White Fill siêu tốc.
  4. Hỗ trợ GPU DirectML (RTX 3050) siêu mượt, tự động fallback CPU nếu cần.
"""

import os
import sys
import json
import numpy as np
import cv2

script_dir = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(script_dir, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "comictextdetector.pt.onnx")

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
            print(f"[Bubble Cleaner] Không tìm thấy model tại {MODEL_PATH}")
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
        print(f"[Bubble Cleaner] Đã nạp ComicTextDetector trên {active_prov}!")
        return _ONNX_SESSION
    except Exception as e:
        print(f"[Bubble Cleaner Error] Không thể nạp ComicTextDetector: {e}")
        return None


def classify_text_block(crop_bgr, blk_box, seg_mask):
    """
    Phân loại khối chữ: Bong bóng thoại (Cần clean) vs SFX/Tranh vẽ (Cần giữ nguyên).
    - Bong bóng thoại: Nền đơn sắc (Trắng, Đen, hoặc Pastel đồng màu), độ lệch chuẩn màu thấp.
    - SFX / Tranh phức tạp: Nền vẽ nhân vật/cảnh vật/tóc/quần áo -> Độ lệch chuẩn màu cao.
    """
    bx1, by1, bx2, by2 = blk_box
    h, w = crop_bgr.shape[:2]
    bx1, by1 = max(0, bx1), max(0, by1)
    bx2, by2 = min(w, bx2), min(h, by2)
    if bx2 <= bx1 or by2 <= by1:
        return False, "invalid_box", None

    blk_img = crop_bgr[by1:by2, bx1:bx2]
    blk_seg = seg_mask[by1:by2, bx1:bx2]
    bg_mask = (blk_seg == 0)

    # Nếu hầu như toàn bộ khối chữ bị phủ kín mà không có nền -> bỏ qua
    if np.count_nonzero(bg_mask) < 25:
        return False, "no_background", None

    gray_blk = cv2.cvtColor(blk_img, cv2.COLOR_BGR2GRAY)
    bg_gray_pixels = gray_blk[bg_mask]

    bg_mean = float(np.mean(bg_gray_pixels))
    bg_std = float(np.std(bg_gray_pixels))

    # 1. Bong bóng thoại trắng tiêu chuẩn (Phần lớn manhwa)
    if bg_mean >= 195 and bg_std <= 32:
        return True, "white_bubble", {
            "type": "white",
            "mean": bg_mean,
            "std": bg_std
        }

    # 2. Bong bóng thoại đen / suy nghĩ tiêu cực
    if bg_mean <= 55 and bg_std <= 25:
        return True, "dark_bubble", {
            "type": "dark",
            "mean": bg_mean,
            "std": bg_std
        }

    # 3. Bong bóng thoại màu pastel / đơn sắc
    b_chan = blk_img[:, :, 0][bg_mask]
    g_chan = blk_img[:, :, 1][bg_mask]
    r_chan = blk_img[:, :, 2][bg_mask]
    max_chan_std = max(float(np.std(b_chan)), float(np.std(g_chan)), float(np.std(r_chan)))
    if max_chan_std <= 20:
        return True, "pastel_bubble", {
            "type": "pastel",
            "mean": bg_mean,
            "std": max_chan_std
        }

    # Nếu không thỏa mãn bất kỳ tiêu chí nền đồng nhất nào -> SFX trên nền tranh!
    return False, f"SFX_or_art (mean={bg_mean:.1f}, std={bg_std:.1f})", None


def clean_image_bubbles(session, img_bgr):
    """
    Thực hiện nhận diện và clean các bong bóng thoại trên một ảnh crop:
    - Loại trừ hoàn toàn SFX.
    - Trả về: (cleaned_bgr, bubbles_count, sfx_count)
    """
    if session is None or img_bgr is None:
        return img_bgr, 0, 0

    h, w = img_bgr.shape[:2]
    scale = 1024.0 / max(h, w)
    nh, nw = int(h * scale), int(w * scale)
    resized = cv2.resize(img_bgr, (nw, nh))

    input_tensor = np.zeros((1, 3, 1024, 1024), dtype=np.float32)
    rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    chw = np.transpose(rgb.astype(np.float32) / 255.0, (2, 0, 1))
    input_tensor[0, :, :nh, :nw] = chw

    outs = session.run(None, {"images": input_tensor})
    blk_raw = outs[0][0]  # Shape [64512, 7] - Block Anchors
    seg_raw = outs[1][0, 0] # Shape [1024, 1024] - Pixel Text Mask

    seg_mask = (seg_raw[:nh, :nw] > 0.25).astype(np.uint8) * 255
    seg_orig = cv2.resize(seg_mask, (w, h), interpolation=cv2.INTER_NEAREST)

    # NMS trích xuất các Text Blocks
    boxes = []
    confs = []
    conf_thresh = 0.22
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

    indices = cv2.dnn.NMSBoxes(boxes, confs, conf_thresh, nms_thresh)
    if len(indices) == 0:
        return img_bgr, 0, 0

    cleaned = img_bgr.copy()
    bubbles_count = 0
    sfx_count = 0

    # Kernel dãn nét chữ để bao trọn stroke và anti-aliasing
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated_mask = cv2.dilate(seg_orig, kernel, iterations=2)

    for idx in indices.flatten():
        bx, by, bw_b, bh_b = boxes[idx]
        bx1, by1 = max(0, bx), max(0, by)
        bx2, by2 = min(w, bx + bw_b), min(h, by + bh_b)

        is_bubble, reason, meta = classify_text_block(img_bgr, (bx1, by1, bx2, by2), seg_orig)
        if not is_bubble:
            sfx_count += 1
            continue

        bubbles_count += 1

        # Trích xuất mask chỉ riêng cho vùng bong bóng này
        bubble_mask = np.zeros((h, w), dtype=np.uint8)
        bubble_mask[by1:by2, bx1:bx2] = dilated_mask[by1:by2, bx1:bx2]

        if cv2.countNonZero(bubble_mask) == 0:
            continue

        b_type = meta["type"] if meta else "white"

        if b_type == "white" and meta["mean"] >= 248:
            # Bong bóng trắng tinh: Fill trực tiếp màu trắng sạch bóng 100%
            cleaned[bubble_mask > 0] = [255, 255, 255]
        else:
            # Bong bóng có gradient, pastel hoặc màu tối: Inpaint mượt mà bằng Telea
            inpaint_crop = cv2.inpaint(cleaned[by1:by2, bx1:bx2], bubble_mask[by1:by2, bx1:bx2], 4, cv2.INPAINT_TELEA)
            cleaned[by1:by2, bx1:bx2] = inpaint_crop

    return cleaned, bubbles_count, sfx_count


def process_batch(script_folder):
    """Xử lý hàng loạt crop theo input json từ Photoshop."""
    input_file = os.path.join(script_folder, "clean_inputs.json")
    output_file = os.path.join(script_folder, "clean_results.json")

    if not os.path.exists(input_file):
        print(f"[Bubble Cleaner] Không tìm thấy {input_file}")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        items = json.load(f)

    session = ensure_comic_text_model()
    if session is None:
        print("[Bubble Cleaner Error] Không thể khởi tạo mô hình AI!")
        return

    results = []
    total_bubbles = 0
    total_sfx_skipped = 0

    for item in items:
        idx = item.get("index")
        crop_file = item.get("crop_file")
        crop_path = os.path.join(script_folder, crop_file)

        if not os.path.exists(crop_path):
            results.append({
                "index": idx,
                "crop_file": crop_file,
                "cleaned": False,
                "reason": "file_not_found"
            })
            continue

        img = cv2.imread(crop_path)
        if img is None:
            results.append({
                "index": idx,
                "crop_file": crop_file,
                "cleaned": False,
                "reason": "cannot_read_image"
            })
            continue

        cleaned_img, b_cnt, sfx_cnt = clean_image_bubbles(session, img)
        total_bubbles += b_cnt
        total_sfx_skipped += sfx_cnt

        clean_file_name = f"clean_crop_{idx}.png"
        clean_file_path = os.path.join(script_folder, clean_file_name)

        if b_cnt > 0:
            cv2.imwrite(clean_file_path, cleaned_img)
            results.append({
                "index": idx,
                "crop_file": crop_file,
                "clean_file": clean_file_name,
                "cleaned": True,
                "bubbles_cleaned": b_cnt,
                "sfx_skipped": sfx_cnt,
                "crop_x1": item.get("crop_x1"),
                "crop_y1": item.get("crop_y1"),
                "crop_w": item.get("crop_w"),
                "crop_h": item.get("crop_h")
            })
        else:
            results.append({
                "index": idx,
                "crop_file": crop_file,
                "cleaned": False,
                "bubbles_cleaned": 0,
                "sfx_skipped": sfx_cnt,
                "reason": "no_bubbles_or_only_sfx"
            })

    results.sort(key=lambda x: x["index"])

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n[Bubble Cleaner Hoàn Tất] Đã clean: {total_bubbles} bóng thoại | Đã bỏ qua: {total_sfx_skipped} SFX/tranh vẽ.")


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else script_dir
    process_batch(folder)
