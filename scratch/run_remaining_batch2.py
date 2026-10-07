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

from scratch.process_single_chapter import process_chapter

batch2_chapters = [
    'ch_009',
    'ch_010',
    'ch_011',
    'ch_012',
    'ch_013',
    'ch_014',
    'ch_015',
]

print(f"Starting translation and QC pipeline for remaining Batch 2 chapters: {batch2_chapters}")

results = {}

for cid in batch2_chapters:
    t0 = time.time()
    try:
        title, paras = process_chapter(cid)
        elapsed = time.time() - t0
        results[cid] = {'status': 'PASS', 'paras': len(paras), 'time': f"{elapsed:.1f}s"}
        print(f"✅ {cid} completed in {elapsed:.1f}s with {len(paras)} paragraphs!\n")
    except Exception as e:
        print(f"❌ Error in {cid}: {e}\n")
        results[cid] = {'status': 'FAIL', 'error': str(e)}
        break
    time.sleep(2)

print("\n==========================================")
print("BATCH 2 PIPELINE SUMMARY:")
for cid, res in results.items():
    print(f"  {cid}: {res}")
print("==========================================")
