import os
import sys
import re
import json
import time
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv(r"d:\Nhung\trans-tool\.env")

from google import genai
from google.genai import types

def now_gmt7():
    return datetime.now(timezone(timedelta(hours=7)))

# -------------------------------------------------------------
# Gemini API Key Rotator & Robust Caller
# -------------------------------------------------------------
class KeyRotator:
    def __init__(self):
        self.clients = []
        for i in range(1, 21):
            key = os.environ.get(f"GEMINI_API_KEY_{i}") or (os.environ.get("GEMINI_API_KEY") if i == 1 else None)
            if key and key.strip():
                self.clients.append(genai.Client(api_key=key.strip()))
        if not self.clients:
            raise RuntimeError("No GEMINI_API_KEY found in environment!")
        self.current_idx = 0
        print(f"[Rotator] Initialized with {len(self.clients)} API keys.")

    def get_client(self):
        return self.clients[self.current_idx], self.current_idx

    def rotate(self):
        prev = self.current_idx
        self.current_idx = (self.current_idx + 1) % len(self.clients)
        print(f"[Rotator] Switched from Key {prev+1} -> Key {self.current_idx+1}")
        return self.clients[self.current_idx]

rotator = KeyRotator()

def call_gemini_with_retry(contents, system_instruction, temp=0.2, max_retries=10):
    safety_settings = [
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
    ]

    models = ["gemini-2.5-flash", "gemini-2.5-flash-lite"]
    
    for attempt in range(max_retries):
        model = models[attempt % len(models)]
        client, k_idx = rotator.get_client()
        try:
            config = types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=temp,
                safety_settings=safety_settings
            )
            resp = client.models.generate_content(
                model=model,
                contents=contents,
                config=config
            )
            if resp and resp.text and resp.text.strip():
                return resp.text.strip()
            print(f"[Gemini] Empty response on attempt {attempt+1}, retrying...")
            time.sleep(2)
        except Exception as e:
            err_str = str(e)
            print(f"[Gemini] Error on attempt {attempt+1} (Key {k_idx+1}, {model}): {err_str[:120]}")
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str or "quota" in err_str.lower():
                rotator.rotate()
                time.sleep(3)
            elif "403" in err_str:
                rotator.rotate()
                time.sleep(2)
            else:
                time.sleep(2)

    raise RuntimeError(f"Gemini API failed after {max_retries} retries!")

# -------------------------------------------------------------
# Helpers
# -------------------------------------------------------------
PROJECT_SLUG = "đại-ma-đầu-nhật-nhật-tưởng-sát-ngã"
BASE_DIR = rf"d:\Nhung\trans-tool\novel_projects\{PROJECT_SLUG}"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
MEMORY_DIR = os.path.join(BASE_DIR, "memory")

def load_json(p, default=None):
    if not os.path.exists(p):
        return default if default is not None else {}
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(p, data):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_config():
    return load_json(os.path.join(BASE_DIR, "config.json"), {})

def load_memory():
    return {
        'characters': load_json(os.path.join(MEMORY_DIR, "characters.json"), []),
        'glossary': load_json(os.path.join(MEMORY_DIR, "glossary.json"), []),
        'relationships': load_json(os.path.join(MEMORY_DIR, "relationships.json"), []),
    }

def format_memory_for_prompt(mem):
    lines = []
    if mem.get('characters'):
        lines.append("=== CHARACTERS (NHÂN VẬT & ĐẠI TỪ) ===")
        for c in mem['characters'][:35]:
            c_name = c.get('name', '')
            hv_name = f" / Hán-Việt: {c['hanviet_name']}" if c.get('hanviet_name') else ""
            pronoun = f" | Đại từ ngôi 3: {c['third_person_pronoun']}" if c.get('third_person_pronoun') else ""
            aliases = ", ".join(c.get('aliases', [])[:5])
            lines.append(f"- {c_name}{hv_name} ({c.get('gender','')}){pronoun} | Aliases: {aliases} | Speech: {c.get('speech_style','')} | Honorifics: {c.get('honorifics','')}")

    if mem.get('relationships'):
        lines.append("\n=== CHARACTER FORMS OF ADDRESS (XƯNG HÔ ĐỐI THOẠI) ===")
        for r in mem['relationships'][:30]:
            lines.append(f"- {r.get('pair', '')}: {r.get('address', '')}")

    if mem.get('glossary'):
        lines.append("\n=== PROJECT GLOSSARY (THUẬT NGỮ BẮT BUỘC) ===")
        for g in mem['glossary'][:65]:
            hv = f" (Hán-Việt: {g['hanviet']})" if g.get('hanviet') else ""
            lines.append(f"- {g.get('original','')} → {g.get('translation','')}{hv} [{g.get('category','')}]")

    return "\n".join(lines)

