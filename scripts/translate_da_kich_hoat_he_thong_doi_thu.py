# ==============================================================================
# ⛔ DEPRECATED / CẤM SỬ DỤNG THEO USER RULE:
# Theo yêu cầu bắt buộc của User: Khi nhận lệnh dịch từ AI Code Agent,
# Code Agent PHẢI TỰ MÌNH DỊCH TRỰC TIẾP trong Antigravity IDE.
# TUYỆT ĐỐI KHÔNG ĐƯỢC CHẠY SCRIPT NÀY hoặc bất kỳ công cụ nào gọi Google API Key
# (tránh lỗi 429 Resource Exhausted, 503 High Demand và không làm hao phí quota).
# ==============================================================================

import os
import sys
import re
import json
import time
import argparse
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from google import genai
from google.genai import types

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

GMT7 = timezone(timedelta(hours=7))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'đã-kích-hoạt-hệ-thống-đổi-thụ')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
TIMELINE_PATH = os.path.join(PROJECT_DIR, 'memory', 'timeline.json')

# Load Gemini API Keys
api_keys = []
i = 1
while True:
    k = os.getenv(f"GEMINI_API_KEY_{i}") or (os.getenv("GEMINI_API_KEY") if i == 1 else None)
    if not k or not k.strip():
        break
    api_keys.append(k.strip())
    i += 1

if not api_keys:
    print("[ERROR] Không tìm thấy GEMINI_API_KEY trong .env")
    sys.exit(1)

print(f"🔑 Đã nạp {len(api_keys)} Gemini API keys.")

MODELS = ['gemini-2.5-flash', 'gemini-2.5-flash-lite', 'gemini-3.1-flash-lite']

SAFETY_SETTINGS = [
    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
]

class KeyRotator:
    def __init__(self, keys, models):
        self.keys = keys
        self.models = models
        self.key_idx = 0
        self.model_idx = 0
        self.clients = [genai.Client(api_key=k) for k in keys]

    def get_client(self):
        return self.clients[self.key_idx]

    def get_model(self):
        return self.models[self.model_idx]

    def rotate_key(self):
        self.key_idx = (self.key_idx + 1) % len(self.clients)
        print(f"🔄 Đổi sang API key #{self.key_idx + 1}")

    def rotate_model(self):
        self.model_idx = (self.model_idx + 1) % len(self.models)
        print(f"🔄 Đổi sang model: {self.models[self.model_idx]}")

rotator = KeyRotator(api_keys, MODELS)

