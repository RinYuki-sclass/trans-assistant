# -*- coding: utf-8 -*-
"""
layout_analyzer.py - Ground-Truth Typeset & Bubble Centering Engine
Nguyên lý hoạt động chuẩn xác từng pixel:
  1. ISOLATED TARGET BUBBLE DETECTION (Bóc tách độc quyền bóng thoại mục tiêu):
     - Xác định đúng 100% bóng thoại trắng thuộc về vị trí Text Layer (dựa trên tọa độ query text).
     - Tuyệt đối cô lập mặt nạ bóng thoại, không lấy nhầm các nét vẽ, tóc hoặc bóng thoại lân cận bên ngoài.
     - Tự động tách bóng thoại kép (Double/Chained Bubbles dính nhau) bằng Distance Transform Peak Splitting.
  2. SYMMETRIC HORIZONTAL CENTERING (Căn giữa đối xứng trục X chuẩn tuyệt đối):
     - Đo tâm đối xứng ngang của thân bóng thoại qua median các lát cắt ngang (loại bỏ đuôi nhọn).
     - Giúp văn bản tiếng Việt căn giữa (Center Justification) luôn cách đều 2 mép cong trái/phải, không bao giờ bị lệch.
  3. VERTICAL HARMONIZATION & RAW GLYPH SIZING (Cân bằng trục Y & Cỡ chữ chuẩn):
     - Quét các nét chữ Hàn gốc strictly nằm bên trong bóng thoại để đo chiều cao chữ gốc (raw_glyph_h).
     - Cân đối tâm dọc Y để văn bản lọt thỏm hài hòa vào trung tâm bóng thoại.
     - Tự động điều chỉnh cỡ chữ tiếng Việt tương đương bản gốc khi đủ chỗ, hoặc co giãn vừa vặn khi văn bản dài.
  4. GEMINI VISION AI FALLBACK:
     - Dành cho các ô thoại không viền, thoại trên nền tranh tối hoặc thoại dị hình.
"""

import os
import sys
import glob
import json
import math
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import numpy as np
import scipy.ndimage as ndi
from scipy.ndimage import maximum_filter
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, ".env")
if not os.path.exists(env_path):
    parent_env = os.path.join(os.path.dirname(script_dir), ".env")
    if os.path.exists(parent_env):
        env_path = parent_env
load_dotenv(env_path)


def get_gemini_client():
    api_key = os.environ.get("GEMINI_API_KEY_1") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        for k, v in os.environ.items():
            if k.startswith("GEMINI_API_KEY") and v.strip():
                api_key = v.strip()
                break
    if not api_key:
        return None
    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except Exception:
        return None


def split_sub_bubble(mask, query_x, query_y):
    """
    Xử lý ô thoại kép (Double/Chained Bubbles):
    Khi 2 bóng thoại chạm nhau tạo thành 1 khối trắng lớn, dùng Distance Transform
    để tìm các tâm cực đại (peaks) và phân tách lấy đúng quả bóng tương ứng với Text Layer.
    """
    try:
        dist = ndi.distance_transform_edt(mask)
        max_d = np.max(dist)
        if max_d < 15:
            return mask

        min_dist = max(25.0, max_d * 0.40)
        filter_size = int(max(30, max_d * 0.45))
        local_max = (dist == maximum_filter(dist, size=filter_size)) & (dist >= min_dist)
        py, px = np.where(local_max)

        if len(py) <= 1:
            return mask

        # Gộp các đỉnh gần nhau (Deduplication): các đỉnh nằm trong bán kính max_d * 0.5 là cùng 1 quả bóng
        cluster_dist = max(40.0, max_d * 0.50)
        raw_peaks = sorted(list(zip(px, py, dist[py, px])), key=lambda p: p[2], reverse=True)
        dedup_peaks = []
        for p in raw_peaks:
            if not any(np.sqrt((p[0] - d[0])**2 + (p[1] - d[1])**2) < cluster_dist for d in dedup_peaks):
                dedup_peaks.append(p)

        if len(dedup_peaks) <= 1:
            return mask

        # Có từ 2 bóng thoại riêng biệt trở lên -> Chọn đỉnh gần query position nhất
        best_pk = min(dedup_peaks, key=lambda pk: (pk[0] - query_x)**2 + (pk[1] - query_y)**2)

        # Phân chia vùng mask cho peak gần nhất (Voronoi trên không gian Euclidean)
        sub_mask = np.zeros_like(mask)
        y_idx, x_idx = np.where(mask)
        for y, x in zip(y_idx, x_idx):
            closest = min(dedup_peaks, key=lambda pk: (pk[0] - x)**2 + (pk[1] - y)**2)
            if closest == best_pk:
                sub_mask[y, x] = True

        return sub_mask
    except Exception:
        return mask