def get_prev_chapter_summary(ch_id):
    # Find preceding chapter number
    m = re.search(r'ch_(\d+)', ch_id)
    if not m:
        return ""
    cur_n = int(m.group(1))
    prev_id = f"ch_{cur_n-1:03d}"
    prev_sum_file = os.path.join(CHAPTERS_DIR, prev_id, "summary.json")
    if os.path.exists(prev_sum_file):
        data = load_json(prev_sum_file, {})
        return data.get('summary', '').strip()
    return ""

def clean_ai_markdown(text):
    text = re.sub(r'^```(?:markdown)?\s*', '', text.strip(), flags=re.IGNORECASE)
    text = re.sub(r'\s*```$', '', text).strip()
    return text

# -------------------------------------------------------------
# Translation Step
# -------------------------------------------------------------
def translate_chunk(chunk_body, cfg, mem, prev_sum, prev_tail):
    target_lang = cfg.get('target_lang', 'Vietnamese')
    style_guide = cfg.get('style_guide', '')
    mem_str = format_memory_for_prompt(mem)

    prompt_parts = []
    if style_guide:
        prompt_parts.append(f"=== STYLE GUIDE & MANDATORY RULES ===\n{style_guide}")
    if prev_sum:
        prompt_parts.append(f"=== PREVIOUS CHAPTER CONTEXT ===\n{prev_sum}")
    if mem_str:
        prompt_parts.append(f"=== NOVEL MEMORY & GLOSSARY ===\n{mem_str}")
    if prev_tail:
        prompt_parts.append(f"=== PREVIOUS CONTEXT (DO NOT RETRANSLATE, ONLY USE FOR CONTINUITY) ===\n{prev_tail}")
    prompt_parts.append(f"=== TRANSLATE THE FOLLOWING TEXT TO {target_lang.upper()} ===\n{chunk_body}")

    prompt = "\n\n".join(prompt_parts)

    sys_instruction = (
        f"You are a professional literary translator specializing in {cfg.get('source_lang','Chinese')} to {target_lang} novel translation.\n"
        "STRICT MANDATORY RULES:\n"
        "1. Output ONLY the translation text. No commentary, no intro/outro, no translators notes.\n"
        "2. Dialogue: All direct speech MUST be wrapped in standard quotation marks “...”. Never use dashes (-) for dialogue.\n"
        "3. Separation: Dialogue and non-dialogue (narrative/description) must NEVER share the same paragraph. Always split into distinct paragraphs separated by blank lines.\n"
        "4. PRONOUN RULES (STRICT):\n"
        "   - Công: Hạ Khanh Tuyên -> in narration use 'hắn'.\n"
        "   - Thụ: Ứng Hàn Y -> in narration use 'y' or 'ma đầu' / 'Ma tôn'. NEVER confuse or swap these two.\n"
        "   - In dialogue: Ứng Hàn Y calls Hạ Khanh Tuyên 'tiểu tử'/'ngươi', self-refers as 'bổn tôn'/'ta'. Hạ Khanh Tuyên calls Ứng Hàn Y 'tiền bối'/'ngài' (initially) or 'ngươi' (later), self-refers as 'ta'. Absolutely NO 'tao - mày'.\n"
        "5. Style: High-grade ancient Xianxia literary Vietnamese, fluid, natural, evocative."
    )

    result = call_gemini_with_retry(prompt, sys_instruction, temp=0.25)
    return clean_ai_markdown(result)

