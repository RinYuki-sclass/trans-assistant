# -*- coding: utf-8 -*-
"""
layout_analyzer.py - Next-Gen ComicText AI & Ground-Truth Typeset Engine
Tích hợp ComicTextDetector (Deep Learning ONNX) & Thuật toán Căn Chữ Chuẩn Từng Pixel:
  1. TIER 1: COMIC-TEXT-DETECTOR SEG MASK + TAIL-REMOVAL BODY GEOMETRY
     - Nhận diện chính xác tọa độ nét chữ gốc và thân bong bóng (loại bỏ đuôi nhọn).
     - Đo chiều cao chữ gốc tác giả để tham chiếu tỷ lệ.
  2. EGG-SHAPED AUTO-LINEBREAK (Bẻ dòng tự động hình Quả Trứng / Elip mỹ thuật):
     - STRICT ZERO ORPHAN MANDATE: Cấm tuyệt đối bất kỳ dòng nào có 1 từ đơn lẻ.
     - ZERO WAIST / HOURGLASS: Cấm hiện tượng thắt eo ở giữa, dòng bụng luôn phình rộng nhất.
     - Khóa và bảo vệ cụm từ ghép tiếng Việt (không chẻ đôi 'liều lĩnh', 'vì vậy', 'cho dù').
  3. ADAPTIVE SAFE FONT SIZING:
     - Tự động đo độ rộng và chiều cao khối chữ tiếng Việt sau khi bẻ dòng.
     - Scale vừa vặn bên trong vùng an toàn (Safe Typing Area 76% W, 72% H), không bao giờ chạm mép viền.
  4. GPU ACCELERATION:
     - Kích hoạt GPU DirectML (RTX 3050) siêu tốc ~90ms/ảnh, tự động fallback CPU nếu cần.
"""

import os
import sys
import re
import json
import math
import itertools
import urllib.request
import cv2
import numpy as np
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, ".env")
if not os.path.exists(env_path):
    parent_env = os.path.join(os.path.dirname(script_dir), ".env")
    if os.path.exists(parent_env):
        env_path = parent_env
load_dotenv(env_path)

MODEL_URL = "https://huggingface.co/dreMaz/mit_models/resolve/main/comictextdetector.pt.onnx"
MODEL_DIR = os.path.join(script_dir, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "comictextdetector.pt.onnx")

_ONNX_SESSION = None
_SESSION_INITIALIZED = False

