import os
import sys
import re
import json
import time
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
load_dotenv('.env')

from google import genai
from google.genai import types

class KeyRotator:
    def __init__(self):
        self.clients = []
        for i in range(1, 10):
            k = os.environ.get(f"GEMINI_API_KEY_{i}") or (os.environ.get("GEMINI_API_KEY") if i == 1 else None)
            if k and k.strip():
                self.clients.append(genai.Client(api_key=k.strip()))
        if not self.clients:
            raise RuntimeError("No GEMINI_API_KEY found!")
        self.current_idx = 0
        print(f"[Rotator] Initialized with {len(self.clients)} API keys.")

    def get_client(self):
        return self.clients[self.current_idx], self.current_idx

    def rotate(self):
        prev = self.current_idx
        self.current_idx = (self.current_idx + 1) % len(self.clients)
        print(f"[Rotator] Switched Key {prev+1} -> Key {self.current_idx+1}")
        return self.clients[self.current_idx]

rotator = KeyRotator()

def call_gemini(contents, system_instruction, temp=0.15, max_retries=25):
    safety = [
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
    ]
    models = ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3.8-flash"]

    for attempt in range(max_retries):
        model = models[attempt % len(models)]
        client, k_idx = rotator.get_client()
        try:
            cfg = types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=temp,
                safety_settings=safety
            )
            resp = client.models.generate_content(
                model=model,
                contents=contents,
                config=cfg
            )
            if resp and resp.text and resp.text.strip():
                return resp.text.strip()
            print(f"[Gemini] Empty response attempt {attempt+1}, retrying...")
            time.sleep(3)
        except Exception as e:
            err = str(e)
            print(f"[Gemini] Error attempt {attempt+1} (Key {k_idx+1}, {model}): {err[:120]}")
            if "429" in err or "RESOURCE_EXHAUSTED" in err or "quota" in err.lower():
                rotator.rotate()
                time.sleep(12)
            elif "403" in err:
                rotator.rotate()
                time.sleep(3)
            else:
                time.sleep(3)

    raise RuntimeError(f"Gemini API failed after {max_retries} retries!")

SYSTEM_PROMPT_ARC2 = """Bạn là dịch giả tiểu thuyết chuyên nghiệp hàng đầu, chuyên dịch thể loại đam mỹ khoái xuyên, chủ công, mạt thế tang thi từ tiếng Trung sang tiếng Việt.
Bộ truyện: Phản Diện Đổi Ý Cầm Kịch Bản Yêu Đương (Thế giới 2: Mạt thế tang thi - Sở Niên Niên công x Cố Xuyên thụ).

QUY TẮC BẮT BUỘC TUÂN THỦ (KHÔNG THỰC HIỆN ĐÚNG SẼ BỊ COI LÀ LỖI NGHIÊM TRỌNG):
1. BẢO TOÀN SỐ ĐOẠN 1:1 TUYỆT ĐỐI (PARAGRAPH ALIGNMENT):
   - Đầu vào gồm đúng N đoạn văn được đánh số [01], [02], ... [N].
   - Đầu ra BẮT BUỘC PHẢI CÓ ĐÚNG N đoạn tương ứng, đánh số đúng [01], [02], ... [N].
   - Không gộp đoạn, không tách đoạn, không thêm bớt bất kỳ đoạn nào.

2. ĐỊNH DẠNG ĐOẠN VĂN:
   - Mỗi đoạn văn tiếng Việt cách nhau đúng một dòng trống (\\n\\n).
   - Tất cả lời thoại trực tiếp BẮT BUỘC nằm trong dấu ngoặc kép tiếng Việt chuẩn “...”. CẤM dùng gạch đầu dòng (-) hoặc dấu nháy đơn ('...').
   - Suy nghĩ nội tâm trong ngoặc đơn (...) hoặc ngoặc kép “...”.
   - Thông báo hệ thống nằm trong ngoặc vuông 【...】.
   - Dấu phân cách cảnh nếu có như '-' thì giữ nguyên là '-'.

3. QUY TẮC ĐẠI TỪ NGÔI 3 TỰ SỰ / TRẦN THUẬT:
   - Sở Niên Niên (Công - dây tơ hồng, trà xanh giả nai, xinh đẹp): Luôn dùng "cậu" hoặc tên riêng "Sở Niên Niên".
   - Cố Xuyên (Thụ - đại lão dị năng giả, thân hình cơ bắp vạm vỡ, lạnh lùng uy nghiêm): Luôn dùng "anh" hoặc tên riêng "Cố Xuyên", "đại lão", "người đàn ông".
   - ⚠️ TUYỆT ĐỐI CẤM dùng "anh" cho Sở Niên Niên trong trần thuật!
   - ⚠️ TUYỆT ĐỐI CẤM dùng "cậu" cho Cố Xuyên trong trần thuật!
   - Tuyệt đối không dùng bừa bãi "hắn" cho cả hai nhân vật nam gây lẫn lộn.

4. QUY TẮC XƯNG HÔ ĐỐI THOẠI TRỰC TIẾP:
   - Sở Niên Niên ↔ Cố Xuyên:
     + Sở Niên Niên: xưng "em", gọi Cố Xuyên là "anh / Cố ca / ca ca / Cố ca ca" (làm nũng, dính người, dỗ dành). Khi chột dạ có thể dùng "tôi - anh".
     + Cố Xuyên: xưng "tôi - cậu" (giai đoạn đầu đề phòng, gắt gỏng), xưng "tôi / anh - em / nhóc con / Niên Niên" (khi yêu chiều, dung túng).
   - Sở Niên Niên ↔ Cấp dưới / Đồng đội (Lục Thiên, Lý Viện Viện, Bụng Bia):
     + Sở Niên Niên: xưng "em / cháu", gọi "Lục ca / chị Viện Viện / chú Bụng Bia".
     + Đồng đội: xưng "anh / chị / chú", gọi Sở Niên Niên là "Niên Niên / em / cậu".
   - Cố Xuyên ↔ Cấp dưới: Cố Xuyên xưng "tôi", gọi "cậu / các cậu". Cấp dưới gọi Cố Xuyên là "Cố đội / anh Cố / anh".
   - Đồng bộ đại từ: Nếu dùng "tao" thì bắt buộc phải đi cùng "mày". CẤM "tao - cậu", CẤM "tôi - mày".

5. THUẬT NGỮ BẮT BUỘC:
   - 菟丝子: dây tơ hồng
   - 丧尸 / 丧尸潮: tang thi / đợt triều tang thi
   - 变异丧尸: tang thi biến dị
   - 异能 / 异能者: dị năng / dị năng giả
   - 晶石: tinh thạch
   - 空间异能: dị năng không gian
   - 龙城基地: căn cứ Long Thành

OUTPUT FORMAT:
Chỉ trả về các đoạn dịch theo định dạng:
[01] Nội dung đoạn 1

[02] Nội dung đoạn 2

...
[N] Nội dung đoạn N
Không viết thêm bất kỳ lời chào, giải thích, markdown fence nào ngoài các đoạn dịch.
"""