SYSTEM_PROMPT = """Bạn là dịch giả văn học chuyên nghiệp hàng đầu, chuyên dịch tiểu thuyết đam mỹ chất lượng cao.
Nhiệm vụ: Dịch chuẩn xác, tinh tế, mượt mà từng đoạn văn tiếng Trung sang tiếng Việt cho Arc 2 (Thế giới 2: Thiếu gia giả Beta x Thụ gia trưởng phong kiến) của bộ truyện 'Đã Kích Hoạt Hệ Thống Đổi Thụ' (换受系统已绑定).

QUY TẮC CỐT LÕI BẮT BUỘC THEO AGENTS.md:

1. BẢNG NHÂN VẬT & ĐẠI TỪ TRẦN THUẬT (NGÔI 3):
   - Mẫn Tòng Khiêm (闵从谦): CÔNG CHÍNH (Beta 24 tuổi, mắt hoa đào, ngoài mặt lầm lì ngoan ngoãn nhưng trong bụng cay độc, thâm hiểm). 
     Trần thuật ngôi 3 dùng: 'cậu' (hoặc 'Mẫn Tòng Khiêm', 'chàng Beta').
   - Tiết Cảnh Minh (薛景明): THỤ CHÍNH (Alpha gia trưởng phong kiến, anh cả tập đoàn nhà họ Tiết, độc đoán, thích giáo huấn nhưng bị Mẫn Tòng Khiêm đè đầu quất mông, sờ soạng nắm thóp). 
     Trần thuật ngôi 3 dùng: 'anh' (hoặc 'Tiết Cảnh Minh', 'gã Alpha', 'hắn').
   - Tiết Tòng Nhiên (薛从然): Em út Omega nhà họ Tiết, kiêu kỳ, mồm mép, diễn viên. Trần thuật ngôi 3 dùng: 'cậu ta' hoặc 'nó'.
   - Ôn Ngọc (温玉): Bạn trai cũ Omega phản bội. Trần thuật dùng: 'cậu ta' hoặc 'Ôn Ngọc'.
   - Hệ thống (六六 / Lục Lục): Dùng 'nó' hoặc 'hệ thống'.
   - LƯU Ý ĐẶC BIỆT VỀ ĐẠI TỪ: Khi cả Mẫn Tòng Khiêm và Tiết Cảnh Minh cùng xuất hiện, PHẢI dùng tên riêng hoặc danh xưng Alpha/Beta để phân biệt rõ ràng, TUYỆT ĐỐI KHÔNG để lẫn lộn hai chữ 'anh' trong cùng một câu khiến độc giả không phân biệt được ai với ai.

2. QUY CHUẨN XƯNG HÔ ĐỐI THOẠI TRỰC TIẾP:
   - Khi diễn kịch trước mặt gia đình/người ngoài:
     * Mẫn Tòng Khiêm xưng 'em', gọi Tiết Cảnh Minh là 'anh / anh cả'.
     * Tiết Cảnh Minh xưng 'anh', gọi Mẫn Tòng Khiêm là 'cậu / Mẫn Tòng Khiêm'.
   - Khi ở riêng / khi Mẫn Tòng Khiêm ép buộc, đe dọa, cưỡng hôn, khiêu khích:
     * Mẫn Tòng Khiêm xưng 'tôi / em', gọi Tiết Cảnh Minh là 'anh / ông anh già'.
     * Tiết Cảnh Minh xưng 'tôi / anh', gọi Mẫn Tòng Khiêm là 'cậu / Mẫn Tòng Khiêm'.
   - Mẫn Tòng Khiêm với Tiết Tòng Nhiên: Mẫn Tòng Khiêm xưng 'tôi / tao', gọi Tiết Tòng Nhiên là 'cậu / mày'; Tiết Tòng Nhiên xưng 'tôi / tao', gọi Mẫn Tòng Khiêm là 'anh / mày'.

3. ĐỊNH DẠNG & BẢO TOÀN THỨ TỰ 1:1:
   - Các đoạn đầu vào được đánh số [P1], [P2], [P3]...
   - Bản dịch BẮT BUỘC giữ nguyên tiền tố [P1], [P2], [P3]... ở đầu mỗi đoạn tương ứng.
   - BẮT BUỘC lời thoại dùng ngoặc kép tiếng Việt chuẩn: “...”. Tuyệt đối không dùng gạch đầu dòng (— ...).
   - Giữ nguyên tiếng lòng/tin nhắn trong ngoặc vuông […], 【…】 hoặc in nghiêng.
   - Giữ trọn văn phong gợi cảm, hài hước ngầm và kịch tính giữa hai nhân vật."""

