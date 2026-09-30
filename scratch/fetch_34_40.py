import os
import sys
import json
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"d:\Nhung\trans-tool")
from scripts.audio.crawler import crawl_chapter

novel_dir = r"d:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho"
chapters_dir = os.path.join(novel_dir, "chapters")
cache_path = r"d:\Nhung\trans-tool\data\cache_series\c3999bfac83cc84ffb1af9072a13250c.json"

series_data = json.load(open(cache_path, encoding='utf-8'))
cached_chapters = series_data.get('chapters', [])

targets = []
for ch_num in range(34, 41):
    idx = ch_num - 1
    ch_info = cached_chapters[idx]
    ch_id = f"ch_{ch_num:03d}"
    raw_title = ch_info.get("title", f"第{ch_num}頁")
    title = f"Chương {ch_num}: {raw_title}"
    url = ch_info.get("url")
    targets.append((ch_id, title, url))

chunk_sz = 20
tz = timezone(timedelta(hours=7))

print(f"Starting crawl for {len(targets)} chapters...")
for ch_id, title, url in targets:
    print(f"Crawling {ch_id}: {title} ({url})...")
    data = crawl_chapter(url)
    paras = data.get("paragraphs", [])
    full_text = "\n\n".join(paras)
    
    ch_folder = os.path.join(chapters_dir, ch_id)
    chunks_folder = os.path.join(ch_folder, "chunks")
    os.makedirs(chunks_folder, exist_ok=True)
    
    # 1. source.md
    source_content = f"---\ntitle: {title}\n---\n\n" + full_text
    with open(os.path.join(ch_folder, "source.md"), "w", encoding="utf-8") as f:
        f.write(source_content)
        
    # 2. chunks
    n_chunks = (len(paras) + chunk_sz - 1) // chunk_sz if paras else 1
    for ci in range(n_chunks):
        c_paras = paras[ci*chunk_sz : (ci+1)*chunk_sz]
        c_text = "\n\n".join(c_paras)
        c_title = f"{title} — Chunk {ci+1}/{n_chunks}"
        c_content = f"---\ntitle: {c_title}\n---\n\n{c_text}"
        chunk_file = os.path.join(chunks_folder, f"chunk_{ci+1:03d}.md")
        with open(chunk_file, "w", encoding="utf-8") as f:
            f.write(c_content)
            
    # 3. meta.json
    now_iso = datetime.now(tz).isoformat()
    meta = {
        "chapter_id": ch_id,
        "title": title,
        "imported_at": now_iso,
        "n_paragraphs": len(paras),
        "n_chunks": n_chunks,
        "chunk_size": chunk_sz
    }
    with open(os.path.join(ch_folder, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
        
    print(f"  -> Saved {ch_id}: {len(paras)} paragraphs, {n_chunks} chunks.")

# 4. Update config.json
config_path = os.path.join(novel_dir, "config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

all_chs = [d for d in os.listdir(chapters_dir) if os.path.isdir(os.path.join(chapters_dir, d)) and d.startswith("ch_")]
config["chapters_count"] = len(all_chs)
with open(config_path, "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print(f"Updated config.json chapters_count to {len(all_chs)}.")
