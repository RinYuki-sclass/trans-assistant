import os
import re
import json
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

KEYS = [
    os.getenv('GEMINI_API_KEY_1'),
    os.getenv('GEMINI_API_KEY_2'),
    os.getenv('GEMINI_API_KEY_3'),
]
KEYS = [k for k in KEYS if k]

current_key_idx = 0

def get_client():
    global current_key_idx
    key = KEYS[current_key_idx % len(KEYS)]
    return genai.Client(api_key=key)

def rotate_key():
    global current_key_idx
    current_key_idx = (current_key_idx + 1) % len(KEYS)
    print(f"Rotated to key index {current_key_idx}", flush=True)

def now_gmt7_iso():
    tz = timezone(timedelta(hours=7))
    return datetime.now(tz).isoformat()

BASE_DIR = r"d:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho"

SYS_PROMPT = """Bạn là dịch giả văn học chuyên nghiệp, chuyên dịch tiểu thuyết đam mỹ / khoái xuyên / trùng tộc Trung - Việt cao cấp.
Nhiệm vụ của bạn là dịch các đoạn văn tiếng Trung sang tiếng Việt mượt mà, chuẩn văn phong truyện dịch, tuân thủ tuyệt đối các quy tắc sau:

1. BẢO TOÀN 1:1 SỐ ĐOẠN (PARAGRAPH ALIGNMENT - TỐI QUAN TRỌNG):
- Input có chính xác N đoạn văn (được đánh số [1], [2], ... [N]).
- Output BẮT BUỘC phải có đúng N đoạn văn tương ứng 1:1, đánh số [1], [2], ... [N].
- Tuyệt đối không tự ý gộp đoạn, không tách đoạn.

2. ZERO OMISSION, ZERO ADDITION:
- Không bỏ sót bất kỳ câu thoại, chi tiết, cử chỉ hay bối cảnh nào.
- Không thêm thắt lời bình, suy diễn của dịch giả.

3. QUY TẮC TÊN NHÂN VẬT (BẮT BUỘC):
- Tất cả tên phương Tây TUYỆT ĐỐI GIỮ NGUYÊN TIẾNG ANH, CẤM DỊCH HÁN VIỆT:
  * 艾利克斯 -> Alex (họ 萨克森 -> Sachsen, Sachsen Nguyên soái)
  * 瑞安 -> Ryan
  * 弗德里希 -> Friedrich
  * 费洛 -> Felo
  * 海德曼 -> Heideman
  * 艾利欧 -> Elio
  * 萨克森 -> Sachsen
  * 莫格拉斯 -> Mogelas (Nhà tù Mogelas)
  * 楚司承 -> Sở Tư Thừa

4. ĐẠI TỪ NGÔI THỨ 3 & XƯNG HÔ ĐỐI THOẠI (CRITICAL):
- TRẦN THUẬT (Ngôi thứ 3):
  * Sở Tư Thừa (楚司承): Luôn dùng "anh".
  * Alex (艾利克斯): Luôn dùng "hắn".
  * Ryan (瑞安 - thân xác nguyên tác): Dùng "cậu".
  * Felo (费洛): Dùng "gã" (hoặc "hắn").
  * Friedrich (弗德里希): Dùng "hắn".
  * Elio (艾利欧): Dùng "hắn" (hoặc "gã").
  * Heideman (海德曼): Dùng "ông / ông ta".
  * Hệ thống: Dùng "nó".
- ĐỐI THOẠI TRỰC TIẾP (Khi nhân vật nói chuyện với Alex bằng '你'):
  * TUYỆT ĐỐI KHÔNG dùng "hắn" khi một nhân vật khác đang nói chuyện trực tiếp với Alex!
  * Thư phụ (Sachsen) nói với Alex: 'con' hoặc 'ngươi' (ví dụ: 'con nói đúng không, Alex?', 'con mau qua đây').
  * Sở Tư Thừa nói với Alex: gọi 'anh' (Sở Tư Thừa xưng 'tôi').
  * Friedrich / Elio nói chuyện với Alex: 'ngài' / 'cậu' / 'em'.
  * Người khác xưng hô với Alex: 'ngài' hoặc 'cậu' hoặc 'Tướng quân'.

5. QUY CHUẨN THUẬT NGỮ TRÙNG TỘC (CRITICAL):
- 雄虫 -> Hùng trùng (TUYỆT ĐỐI KHÔNG DÙNG "con hùng trùng")
- 雌虫 -> Thư trùng (TUYỆT ĐỐI KHÔNG DÙNG "con thư trùng")
- 军雌 -> Quân thư (TUYỆT ĐỐI KHÔNG DÙNG "con quân thư")
- 亚雌 -> Á thư (TUYỆT ĐỐI KHÔNG DÙNG "con á thư")
- Không thêm lượng từ "con" phía trước danh xưng trùng tộc.
- 雌父 -> Thư phụ
- 雄父 -> Hùng phụ
- 虫皇 -> Trùng Hoàng
- 虫神 -> Trùng Thần
- 信息素 -> Pheromone
- 暴动期 / 狂暴期 -> Kỳ cuồng bạo
- 精神力 -> Tinh thần lực
- 虫化 -> Trùng hóa

6. ĐỊNH DẠNG:
- Bắt đầu mỗi đoạn bằng [1], [2], ... [N] theo đúng thứ tự.
- Nội dung văn bản dịch chuẩn xác, chau chuốt, không giải thích bên lề."""