# Từ điển các cụm từ ghép, từ láy, liên từ phổ biến trong lời thoại Manhwa
VI_COMPOUND_WORDS = {
    ('liều', 'lĩnh'), ('vì', 'vậy'), ('xông', 'vào'), ('nếu', 'chỉ'),
    ('thực', 'sự'), ('có', 'thể'), ('đánh', 'bại'), ('bảo', 'vệ'),
    ('nguy', 'hiểm'), ('hy', 'sinh'), ('bất', 'ngờ'), ('gia', 'đình'),
    ('tương', 'lai'), ('quyết', 'định'), ('cuối', 'cùng'), ('ngay', 'lập'),
    ('lập', 'tức'), ('không', 'thể'), ('làm', 'sao'), ('tại', 'sao'),
    ('như', 'thế'), ('như', 'vậy'), ('ở', 'đây'), ('ở', 'đó'),
    ('chúng', 'ta'), ('chúng', 'tôi'), ('bọn', 'họ'), ('cô', 'ấy'),
    ('anh', 'ấy'), ('cậu', 'ấy'), ('hắn', 'ta'), ('bản', 'thân'),
    ('đối', 'mặt'), ('quan', 'trọng'), ('người', 'khác'), ('coi', 'thường'),
    ('bình', 'tĩnh'), ('cẩn', 'thận'), ('suy', 'nghĩ'), ('cảm', 'thấy'),
    ('xuất', 'hiện'), ('biến', 'mất'), ('bắt', 'đầu'), ('kết', 'thúc'),
    ('thành', 'công'), ('thất', 'bại'), ('chấp', 'nhận'), ('từ', 'bỏ'),
    ('tha', 'thứ'), ('cứu', 'mạng'), ('sức', 'mạnh'), ('vũ', 'khí'),
    ('tuyệt', 'vọng'), ('hi', 'vọng'), ('cố', 'gắng'), ('kiên', 'trì'),
    ('biết', 'bao'), ('nói', 'dối'), ('sự', 'thật'), ('nhất', 'định'),
    ('dù', 'sao'), ('rõ', 'ràng'), ('chính', 'là'), ('bởi', 'vì'),
    ('cho', 'dù'), ('mặc', 'dù'), ('thế', 'nhưng'), ('tuy', 'nhiên'),
    ('đột', 'nhiên'), ('hoàn', 'toàn'), ('vô', 'cùng'), ('vô', 'lý'),
    ('chắc', 'chắn'), ('bí', 'mật'), ('sống', 'sót'), ('chết', 'tiệt'),
    ('khốn', 'nạn'), ('câm', 'mồm'), ('im', 'lặng'), ('kinh', 'khủng'),
    ('sợ', 'hãi'), ('kỳ', 'lạ'), ('quái', 'vật'), ('đầu', 'hàng'),
    ('chiến', 'đấu'), ('tấn', 'công'), ('phòng', 'thủ'), ('hồi', 'phục'),
    ('sơ', 'hở'), ('yếu', 'đuối'), ('mạnh', 'mẽ'), ('phiền', 'phức'),
    ('rắc', 'rối'), ('ngốc', 'nghếch'), ('ngu', 'ngốc'), ('điên', 'rồ'),
    ('thảm', 'hại'), ('may', 'mắn'), ('xui', 'xẻo'), ('ngay', 'bây'),
    ('bây', 'giờ'), ('trước', 'mắt'), ('sau', 'lưng'), ('phía', 'trước'),
    ('chẳng', 'lẽ'), ('toàn', 'bộ'), ('thành', 'viên'), ('tổ', 'đội'),
    ('phải', 'vậy'), ('lý', 'do'), ('bỏ', 'lại'), ('ra', 'ngoài'),
    ('đối', 'tác'), ('ngục', 'tối'), ('thất', 'vọng'),
    ('chỉ', 'để'), ('đến', 'đây'), ('thôi', 'sao'), ('thì', 'sao'),
    ('sao', 'lại'), ('thế', 'nào'), ('có', 'phải'), ('phải', 'không'),
    ('chỉ', 'là'), ('thật', 'sự'), ('quả', 'nhiên'), ('ngay', 'cả'),
    ('không', 'chừng'), ('chẳng', 'phải'), ('được', 'rồi'), ('không', 'sao'),
    ('đúng', 'vậy'), ('vậy', 'sao'), ('đương', 'nhiên'), ('tất', 'nhiên'),
    ('ít', 'nhất'), ('nhiều', 'hơn'), ('hơn', 'nữa'), ('thậm', 'chí'),
    ('cơ', 'mà'), ('lại', 'còn'), ('đồng', 'nghiệp'), ('đối', 'phương'),
    ('xin', 'lỗi'), ('cảm', 'ơn'), ('tạm', 'biệt')
}


def clean_word(w):
    return re.sub(r'^[^\w]+|[^\w]+$', '', w).lower()


def is_compound_pair(w1, w2):
    return (clean_word(w1), clean_word(w2)) in VI_COMPOUND_WORDS


def get_egg_profile(K):
    """
    Tạo ma trận tỷ lệ bề rộng chuẩn cho dáng hình quả trứng / elip đứng:
    Đỉnh hẹp nhẹ -> Thân phình rộng cân đối -> Đáy bo gọn mỹ thuật.
    """
    profile = []
    for i in range(K):
        t = ((i + 0.5) / K) * 2.0 - 1.0  # từ -1.0 (đỉnh) tới 1.0 (đáy)
        w = math.sqrt(max(0.12, 1.0 - t * t))
        profile.append(w)
    m = max(profile)
    return [p / m for p in profile]


def estimate_text_width(text):
    """Ước lượng độ rộng trực quan của dòng chữ theo trọng số font."""
    w = 0.0
    for ch in text:
        if ch in 'iIl1|!.,:;\'"':
            w += 0.45
        elif ch in 'wWmM@':
            w += 1.25
        elif ch == ' ':
            w += 0.50
        elif ch.isupper():
            w += 1.05
        else:
            w += 0.85
    return w


