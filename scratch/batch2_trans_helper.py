import os
import sys
import re
import json
import time
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv('.env')

from google import genai
from google.genai import types

def now_gmt7():
    return datetime.now(timezone(timedelta(hours=7)))

# -------------------------------------------------------------
# API Key Rotator
# -------------------------------------------------------------
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

def call_gemini(contents, system_instruction, temp=0.2, max_retries=12):
    safety = [
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
    ]
    models = ["gemini-3.8-flash", "gemini-2.5-flash-lite"]

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
            time.sleep(2)
        except Exception as e:
            err = str(e)
            print(f"[Gemini] Error attempt {attempt+1} (Key {k_idx+1}, {model}): {err[:120]}")
            if "429" in err or "RESOURCE_EXHAUSTED" in err or "quota" in err.lower():
                rotator.rotate()
                time.sleep(3)
            elif "403" in err:
                rotator.rotate()
                time.sleep(2)
            else:
                time.sleep(2)

    raise RuntimeError(f"Gemini API failed after {max_retries} retries!")

# -------------------------------------------------------------
# Translation Prompt & Rules
# -------------------------------------------------------------
SYSTEM_PROMPT = """Bạn là dịch giả tiểu thuyết chuyên nghiệp hàng đầu, chuyên dịch thể loại đam mỹ khoái xuyên, chủ công, vườn trường ngọt ngào từ tiếng Trung sang tiếng Việt.

QUY TẮC BẮT BUỘC TUÂN THỦ (KHÔNG THỰC HIỆN ĐÚNG SẼ BỊ COI LÀ LỖI NGHIÊM TRỌNG):
1. BẢO TOÀN SỐ ĐOẠN 1:1 TUYỆT ĐỐI (PARAGRAPH ALIGNMENT):
   - Đầu vào gồm đúng N đoạn văn được đánh số [01], [02], ... [N].
   - Đầu ra BẮT BUỘC PHẢI CÓ ĐÚNG N đoạn tương ứng, đánh số đúng [01], [02], ... [N].
   - Không được gộp đoạn, không được tách đoạn, không được thêm hoặc bớt bất kỳ đoạn nào.

2. ĐỊNH DẠNG ĐOẠN VĂN:
   - Mỗi đoạn văn tiếng Việt phải cách nhau đúng một dòng trống (\n\n).
   - Tất cả lời thoại trực tiếp BẮT BUỘC nằm trong dấu ngoặc kép tiếng Việt chuẩn “...”. CẤM dùng gạch đầu dòng (-) hoặc ngoặc đơn ('...').
   - Suy nghĩ nội tâm trong ngoặc đơn (...) hoặc ngoặc kép “...”.
   - Thông báo hệ thống nằm trong ngoặc vuông 【...】.

3. QUY TẮC ĐẠI TỪ NGÔI 3 TỰ SỰ / TRẦN THUẬT:
   - Bạch Huân (Công): Luôn dùng "anh" hoặc tên riêng "Bạch Huân".
   - Tần Diễm (Thụ): Luôn dùng "cậu" hoặc tên riêng "Tần Diễm", "Tần thiếu gia".
   - ⚠️ TUYỆT ĐỐI CẤM dùng "anh" cho Tần Diễm trong văn trần thuật!
   - Không dùng lẫn lộn "hắn" cho cả hai nhân vật gây mơ hồ.

4. QUY TẮC XƯNG HÔ ĐỐI THOẠI TRỰC TIẾP:
   - Bạch Huân và Tần Diễm: Bằng tuổi nhau, thống nhất xưng hô "tôi - cậu" 100%!
     + Bạch Huân gọi Tần Diễm là "cậu", xưng "tôi" (hoặc "anh - em / bạn trai" khi trêu đùa tán tỉnh).
     + Tần Diễm gọi Bạch Huân là "cậu", xưng "tôi". (TUYỆT ĐỐI KHÔNG dùng "tao - mày" với Bạch Huân!).
   - Tần Diễm với đám bạn thân (Chu Táp, Lý Nhĩ): có thể dùng "tôi - cậu" hoặc "tao - mày", "ông đây".
   - Tần Diễm với kẻ thù ngoài xã hội: dùng "tao - mày", "ông đây".
   - ⚠️ CẤM ghép lệch pha đại từ: CẤM "tao - cậu", CẤM "tôi - mày".

5. VĂN PHONG VÀ THUẬT NGỮ:
   - Văn phong tự nhiên, mượt mà, thuần Việt, đúng phong vị vườn trường, bắt trọn sự tâm cơ ôn nhu của Bạch Huân và tính khí ngạo kiều của Tần Diễm.
   - Thuật ngữ chuẩn: Hệ thống Yêu Đương, kính gọng vàng, phú nhị đại, môtô phân khối lớn, diễn đàn trường.

OUTPUT FORMAT:
Chỉ trả về các đoạn dịch theo định dạng:
[01] Nội dung đoạn 1

[02] Nội dung đoạn 2

...
[N] Nội dung đoạn N
Không viết thêm bất kỳ lời chào, giải thích, markdown fence codeblock nào ngoài các đoạn dịch.
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
        raw_res = call_gemini(prompt, SYSTEM_PROMPT, temp=0.15)
        # Parse numbered blocks
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
                # If there are sub-blocks without [xx], might be part of previous block
                if parsed:
                    last_k = max(parsed.keys())
                    parsed[last_k] += "\n" + block

        if len(parsed) == n and all(i in parsed for i in range(1, n+1)):
            return [parsed[i] for i in range(1, n+1)]

        print(f"[Retry] Paragraph count mismatch on chunk {start_idx}: expected {n}, got {len(parsed)}. Retrying attempt {attempt+1}...")
        time.sleep(2)

    raise RuntimeError(f"Failed to get 1:1 translation for chunk {start_idx} after {max_attempts} attempts!")

print("Loaded translation module.")