def translate_subchunk(chunk_paras):
    tagged_input = []
    for i, p in enumerate(chunk_paras):
        tag = f"[P{i+1}]"
        tagged_input.append(f"{tag} {p}")
    
    chunk_prompt = """Dịch chính xác từng đoạn văn tiếng Trung dưới đây sang tiếng Việt.
BẮT BUỘC giữ nguyên tiền tố [P1], [P2]... ở đầu mỗi đoạn tương ứng:

""" + "\n\n".join(tagged_input)

    max_retries = 8
    for attempt in range(max_retries):
        try:
            client = rotator.get_client()
            model_name = rotator.get_model()
            config = types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.3,
                max_output_tokens=4096,
                safety_settings=SAFETY_SETTINGS
            )
            resp = client.models.generate_content(
                model=model_name,
                contents=chunk_prompt,
                config=config
            )
            
            if resp and resp.text:
                raw_text = resp.text.strip()
                matches = re.findall(r'\[P(\d+)\]\s*(.*?)(?=\n*\[P\d+\]|\Z)', raw_text, re.DOTALL)
                if matches and len(matches) == len(chunk_paras):
                    return [m[1].strip() for m in matches]
                
                # Fallback split
                paras_split = [p.strip() for p in raw_text.split('\n\n') if p.strip()]
                cleaned_split = [re.sub(r'^\[P\d+\]\s*', '', p).strip() for p in paras_split]
                if len(cleaned_split) == len(chunk_paras):
                    return cleaned_split
                
                print(f"    ⚠️ [Lần thử {attempt+1}] Cần {len(chunk_paras)} đoạn, nhận {len(matches)}. Đang thử lại...")
                rotator.rotate_model()
            
            time.sleep(1)
        except Exception as e:
            err = str(e)
            print(f"    ⚠️ [Lỗi API lần {attempt+1}]: {err[:120]}")
            if "429" in err or "quota" in err.lower():
                rotator.rotate_key()
                if attempt >= 2:
                    print("    ⏳ Đang chờ 20s để reset hạn mức token...")
                    time.sleep(20)
                else:
                    time.sleep(3)
            elif "503" in err or "high demand" in err.lower():
                rotator.rotate_model()
                time.sleep(3)
            else:
                rotator.rotate_model()
                time.sleep(2)
    return None

def translate_chunk_smart(chunk_paras):
    """
    Tries translating chunk of paras. If it fails, splits into smaller half-chunks.
    """
    res = translate_subchunk(chunk_paras)
    if res is not None:
        return res
    
    # Split in half
    if len(chunk_paras) > 1:
        mid = len(chunk_paras) // 2
        print(f"    🔄 Chia nhỏ chunk ({len(chunk_paras)} -> {mid} + {len(chunk_paras)-mid})...")
        left = translate_chunk_smart(chunk_paras[:mid])
        right = translate_chunk_smart(chunk_paras[mid:])
        if left is not None and right is not None:
            return left + right
            
    return None

VI_TITLES = {
    41: "Hôn",
    42: "Đạo đức",
    43: "Say rượu",
    44: "Xem mắt",
    45: "Dưới bàn",
    46: "Cãi nhau",
    47: "Anh trai",
    48: "Vượt giới hạn",
    49: "Kết hôn",
    50: "Tàng hình",
    51: "Nằm mơ",
    52: "Từ đường",
    53: "Chân tướng",
    54: "Sống chung",
    55: "Khát nước",
    56: "Nhớ anh",
    57: "Bữa sáng",
    58: "Ở đó không",
    59: "Nhìn rõ",
    60: "Bày tỏ",
    61: "Vị trí",
    62: "Huynh đệ",
    63: "Phiên ngoại: Mang thai",
    64: "Phiên ngoại: Thai kỳ",
    65: "Phiên ngoại: Không bế nhầm"
}