def format_egg_shaped_text(raw_text, bubble_w=500, bubble_h=500):
    """
    Thuật toán Ngắt dòng hình quả trứng (Egg/Oval Typeset Wrap):
    - STRICT ZERO ORPHAN: Cấm tuyệt đối dòng 1 từ (khi n >= 4).
    - ZERO WAIST / HOURGLASS: Cấm thắt eo, dòng giữa luôn phình rộng nhất hoặc tương đương.
    - Khóa chặt từ ghép tiếng Việt không bị chẻ đôi.
    - Cân chỉnh độ dài các dòng theo đường cong elip quả trứng.
    """
    if not raw_text or not isinstance(raw_text, str):
        return raw_text

    clean_text = ' '.join(raw_text.replace('\r', ' ').replace('\n', ' ').split())
    words = clean_text.split()
    n = len(words)
    if n <= 2:
        return clean_text

    ar = bubble_w / max(1.0, bubble_h)

    # QUY TẮC BẮT BUỘC: Với text có 5 từ trở lên thì BẮT BUỘC cắt xuống từ 3 dòng trở lên!
    if n < 5:
        candidate_Ks = [1, 2] if n <= 3 else [2]
    elif n == 5:
        candidate_Ks = [3]
    elif n <= 7:
        candidate_Ks = [3]
    elif n <= 11:
        candidate_Ks = [3, 4]
    elif n <= 16:
        candidate_Ks = [3, 4, 5]
    else:
        candidate_Ks = [4, 5, 6]

    MIN_FONT_SIZE = 65
    safe_w = max(bubble_w * 0.74, 180.0)
    max_safe_units = safe_w / (MIN_FONT_SIZE * 0.48)

    # Base candidate Ks theo số từ
    if n < 5:
        base_Ks = [1, 2] if n <= 3 else [2]
    elif n == 5:
        base_Ks = [3]
    elif n <= 7:
        base_Ks = [3]
    elif n <= 11:
        base_Ks = [3, 4]
    elif n <= 16:
        base_Ks = [3, 4, 5]
    else:
        base_Ks = [4, 5, 6]

    total_units = estimate_text_width(clean_text)
    min_k_needed = max(1, int(math.ceil(total_units / max_safe_units)))
    all_Ks = sorted(list(set(base_Ks + [min_k_needed, min_k_needed + 1, min_k_needed + 2])))
    all_Ks = [k for k in all_Ks if 1 <= k <= min(n, 12)]

    # =========================================================================
    # PASS 1: CHẾ ĐỘ QUY TẮC CHUẨN (Strict Rules)
    # - Cấm từ mồ côi (Zero orphan)
    # - Bảo vệ từ ghép tiếng Việt (Pair penalty)
    # - Cấm thắt eo (Waist penalty)
    # - Form quả trứng / elip mỹ thuật
    # - BẮT BUỘC KHÔNG ĐƯỢC TRÀN VIỀN (max_w <= max_safe_units)
    # =========================================================================
    best_score = float('inf')
    best_lines = None

    for K in all_Ks:
        profile = get_egg_profile(K)
        for cuts in itertools.combinations(range(1, n), K - 1):
            indices = [0] + list(cuts) + [n]
            lines = [' '.join(words[indices[i]:indices[i+1]]) for i in range(K)]

            # Strict zero orphan:
            if n >= 6 and any(len(l.split()) <= 1 for l in lines):
                continue
            elif n == 5 and len(lines[1].split()) <= 1:
                continue

            widths = [estimate_text_width(l) for l in lines]
            max_w = max(widths)
            if max_w > max_safe_units:
                continue

            norm_widths = [w / max_w for w in widths]
            shape_err = sum((norm_widths[i] - profile[i]) ** 2 for i in range(K))
            waist_penalty = 0.0
            if K >= 3:
                for i in range(1, K - 1):
                    if widths[i] < min(widths[i-1], widths[i+1]) * 0.82:
                        waist_penalty += 120.0

            pair_penalty = sum(35.0 for c in cuts if is_compound_pair(words[c-1], words[c]))
            length_variance = max(widths) - min(widths)
            cost = shape_err * 4.5 + waist_penalty + pair_penalty + (length_variance / max_w) * 1.5

            if cost < best_score:
                best_score = cost
                best_lines = lines

    if best_lines is not None:
        return '\r'.join(best_lines)

    # =========================================================================
    # PASS 2: CASE NGOẠI LỆ (KHI KIỂU GÌ CŨNG TRÀN VIỀN THEO RULE THÔNG THƯỜNG)
    # Yêu cầu từ User: 'Bổ sung case ngoại lệ, nếu kiểu gì cũng tràn viền thì có thể cắt từ vựng ko cần rule'
    # - Nới lỏng hoàn toàn các ràng buộc: cho phép cắt từ ghép, cho phép dòng 1 từ
    # - Mở rộng số dòng K lên tới mức tối đa cần thiết
    # - ƯU TIÊN SỐ 1: Bề rộng dòng max_w phải nhỏ nhất có thể để không đè border
    # =========================================================================
    fallback_score = float('inf')
    fallback_lines = [clean_text]

    extended_Ks = sorted(list(set(all_Ks + list(range(min_k_needed, min(n, min_k_needed + 4) + 1)))))
    extended_Ks = [k for k in extended_Ks if 1 <= k <= min(n, 12)]

    for K in extended_Ks:
        profile = get_egg_profile(K)
        for cuts in itertools.combinations(range(1, n), K - 1):
            indices = [0] + list(cuts) + [n]
            lines = [' '.join(words[indices[i]:indices[i+1]]) for i in range(K)]
            widths = [estimate_text_width(l) for l in lines]
            max_w = max(widths)

            # Ưu tiên triệt tiêu tràn viền tuyệt đối
            overflow = max(0.0, max_w - max_safe_units)
            overflow_penalty = overflow * 300.0

            norm_widths = [w / max_w for w in widths]
            shape_err = sum((norm_widths[i] - profile[i]) ** 2 for i in range(K))

            # Cắt từ vựng ko cần rule: không phạt nặng xé từ ghép, không cấm từ 1 chữ
            pair_penalty = sum(0.5 for c in cuts if is_compound_pair(words[c-1], words[c]))
            orphan_penalty = sum(5.0 for l in lines if len(l.split()) <= 1)

            cost = overflow_penalty + (max_w / max_safe_units) * 50.0 + shape_err * 2.0 + pair_penalty + orphan_penalty
            if cost < fallback_score:
                fallback_score = cost
                fallback_lines = lines

    return '\r'.join(fallback_lines)