# -------------------------------------------------------------
# QC / Review & Polish Step
# -------------------------------------------------------------
def qc_and_polish_chapter(ch_id, title_str, draft_text, cfg, mem):
    style_guide = cfg.get('style_guide', '')
    mem_str = format_memory_for_prompt(mem)

    # Step 1: Generate Consistency & QC Review Report
    prompt_rev = (
        f"=== STYLE GUIDE & PROJECT RULES ===\n{style_guide}\n\n"
        f"=== NOVEL MEMORY & GLOSSARY ===\n{mem_str}\n\n"
        f"=== TRANSLATION OF {ch_id} TO REVIEW ===\n{draft_text[:9000]}"
    )

    sys_rev = (
        "You are a strict, senior literary editor reviewing a Vietnamese Xianxia novel translation.\n"
        "Check specifically for:\n"
        "1. Pronoun consistency: Hạ Khanh Tuyên (công) must be 'hắn'; Ứng Hàn Y (thụ) must be 'y' or 'ma đầu'/'Ma tôn'. Flag any inversions.\n"
        "2. Dialogue formatting: Must use standard quotation marks “...”, dialogue separate from narrative, no 'tao - mày'.\n"
        "3. Terminology & Names: Must match Glossary and Character List exactly.\n"
        "4. Flow & Tone: Flag any robotic, Sino-Vietnamese word-for-word clunky phrasing.\n"
        "Output a concise Markdown Review Report detailing issues and suggested corrections."
    )

    print(f"  [QC Review] Analyzing translation consistency for {ch_id}...")
    report_text = call_gemini_with_retry(prompt_rev, sys_rev, temp=0.1)

    # Step 2: Apply QC Polish directly to ensure the highest final text quality
    prompt_apply = (
        f"=== STYLE GUIDE & PROJECT RULES ===\n{style_guide}\n\n"
        f"=== NOVEL MEMORY & GLOSSARY ===\n{mem_str}\n\n"
        f"=== QC REVIEW REPORT ===\n{report_text}\n\n"
        f"=== BẢN DỊCH CẦN BIÊN TẬP & SỬA LỖI THEO QC ===\n{draft_text}"
    )

    sys_apply = (
        "You are an expert literary copyeditor specializing in Vietnamese novel translations.\n"
        "Your task is to revise, polish and finalize this chapter strictly addressing any issues from the QC Review Report.\n"
        "RULES:\n"
        "1. Output ONLY the complete revised translation text. Do NOT include Markdown code fences (```markdown), intro/outro remarks, or notes.\n"
        "2. Ensure pronouns are 100% strictly accurate: Hạ Khanh Tuyên (công) = hắn; Ứng Hàn Y (thụ) = y / ma đầu / Ma tôn.\n"
        "3. Format all dialogues cleanly with “...” on separate lines.\n"
        "4. Smooth out any awkward sentences into engaging, immersive literary prose.\n"
        "5. Keep the heading at the top if present, e.g. '# {title_str}'."
    )

    print(f"  [QC Apply] Polishing and finalizing {ch_id} text...")
    polished_text = call_gemini_with_retry(prompt_apply, sys_apply, temp=0.15)
    polished_text = clean_ai_markdown(polished_text)

    # Ensure title heading exists at the top
    if not polished_text.startswith("#"):
        polished_text = f"# {title_str}\n\n{polished_text}"

    return polished_text, report_text

# -------------------------------------------------------------
# Summary Generator
# -------------------------------------------------------------
def generate_summary(ch_id, text_content):
    sys_prompt = (
        "You are a novel editor. Write a concise 2-4 sentence summary in Vietnamese of this chapter's key plot events and character interactions.\n"
        "Output ONLY the summary text."
    )
    prompt = f"=== CHƯƠNG {ch_id} ===\n{text_content[:4000]}"
    sum_res = call_gemini_with_retry(prompt, sys_prompt, temp=0.2)
    return clean_ai_markdown(sum_res)