MODELS = [
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash-lite",
    "gemini-3-flash-preview"
]

def extract_text(res):
    if res and res.text:
        return res.text
    if res and res.candidates and res.candidates[0].content and res.candidates[0].content.parts:
        parts_text = [p.text for p in res.candidates[0].content.parts if hasattr(p, 'text') and p.text]
        if parts_text:
            return "".join(parts_text)
    return ""

def translate_chunk(chunk_paras, prev_context=""):
    safety_settings = [
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
    ]
    
    input_text = ""
    for i, p in enumerate(chunk_paras):
        input_text += f"[{i+1}] {p}\n\n"
    
    prompt = f"Dịch danh sách {len(chunk_paras)} đoạn văn sau sang tiếng Việt, giữ đúng thứ tự từ [1] đến [{len(chunk_paras)}].\n"
    if prev_context:
        prompt += f"Bối cảnh đoạn trước (tham khảo, KHÔNG dịch lại):\n\"\"\"\n{prev_context}\n\"\"\"\n\n"
    prompt += f"Nội dung cần dịch ({len(chunk_paras)} đoạn):\n\"\"\"\n{input_text.strip()}\n\"\"\"\n\n"
    prompt += f"Yêu cầu: Trả về chính xác {len(chunk_paras)} đoạn dịch tiếng Việt. Bắt đầu mỗi đoạn bằng số thứ tự [1], [2], ... [{len(chunk_paras)}] để đối chiếu 1:1."

    max_attempts = 6
    for attempt in range(max_attempts):
        model_name = MODELS[attempt % len(MODELS)]
        client = get_client()
        try:
            print(f"    Calling {model_name} (key {current_key_idx})...", flush=True)
            res = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYS_PROMPT,
                    temperature=0.2,
                    safety_settings=safety_settings,
                    max_output_tokens=8192
                )
            )
            raw_output = extract_text(res).strip()
            if not raw_output:
                raise ValueError("Empty response received from model")
            
            # Parse output by [i]
            pattern = re.compile(r'^\[(\d+)\]\s*(.*)$', re.MULTILINE)
            matches = list(pattern.finditer(raw_output))
            
            if len(matches) == len(chunk_paras):
                parsed_paras = []
                for idx, m in enumerate(matches):
                    start_pos = m.start(2)
                    end_pos = matches[idx+1].start() if idx + 1 < len(matches) else len(raw_output)
                    para_text = raw_output[start_pos:end_pos].strip()
                    parsed_paras.append(para_text)
                return parsed_paras
            else:
                splits = [p.strip() for p in raw_output.split("\n\n") if p.strip()]
                clean_splits = [re.sub(r'^\[\d+\]\s*', '', p).strip() for p in splits]
                if len(clean_splits) == len(chunk_paras):
                    return clean_splits
                
                print(f"Warning: expected {len(chunk_paras)} paras, got {len(matches)} matches / {len(clean_splits)} splits. Retrying attempt {attempt+1}...", flush=True)
                time.sleep(2)
        except Exception as e:
            err_str = str(e)
            print(f"API error on attempt {attempt+1} ({model_name}): {err_str[:120]}...", flush=True)
            rotate_key()
            time.sleep(2)

    raise RuntimeError(f"Failed to translate chunk of {len(chunk_paras)} paragraphs after {max_attempts} attempts.")

