import glob
import os
import sys
import json
import re
import time
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')

from google import genai
from google.genai import types

load_dotenv('d:/Nhung/RIDI/trans-assistant/.env')

dir_path = glob.glob('d:/Nhung/RIDI/trans-assistant/novel_projects/*khi*')[0]

# Setup keys
keys = []
for i in range(1, 10):
    k = os.getenv(f'GEMINI_API_KEY_{i}')
    if k and k.strip():
        keys.append(k.strip())
if not keys and os.getenv('GEMINI_API_KEY'):
    keys.append(os.getenv('GEMINI_API_KEY').strip())

print(f"Loaded {len(keys)} Gemini API keys.")

clients = [genai.Client(api_key=k) for k in keys]
current_key_idx = 0

def call_gemini(prompt: str, sys_instruction: str, model="gemini-3.5-flash-lite", retries=5):
    global current_key_idx
    config = types.GenerateContentConfig(
        system_instruction=sys_instruction,
        temperature=0.3,
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
            types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
            types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
        ]
    )
    fallback_models = ["gemini-3.5-flash-lite", "gemini-3.1-flash-lite", "gemini-flash-lite-latest", "gemini-2.5-flash-lite"]
    
    for attempt in range(retries):
        client = clients[current_key_idx]
        cur_model = model
        try:
            resp = client.models.generate_content(model=cur_model, contents=prompt, config=config)
            if resp and resp.text:
                return resp.text.strip()
        except Exception as e:
            err_str = str(e)
            print(f"Attempt {attempt+1} failed with Key {current_key_idx+1} and model {cur_model}: {err_str[:80]}")
            # Rotate key
            current_key_idx = (current_key_idx + 1) % len(clients)
            # If 429 quota, wait slightly
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                time.sleep(3)
            else:
                time.sleep(1)
                
    # Fallback to other models
    for m in fallback_models:
        for ki in range(len(clients)):
            try:
                client = clients[ki]
                resp = client.models.generate_content(model=m, contents=prompt, config=config)
                if resp and resp.text:
                    current_key_idx = ki
                    return resp.text.strip()
            except Exception:
                time.sleep(1)
                continue
    raise RuntimeError("All Gemini attempts failed.")

def format_memory_for_prompt(mem_dict):
    lines = []
    chars = mem_dict.get('characters', [])
    if chars:
        lines.append("Characters:")
        for c in chars:
            name = c.get('name')
            orig = c.get('original_name')
            p3 = c.get('third_person_pronoun')
            notes = c.get('notes', '')
            lines.append(f"  - {orig} -> {name} | Ngôi 3: {p3} | {notes}")
    gloss = mem_dict.get('glossary', [])
    if gloss:
        lines.append("\nGlossary:")
        for g in gloss:
            lines.append(f"  - {g.get('original')} -> {g.get('translation')}")
    return '\n'.join(lines)

def format_clarifications_for_prompt(clar_dict):
    answers = clar_dict.get('answers', {})
    questions = clar_dict.get('questions', [])
    q_map = {q['id']: q for q in questions if 'id' in q}
    lines = []
    for aid, a in answers.items():
        q = q_map.get(aid, {})
        orig = q.get('original', aid)
        choice = a.get('choice') or a.get('custom')
        if choice:
            lines.append(f"  - {orig}: {choice}")
    return '\n'.join(lines) if lines else "None"

def build_prompt(cfg, mem_dict, prev_summary, curr_analysis, clar_dict, prev_tail, chunk_text):
    parts = []
    style_guide = cfg.get('style_guide', '')
    if style_guide:
        parts.append(f"=== STYLE GUIDE ===\n{style_guide}")
    if prev_summary:
        parts.append(f"=== PREVIOUS CHAPTER SUMMARY ===\n{prev_summary}")
    ch_sum = curr_analysis.get('chapter_summary', '')
    if ch_sum:
        parts.append(f"=== CURRENT CHAPTER CONTEXT ===\n{ch_sum}")
    mem_str = format_memory_for_prompt(mem_dict)
    if mem_str:
        parts.append(f"=== NOVEL MEMORY ===\n{mem_str}")
    clar_str = format_clarifications_for_prompt(clar_dict)
    if clar_str and clar_str != "None":
        parts.append(f"=== USER DECISIONS (CLARIFICATIONS) ===\n{clar_str}")
    if prev_tail:
        parts.append(f"=== PREVIOUS CONTEXT (DO NOT RETRANSLATE) ===\n{prev_tail}")
    parts.append(f"=== TRANSLATE TO VIETNAMESE ===\n{chunk_text}")
    return '\n\n'.join(parts)

sys_instruction = (
    "You are a professional literary translator specializing in Chinese to Vietnamese novel translation.\n"
    "RULES:\n"
    "1. Output ONLY the translation. No notes, no commentary, no extra text.\n"
    "2. Dialogue (direct speech starting/ending with quotation marks or starting with dashes) and non-dialogue (narratives, descriptions) must NEVER share the same paragraph. Always split them into separate, distinct paragraphs.\n"
    "3. Follow all style guide rules, character names, and glossary entries provided.\n"
    "   - Sở Tư Thừa (楚司承): Luôn dùng đại từ ngôi thứ 3 trong văn trần thuật là 'anh'.\n"
    "   - Ryan (瑞安): Dùng 'cậu'.\n"
    "   - Alex Sachsen (艾利克斯·萨克森): Dùng 'hắn'.\n"
    "   - Felo (费洛): Dùng 'gã' hoặc 'hắn'.\n"
    "   - Friedrich (弗德里希): Dùng 'hắn'.\n"
    "   - Hệ thống (系统): Dùng 'nó'.\n"
    "   - Hư ảnh đầu lâu (骷髅): Dùng 'nó'.\n"
    "4. Apply all user clarification decisions exactly as specified.\n"
    "5. DO NOT translate the 'PREVIOUS CONTEXT' section.\n"
    "6. Style & Flow: Write smooth, natural, high quality literary Vietnamese."
)

