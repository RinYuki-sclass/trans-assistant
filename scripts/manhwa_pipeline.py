#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/manhwa_pipeline.py
Automated Manhwa Translation Pipeline for Antigravity Orchestrator:
- Reads raw chapter images
- Slices tall images with overlap for high-precision OCR
- Rotates Gemini API keys across requests
- Strictly enforces Manhwa translation rules and visual speaker attribution
- Deduplicates overlap boundaries
- Writes to output/manhwa_history/<chapter>/ (images/ and script.txt)
- Performs automated QC audit
"""

import os
import sys
import re
import time
import json
import shutil
from typing import List, Tuple, Dict, Any, Optional
from PIL import Image, ImageEnhance
Image.MAX_IMAGE_PIXELS = None
from dotenv import load_dotenv

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HIST_DIR = os.path.join(BASE_DIR, "output", "manhwa_history")

# System prompt adhering strictly to rules
SYSTEM_PROMPT = """You are an expert Manhwa/Webtoon translator and typesetter assistant using Gemini Vision.
Your primary task is to accurately OCR Korean text from speech bubbles and translate it into natural Vietnamese.

TASK:
1. Examine this manhwa image carefully.
2. Read dialogue bubbles and text boxes strictly in natural reading order (top to bottom, right to left).
3. Transcribe Korean text with 100% precision. Do not hallucinate or omit words.
4. Identify who is speaking [Speaker/narrator] using visual balloon tails and character visual features:
   - [Han Yoojin]: Black hair, warm brown eyes, slender build, often wearing knit sweater/cardigan or Haeyeon suit.
   - [Han Yoohyun]: Black neat hair, sharp dark/grey eyes, tall, broad shoulders, black suit or battle armor, fire skills. Calls Yoojin "Hyung".
   - [Sung Hyunjae]: Bright blonde swept-back hair, amber/gold eyes, tall (1m90), luxurious 3-piece suit, teasing smile, lightning/chains. Calls Yoojin "Han Yoojin-gun".
   - [Park Yerim]: Long dark hair in high ponytail, water/ice skills, school uniform/sportswear. Calls Yoojin "Ahjussi" or "Chú".
   - [Song Taewon]: Black crew cut, dark tired eyes with prominent dark circles, bulky physique, black civil service suit. Calls Yoojin "Han Yoojin-ssi".
   - [Noah Rugir]: Wavy shoulder-length light blonde hair, clear blue eyes, shy expression. Gold baby dragon form or dragon wings.
   - [Moon Hyuna]: Short magenta/pink hair, athletic build, Breaker guild master.
   - [Yoo Myungwoo]: Messy brown/black hair, round glasses, blacksmith attire/apron.
   - [Narrator]: Background narration boxes, rectangular explanation panels.
   - [Độc thoại]: Internal monologue (specify [Han Yoojin - Độc thoại] if Yoojin's inner thoughts).
   - [SFX]: Crucial sound effects only (explosions, thunder, crashes). Skip minor background SFX.
   - [Dân chúng] / [Thợ săn] / [Người qua đường]: Background crowd/extras.
   - [Bóng thoại]: If speaker cannot be identified.
5. Translate into natural, flowing Vietnamese adhering strictly to:
   - Punctuation Matching (SUPREME RULE): The number, type, and order of punctuation marks (!, !!, ?, ?!, ~, ~!!, ..., ., commas, quotes) in the Vietnamese translation MUST MATCH the KR line 100%. If KR has no ending punctuation, Vietnamese MUST have no ending punctuation.
   - "형" (Hyung): When Han Yoohyun addresses Han Yoojin as "형", ALWAYS preserve as "Hyung" (capital H, never translate to "anh").
   - Name Suffixes: -아/-야 -> -ah/-yah (Yoohyun-ah, Yerim-ah, Yoojin-ah); -씨 -> -ssi (Sung Hyunjae-ssi, Sungmo-ssi, Han Yoojin-ssi); -군 -> -gun (Han Yoojin-gun); -양 -> -yang.
   - Pronouns:
     * Han Yoojin <-> Han Yoohyun: Anh - Em (Yoohyun-ah / em trai) & Em - Hyung / Anh.
     * Sung Hyunjae <-> Han Yoojin: Tôi - Cậu (Han Yoojin-gun) & Tôi - Anh (Sung Hyunjae-ssi).
     * Park Yerim <-> Han Yoojin: Tôi/Bọn mình - Chú/Ahjussi.
     * Park Yerim <-> Han Yoohyun: Tôi - Anh (Hội trưởng).
     * Park Yerim <-> Sung Hyunjae: Cháu - Chú (chú Hội trưởng).
     * Song Taewon <-> Han Yoojin: Tôi - Cậu (Han Yoojin-ssi) & Tôi - Anh.
     * Yoo Myungwoo: Tự xưng "Tôi" hoặc "Mình".

CRITICAL FORMAT RULES:
- If a bubble has multiple lines, join them into a SINGLE line separated by space.
- EXACT structure for each bubble (NO 'VN:' prefix, NO extra markdown):
[Speaker/narrator]
KR: <Exact Korean transcription in a single line>
<Natural Vietnamese translation in a single line>

- If the image contains NO dialogue or text, return exactly:
[NO_TEXT]
"""

class KeyRotator:
    def __init__(self):
        from google import genai
        self.keys = []
        i = 1
        while True:
            k = os.environ.get(f"GEMINI_API_KEY_{i}") or (os.environ.get("GEMINI_API_KEY") if i == 1 else None)
            if not k or not k.strip():
                break
            self.keys.append(k.strip())
            i += 1
            if i > 20:
                break
        if not self.keys:
            raise ValueError("No GEMINI_API_KEY found in environment or .env!")
        
        self.clients = [genai.Client(api_key=k) for k in self.keys]
        self.current_idx = 0
        print(f"🔑 Initialized KeyRotator with {len(self.keys)} API key(s).")

    def get_client(self):
        return self.clients[self.current_idx], self.current_idx

    def rotate(self):
        self.current_idx = (self.current_idx + 1) % len(self.clients)
        print(f"🔄 Rotated to API Key {self.current_idx + 1}/{len(self.keys)}")


def slice_image(img_path: str, cache_dir: str, max_h: int = 4500, overlap: int = 250) -> List[str]:
    """Splits a long image into overlapping slices and saves them."""
    os.makedirs(cache_dir, exist_ok=True)
    fname = os.path.basename(img_path)
    base, _ = os.path.splitext(fname)

    im = Image.open(img_path).convert('RGB')
    w, h = im.size

    if h <= max_h:
        out_p = os.path.join(cache_dir, f"{base}_p01.jpg")
        im.save(out_p, format="JPEG", quality=95)
        return [out_p]

    slices = []
    y = 0
    p_idx = 1
    while y < h:
        end_y = min(y + max_h, h)
        box = (0, y, w, end_y)
        cropped = im.crop(box)

        # Enhance contrast slightly for text clarity
        enhancer = ImageEnhance.Contrast(cropped)
        enhanced = enhancer.enhance(1.15)

        out_p = os.path.join(cache_dir, f"{base}_p{p_idx:02d}.jpg")
        enhanced.save(out_p, format="JPEG", quality=95)
        slices.append(out_p)

        if end_y == h:
            break
        y = end_y - overlap
        p_idx += 1

    return slices


def parse_dialogue_blocks(raw_text: str) -> List[Dict[str, str]]:
    """Parses LLM output into individual dialogue blocks."""
    if not raw_text or "[NO_TEXT]" in raw_text:
        return []

    blocks = []
    pattern = r'\[([^\]]+)\]\s*\n\s*KR:\s*([^\n]+)\s*\n\s*(?:(?:VN|VI):\s*)?([^\n]+)'
    matches = re.findall(pattern, raw_text)
    for speaker, kr, vi in matches:
        blocks.append({
            "speaker": speaker.strip(),
            "kr": kr.strip(),
            "vi": vi.strip()
        })
    return blocks


def deduplicate_blocks(blocks_list: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Deduplicates blocks that appear repeatedly across overlapping slices."""
    cleaned = []
    for b in blocks_list:
        kr = b["kr"].replace(" ", "").strip()
        if not kr:
            continue
        is_dup = False
        for prev in cleaned[-3:]:
            prev_kr = prev["kr"].replace(" ", "").strip()
            if kr == prev_kr or (len(kr) > 6 and (kr in prev_kr or prev_kr in kr)):
                is_dup = True
                break
        if not is_dup:
            cleaned.append(b)
    return cleaned


def format_blocks_to_text(blocks: List[Dict[str, str]]) -> str:
    lines = []
    for b in blocks:
        lines.append(f"[{b['speaker']}]")
        lines.append(f"KR: {b['kr']}")
        lines.append(b['vi'])
        lines.append("")
    return "\n".join(lines).strip()


def run_ocr_and_translate(rotator: KeyRotator, slice_path: str, models: List[str] = None) -> str:
    """Sends slice to Gemini API with retry and key rotation."""
    if models is None:
        models = ["gemini-3.8-flash", "gemini-3-flash-preview", "gemini-2.5-flash-lite"]

    from google.genai import types

    safety_settings = [
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
    ]

    img = Image.open(slice_path)
    prompt = "Extract and translate all dialogue bubbles from this manhwa slice strictly following the system instructions."

    max_retries = 6
    for attempt in range(max_retries):
        client, key_idx = rotator.get_client()
        model_name = models[attempt % len(models)]
        try:
            config = types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.1,
                safety_settings=safety_settings
            )
            response = client.models.generate_content(
                model=model_name,
                contents=[img, prompt],
                config=config
            )
            res_text = response.text or ""
            return res_text.strip()
        except Exception as e:
            err_str = str(e)
            print(f"⚠️ Error on {os.path.basename(slice_path)} (Key {key_idx+1}, {model_name}): {err_str[:120]}")
            rotator.rotate()
            time.sleep(3)

    return ""


