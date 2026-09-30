import os, json, sys, re
sys.stdout.reconfigure(encoding='utf-8')
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY_1'))
base_dir = r"d:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters"

for i in range(26, 34):
    ch_id = f"ch_{i:03d}"
    ch_dir = os.path.join(base_dir, ch_id)
    tr_path = os.path.join(ch_dir, "translation.md")
    sum_path = os.path.join(ch_dir, "summary.json")

    with open(tr_path, "r", encoding="utf-8") as f:
        text = f.read()

    body = re.sub(r"^---[\s\S]*?---\s*", "", text, count=1).strip()
    prompt = (
        "Bạn là biên tập viên tiểu thuyết chuyên nghiệp. Nhiệm vụ của bạn là tóm tắt chương truyện sau bằng Tiếng Việt.\n"
        "Yêu cầu:\n"
        "1. Tóm tắt súc tích, mạch lạc (khoảng 150 - 250 từ).\n"
        "2. Nêu bật các sự kiện và hành động chính diễn ra trong chương.\n"
        "3. Thể hiện sự phát triển tâm lý, lời thoại quan trọng hoặc biến chuyển quan hệ nhân vật.\n"
        "4. Nêu tình huống kết chương / điểm thắt (cliffhanger) nếu có.\n"
        "5. Tuyệt đối không mở đầu bằng câu sáo rỗng như 'Chương này nói về...', 'Sau đây là tóm tắt...', hãy đi thẳng vào nội dung.\n\n"
        f"=== NỘI DUNG CHƯƠNG ===\n{body[:12000]}"
    )

    try:
        res = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=1000
            )
        )
        s_text = res.text.strip() if res and res.text else ""
        if len(s_text) > 100:
            sum_data = {
                "chapter_id": ch_id,
                "summary": s_text,
                "translated_at": "2026-09-30T23:35:00+07:00"
            }
            with open(sum_path, "w", encoding="utf-8") as f:
                json.dump(sum_data, f, ensure_ascii=False, indent=2)
            print(f"✅ {ch_id}: Summary enriched ({len(s_text)} chars)")
        else:
            print(f"⚠️ {ch_id}: Response too short ({len(s_text)} chars)")
    except Exception as e:
        print(f"❌ {ch_id}: Error {e}")
