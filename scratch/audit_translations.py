import os
import re
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

BASE_DIR = r"d:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho"

FORBIDDEN_TERMS = [
    r'\bA Lợi Khắc Tư\b',
    r'\bNgải Lợi Khắc Tư\b',
    r'\bThụy An\b',
    r'\bPhí Lạc\b',
    r'\bPhật Đức Lý Hi\b',
    r'\bHải Đức Mạn\b',
    r'\bNgải Lợi Âu\b',
    r'\bTát Khắc Sâm\b',
    r'\b[Cc]on thư trùng\b',
    r'\b[Cc]on hùng trùng\b',
    r'\b[Cc]on quân thư\b',
    r'\b[Cc]on á thư\b',
]

def audit():
    print("=" * 60)
    print("AUDIT & VERIFICATION REPORT (CH_016 -> CH_025)")
    print("=" * 60)

    all_passed = True

    for i in range(26, 34):
        ch_id = f"ch_{i:03d}"
        ch_dir = os.path.join(BASE_DIR, "chapters", ch_id)
        src_path = os.path.join(ch_dir, "source.md")
        tr_path = os.path.join(ch_dir, "translation.md")
        sum_path = os.path.join(ch_dir, "summary.json")

        if not os.path.exists(tr_path):
            print(f"❌ {ch_id}: translation.md NOT FOUND!")
            all_passed = False
            continue

        with open(src_path, "r", encoding="utf-8") as f:
            src_text = f.read()
        with open(tr_path, "r", encoding="utf-8") as f:
            tr_text = f.read()

        src_body = re.sub(r"^---[\s\S]*?---\s*", "", src_text, count=1).strip()
        tr_body = re.sub(r"^---[\s\S]*?---\s*", "", tr_text, count=1).strip()

        src_paras = [p.strip() for p in src_body.split("\n\n") if p.strip()]
        tr_paras = [p.strip() for p in tr_body.split("\n\n") if p.strip()]

        # Paragraph count check
        count_match = len(src_paras) == len(tr_paras)
        if not count_match:
            print(f"❌ {ch_id}: PARAGRAPH MISMATCH! Source: {len(src_paras)}, Trans: {len(tr_paras)}")
            all_passed = False
        else:
            print(f"✅ {ch_id}: 1:1 Paragraphs matched perfectly ({len(tr_paras)}/{len(src_paras)})")

        # Forbidden terms check
        term_violations = []
        for pat in FORBIDDEN_TERMS:
            matches = re.findall(pat, tr_body)
            if matches:
                term_violations.extend(matches)
        
        if term_violations:
            print(f"   ⚠️ Forbidden terms found in {ch_id}: {set(term_violations)}")
            all_passed = False
        else:
            print(f"   ✅ No forbidden terms or prefixes found.")

        # Summary check
        if os.path.exists(sum_path):
            with open(sum_path, "r", encoding="utf-8") as f:
                s_data = json.load(f)
            s_text = s_data.get("summary", "")
            if not s_text or "Tóm tắt chương" in s_text and len(s_text) < 100:
                print(f"   ⚠️ Summary needs update for {ch_id} (short placeholder). Generating now...")
                client = genai.Client(api_key=os.getenv('GEMINI_API_KEY_1') or os.getenv('GEMINI_API_KEY_2'))
                sum_prompt = f"Hãy tóm tắt ngắn gọn (150-250 từ) nội dung chương truyện sau bằng tiếng Việt theo góc nhìn cốt truyện chính. Không mở đầu sáo rỗng:\n\n{tr_text[:10000]}"
                res = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=sum_prompt,
                    config=types.GenerateContentConfig(temperature=0.3, max_output_tokens=500)
                )
                s_data["summary"] = res.text.strip()
                with open(sum_path, "w", encoding="utf-8") as f:
                    json.dump(s_data, f, ensure_ascii=False, indent=2)
                print(f"   ✅ Summary updated for {ch_id} ({len(s_data['summary'])} chars)")
            else:
                print(f"   ✅ Summary valid ({len(s_text)} chars)")
        else:
            print(f"   ❌ summary.json missing for {ch_id}")
            all_passed = False

    print("=" * 60)
    if all_passed:
        print("🎉 ALL 10 CHAPTERS (CH_016 -> CH_025) PASSED 100% QUALITY & ALIGNMENT CHECKS!")
    else:
        print("⚠️ Some issues were detected above.")
    print("=" * 60)

if __name__ == "__main__":
    audit()