CHUNK_OVERRIDE = {
    ("ch_031", 4): [
        "Yết hầu khẽ trượt lên trượt xuống hai cái, hùng trùng xinh đẹp khẽ nâng mắt, đầu ngón tay chạm vào bên má ướt đẫm mồ hôi của Alex, sau đó tựa như một phần thưởng, vào lúc thư trùng cúi đầu đòi một nụ hôn, anh liền ngửa đầu áp đôi môi mình lên cánh môi đỏ mọng, ướt át và nóng bỏng của đối phương.",
        '"Ưm..."',
        "Giữa bóng tối mịt mùng, chẳng rõ là ai giở trò dùng thêm chút lực, càng không phân biệt nổi là ai dưới kích thích bất ngờ ập đến mà không kìm nén được khẽ thốt lên tiếng rên trầm thấp từ nơi cuống họng.",
        "Đầu ngón tay bất giác dùng sức, lưu lại những dấu vết mờ ám trên làn da mịn màng ấy.",
        "Mùi cam quýt xung quanh càng lúc càng nồng đậm, có một khoảnh khắc, Alex thậm chí có chút không phân biệt nổi những việc mình đang làm vào giờ phút này rốt cuộc là một giấc mộng hay là hiện thực.",
        "Tiếng nước róc rách.",
        "Tiếng thở dốc ngắt quãng.",
        "Cùng với hương cam quýt gần như muốn ép cạn toàn bộ không khí ra ngoài.",
        "Mọi thứ, hết thảy đều mờ ám và huyễn hoặc như một giấc mộng.",
        "Đặc biệt là hùng trùng trước mắt hắn.",
        "Đôi mắt màu lam xám khẽ rũ, cánh môi đỏ mọng xưa nay chỉ hé lộ nụ cười mỉa mai và xấu xa nay khẽ mở ra thở dốc, cả người dưới sự phản chiếu của bức tường nền đen kịt tựa như một vị tà thần được thai nghén từ trong bóng tối, dụ dỗ người ta cắn câu, mê hoặc người ta nghiện ngập, dễ dàng khiến bọn họ thổ lộ ra những bí mật vốn thường ngày luôn chôn giấu tận đáy lòng.",
        "Alex nhìn vị tà thần trước mắt nâng bàn tay mềm mại dường như không có xương cốt của mình lên, đặt lên cần cổ của hắn, ngón tay cái khẽ ấn nhẹ lên yết hầu hắn, đầu ngón tay xoay nhẹ, sau đó từng chút một tăng thêm lực đạo.",
        "Làn da trắng nõn dưới sự vuốt ve của đầu ngón tay trở nên ửng đỏ, cùng lúc đó, pheromone xung quanh càng lúc càng nồng đậm, nồng đậm đến mức Alex cảm giác như từng lỗ chân lông trên cơ thể mình đều đã tiếp nhận lấy mùi hương cam quýt ấy.",
        "Trong lúc đầu óc hoàn toàn trống rỗng, Alex thậm chí sinh ra một ảo giác rằng toàn bộ thân tâm mình đều đã bị Sở Tư Thừa khống chế triệt để.",
        '"Trùng chủ..."'
    ]
}