with open(f'{dir_path}/config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

with open(f'{dir_path}/memory/characters.json', 'r', encoding='utf-8') as f:
    mem_chars = json.load(f)

with open(f'{dir_path}/memory/glossary.json', 'r', encoding='utf-8') as f:
    mem_gloss = json.load(f)

mem_dict = {'characters': mem_chars, 'glossary': mem_gloss}

target_chapters = ['ch_001', 'ch_002', 'ch_003', 'ch_004', 'ch_005']
prev_summary = ""

for ch in target_chapters:
    ch_dir = f'{dir_path}/chapters/{ch}'
    trans_file = f'{ch_dir}/translation.md'
    
    with open(f'{ch_dir}/analysis.json', 'r', encoding='utf-8') as f:
        curr_analysis = json.load(f)
        
    if os.path.exists(trans_file) and os.path.getsize(trans_file) > 1000:
        print(f"Skipping {ch} (already translated).")
        prev_summary = curr_analysis.get('chapter_summary', '')
        continue
        
    chunks_dir = f'{ch_dir}/chunks'
    chunk_files = sorted([f for f in os.listdir(chunks_dir) if f.endswith('.md') and not f.endswith('_trans.md')])
    
    clar_file = f'{ch_dir}/clarifications.json'
    clar_dict = {}
    if os.path.exists(clar_file):
        with open(clar_file, 'r', encoding='utf-8') as f:
            clar_dict = json.load(f)
            
    print(f"\n==================== TRANSLATING {ch} ({len(chunk_files)} chunks) ====================")
    translated_chunks = []
    
    for ci, cf in enumerate(chunk_files):
        trans_chunk_file = f'{chunks_dir}/{cf.replace(".md", "_trans.md")}'
        if os.path.exists(trans_chunk_file) and os.path.getsize(trans_chunk_file) > 200:
            print(f"[{ch}] Loading existing translation for {cf}...")
            with open(trans_chunk_file, 'r', encoding='utf-8') as f:
                c_content = f.read()
            c_body = re.sub(r'^---[\s\S]*?---\s*', '', c_content, count=1).strip()
            translated_chunks.append(c_body)
            continue
            
        print(f"[{ch}] Translating chunk {ci+1}/{len(chunk_files)}: {cf}...")
        with open(f'{chunks_dir}/{cf}', 'r', encoding='utf-8') as f:
            raw_text = f.read()
            
        body = re.sub(r'^---[\s\S]*?---\s*', '', raw_text, count=1).strip()
        
        prev_tail = ""
        if translated_chunks:
            tail_lines = [l for l in translated_chunks[-1].split('\n') if l.strip()]
            prev_tail = '\n'.join(tail_lines[-2:])
            
        prompt = build_prompt(cfg, mem_dict, prev_summary, curr_analysis, clar_dict, prev_tail, body)
        
        translated_text = call_gemini(prompt, sys_instruction)
        
        # Save chunk translation
        with open(trans_chunk_file, 'w', encoding='utf-8') as f:
            f.write(f"---\ntitle: {ch} chunk {ci+1}\n---\n\n{translated_text}")
            
        translated_chunks.append(translated_text)
        print(f"[{ch}] Chunk {ci+1} done! Length: {len(translated_text)} chars")
        time.sleep(1) # courteous delay
        
    # Merge chapter
    merged_translation = '\n\n'.join(translated_chunks)
    meta_file = f'{ch_dir}/meta.json'
    ch_title = f"{ch.upper()}"
    if os.path.exists(meta_file):
        with open(meta_file, 'r', encoding='utf-8') as f:
            meta_data = json.load(f)
            ch_title = meta_data.get('title', ch_title)
            
    final_md = f"---\ntitle: Khi Đại Lão Phản Diện Sắm Vai Nhân Vật Chính [Khoái Xuyên] — {ch_title}\n---\n\n{merged_translation}"
    with open(f'{ch_dir}/translation.md', 'w', encoding='utf-8') as f:
        f.write(final_md)
        
    # Update summary
    prev_summary = curr_analysis.get('chapter_summary', '')
    summary_data = {
        'chapter_id': ch,
        'summary': prev_summary,
        'translated_at': time.strftime("%Y-%m-%dT%H:%M:%S+07:00")
    }
    with open(f'{ch_dir}/summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary_data, f, ensure_ascii=False, indent=2)
        
    print(f"[OK] FINISHED {ch}: Saved translation.md ({len(merged_translation)} chars)")

# Update chapters_count in config.json
cfg['chapters_count'] = len([ch for ch in target_chapters if os.path.exists(f'{dir_path}/chapters/{ch}/translation.md')])
with open(f'{dir_path}/config.json', 'w', encoding='utf-8') as f:
    json.dump(cfg, f, ensure_ascii=False, indent=2)

print("\n[ALL COMPLETE] ALL CHAPTERS ch_001 -> ch_005 TRANSLATED SUCCESSFULLY!")