def process_chapter(chapter_num: str, raw_dir: str):
    rotator = KeyRotator()

    dest_dir = os.path.join(HIST_DIR, chapter_num)
    dest_images_dir = os.path.join(dest_dir, "images")
    cache_dir = os.path.join(dest_dir, ".cache_slices")
    script_path = os.path.join(dest_dir, "script.txt")
    cache_json_path = os.path.join(dest_dir, ".progress.json")

    os.makedirs(dest_images_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    # 1. Natural sort of raw images
    raw_files = [f for f in os.listdir(raw_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    raw_files.sort(key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else x)

    print(f"📖 Processing Chapter {chapter_num} with {len(raw_files)} raw image(s)...")

    # Load cache if exists
    progress_data = {}
    if os.path.exists(cache_json_path):
        try:
            with open(cache_json_path, 'r', encoding='utf-8') as f:
                progress_data = json.load(f)
        except Exception:
            progress_data = {}

    chapter_script_entries = []

    for img_idx, raw_fname in enumerate(raw_files, start=1):
        src_path = os.path.join(raw_dir, raw_fname)
        dst_path = os.path.join(dest_images_dir, raw_fname)

        if not os.path.exists(dst_path):
            shutil.copy2(src_path, dst_path)

        print(f"\n==========================================")
        print(f"🖼️ [{img_idx}/{len(raw_files)}] Analyzing {raw_fname}...")

        # Slice image
        slices = slice_image(dst_path, cache_dir, max_h=4500, overlap=250)
        print(f"   ✂️ Sliced into {len(slices)} part(s).")

        img_all_blocks = []

        for s_idx, sl_path in enumerate(slices, start=1):
            sl_name = os.path.basename(sl_path)
            
            # Check cache
            if sl_name in progress_data:
                cached_text = progress_data[sl_name]
                blocks = parse_dialogue_blocks(cached_text)
                img_all_blocks.extend(blocks)
                print(f"   ⏩ Part {s_idx}/{len(slices)} loaded from cache ({len(blocks)} bubble(s)).")
                continue

            print(f"   🤖 Part {s_idx}/{len(slices)} sending to Gemini Vision...")
            ocr_res = run_ocr_and_translate(rotator, sl_path)
            progress_data[sl_name] = ocr_res
            
            # Save progress json
            with open(cache_json_path, 'w', encoding='utf-8') as f:
                json.dump(progress_data, f, ensure_ascii=False, indent=2)

            blocks = parse_dialogue_blocks(ocr_res)
            img_all_blocks.extend(blocks)
            print(f"   ✅ Part {s_idx}/{len(slices)} done -> {len(blocks)} bubble(s) detected.")
            time.sleep(2)

        # Deduplicate blocks
        cleaned_blocks = deduplicate_blocks(img_all_blocks)
        formatted_text = format_blocks_to_text(cleaned_blocks)

        entry = f"📄 ẢNH: {raw_fname}\n\n{formatted_text}\n"
        chapter_script_entries.append(entry)

        # Progressive backup save of master script.txt
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(chapter_script_entries) + "\n")

        print(f"💾 Saved {raw_fname} to script.txt ({len(cleaned_blocks)} dialogue(s) in total).")

    print(f"\n🎉 ALL {len(raw_files)} IMAGES PROCESSED SUCCESSFULLY!")
    print(f"📍 Output script: {script_path}")

    # Perform automated QC Audit
    run_qc_audit(script_path)


def run_qc_audit(script_path: str):
    """Audits punctuation, character attribution, and format."""
    print("\n🔍 Running Automated QC Audit...")
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = re.findall(r'\[([^\]]+)\]\s*\n\s*KR:\s*([^\n]+)\s*\n\s*([^\n]+)', content)
    print(f"📊 Total dialogue blocks found: {len(blocks)}")

    warnings = []
    for idx, (spk, kr, vi) in enumerate(blocks, start=1):
        # 1. Punctuation checks
        for p in ['!', '?', '...', '~']:
            c_kr = kr.count(p)
            c_vi = vi.count(p)
            if c_kr != c_vi:
                warnings.append(f"Line {idx} [{spk}]: Punctuation '{p}' mismatch (KR:{c_kr} vs VI:{c_vi}) -> KR: {kr} | VI: {vi}")

        # 2. Check Hyung preservation
        if spk == "Han Yoohyun" and "형" in kr:
            if "Hyung" not in vi:
                warnings.append(f"Line {idx} [Han Yoohyun]: '형' in KR but 'Hyung' missing in VI -> VI: {vi}")

        # 3. Check forbidden "anh" for Yoohyun when addressing Yoojin
        if spk == "Han Yoohyun" and re.search(r'\banh\b', vi, re.IGNORECASE) and "Hyung" not in vi:
            warnings.append(f"Line {idx} [Han Yoohyun]: Used 'anh' instead of 'Hyung' -> VI: {vi}")

    if not warnings:
        print("✅ 100% QC PASSED: No punctuation drift or prohibited pronoun mismatches detected!")
    else:
        print(f"⚠️ QC Audit found {len(warnings)} potential note(s):")
        for w in warnings[:15]:
            print(f"   • {w}")


if __name__ == "__main__":
    ch = sys.argv[1] if len(sys.argv) > 1 else "183"
    raw = sys.argv[2] if len(sys.argv) > 2 else r"C:\Users\thuyn\Downloads\183\raw"
    process_chapter(ch, raw)