# -------------------------------------------------------------
# Main Process Loop
# -------------------------------------------------------------
def process_all_missing():
    target_chapters = [
        "ch_048", "ch_053", "ch_073", "ch_079", "ch_082",
        "ch_086", "ch_092", "ch_093", "ch_099", "ch_102",
        "ch_113", "ch_115", "ch_119"
    ]

    cfg = load_config()
    mem = load_memory()

    print(f"\n=======================================================")
    print(f"Starting Batch Translation & QC for {len(target_chapters)} chapters")
    print(f"Project: {PROJECT_SLUG}")
    print(f"Chapters: {', '.join(target_chapters)}")
    print(f"=======================================================\n")

    for idx, ch_id in enumerate(target_chapters, 1):
        ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
        chunks_dir = os.path.join(ch_dir, "chunks")
        meta = load_json(os.path.join(ch_dir, "meta.json"), {})
        title_str = meta.get("title", ch_id)

        print(f"\n[{idx}/{len(target_chapters)}] >>> PROCESSING {ch_id} ({title_str}) <<<")

        # 1. Check chunk files
        chunk_files = sorted([f for f in os.listdir(chunks_dir) if f.startswith("chunk_") and f.endswith(".md") and "_trans" not in f])
        if not chunk_files:
            print(f"  [ERROR] No chunk files found for {ch_id}! Skipping.")
            continue

        prev_sum = get_prev_chapter_summary(ch_id)
        translated_chunks = []

        # 2. Translate each chunk
        for ci, cf in enumerate(chunk_files, 1):
            c_path = os.path.join(chunks_dir, cf)
            with open(c_path, 'r', encoding='utf-8') as f:
                c_raw = f.read()
            c_body = re.sub(r'^---[\s\S]*?---\s*', '', c_raw, count=1).strip()

            prev_tail = ""
            if translated_chunks:
                lines = [l for l in translated_chunks[-1].split('\n') if l.strip()]
                prev_tail = '\n'.join(lines[-2:])

            print(f"  [Translate] Chunk {ci}/{len(chunk_files)} ({len(c_body)} chars)...")
            t_chunk = translate_chunk(c_body, cfg, mem, prev_sum, prev_tail)
            translated_chunks.append(t_chunk)

            # Save chunk trans file
            trans_c_path = os.path.join(chunks_dir, cf.replace(".md", "_trans.md"))
            with open(trans_c_path, 'w', encoding='utf-8') as f:
                f.write(f"---\ntitle: {ch_id} chunk {ci}\n---\n\n{t_chunk}")

        draft_merged = "\n\n".join(translated_chunks)

        # 3. QC & Polish
        print(f"  [QC & Polish] Running consistency review and refinement...")
        final_trans, report_text = qc_and_polish_chapter(ch_id, title_str, draft_merged, cfg, mem)

        # 4. Save translation.md
        trans_md_path = os.path.join(ch_dir, "translation.md")
        with open(trans_md_path, 'w', encoding='utf-8') as f:
            f.write(final_trans)
        print(f"  -> Saved translation: {trans_md_path} ({len(final_trans)} chars)")

        # 5. Save review_report.json
        review_path = os.path.join(ch_dir, "review_report.json")
        save_json(review_path, {
            "chapter_id": ch_id,
            "reviewed_at": now_gmt7().isoformat(),
            "report": report_text,
            "applied_at": now_gmt7().isoformat()
        })
        print(f"  -> Saved review report: {review_path}")

        # 6. Generate and save summary.json
        ch_sum = generate_summary(ch_id, final_trans)
        sum_path = os.path.join(ch_dir, "summary.json")
        save_json(sum_path, {
            "chapter_id": ch_id,
            "summary": ch_sum,
            "generated_at": now_gmt7().isoformat()
        })
        print(f"  -> Saved chapter summary: {ch_sum[:100]}...")

        # Small pause between chapters
        time.sleep(1.5)

    print("\n=======================================================")
    print("ALL 13 CHAPTERS TRANSLATED AND QC'D SUCCESSFULLY!")
    print("=======================================================")

if __name__ == "__main__":
    process_all_missing()