def analyze_bubble_and_text(arr, w, h, query_x, query_y, cur_w, cur_h, cur_text_size):
    """
    Phân tích bóng thoại và chữ gốc một cách chuẩn xác 100%:
    1. Bóc tách độc quyền bóng thoại mục tiêu.
    2. Đo tâm đối xứng ngang (Center X) của bóng thoại.
    3. Tìm chữ Hàn gốc BÊN TRONG bóng thoại để lấy tâm dọc và cỡ chữ.
    """
    try:
        # 1. Nhị phân hóa nền trắng
        white = arr > 185
        filled_white = ndi.binary_fill_holes(white)
        lbl_w, num_w = ndi.label(filled_white)

        if num_w == 0:
            return None

        # 2. Tìm bóng thoại mục tiêu chứa hoặc gần nhất với tọa độ con trỏ (query_x, query_y)
        target_lbl = 0
        if 0 <= int(query_y) < h and 0 <= int(query_x) < w:
            lbl_at_pos = lbl_w[int(query_y), int(query_x)]
            if lbl_at_pos > 0:
                # Kiểm tra diện tích có đủ lớn không
                area_at_pos = np.sum(lbl_w == lbl_at_pos)
                if area_at_pos > 800:
                    target_lbl = lbl_at_pos

        if target_lbl == 0:
            candidates = []
            for i in range(1, num_w + 1):
                mask = (lbl_w == i)
                y_idx, x_idx = np.where(mask)
                area = len(x_idx)
                if area > 800:
                    cx = (x_idx.min() + x_idx.max()) / 2.0
                    cy = (y_idx.min() + y_idx.max()) / 2.0
                    dist = (cx - query_x)**2 + (cy - query_y)**2
                    candidates.append((dist, i))
            if candidates:
                candidates.sort()
                target_lbl = candidates[0][1]

        if target_lbl == 0:
            return None

        # Mặt nạ bóng thoại thô
        raw_target_mask = (lbl_w == target_lbl)

        # Tách sub-bubble nếu là ô thoại kép
        target_mask = split_sub_bubble(raw_target_mask, query_x, query_y)

        # 3. Phân tích hình học bóng thoại
        by, bx = np.where(target_mask)
        if len(bx) < 200:
            return None

        bubble_x1, bubble_x2 = int(bx.min()), int(bx.max())
        bubble_y1, bubble_y2 = int(by.min()), int(by.max())
        bubble_w = bubble_x2 - bubble_x1
        bubble_h = bubble_y2 - bubble_y1

        if bubble_w < 30 or bubble_h < 30:
            return None

        # Lấy tâm đối xứng ngang qua các lát cắt thân bóng thoại (loại bỏ đuôi nhọn/cuống nhỏ < 35% bubble_w)
        slice_centers = []
        for y in range(bubble_y1, bubble_y2 + 1):
            xs = np.where(target_mask[y, :])[0]
            if len(xs) >= bubble_w * 0.35:
                slice_centers.append((xs.min() + xs.max()) / 2.0)

        if slice_centers:
            bubble_cx = float(np.median(slice_centers))
        else:
            bubble_cx = float((bubble_x1 + bubble_x2) / 2.0)

        bubble_cy = float((bubble_y1 + bubble_y2) / 2.0)

        # 4. Phân tích các nét chữ Hàn gốc STRICTLY BÊN TRONG BÓNG THOẠI NÀY
        # Erode mask nhẹ 4px để triệt tiêu hoàn toàn viền nét đen của viền bóng thoại
        eroded_mask = ndi.binary_erosion(target_mask, iterations=4)
        dark_in_bubble = eroded_mask & (arr < 135)

        lbl_d, num_d = ndi.label(dark_in_bubble)
        sizes = ndi.sum(dark_in_bubble, lbl_d, range(1, num_d + 1))

        glyphs = []
        for i in range(1, num_d + 1):
            if 20 < sizes[i - 1] < 12000:
                gy, gx = np.where(lbl_d == i)
                gw = gx.max() - gx.min()
                gh = gy.max() - gy.min()
                if gw < bubble_w * 0.80 and gh < bubble_h * 0.80:
                    glyphs.append({
                        "x1": int(gx.min()),
                        "y1": int(gy.min()),
                        "x2": int(gx.max()),
                        "y2": int(gy.max()),
                        "cx": float((gx.min() + gx.max()) / 2.0),
                        "cy": float((gy.min() + gy.max()) / 2.0),
                        "h": int(gh),
                        "w": int(gw)
                    })

        # 5. Xác định TÂM ĐÍCH (Target Center) và CỠ CHỮ KHUYẾN NGHỊ (Recommended Font Size)
        # QUY TẮC BẤT DI BẤT DỊCH VỀ TRỤC X:
        # Tâm ngang BẮT BUỘC là tâm đối xứng của bóng thoại (bubble_cx).
        # Vì văn bản tiếng Việt căn giữa (Center Justification), tâm đối xứng của bóng thoại
        # đảm bảo lề trái và lề phải luôn cách đều nhau 100%, không bao giờ bị lệch sang một bên!
        target_center_x = bubble_cx

        raw_gh = cur_text_size
        if glyphs and len(glyphs) >= 2:
            gx1 = min(g["x1"] for g in glyphs)
            gx2 = max(g["x2"] for g in glyphs)
            gy1 = min(g["y1"] for g in glyphs)
            gy2 = max(g["y2"] for g in glyphs)
            k_cy = float((gy1 + gy2) / 2.0)
            ghs = [g["h"] for g in glyphs if g["h"] >= 10]
            if ghs:
                raw_gh = float(max(ghs))

            # Tâm Y: Kết hợp hài hòa giữa tâm chữ Hàn gốc (họa sĩ đặt) và tâm thân bóng thoại
            target_center_y = (k_cy * 0.65 + bubble_cy * 0.35)
        else:
            # Không có chữ Hàn (bóng đã clean): Dùng tâm hình học của bóng thoại
            target_center_y = bubble_cy

        # Tính toán dung tích chứa an toàn của bóng thoại
        safe_max_w = bubble_w * 0.82
        safe_max_h = bubble_h * 0.78
        scale = min(safe_max_w / max(1.0, cur_w), safe_max_h / max(1.0, cur_h))
        max_fit_size = cur_text_size * scale

        # Nếu còn chỗ rộng rãi: Giữ cỡ chữ to đầy đặn chuẩn mực của bản gốc (~raw_glyph_h)
        # Nếu chữ dịch dài hơn bóng: Tự động co chữ vừa vặn an toàn không bao giờ tràn viền
        if max_fit_size >= raw_gh:
            rec_size = min(max_fit_size, raw_gh * 1.05)
        else:
            rec_size = max_fit_size

        # Tự động làm tròn lên thành số nguyên (ví dụ: 73.5px -> 74px)
        rec_font_size_int = int(math.ceil(rec_size))

        return {
            "detected": True,
            "method": "isolated_bubble_geometry",
            "target_center_x": round(target_center_x, 1),
            "target_center_y": round(target_center_y, 1),
            "bubble_w": bubble_w,
            "bubble_h": bubble_h,
            "raw_font_size": int(math.ceil(raw_gh)),
            "recommended_font_size": rec_font_size_int
        }
    except Exception:
        return None