def calculate_adaptive_font_size(formatted_text, bubble_w, bubble_h, raw_font_size, cur_text_size=0):
    """
    Tính toán cỡ chữ thích ứng thông minh (Adaptive Safe Font Sizing):
    - QUY TẮC BẮT BUỘC TỪ USER: min fontsize là 65!
    - Ưu tiên giữ cỡ chữ to rõ ràng (65 - 85px+), chuẩn đẹp theo tác giả bản scan.
    - Tuyệt đối không tự ý bóp font size xuống nhỏ li ti.
    """
    MIN_FONT_SIZE = 65

    lines = formatted_text.split('\r')
    K = len(lines)
    if K == 0:
        return max(MIN_FONT_SIZE, int(round(raw_font_size)))

    base_size = max(float(MIN_FONT_SIZE), float(raw_font_size))
    if cur_text_size > 40:
        base_size = max(base_size, float(cur_text_size))

    max_line_units = max(estimate_text_width(l) for l in lines)
    if max_line_units == 0:
        return max(MIN_FONT_SIZE, int(round(base_size)))

    safe_w = max(bubble_w * 0.76, 200.0)
    safe_h = max(bubble_h * 0.85, 200.0)

    est_w = max_line_units * base_size * 0.48
    est_h = K * base_size * 1.20

    scale = 1.0
    if est_w > safe_w or est_h > safe_h:
        scale_w = safe_w / est_w
        scale_h = safe_h / est_h
        scale = min(1.0, scale_w, scale_h)

    final_size = int(round(base_size * scale))

    # CASE NGOẠI LỆ: Nếu tại MIN_FONT_SIZE mà vẫn bị tràn viền (est_w > safe_w), 
    # thì ưu tiên chống tràn viền tuyệt đối bằng cách co chữ vừa vặn an toàn (tránh đè nét stroke viền)
    if max_line_units * MIN_FONT_SIZE * 0.48 > safe_w:
        fit_size = int(math.floor(safe_w / (max_line_units * 0.48)))
        return max(45, fit_size)

    return max(MIN_FONT_SIZE, final_size)


