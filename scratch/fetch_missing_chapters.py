import os
import sys
import json
import time
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"d:\Nhung\trans-tool")
from scripts.audio.crawler import crawl_chapter

novel_dir = r"d:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho"
chapters_dir = os.path.join(novel_dir, "chapters")
cache_path = r"d:\Nhung\trans-tool\data\cache_series\c3999bfac83cc84ffb1af9072a13250c.json"

series_data = json.load(open(cache_path, encoding='utf-8'))
cached_chapters = series_data.get('chapters', [])

# Find all missing chapters between 41 and 103
missing_ch_nums = []
for ch_num in range(41, len(cached_chapters) + 1):
    ch_id = f"ch_{ch_num:03d}"
    src_file = os.path.join(chapters_dir, ch_id, "source.md")
    if not os.path.exists(src_file) or os.path.getsize(src_file) == 0:
        missing_ch_nums.append(ch_num)

print(f"Missing {len(missing_ch_nums)} chapters: {missing_ch_nums}")

chunk_sz = 20
tz = timezone(timedelta(hours=7))

success_count = 0
failed = []

for idx_i, ch_num in enumerate(missing_ch_nums):
    idx = ch_num - 1
    ch_info = cached_chapters[idx]
    ch_id = f"ch_{ch_num:03d}"
    raw_title = ch_info.get("title", f"第{ch_num}頁")
    title = f"Chương {ch_num}: {raw_title}"
    url = ch_info.get("url")
    
    print(f"[{idx_i + 1}/{len(missing_ch_nums)}] Crawling {ch_id}: {title}...")
    
    # Retry loop
    saved = False
    for attempt in range(4):
        try:
            data = crawl_chapter(url)
            paras = data.get("paragraphs", [])
            if not paras:
                raise ValueError("No paragraphs parsed")
                
            ch_folder = os.path.join(chapters_dir, ch_id)
            chunks_folder = os.path.join(ch_folder, "chunks")
            os.makedirs(chunks_folder, exist_ok=True)
            
            # source.md
            full_text = "\n\n".join(paras)
            source_content = f"---\ntitle: {title}\n---\n\n" + full_text
            with open(os.path.join(ch_folder, "source.md"), "w", encoding="utf-8") as f:
                f.write(source_content)
                
            # chunks
            n_chunks = (len(paras) + chunk_sz - 1) // chunk_sz if paras else 1
            for ci in range(n_chunks):
                c_paras = paras[ci*chunk_sz : (ci+1)*chunk_sz]
                c_text = "\n\n".join(c_paras)
                c_title = f"{title} — Chunk {ci+1}/{n_chunks}"
                c_content = f"---\ntitle: {c_title}\n---\n\n{c_text}"
                chunk_file = os.path.join(chunks_folder, f"chunk_{ci+1:03d}.md")
                with open(chunk_file, "w", encoding="utf-8") as f:
                    f.write(c_content)
                    
            # meta.json
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
                
            print(f"  -> OK: {len(paras)} paras, {n_chunks} chunks")
            saved = True
            success_count += 1
            break
        except Exception as e:
            print(f"  Attempt {attempt + 1} failed: {e}")
            time.sleep(3.0 * (attempt + 1))
            
    if not saved:
        failed.append(ch_id)
        
    time.sleep(1.2)

# Update config.json
config_path = os.path.join(novel_dir, "config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

all_chs = [d for d in os.listdir(chapters_dir) if os.path.isdir(os.path.join(chapters_dir, d)) and d.startswith("ch_")]
config["chapters_count"] = len(all_chs)
with open(config_path, "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print("\n=== HOÀN TẤT TẢI BỔ SUNG ===")
print(f"Thành công: {success_count}/{len(missing_ch_nums)} chương.")
if failed:
    print(f"Thất bại: {failed}")
print(f"Tổng số chương trong config.json: {len(all_chs)}")
