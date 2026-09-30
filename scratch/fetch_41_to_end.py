import os
import sys
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"d:\Nhung\trans-tool")
from scripts.audio.crawler import crawl_chapter

novel_dir = r"d:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho"
chapters_dir = os.path.join(novel_dir, "chapters")
cache_path = r"d:\Nhung\trans-tool\data\cache_series\c3999bfac83cc84ffb1af9072a13250c.json"

series_data = json.load(open(cache_path, encoding='utf-8'))
cached_chapters = series_data.get('chapters', [])

total_cached = len(cached_chapters)
targets = []
for ch_num in range(41, total_cached + 1):
    idx = ch_num - 1
    ch_info = cached_chapters[idx]
    ch_id = f"ch_{ch_num:03d}"
    raw_title = ch_info.get("title", f"第{ch_num}頁")
    title = f"Chương {ch_num}: {raw_title}"
    url = ch_info.get("url")
    targets.append((ch_num, ch_id, title, url))

chunk_sz = 20
tz = timezone(timedelta(hours=7))

print(f"Total chapters to crawl: {len(targets)} (Chương 41 -> {total_cached})")

def process_chapter(item):
    ch_num, ch_id, title, url = item
    ch_folder = os.path.join(chapters_dir, ch_id)
    chunks_folder = os.path.join(ch_folder, "chunks")
    
    # Retry loop up to 3 times
    for attempt in range(3):
        try:
            data = crawl_chapter(url)
            paras = data.get("paragraphs", [])
            if not paras:
                raise ValueError(f"Empty paragraphs for {ch_id}")
            
            os.makedirs(chunks_folder, exist_ok=True)
            full_text = "\n\n".join(paras)
            
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
                
            return ch_num, True, f"{ch_id}: {len(paras)} paras, {n_chunks} chunks"
        except Exception as e:
            if attempt == 2:
                return ch_num, False, f"{ch_id} failed: {e}"
            time.sleep(1.0)

results = []
success_count = 0
failed = []

with ThreadPoolExecutor(max_workers=5) as executor:
    future_to_ch = {executor.submit(process_chapter, item): item for item in targets}
    for future in as_completed(future_to_ch):
        ch_num, ok, msg = future.result()
        if ok:
            success_count += 1
            print(f"[{success_count}/{len(targets)}] {msg}")
        else:
            failed.append(msg)
            print(f"[ERROR] {msg}")

# Update config.json
config_path = os.path.join(novel_dir, "config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

all_chs = [d for d in os.listdir(chapters_dir) if os.path.isdir(os.path.join(chapters_dir, d)) and d.startswith("ch_")]
config["chapters_count"] = len(all_chs)
with open(config_path, "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print("\n--- HOÀN TẤT ---")
print(f"Đã crawl thành công: {success_count}/{len(targets)} chương.")
if failed:
    print(f"Thất bại ({len(failed)}): {failed}")
print(f"Tổng số chương hiện tại trong config.json: {len(all_chs)}.")