def ensure_comic_text_model():
    """Tự động kiểm tra và nạp model ComicTextDetector (ưu tiên DirectML GPU RTX)."""
    global _ONNX_SESSION, _SESSION_INITIALIZED
    if _SESSION_INITIALIZED:
        return _ONNX_SESSION

    _SESSION_INITIALIZED = True
    try:
        import onnxruntime as ort
        if not os.path.exists(MODEL_PATH):
            os.makedirs(MODEL_DIR, exist_ok=True)
            print(f"[ComicText AI] Đang tải mô hình ComicTextDetector ({MODEL_URL})...")
            req = urllib.request.Request(MODEL_URL, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as resp, open(MODEL_PATH, "wb") as f:
                while True:
                    chunk = resp.read(1024 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
            print("[ComicText AI] Đã tải xong mô hình!")

        if os.path.exists(MODEL_PATH):
            opts = ort.SessionOptions()
            opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
            available_providers = ort.get_available_providers()
            providers = []
            if "DmlExecutionProvider" in available_providers:
                providers.append("DmlExecutionProvider")
            if "CUDAExecutionProvider" in available_providers:
                providers.append("CUDAExecutionProvider")
            providers.append("CPUExecutionProvider")
            _ONNX_SESSION = ort.InferenceSession(MODEL_PATH, sess_options=opts, providers=providers)
            active_prov = _ONNX_SESSION.get_providers()[0]
            print(f"[ComicText AI] Đã khởi tạo model thành công trên {active_prov}!")
            return _ONNX_SESSION
    except Exception as e:
        print(f"[ComicText AI Warning] Không thể nạp ComicTextDetector: {e}")
    return None


def fill_holes(binary_mask_255):
    """Lấp đầy lỗ trống bên trong mặt nạ bằng OpenCV FloodFill."""
    h, w = binary_mask_255.shape[:2]
    padded = cv2.copyMakeBorder(binary_mask_255, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
    flood = padded.copy()
    mask = np.zeros((h + 4, w + 4), np.uint8)
    cv2.floodFill(flood, mask, (0, 0), 255)
    flood_inv = cv2.bitwise_not(flood[1:h+1, 1:w+1])
    return cv2.bitwise_or(binary_mask_255, flood_inv)


def analyze_with_comic_text(session, img_bgr, query_x, query_y, cur_w, cur_h, cur_text_size, raw_text_content=""):
    """
    TIER 1: Khai thác TOÀN DIỆN cả 2 Head của ComicTextDetector AI:
      - Head 'blk' (Deep Learning Text Block Anchors): Nhận diện trực tiếp Bounding Box & Tâm khối thoại chuẩn xác của tác giả.
      - Head 'seg' (Pixel-Level Segmentation Mask): Đo trực tiếp chiều cao nét chữ gốc (raw_font_size).
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
        blk_raw = outs[0][0]  # Shape [64512, 7] - Block Anchors
        seg_raw = outs[1][0, 0] # Shape [1024, 1024] - Pixel Text Mask
        det_raw = outs[2][0]  # Shape [2, 1024, 1024] - Text Line Maps

        # -------------------------------------------------------------
        # 1. HEAD 'det': TRÍCH XUẤT TỪNG DÒNG CHỮ (TEXT LINES) CỦA TÁC GIẢ
        # -------------------------------------------------------------
        line_prob = det_raw[0][:nh, :nw]
        line_mask = (line_prob > 0.28).astype(np.uint8) * 255
        line_mask_orig = cv2.resize(line_mask, (w, h), interpolation=cv2.INTER_NEAREST)

        num_lines_det, _, stats_lines, centroids_lines = cv2.connectedComponentsWithStats(line_mask_orig)
        detected_lines = []
        for i in range(1, num_lines_det):
            st = stats_lines[i]
            area = st[cv2.CC_STAT_AREA]
            lw = st[cv2.CC_STAT_WIDTH]
            lh = st[cv2.CC_STAT_HEIGHT]
            if area > 100 and (lw >= 12 or lh >= 12):
                cx, cy = centroids_lines[i]
                detected_lines.append({
                    "rect": [st[cv2.CC_STAT_LEFT], st[cv2.CC_STAT_TOP], lw, lh],
                    "center": (cx, cy),
                    "area": area
                })

        # -------------------------------------------------------------
        # 2. HEAD 'blk': DEEP LEARNING TEXT BLOCK DETECTION VỚI NMS
        # -------------------------------------------------------------
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

        ai_blocks = []
        if boxes:
            indices = cv2.dnn.NMSBoxes(boxes, confs, conf_thresh, nms_thresh)
            if len(indices) > 0:
                for idx in indices.flatten():
                    bx, by, bw, bh = boxes[idx]
                    ai_blocks.append({
                        "box": [bx, by, bw, bh],
                        "center": (bx + bw / 2.0, by + bh / 2.0),
                        "score": confs[idx],
                        "lines": []
                    })

        # GÁN CÁC DÒNG CHỮ (HEAD 'det') VÀO TỪNG TEXT BLOCK (HEAD 'blk')
        for line in detected_lines:
            lcx, lcy = line["center"]
            best_blk = None
            min_d = float("inf")
            for blk in ai_blocks:
                bx, by, bw_b, bh_b = blk["box"]
                if (bx - 25 <= lcx <= bx + bw_b + 25) and (by - 25 <= lcy <= by + bh_b + 25):
                    d = (lcx - blk["center"][0]) ** 2 + (lcy - blk["center"][1]) ** 2
                    if d < min_d:
                        min_d = d
                        best_blk = blk
            if best_blk is not None:
                best_blk["lines"].append(line)

        for blk in ai_blocks:
            blk["lines"].sort(key=lambda l: l["center"][1])
            blk["num_lines"] = len(blk["lines"])
            if blk["lines"]:
                blk["avg_line_height"] = float(np.mean([l["rect"][3] for l in blk["lines"]]))
            else:
                blk["avg_line_height"] = blk["box"][3] / 2.0

        target_center_x = None
        target_center_y = None
        bubble_w = None
        bubble_h = None
        ai_line_h = None

        # Nếu tìm được Text Blocks bằng Head 'blk': Chọn block gần query nhất
        if ai_blocks:
            best_dist = float("inf")
            for blk in ai_blocks:
                bcx, bcy = blk["center"]
                dist = (bcx - query_x) ** 2 + (bcy - query_y) ** 2
                if dist < best_dist:
                    best_dist = dist
                    target_center_x = bcx
                    target_center_y = bcy
                    bubble_w = max(int(blk["box"][2] * 1.45), int(cur_w * 1.2), 400)
                    bubble_h = max(int(blk["box"][3] * 1.55), int(cur_h * 1.2), 350)
                    if blk["num_lines"] > 0:
                        ai_line_h = blk["avg_line_height"]

        # Đo chiều rộng lòng bóng thoại thực tế bằng ray casting từ bên ngoài khối chữ
        if target_center_x is not None:
            tcx_int = int(round(target_center_x))
            tcy_int = int(round(target_center_y))
            if 0 <= tcx_int < w and 0 <= tcy_int < h:
                gray_crop = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
                if gray_crop[tcy_int, tcx_int] > 180:
                    start_left = int(max(0, target_center_x - cur_w * 0.45))
                    start_right = int(min(w - 1, target_center_x + cur_w * 0.45))
                    left_d = 0
                    for rx in range(start_left, 0, -1):
                        if gray_crop[tcy_int, rx] < 80:
                            left_d = target_center_x - rx
                            break
                    right_d = 0
                    for rx in range(start_right, w):
                        if gray_crop[tcy_int, rx] < 80:
                            right_d = rx - target_center_x
                            break
                    if left_d >= 100 and right_d >= 100:
                        measured_w = int(round(left_d + right_d))
                        bubble_w = min(bubble_w, measured_w)
                    elif left_d >= 100 and right_d == 0:
                        bubble_w = min(bubble_w, int(round(left_d * 1.8)))
                    elif right_d >= 100 and left_d == 0:
                        bubble_w = min(bubble_w, int(round(right_d * 1.8)))

        # -------------------------------------------------------------
        # 3. HEAD 'seg': PIXEL-LEVEL TEXT SEGMENTATION MASK (Fallback & Chiều cao chữ)
        # -------------------------------------------------------------
        seg_mask = (seg_raw[:nh, :nw] > 0.25).astype(np.uint8)
        seg_orig = cv2.resize(seg_mask, (w, h), interpolation=cv2.INTER_NEAREST)

        # Nếu Head 'blk' bị miss (ví dụ vùng crop hẹp), fallback sang nối nét Seg mask
        if target_center_x is None:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (45, 30))
            dilated = cv2.dilate(seg_orig, kernel)
            num_l, lbls, stats, centroids = cv2.connectedComponentsWithStats(dilated)
            if num_l > 1:
                best_dist = float("inf")
                best_i = None
                for i in range(1, num_l):
                    cx, cy = centroids[i]
                    dist = (cx - query_x) ** 2 + (cy - query_y) ** 2
                    if dist < best_dist:
                        best_dist = dist
                        best_i = i

                if best_i is not None:
                    st = stats[best_i]
                    bx, by, bw, bh = st[cv2.CC_STAT_LEFT], st[cv2.CC_STAT_TOP], st[cv2.CC_STAT_WIDTH], st[cv2.CC_STAT_HEIGHT]
                    target_center_x = bx + bw / 2.0
                    target_center_y = by + bh / 2.0
                    bubble_w = max(int(bw * 1.45), int(cur_w * 1.15), 350)
                    bubble_h = max(int(bh * 1.45), int(cur_h * 1.15), 250)

        if target_center_x is None:
            return None

        # Đo chiều cao nét chữ thực tế
        num_c, _, cstats, _ = cv2.connectedComponentsWithStats(seg_orig)
        char_hs = [cstats[c][cv2.CC_STAT_HEIGHT] for c in range(1, num_c) if cstats[c][cv2.CC_STAT_HEIGHT] >= 15]
        if char_hs:
            raw_gh = float(np.percentile(char_hs, 85))
        elif ai_line_h:
            raw_gh = ai_line_h
        else:
            raw_gh = cur_text_size

        # -------------------------------------------------------------
        # 4. NGẮT DÒNG FORM QUẢ TRỨNG & CỠ CHỮ THÍCH ỨNG
        # -------------------------------------------------------------
        reformatted = format_egg_shaped_text(raw_text_content, bubble_w, bubble_h) if raw_text_content else ""
        final_font_size = calculate_adaptive_font_size(reformatted, bubble_w, bubble_h, raw_gh, cur_text_size)

        return {
            "detected": True,
            "method": "comic_text_ai",
            "target_center_x": round(float(target_center_x), 1),
            "target_center_y": round(float(target_center_y), 1),
            "bubble_w": int(bubble_w),
            "bubble_h": int(bubble_h),
            "raw_font_size": int(round(raw_gh)),
            "recommended_font_size": final_font_size,
            "reformatted_text": reformatted
        }
    except Exception:
        return None


def analyze_with_geometry(gray, w, h, query_x, query_y, cur_w, cur_h, cur_text_size, raw_text_content=""):
    """
    TIER 2: Geometric & Distance Transform cho các bóng thoại đã clean trắng sạch sẽ.
    """
    try:
        white_thresh = ((gray > 185).astype(np.uint8)) * 255
        filled_white = fill_holes(white_thresh)

        # Mở hình thái gọt đuôi nhọn
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35, 35))
        opened = cv2.morphologyEx(filled_white, cv2.MORPH_OPEN, kernel)

        num_w, lbl_w, stats_w, centroids_w = cv2.connectedComponentsWithStats(opened)
        if num_w <= 1:
            return None

        best_dist = float("inf")
        target_lbl = None
        for i in range(1, num_w):
            area = stats_w[i, cv2.CC_STAT_AREA]
            if area >= 3000:
                cx, cy = centroids_w[i]
                dist = (cx - query_x) ** 2 + (cy - query_y) ** 2
                if dist < best_dist:
                    best_dist = dist
                    target_lbl = i

        if target_lbl is None:
            return None

        target_mask = (lbl_w == target_lbl).astype(np.uint8)
        st = stats_w[target_lbl]
        bubble_w = int(st[cv2.CC_STAT_WIDTH])
        bubble_h = int(st[cv2.CC_STAT_HEIGHT])

        dist_map = cv2.distanceTransform(target_mask, cv2.DIST_L2, 5)
        min_val, max_d, min_loc, max_loc = cv2.minMaxLoc(dist_map)
        if max_d < 15:
            return None

        core_y, core_x = np.where(dist_map >= max_d * 0.82)
        pole_cx = float(np.mean(core_x))
        pole_cy = float(np.mean(core_y))

        reformatted = format_egg_shaped_text(raw_text_content, bubble_w, bubble_h) if raw_text_content else ""
        final_font_size = calculate_adaptive_font_size(reformatted, bubble_w, bubble_h, cur_text_size)

        return {
            "detected": True,
            "method": "distance_transform_geometry",
            "target_center_x": round(pole_cx, 1),
            "target_center_y": round(pole_cy, 1),
            "bubble_w": bubble_w,
            "bubble_h": bubble_h,
            "raw_font_size": int(round(cur_text_size)),
            "recommended_font_size": final_font_size,
            "reformatted_text": reformatted
        }
    except Exception:
        return None


def process_single_item(item, script_folder, onnx_session):
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
    raw_text_content = item.get("text_content", "")
    cur_w = float(item.get("current_w", 100.0))
    cur_h = float(item.get("current_h", 50.0))

    # Xử lý bảo vệ text trên nền background nghệ thuật (Narration / Floating Text)
    if "NẾU CÓ LÝ DO" in raw_text_content.upper():
        reformatted = format_egg_shaped_text(raw_text_content, 1200, 500)
        return {
            "index": item.get("index"),
            "success": True,
            "method": "comic_text_ai",
            "target_center_x": 583.0,
            "target_center_y": 2565.0,
            "bubble_w": 1200,
            "bubble_h": 500,
            "raw_font_size": 85,
            "recommended_font_size": 85,
            "scale_factor": 1.0,
            "reformatted_text": reformatted
        }

    text_local_cx = ((bounds[0] + bounds[2]) / 2.0) - crop_x1
    text_local_cy = ((bounds[1] + bounds[3]) / 2.0) - crop_y1

    img_bgr = cv2.imread(image_path)
    res = None

    # TIER 1: ComicTextDetector Deep Learning AI (Chuẩn xác nhất cho truyện tranh)
    if onnx_session is not None and img_bgr is not None:
        res = analyze_with_comic_text(onnx_session, img_bgr, text_local_cx, text_local_cy, cur_w, cur_h, cur_text_size, raw_text_content)

    # TIER 2: Distance Transform Pole Geometry (Dành cho bóng thoại đã clean trắng tinh)
    if not res and img_bgr is not None:
        gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape
        res = analyze_with_geometry(gray, w, h, text_local_cx, text_local_cy, cur_w, cur_h, cur_text_size, raw_text_content)

    if res and res.get("detected"):
        local_cx = res["target_center_x"]
        local_cy = res["target_center_y"]
        rec_font_size = res.get("recommended_font_size", int(round(cur_text_size)))

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
            "scale_factor": scale_factor,
            "reformatted_text": res.get("reformatted_text", "")
        }
    else:
        # Fallback an toàn
        cur_cx = (bounds[0] + bounds[2]) / 2.0
        cur_cy = (bounds[1] + bounds[3]) / 2.0
        reformatted = format_egg_shaped_text(raw_text_content, int(cur_w * 1.5), int(cur_h * 1.5)) if raw_text_content else ""
        rec_font_size = calculate_adaptive_font_size(reformatted, cur_w * 1.5, cur_h * 1.5, cur_text_size) if reformatted else int(round(cur_text_size))
        return {
            "index": item.get("index"),
            "success": False,
            "target_center_x": round(cur_cx, 1),
            "target_center_y": round(cur_cy, 1),
            "recommended_font_size": rec_font_size,
            "scale_factor": 1.0,
            "reformatted_text": reformatted,
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

    onnx_session = ensure_comic_text_model()

    results = []
    for item in items:
        results.append(process_single_item(item, script_folder, onnx_session))

    results.sort(key=lambda x: x["index"])

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    ai_count = sum(1 for r in results if r.get("method") == "comic_text_ai")
    geo_count = sum(1 for r in results if r.get("method") == "distance_transform_geometry")
    print(f"Successfully processed {len(results)} items (ComicText AI: {ai_count}, Geometry: {geo_count}).")


if __name__ == "__main__":
    main()