def translate_chunk_with_retry(chunk_paras, start_idx, chapter_title, context_prev="", max_attempts=5):
    n = len(chunk_paras)
    numbered_input = []
    for i, p in enumerate(chunk_paras):
        numbered_input.append(f"[{i+1:02d}] {p}")
    input_text = "\n\n".join(numbered_input)

    prompt = f"""Chương: {chapter_title}
Ngữ cảnh trước (nếu có): {context_prev[-300:] if context_prev else 'Đầu chương'}

Dịch đoạn sau (gồm đúng {n} đoạn, từ [{1:02d}] đến [{n:02d}]):
{input_text}
"""
    for attempt in range(max_attempts):
        raw_res = call_gemini(prompt, SYSTEM_PROMPT_ARC2, temp=0.15)
        lines = raw_res.split('\n\n')
        parsed = {}
        for block in lines:
            block = block.strip()
            if not block:
                continue
            m = re.match(r'^\[(\d+)\]\s*(.*)$', block, re.DOTALL)
            if m:
                idx = int(m.group(1))
                parsed[idx] = m.group(2).strip()
            else:
                if parsed:
                    last_k = max(parsed.keys())
                    parsed[last_k] += "\n" + block

        if len(parsed) == n and all(i in parsed for i in range(1, n+1)):
            return [parsed[i] for i in range(1, n+1)]

        print(f"[Retry] Paragraph count mismatch on chunk {start_idx}: expected {n}, got {len(parsed)}. Retrying attempt {attempt+1}...")
        time.sleep(2)

    raise RuntimeError(f"Failed to get 1:1 translation for chunk {start_idx} after {max_attempts} attempts!")

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

def parse_source(cid):
    p = os.path.join(CHAPTERS_DIR, cid, "source.md")
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    title = ""
    m = re.search(r'title:\s*(.*)', content)
    if m:
        title = m.group(1).strip()
    parts = content.split('---\n\n', 1)
    body = parts[1] if len(parts) >= 2 else content
    paras = [x.strip() for x in body.split('\n\n') if x.strip()]
    return title, paras

def post_process_paras(paras):
    cleaned = []
    for p in paras:
        p = re.sub(r'\"([^\"]+)\"', r'“\1”', p)
        p = re.sub(r'\'([^\']+)\'', r'“\1”', p)
        p = p.replace('"', '“')
        cleaned.append(p)
    return cleaned

def translate_chapter(cid, chunk_size=20):
    title, s_paras = parse_source(cid)
    print(f"\n==========================================")
    print(f"Translating {cid}: {title} ({len(s_paras)} paras)...")
    print(f"==========================================")

    out_file = os.path.join(CHAPTERS_DIR, cid, "translation.md")
    if os.path.exists(out_file):
        with open(out_file, 'r', encoding='utf-8') as f:
            existing = f.read()
        ex_body = existing.split('---\n\n', 1)[1] if '---\n\n' in existing else existing
        ex_paras = [x.strip() for x in ex_body.split('\n\n') if x.strip()]
        if len(ex_paras) == len(s_paras):
            print(f"[{cid}] Already translated with matching {len(ex_paras)} paras. Skipping.")
            return title, s_paras, ex_paras

    t_paras = []
    total = len(s_paras)
    for start in range(0, total, chunk_size):
        end = min(start + chunk_size, total)
        chunk = s_paras[start:end]
        print(f"[{cid}] Chunk {start+1}-{end} of {total}...")
        context_prev = " ".join(t_paras[-3:]) if t_paras else ""
        res_chunk = translate_chunk_with_retry(chunk, start, title, context_prev)
        t_paras.extend(res_chunk)
        time.sleep(1)

    t_paras = post_process_paras(t_paras)

    if len(t_paras) != len(s_paras):
        raise ValueError(f"Count mismatch in {cid}: {len(t_paras)} vs {len(s_paras)}")

    header = f"---\ntitle: {title}\n---\n\n"
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(header + "\n\n".join(t_paras) + "\n")

    print(f"[{cid}] Successfully written translation.md ({len(t_paras)} paras)")
    return title, s_paras, t_paras

if __name__ == '__main__':
    cids = ['ch_045', 'ch_046', 'ch_047', 'ch_048', 'ch_049', 'ch_050', 'ch_051']
    for cid in cids:
        translate_chapter(cid)
    print("\nAll Batch 3 chapters translated successfully!")