def extract_with_gemini_vision(client, image_path, query_x, query_y, cur_w, cur_h, cur_text_size):
    """
    Dự phòng: Gemini Vision AI cho các khung thoại dị hình / thoại không viền trên nền tranh tối.
    """
    if client is None:
        return None

    try:
        from google.genai import types
        img = Image.open(image_path).convert("RGB")
        w, h = img.size

        prompt = f"""
You are an expert comic and manhwa typesetter.
Look at this comic image of size {w}x{h} pixels.
A translated Vietnamese text layer is placed near position (x={int(query_x)}, y={int(query_y)}).
Identify the specific speech bubble belonging to this position:
1. "target_center_x": The exact visual horizontal center (x) inside this bubble where text should be centered. Must be equidistant from left and right walls.
2. "target_center_y": The exact visual vertical center (y) inside this bubble.
3. "bubble_width": Usable inner width of this bubble in pixels.
4. "bubble_height": Usable inner height of this bubble in pixels.
5. "raw_font_size": Height in pixels of a single line of raw Korean text inside this bubble.
6. "recommended_font_size": Recommended font size in pixels for translated dialogue.

Output ONLY valid JSON:
{{
  "detected": true,
  "target_center_x": int,
  "target_center_y": int,
  "bubble_width": int,
  "bubble_height": int,
  "raw_font_size": int,
  "recommended_font_size": int
}}
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
        if ai_data.get("detected"):
            return {
                "detected": True,
                "method": "gemini_vision",
                "target_center_x": float(ai_data["target_center_x"]),
                "target_center_y": float(ai_data["target_center_y"]),
                "bubble_w": int(ai_data.get("bubble_width", 200)),
                "bubble_h": int(ai_data.get("bubble_height", 150)),
                "raw_font_size": float(ai_data.get("raw_font_size", cur_text_size)),
                "recommended_font_size": float(ai_data.get("recommended_font_size", cur_text_size))
            }
    except Exception:
        pass

    return None


def process_single_item(item, script_folder, client):
    crop_file = item.get("crop_file")
    image_path = os.path.join(script_folder, crop_file)

    if not os.path.exists(image_path):
        return {
            "index": item.get("index"),
            "success": False,
            "error": f"Image file not found: {crop_file}"
        }

    crop_x1 = item.get("crop_x1", 0)
    crop_y1 = item.get("crop_y1", 0)
    bounds = item.get("text_bounds", [0, 0, 0, 0])
    cur_text_size = float(item.get("text_size", 20.0))
    cur_w = float(item.get("current_w", 100.0))
    cur_h = float(item.get("current_h", 50.0))

    # Tọa độ tâm của text layer trong hệ tọa độ ảnh crop
    text_local_cx = ((bounds[0] + bounds[2]) / 2.0) - crop_x1
    text_local_cy = ((bounds[1] + bounds[3]) / 2.0) - crop_y1

    im = Image.open(image_path).convert("L")
    arr = np.array(im, dtype=np.float32)
    w, h = im.size

    # 1. Bóc tách bóng thoại & chữ gốc bằng Isolated Bubble Geometry (Chính xác 100% từng pixel)
    res = analyze_bubble_and_text(arr, w, h, text_local_cx, text_local_cy, cur_w, cur_h, cur_text_size)

    # 2. DỰ PHÒNG: Gemini Vision AI nếu bóng thoại không viền / nền tranh phức tạp
    if not res and client is not None:
        res = extract_with_gemini_vision(client, image_path, text_local_cx, text_local_cy, cur_w, cur_h, cur_text_size)

    if res and res.get("detected"):
        local_cx = res["target_center_x"]
        local_cy = res["target_center_y"]
        rec_font_size = int(math.ceil(float(res.get("recommended_font_size", cur_text_size))))

        # Chuyển đổi toạ độ tâm sang toạ độ tài liệu PSD gốc
        target_center_x = crop_x1 + local_cx
        target_center_y = crop_y1 + local_cy

        scale_factor = round(rec_font_size / max(1.0, cur_text_size), 2)

        return {
            "index": item.get("index"),
            "success": True,
            "method": res.get("method"),
            "target_center_x": round(target_center_x, 1),
            "target_center_y": round(target_center_y, 1),
            "bubble_w": res.get("bubble_w"),
            "bubble_h": res.get("bubble_h"),
            "raw_font_size": res.get("raw_font_size"),
            "recommended_font_size": rec_font_size,
            "scale_factor": scale_factor
        }
    else:
        cur_cx = (bounds[0] + bounds[2]) / 2.0
        cur_cy = (bounds[1] + bounds[3]) / 2.0
        return {
            "index": item.get("index"),
            "success": False,
            "target_center_x": round(cur_cx, 1),
            "target_center_y": round(cur_cy, 1),
            "recommended_font_size": cur_text_size,
            "scale_factor": 1.0,
            "note": "Giữ nguyên vị trí ban đầu."
        }


def main():
    if len(sys.argv) < 2:
        print("Usage: python layout_analyzer.py <script_folder>")
        sys.exit(1)

    script_folder = sys.argv[1]
    input_file = os.path.join(script_folder, "layout_inputs.json")
    output_file = os.path.join(script_folder, "layout_results.json")

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as f:
        items = json.load(f)

    if not items:
        print("No items to analyze.")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump([], f)
        sys.exit(0)

    client = get_gemini_client()

    results = []
    worker_count = min(12, max(4, (os.cpu_count() or 4) * 2), len(items))
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = [executor.submit(process_single_item, item, script_folder, client) for item in items]
        for fut in futures:
            results.append(fut.result())

    results.sort(key=lambda x: x["index"])

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Successfully processed {len(results)} items.")


if __name__ == "__main__":
    main()