def translate_chapter(ch_num):
    ch_id = f"ch_{ch_num:03d}"
    ch_dir = os.path.join(BASE_DIR, "chapters", ch_id)
    meta_path = os.path.join(ch_dir, "meta.json")
    src_path = os.path.join(ch_dir, "source.md")
    out_path = os.path.join(ch_dir, "translation.md")
    sum_path = os.path.join(ch_dir, "summary.json")

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(src_path, "r", encoding="utf-8") as f:
        src = f.read()

    body = re.sub(r"^---[\s\S]*?---\s*", "", src, count=1).strip()
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    total_paras = len(paras)

    print(f"\n==================================================", flush=True)
    print(f"Translating {ch_id} ({meta.get('title')}) - {total_paras} paragraphs", flush=True)
    print(f"==================================================", flush=True)

    chunk_size = 15
    translated_all = []
    
    for i in range(0, total_paras, chunk_size):
        chunk_idx = i // chunk_size
        chunk = paras[i:i+chunk_size]
        prev_tail = "\n\n".join(translated_all[-2:]) if translated_all else ""
        print(f"  Chunk {chunk_idx + 1}/{(total_paras + chunk_size - 1)//chunk_size} (paras {i+1} to {min(i+chunk_size, total_paras)})...", flush=True)
        if (ch_id, chunk_idx) in CHUNK_OVERRIDE:
            print(f"    Using verified manual translation for {ch_id} chunk {chunk_idx+1}...", flush=True)
            trans_chunk = CHUNK_OVERRIDE[(ch_id, chunk_idx)]
        else:
            trans_chunk = translate_chunk(chunk, prev_tail)
        translated_all.extend(trans_chunk)

    if len(translated_all) != total_paras:
        raise ValueError(f"Paragraph mismatch in {ch_id}: source has {total_paras}, translation has {len(translated_all)}")

    # Post processing QC replacements
    cleaned_all = []
    for p in translated_all:
        # Rule: No "con thư trùng", "con hùng trùng", "con quân thư", "con á thư"
        p = re.sub(r'\b[Cc]on thư trùng\b', 'thư trùng', p)
        p = re.sub(r'\b[Cc]on hùng trùng\b', 'hùng trùng', p)
        p = re.sub(r'\b[Cc]on quân thư\b', 'quân thư', p)
        p = re.sub(r'\b[Cc]on á thư\b', 'á thư', p)
        # Rule: Western names
        p = re.sub(r'\bA Lợi Khắc Tư\b', 'Alex', p)
        p = re.sub(r'\bNgải Lợi Khắc Tư\b', 'Alex', p)
        p = re.sub(r'\bThụy An\b', 'Ryan', p)
        p = re.sub(r'\bPhí Lạc\b', 'Felo', p)
        p = re.sub(r'\bPhật Đức Lý Hi\b', 'Friedrich', p)
        p = re.sub(r'\bHải Đức Mạn\b', 'Heideman', p)
        p = re.sub(r'\bNgải Lợi Âu\b', 'Elio', p)
        p = re.sub(r'\bTát Khắc Sâm\b', 'Sachsen', p)
        cleaned_all.append(p)

    title_str = f"Khi Đại Lão Phản Diện Sắm Vai Nhân Vật Chính [Khoái Xuyên] — {meta.get('title')}"
    md_content = f"---\ntitle: {title_str}\n---\n\n" + "\n\n".join(cleaned_all) + "\n"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Saved translation to {out_path} ({len(cleaned_all)} paragraphs)", flush=True)

    # Generate summary
    print(f"Generating summary for {ch_id}...", flush=True)
    client = get_client()
    sum_prompt = f"Hãy tóm tắt ngắn gọn (150-250 từ) nội dung chương truyện sau bằng tiếng Việt theo góc nhìn cốt truyện chính. Không mở đầu sáo rỗng:\n\n{md_content[:10000]}"
    try:
        s_res = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=sum_prompt,
            config=types.GenerateContentConfig(temperature=0.3, max_output_tokens=500)
        )
        summary_text = s_res.text.strip()
    except Exception as e:
        print(f"Failed to generate summary: {e}", flush=True)
        summary_text = f"Tóm tắt chương {ch_num} tác phẩm Khi Đại Lão Phản Diện Sắm Vai Nhân Vật Chính [Khoái Xuyên]."

    sum_data = {
        "chapter_id": ch_id,
        "summary": summary_text,
        "translated_at": now_gmt7_iso()
    }
    with open(sum_path, "w", encoding="utf-8") as f:
        json.dump(sum_data, f, ensure_ascii=False, indent=2)
    print(f"Saved summary for {ch_id}", flush=True)

if __name__ == "__main__":
    start_ch = int(sys.argv[1]) if len(sys.argv) > 1 else 31
    end_ch = int(sys.argv[2]) if len(sys.argv) > 2 else start_ch
    for ch in range(start_ch, end_ch + 1):
        translate_chapter(ch)
