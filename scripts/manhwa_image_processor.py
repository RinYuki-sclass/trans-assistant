#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/manhwa_image_processor.py
Bộ công cụ tiền xử lý ảnh Manhwa / Truyện tranh độc lập:
- Sắp xếp tự nhiên (Natural Sort + Windows duplicate)
- Ghép dải ảnh ngắn (Stitching)
- Cắt ảnh dải dài với khoảng đè (Smart Slicing with overlap)
- Tối ưu chất lượng ảnh cho Multimodal Vision Model (Contrast, Sharpness, Resize, Quality)
- CLI tiện lợi dùng cho cả Antigravity subagent và scripts tự động
"""

import os
import sys
import re
import io
import argparse
from typing import List, Tuple, Dict, Any
from PIL import Image, ImageEnhance


def get_windows_sort_key(filename: str):
    """Hỗ trợ sort Natural và format copy của Windows: '60.jpg' vs '60 (1).jpg'"""
    name = os.path.basename(filename)
    m = re.match(r'^(.*?)(?: \(([0-9]+)\))?(\.[a-zA-Z0-9_]+)?$', name)
    if m:
        base, dup_num, ext = m.groups()
        base_parts = [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', base or "")]
        return base_parts + [int(dup_num) if dup_num else 0, ext or ""]
    return [name]


def sort_image_files(file_list: List[str]) -> List[str]:
    """Sắp xếp danh sách file theo thứ tự đọc tự nhiên."""
    return sorted(file_list, key=get_windows_sort_key)


def get_image_files(directory: str) -> List[str]:
    """Quét tất cả file ảnh hợp lệ trong thư mục."""
    valid_exts = {'.png', '.jpg', '.jpeg', '.webp', '.bmp'}
    images = []
    if not os.path.exists(directory):
        return []
    for f in os.listdir(directory):
        ext = os.path.splitext(f)[1].lower()
        if ext in valid_exts:
            images.append(os.path.join(directory, f))
    return sort_image_files(images)


def optimize_image_for_api(
    img: Image.Image,
    max_w: int = 1100,
    max_h: int = 5000,
    contrast: float = 1.2,
    sharpness: float = 1.5,
    quality: int = 88
) -> Image.Image:
    """
    Tăng cường độ tương phản và sắc nét cho chữ Hàn,
    resize thông minh và nén JPEG để tối ưu payload gửi tới AI Vision.
    """
    if not isinstance(img, Image.Image):
        return img

    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')

    # 1. Tăng độ tương phản
    if contrast != 1.0:
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)

    # 2. Tăng độ sắc nét
    if sharpness != 1.0:
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(sharpness)

    # 3. Resize thông minh giữ tỉ lệ
    w, h = img.size
    if w > max_w or h > max_h:
        ratio = min(max_w / w, max_h / h)
        new_w = max(1, int(w * ratio))
        new_h = max(1, int(h * ratio))
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # 4. Nén JPEG qua RAM buffer
    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=quality)
    buf.seek(0)
    return Image.open(buf)


def find_smart_cut_y(img: Image.Image, target_y: int, search_range: int = 500) -> Tuple[int, bool]:
    """
    Tìm điểm cắt thông minh (Smart Gutter Cut) tại khoảng trống trắng/đen giữa các khung tranh
    trong phạm vi [target_y - search_range, target_y].
    Trả về (best_y, is_clean_gutter).
    """
    import numpy as np

    w, h = img.size
    min_y = max(0, target_y - search_range)
    max_y = min(h - 1, target_y + 100)

    if min_y >= max_y:
        return target_y, False

    crop = img.crop((0, min_y, w, max_y)).convert('L')
    arr = np.array(crop, dtype=np.float32)

    # Tính độ biến thiên pixel và giá trị trung bình theo từng hàng ngang
    row_stds = np.std(arr, axis=1)
    row_means = np.mean(arr, axis=1)

    # Gutter chuẩn webtoon: nền trắng (mean > 220) hoặc nền đen (mean < 35) có độ biến thiên rất thấp (std < 6)
    is_white_gutter = (row_stds < 6.0) & (row_means > 220.0)
    is_black_gutter = (row_stds < 6.0) & (row_means < 35.0)
    is_gutter_row = is_white_gutter | is_black_gutter

    def _find_longest_block(mask):
        best_start = -1
        best_len = 0
        cur_start = -1
        cur_len = 0
        for idx, val in enumerate(mask):
            if val:
                if cur_start == -1:
                    cur_start = idx
                    cur_len = 1
                else:
                    cur_len += 1
            else:
                if cur_len > best_len:
                    best_len = cur_len
                    best_start = cur_start
                cur_start = -1
                cur_len = 0
        if cur_len > best_len:
            best_len = cur_len
            best_start = cur_start
        return best_start, best_len

    # Ưu tiên 1: Gutter trắng hoặc đen chuẩn của webtoon
    best_start, best_len = _find_longest_block(is_gutter_row)
    if best_len >= 8:
        mid_idx = best_start + best_len // 2
        return int(min_y + mid_idx), True

    # Ưu tiên 2: Bất kỳ hàng nào có màu đồng nhất (std < 5.0)
    any_solid_row = row_stds < 5.0
    best_start, best_len = _find_longest_block(any_solid_row)
    if best_len >= 8:
        mid_idx = best_start + best_len // 2
        return int(min_y + mid_idx), True

    # Ưu tiên 3: Chọn hàng có độ biến thiên nhỏ nhất gần target_y
    best_row = int(np.argmin(row_stds))
    return int(min_y + best_row), False


def split_long_image(img: Image.Image, max_h: int = 2400, overlap: int = 150) -> List[Image.Image]:
    """
    Tự động cắt ảnh dải dài thành các phần nhỏ (~2400px).
    Sử dụng Smart Gutter Detection để cắt vào khe trống giữa các khung tranh,
    tuyệt đối không cắt xuyên qua bóng thoại hay nét vẽ.
    """
    w, h = img.size
    if h <= max_h:
        return [img]

    parts = []
    y = 0
    while y < h:
        target_end = y + max_h
        if target_end >= h:
            parts.append(img.crop((0, y, w, h)))
            break

        cut_y, is_clean = find_smart_cut_y(img, target_end, search_range=500)
        # Đảm bảo lát cắt không quá ngắn (< 800px) nếu còn dài
        if cut_y <= y + 800:
            cut_y = target_end

        parts.append(img.crop((0, y, w, cut_y)))

        # Nếu cắt trúng gutter sạch thì không cần overlap; nếu không thì lùi lại overlap
        if is_clean:
            y = cut_y
        else:
            y = max(y + 1, cut_y - overlap)

    return parts


def stitch_images(
    image_paths: List[str],
    max_height: int = 2400
) -> List[Tuple[str, Image.Image]]:
    """
    Ghép chuỗi ảnh bị cắt ngắn thành các dải liền mạch tối đa max_height (~2400px).
    Trả về danh sách (suggested_name, PIL.Image).
    """
    loaded = []
    for p in image_paths:
        try:
            im = Image.open(p).convert('RGB')
            loaded.append((os.path.basename(p), im))
        except Exception as e:
            print(f"⚠️ Bỏ qua file lỗi {p}: {e}", file=sys.stderr)

    if not loaded:
        return []

    stitched_chunks = []
    current_chunk = []
    current_h = 0
    current_w = 0

    for name, img in loaded:
        if current_h + img.height > max_height and current_chunk:
            stitched_chunks.append((current_chunk, current_w, current_h))
            current_chunk = [(name, img)]
            current_h = img.height
            current_w = img.width
        else:
            current_chunk.append((name, img))
            current_h += img.height
            current_w = max(current_w, img.width)

    if current_chunk:
        stitched_chunks.append((current_chunk, current_w, current_h))

    results = []
    for i, (chunk, w, h) in enumerate(stitched_chunks):
        canvas = Image.new('RGB', (w, h), (255, 255, 255))
        y_offset = 0
        for _, img in chunk:
            x_offset = (w - img.width) // 2
            canvas.paste(img, (x_offset, y_offset))
            y_offset += img.height

        fname = f"slice_{i+1:03d}.jpg"
        results.append((fname, canvas))

    return results


def prepare_chapter_images(
    input_dir: str,
    output_dir: str,
    do_stitch: bool = True,
    max_height: int = 2400,
    overlap: int = 150,
    optimize: bool = True
) -> List[str]:
    """
    Pipeline hoàn chỉnh xử lý toàn bộ ảnh của 1 chapter:
    - Đọc ảnh và sắp xếp tự nhiên
    - Stitch hoặc Slice tùy kích thước
    - Tối ưu contrast/sharpness cho OCR Vision
    - Lưu vào output_dir (chuẩn bị sẵn sàng cho Model Pro)
    """
    os.makedirs(output_dir, exist_ok=True)
    raw_files = get_image_files(input_dir)
    if not raw_files:
        print(f"❌ Không tìm thấy ảnh nào trong: {input_dir}")
        return []

    print(f"🔍 Tìm thấy {len(raw_files)} ảnh raw. Đang phân tích...")

    final_slices: List[Tuple[str, Image.Image]] = []

    if do_stitch and len(raw_files) > 1:
        print(f"🧩 Đang ghép dải ảnh (Stitching, max_height={max_height}px)...")
        stitched = stitch_images(raw_files, max_height=max_height)
        for sname, simg in stitched:
            if simg.height > max_height:
                sub_parts = split_long_image(simg, max_h=max_height, overlap=overlap)
                for sp_idx, sp in enumerate(sub_parts):
                    base, ext = os.path.splitext(sname)
                    part_name = f"{base}_p{sp_idx+1:02d}{ext}"
                    final_slices.append((part_name, sp))
            else:
                final_slices.append((sname, simg))
    else:
        for idx, fpath in enumerate(raw_files):
            fname = os.path.basename(fpath)
            try:
                img = Image.open(fpath).convert('RGB')
            except Exception as e:
                print(f"⚠️ Lỗi mở ảnh {fname}: {e}")
                continue

            if img.height > max_height:
                sub_parts = split_long_image(img, max_h=max_height, overlap=overlap)
                base, ext = os.path.splitext(fname)
                for sp_idx, sp in enumerate(sub_parts):
                    part_name = f"{base}_p{sp_idx+1:02d}.jpg"
                    final_slices.append((part_name, sp))
            else:
                final_slices.append((fname, img))

    saved_paths = []
    print(f"💾 Đang tối ưu và lưu {len(final_slices)} ảnh đầu ra...")
    for idx, (name, img) in enumerate(final_slices):
        if optimize:
            processed = optimize_image_for_api(img, max_h=max_height)
        else:
            processed = img

        out_name = f"{idx+1:03d}_{name}" if not name.startswith(f"{idx+1:03d}") else name
        # Chuẩn hóa đuôi .jpg
        if not out_name.lower().endswith(('.jpg', '.jpeg')):
            out_name = os.path.splitext(out_name)[0] + ".jpg"

        out_path = os.path.join(output_dir, out_name)
        processed.save(out_path, format="JPEG", quality=90)
        saved_paths.append(out_path)

    print(f"✅ Đã xử lý xong {len(saved_paths)} ảnh lưu tại: {output_dir}")
    return saved_paths


def main():
    parser = argparse.ArgumentParser(description="Manhwa Image Pre-processing Tool for Vision AI")
    parser.add_argument("--input", "-i", required=True, help="Thư mục chứa ảnh raw ban đầu")
    parser.add_argument("--output", "-o", required=True, help="Thư mục lưu ảnh đã xử lý")
    parser.add_argument("--no-stitch", action="store_true", help="Không tự động ghép dải ảnh")
    parser.add_argument("--max-height", type=int, default=2400, help="Chiều cao tối đa mỗi lát ảnh (default: 2400px)")
    parser.add_argument("--overlap", type=int, default=150, help="Độ đè chồng lấp khi cắt ảnh quá dài (default: 150px)")
    parser.add_argument("--no-opt", action="store_true", help="Bỏ qua bước tối ưu contrast/sharpness")

    args = parser.parse_args()
    prepare_chapter_images(
        input_dir=args.input,
        output_dir=args.output,
        do_stitch=not args.no_stitch,
        max_height=args.max_height,
        overlap=args.overlap,
        optimize=not args.no_opt
    )


if __name__ == "__main__":
    main()
