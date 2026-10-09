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

4. BẢO VỆ TÊN RIÊNG & PHÂN VAI NHÂN VẬT (TUYỆT ĐỐI CẤM NHẦM LẪN):
   - 陆阡: Lục Thiên (CẤM thay bằng Sở Niên Niên!)
   - 楚月月: Sở Nguyệt Nguyệt (chị gái ruột đã khuất của Sở Niên Niên, CẤM thay bằng Sở Niên Niên!)
   - 大海: Đại Hải (CẤM thay bằng Sở Niên Niên!)
   - 赵昀: Triệu Doãn (quản lý cũ trong giới giải trí của Sở Niên Niên)
   - 陈骞: Trần Khiêm (trợ lý / cấp dưới thân cận của Cố Xuyên)
   - 赵哲: Triệu Triết
   - 李媛媛: Lý Viện Viện
   - 蜜寶: Mật Bảo (Hệ thống hình bướm bảy sắc)

5. QUY TẮC XƯNG HÔ ĐỐI THOẠI TRỰC TIẾP:
   - Sở Niên Niên ↔ Cố Xuyên:
     + Sở Niên Niên: xưng "em", gọi Cố Xuyên là "anh / Cố ca / ca ca / Cố ca ca" (làm nũng, dính người, dỗ dành). Khi chột dạ có thể dùng "tôi - anh".
     + Cố Xuyên: xưng "tôi / anh - em / nhóc con / Niên Niên" (giai đoạn này Cố Xuyên đã yêu sâu sắc, cưng chiều, giam lỏng không cho đi).
   - Sở Niên Niên ↔ Lục Thiên:
     + Sở Niên Niên: gọi "anh" (hoặc "Lục ca"), xưng "tôi" (đặc biệt khi đối thoại riêng/đối chất).
     + Lục Thiên: xưng "tôi", gọi "Sở Niên Niên / cậu".
   - Sở Niên Niên ↔ Đồng đội (Lý Viện Viện, Đại Hải): xưng "em / cháu", gọi "chị Viện Viện / anh Đại Hải".
   - Cố Xuyên ↔ Cấp dưới: Cố Xuyên xưng "tôi", gọi "cậu / các cậu". Cấp dưới gọi Cố Xuyên là "Cố đội / ông chủ / anh".
   - Đồng bộ đại từ: Nếu dùng "tao" thì bắt buộc phải đi cùng "mày". CẤM "tao - cậu", CẤM "tôi - mày".

6. THUẬT NGỮ BẮT BUỘC:
   - 菟丝子: dây tơ hồng
   - 丧尸 / 丧尸潮: tang thi / đợt triều tang thi
   - 变异丧尸: tang thi biến dị
   - 异能 / 异能者: dị năng / dị năng giả
   - 晶石: tinh thạch
   - 空间异能: dị năng không gian
   - 龙城基地: căn cứ Long Thành
   - A城基地: căn cứ A Thành

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
Số đoạn cần dịch: ĐÚNG {n} ĐOẠN (từ [{1:02d}] đến [{n:02d}]).
Bối cảnh trước đó (nếu có):
{context_prev[-300:] if context_prev else "Mở đầu chương."}

VĂN BẢN NGUỒN CẦN DỊCH:
{input_text}
"""
    for attempt in range(max_attempts):
        raw_res = call_gemini(prompt, SYSTEM_PROMPT_ARC2, temp=0.15)
        # Parse [01] ... [N]
        pattern = re.compile(r'^\s*\[(\d+)\]\s*(.*)$', re.MULTILINE)
        matches = pattern.findall(raw_res)

        if len(matches) == n:
            trans_paras = []
            for num_str, content in matches:
                clean_c = content.strip()
                trans_paras.append(clean_c)
            return trans_paras

        print(f"  [Chunk {start_idx+1}-{start_idx+n}] Output count mismatch: expected {n}, got {len(matches)}. Attempt {attempt+1}/{max_attempts}...")
        time.sleep(2)

    # Fallback paragraph by paragraph if chunk repeatedly fails
    print(f"  [Chunk {start_idx+1}-{start_idx+n}] Fallback to 1-by-1 translation...")
    trans_paras = []
    for i, p in enumerate(chunk_paras):
        one_prompt = f"Dịch đoạn sau sang tiếng Việt chuẩn theo đúng quy tắc Arc 2:\n[{1:02d}] {p}"
        one_res = call_gemini(one_prompt, SYSTEM_PROMPT_ARC2, temp=0.1)
        m = re.search(r'^\s*\[\d+\]\s*(.*)$', one_res, re.MULTILINE)
        if m:
            trans_paras.append(m.group(1).strip())
        else:
            trans_paras.append(one_res.strip())
        time.sleep(0.5)

    return trans_paras

def translate_chapter(cid, title, paras):
    print(f"\n==========================================")
    print(f"Translating {cid}: {title} ({len(paras)} paras)")
    print(f"==========================================")

    chunk_size = 20
    translated_paras = []
    context = ""

    for i in range(0, len(paras), chunk_size):
        chunk = paras[i:i+chunk_size]
        print(f"Translating chunk {i+1} to {i+len(chunk)} / {len(paras)}...")
        t_chunk = translate_chunk_with_retry(chunk, i, title, context)
        translated_paras.extend(t_chunk)
        context = "\n".join(t_chunk[-3:])
        print(f"-> Completed {len(translated_paras)} / {len(paras)} paras.")
        time.sleep(1)

    return translated_paras

def main():
    with open('scratch/cleaned_batch4_arc2.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    chapter_titles = {
        'ch_052': 'Chương 52: Khắc tinh tang thi',
        'ch_053': 'Chương 53: Đổi mới Long Thành',
        'ch_054': 'Chương 54: Thủ lĩnh tối cao',
        'ch_055': 'Chương 55: Tái thiết căn cứ',
        'ch_056': 'Chương 56: Kịch bản hoàn thành',
        'ch_057': 'Chương 57: Chạy trốn bất thành',
        'ch_058': 'Chương 58: Ngoại truyện viên mãn - Kết thúc Thế giới 2',
    }

    base_dir = 'novel_projects/phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương/chapters'

    for cid in ['ch_052', 'ch_053', 'ch_054', 'ch_055', 'ch_056', 'ch_057', 'ch_058']:
        cdata = data[cid]
        paras = cdata['paras']
        title = chapter_titles[cid]

        cdir = os.path.join(base_dir, cid)
        os.makedirs(cdir, exist_ok=True)
        trans_path = os.path.join(cdir, 'translation.md')

        # Check if already translated with matching line count
        if os.path.exists(trans_path):
            existing_paras = [p.strip() for p in open(trans_path, encoding='utf-8').read().split('\n\n') if p.strip()]
            if len(existing_paras) == len(paras):
                print(f"[{cid}] Already translated ({len(existing_paras)} paras). Skipping.")
                continue

        trans_paras = translate_chapter(cid, title, paras)

        # Write translation.md
        with open(trans_path, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(trans_paras))

        print(f"[{cid}] Successfully wrote {trans_path} ({len(trans_paras)} paras)")

if __name__ == '__main__':
    main()
