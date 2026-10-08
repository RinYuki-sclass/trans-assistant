import os
import json
import re

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters"

chapters_summary = []
for i in range(1, 36):
    cid = f"ch_{i:03d}"
    cdir = os.path.join(base_dir, cid)
    source_path = os.path.join(cdir, "source.md")
    meta_path = os.path.join(cdir, "meta.json")
    
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(source_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    # Get paragraphs
    body_paras = [l.strip() for l in lines if l.strip() and not l.startswith('---') and not l.startswith('title:')]
    
    first_few = " ".join(body_paras[:3])[:120]
    last_few = " ".join(body_paras[-2:])[:120] if len(body_paras) >= 2 else ""
    
    chapters_summary.append({
        "id": cid,
        "num": i,
        "title": meta["title"],
        "orig_title": meta["original_title"],
        "n_paras": len(body_paras),
        "first_preview": first_few,
        "last_preview": last_few
    })

for c in chapters_summary:
    print(f"{c['id']} | {c['title']} | {c['n_paras']}p | Head: {c['first_preview'][:60]}... | Tail: {c['last_preview'][:60]}...")