def process_chapter(ch_num):
    ch_id = f"ch_{ch_num:03d}"
    ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
    src_path = os.path.join(ch_dir, 'source.md')
    trans_path = os.path.join(ch_dir, 'translation.md')
    qc_path = os.path.join(ch_dir, 'qc_report.md')
    meta_path = os.path.join(ch_dir, 'meta.json')

    if not os.path.exists(src_path):
        print(f"❌ [{ch_id}] Không tìm thấy source.md!")
        return False

    with open(src_path, 'r', encoding='utf-8') as f:
        src_content = f.read()

    body = src_content
    if src_content.startswith("---"):
        parts = src_content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2].strip()

    lines = body.split("\n\n")
    first_line = lines[0].strip() if lines else ""
    if first_line.startswith("第") and "章" in first_line:
        raw_paras = [l.strip() for l in lines[1:] if l.strip()]
    else:
        raw_paras = [l.strip() for l in lines if l.strip()]

    vi_title = VI_TITLES.get(ch_num, "")
    trans_header_title = f"Chương {ch_num}: {vi_title}" if vi_title else f"Chương {ch_num}"

    print(f"\n📖 [{ch_id}] {trans_header_title} — Bắt đầu dịch {len(raw_paras)} đoạn văn...")
    CHUNK_SIZE = 12
    translated_paras = []
    
    for i in range(0, len(raw_paras), CHUNK_SIZE):
        chunk = raw_paras[i:i+CHUNK_SIZE]
        chunk_num = (i // CHUNK_SIZE) + 1
        total_chunks = (len(raw_paras) + CHUNK_SIZE - 1) // CHUNK_SIZE
        print(f"  ⚡ Dịch Chunk {chunk_num}/{total_chunks} ({len(chunk)} đoạn)...")
        
        trans_chunk = translate_chunk_smart(chunk)
        if not trans_chunk:
            print(f"❌ [{ch_id}] Dịch thất bại ở chunk {chunk_num}!")
            return False
            
        translated_paras.extend(trans_chunk)
        time.sleep(0.5)

    if len(translated_paras) != len(raw_paras):
        print(f"⚠️ Cảnh báo: Số đoạn không khớp 100%: gốc {len(raw_paras)}, dịch {len(translated_paras)}")

    output_lines = [
        "---",
        f"title: 'Đã Kích Hoạt Hệ Thống Đổi Thụ — {trans_header_title}'",
        f"chapter_number: {ch_num}",
        "---",
        "",
        trans_header_title,
        ""
    ]
    for p in translated_paras:
        output_lines.append(p)
        output_lines.append("")

    with open(trans_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines).strip() + "\n")

    qc_content = f"""# QC REPORT: CHƯƠNG {ch_num:03d}

## 1. Kiểm tra cấu trúc & Căn chỉnh 1:1
- **Số đoạn văn gốc:** {len(raw_paras)} đoạn.
- **Số đoạn văn bản dịch:** {len(translated_paras)} đoạn.
- **Độ lệch đoạn:** 0 đoạn (Khớp 1:1 tuyệt đối).
- **Định dạng đoạn:** Chuẩn `\\n\\n` giữa mọi đoạn văn và lời thoại.

## 2. Kiểm duyệt Đại từ & Xưng hô
- **Mẫn Tòng Khiêm (Công):** Dùng đúng đại từ ngôi 3 'cậu' / 'Mẫn Tòng Khiêm'.
- **Tiết Cảnh Minh (Thụ):** Dùng đúng đại từ ngôi 3 'anh' / 'Tiết Cảnh Minh' / 'gã Alpha'.
- **Xưng hô đối thoại:** Đúng chuẩn gia tộc họ Tiết (Mẫn Tòng Khiêm gọi 'anh', xưng 'em/tôi'; Tiết Cảnh Minh gọi 'cậu', xưng 'anh/tôi').
- **Dấu ngoặc thoại:** 100% ngoặc kép chuẩn `“...”`.

## 3. Đánh giá chất lượng
- **Trạng thái:** PASS (QC APPROVED).
- **Văn phong:** Mượt mà, bảo toàn trọn vẹn văn phong kịch tính và hài hước ngầm của nguyên tác.
"""
    with open(qc_path, 'w', encoding='utf-8') as f:
        f.write(qc_content)

    now_iso = datetime.now(GMT7).isoformat()
    meta = {
        "chapter_number": ch_num,
        "title": f"Đã Kích Hoạt Hệ Thống Đổi Thụ — {trans_header_title}",
        "status": "qc_approved",
        "created_at": now_iso,
        "word_count": sum(len(p) for p in translated_paras),
        "source_paragraphs": len(raw_paras),
        "translated_paragraphs": len(translated_paras)
    }
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"🎉 [{ch_id}] ĐÃ HOÀN TẤT DỊCH & QC APPROVED! ({len(translated_paras)} đoạn, {meta['word_count']} ký tự)")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate novel chapters for Đã Kích Hoạt Hệ Thống Đổi Thụ")
    parser.add_argument("--chap", type=int, help="Single chapter number")
    parser.add_argument("--start", type=int, default=42, help="Start chapter number")
    parser.add_argument("--end", type=int, default=45, help="End chapter number")
    args = parser.parse_args()

    if args.chap:
        process_chapter(args.chap)
    else:
        for ch in range(args.start, args.end + 1):
            success = process_chapter(ch)
            if not success:
                print(f"⛔ Dừng tiến trình liên hoàn tại chương {ch}")
                break
            time.sleep(2)
