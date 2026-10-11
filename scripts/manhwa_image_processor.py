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


def split_long_image(img: Image.Image, max_h: int = 4500, overlap: int = 250) -> List[Image.Image]:
    """
    Tự động cắt ảnh dải dài thành các phần nhỏ với khoảng đè (overlap)
    để không bị đứt hoặc mất bong bóng thoại ở đường cắt.
    """
    w, h = img.size
    if h <= max_h:
        return [img]

    parts = []
    y = 0
    while y < h:
        end_y = y + max_h
        if end_y > h:
            end_y = h

        box = (0, y, w, end_y)
        parts.append(img.crop(box))

        if end_y == h:
            break
        y = end_y - overlap
        if y < 0:
            y = 0
    return parts


def stitch_images(
    image_paths: List[str],
    max_height: int = 4500
) -> List[Tuple[str, Image.Image]]:
    """
    Ghép chuỗi ảnh bị cắt ngắn thành các dải liền mạch tối đa max_height.
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
    max_height: int = 4500,
    overlap: int = 250,
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
    parser.add_argument("--max-height", type=int, default=4500, help="Chiều cao tối đa mỗi lát ảnh (default: 4500px)")
    parser.add_argument("--overlap", type=int, default=250, help="Độ đè chồng lấp khi cắt ảnh quá dài (default: 250px)")
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
