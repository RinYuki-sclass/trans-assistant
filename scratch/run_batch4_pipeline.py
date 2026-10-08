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

from scratch.process_single_chapter import process_chapter, parse_source, generate_qa_and_qc, post_process_qc
from scratch.batch2_trans_helper import translate_chunk_with_retry
from scratch.check_all_qc import parse_md

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

batch4_chapters = [
    'ch_024',
    'ch_025',
    'ch_026',
    'ch_027',
    'ch_028',
    'ch_029',
    'ch_030',
]

print(f"==================================================")
print(f"🚀 STARTING BATCH 4 PIPELINE: {batch4_chapters}")
print(f"==================================================")

results = {}

for cid in batch4_chapters:
    t0 = time.time()
    cdir = os.path.join(CHAPTERS_DIR, cid)
    s_path = os.path.join(cdir, "source.md")
    t_path = os.path.join(cdir, "translation.md")
    
    title, s_paras = parse_source(cid)
    print(f"\n>>> {cid}: {title} ({len(s_paras)} paragraphs)")
    
    # Check if already translated and matched
    if os.path.exists(t_path):
        parsed_s = parse_md(s_path)
        parsed_t = parse_md(t_path)
        if len(parsed_s) == len(parsed_t) and len(parsed_t) > 0:
            print(f"⏩ {cid} already translated and verified ({len(parsed_t)} paras). Skipping!")
            results[cid] = {'status': 'PASS', 'paras': len(parsed_t), 'time': 'cached'}
            continue

    # Process translation
    for retry in range(3):
        try:
            _, t_paras = process_chapter(cid)
            
            # Audit check
            parsed_s = parse_md(s_path)
            parsed_t = parse_md(t_path)
            
            if len(parsed_s) != len(parsed_t):
                print(f"❌ Mismatch in {cid}: {len(parsed_s)} vs {len(parsed_t)}, retrying...")
                continue
                
            elapsed = time.time() - t0
            results[cid] = {'status': 'PASS', 'paras': len(parsed_t), 'time': f"{elapsed:.1f}s"}
            print(f"✅ {cid} verified 100% PASS ({len(parsed_t)} paras) in {elapsed:.1f}s!\n")
            break
        except Exception as e:
            print(f"⚠️ Attempt {retry+1} failed for {cid}: {e}")
            time.sleep(3)
    else:
        print(f"❌ Failed to process {cid} after retries!")
        results[cid] = {'status': 'FAIL'}
        break
    time.sleep(2)

print("\n==========================================")
print("BATCH 4 PIPELINE SUMMARY:")
for cid, res in results.items():
    print(f"  {cid}: {res}")
print("==========================================")
