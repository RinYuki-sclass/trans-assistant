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

def call_gemini(contents, system_instruction, temp=0.15, max_retries=15):
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
# System Prompt Arc 4 (ABO: Kỷ Cảnh x Lục Tư Niên)
# -------------------------------------------------------------
SYSTEM_PROMPT_ARC4 = """Bạn là dịch giả tiểu thuyết chuyên nghiệp hàng đầu, chuyên dịch thể loại đam mỹ khoái xuyên, chủ công, ABO từ tiếng Trung sang tiếng Việt.
Bộ truyện: Phản Diện Đổi Ý Cầm Kịch Bản Yêu Đương (Thế giới 4: ABO - Alpha niên hạ chiến lực đỉnh cấp Kỷ Cảnh x Cổ hủ cấm dục nho nhã Omega thụ Lục Tư Niên).

QUY TẮC BẮT BUỘC TUÂN THỦ (KHÔNG THỰC HIỆN ĐÚNG SẼ BỊ COI LÀ LỖI NGHIÊM TRỌNG):
1. BẢO TOÀN SỐ ĐOẠN 1:1 TUYỆT ĐỐI (PARAGRAPH ALIGNMENT):
   - Đầu vào gồm đúng N đoạn văn được đánh số [01], [02], ... [N].
   - Đầu ra BẮT BUỘC PHẢI CÓ ĐÚNG N đoạn tương ứng, đánh số đúng [01], [02], ... [N].
   - Không gộp đoạn, không tách đoạn, không thêm bớt bất kỳ đoạn nào.

2. ĐỊNH DẠNG ĐOẠN VĂN:
   - Mỗi đoạn văn tiếng Việt cách nhau đúng một dòng trống (\\n\\n).
   - Tất cả lời thoại trực tiếp BẮT BUỘC nằm trong dấu ngoặc kép tiếng Việt chuẩn “...”. CẤM dùng gạch đầu dòng (-) hoặc dấu nháy đơn ('...').
   - Suy nghĩ nội tâm trong ngoặc đơn (...) hoặc ngoặc kép “...”.
   - Tin nhắn, thông báo hệ thống nằm trong ngoặc vuông 【...】.
   - Dấu phân cách cảnh nếu có như '-' thì giữ nguyên là '-'.

3. QUY TẮC ĐẠI TỪ NGÔI 3 TỰ SỰ / TRẦN THUẬT:
   - Kỷ Cảnh (Công - niên hạ, nhỏ tuổi hơn): Luôn dùng "cậu" hoặc tên riêng "Kỷ Cảnh", "thiếu niên".
   - Lục Tư Niên (Thụ - niên thượng, lớn tuổi hơn, giáo sư): Luôn dùng "anh" hoặc tên riêng "Lục Tư Niên", "Lục giáo sư", "người đàn ông".
   - ⚠️ TUYỆT ĐỐI CẤM dùng "anh" cho Kỷ Cảnh trong văn trần thuật!
   - ⚠️ TUYỆT ĐỐI CẤM dùng "cậu" cho Lục Tư Niên trong văn trần thuật!
   - Tuyệt đối không dùng bừa bãi "hắn" cho cả hai nhân vật gây lẫn lộn.
   - Các Alpha / Beta khác: dùng "gã", "hắn", "bọn họ", "tên".
   - Bác sĩ Nguyễn Uyên: "Nguyễn Uyên", "bác sĩ Nguyễn", "anh".

4. QUY TẮC XƯNG HÔ ĐỐI THOẠI TRỰC TIẾP:
   - Kỷ Cảnh ↔ Lục Tư Niên:
     + Kỷ Cảnh: xưng "em / tôi", gọi Lục Tư Niên là "thầy Lục / giáo sư Lục / anh Lục / Lục Tư Niên / anh" (ranh mãnh trêu chọc, giả vờ ngoan ngoãn khi đóng giả nữ sinh Dịch Nam).
     + Lục Tư Niên: xưng "tôi", gọi Kỷ Cảnh là "cậu / bạn học Kỷ / Kỷ Cảnh / bạn học Dịch Nam" (nghiêm nghị, chuẩn mực, răn đe học sinh).
   - Lục Tư Niên ↔ Nguyễn Uyên: xưng "tôi – cậu / bác sĩ Nguyễn" (bạn bè, đồng nghiệp).
   - Kỷ Cảnh ↔ Bạn học: xưng "tao – mày", "ông đây".
   - Đồng bộ đại từ: Nếu dùng "tao" thì bắt buộc phải đi cùng "mày". CẤM "tao - cậu", CẤM "tôi - mày".

5. THUẬT NGỮ ABO BẮT BUỘC:
   - 信息素: tin tức tố (pheromone)
   - 龙舌兰: rượu Tequila
   - 腺体: tuyến thể
   - 标记 / 终身标记 / 永久标记: đánh dấu / đánh dấu trọn đời / đánh dấu vĩnh viễn
   - 临时标记: đánh dấu tạm thời
   - 抑制剂: thuốc ức chế
   - 易感期: kỳ mẫn cảm (của Alpha)
   - 发情期: kỳ phát tình (của Omega)
   - 防御四班: lớp 4 phòng ngự
   - 帝国第一军校: Học viện quân sự đệ nhất Đế quốc
   - 易南: Dịch Nam (tên giả Kỷ Cảnh dùng để trêu giáo sư)
   - 阮渊: Nguyễn Uyên (bác sĩ quân y)

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
        raw_res = call_gemini(prompt, SYSTEM_PROMPT_ARC4, temp=0.15)
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
        # replace straight double quotes if not inside already
        p = re.sub(r'\"([^\"]+)\"', r'“\1”', p)
        # replace single quotes used as speech
        p = re.sub(r'\'([^\']+)\'', r'“\1”', p)
        # replace any remaining straight quotes
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
    cids = ['ch_090', 'ch_091', 'ch_092', 'ch_093', 'ch_094', 'ch_095']
    for cid in cids:
        translate_chapter(cid)
    print("\nAll Batch 1 chapters translated successfully!")
