"""
sync_novel_toc.py - Offline, Zero-API Utility to generate and synchronize chapters_index.json & TOC.md
Usage:
    python scripts/sync_novel_toc.py --slug <project_slug>
    python scripts/sync_novel_toc.py --all
"""

import os
import re
import sys
import json
import argparse
from datetime import datetime
from typing import Dict, List, Any, Optional

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOVEL_PROJECTS_DIR = os.path.join(BASE_DIR, "novel_projects")

STATUS_MAP = {
    "pending": ("⚪", "Chưa có raw"),
    "raw_ready": ("⚪", "Đã cào raw"),
    "prescanned": ("🟡", "Đã duyệt QA"),
    "translating": ("🟠", "Đang dịch"),
    "translated": ("🔵", "Đã dịch"),
    "qc_approved": ("🟢", "Đã duyệt QC"),
    "published": ("🟣", "Đã xuất bản")
}

def contains_hanzi(text: str) -> bool:
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def natural_sort_key(s: str):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def sync_project(slug: str, skip_dropped: bool = True) -> bool:
    proj_dir = os.path.join(NOVEL_PROJECTS_DIR, slug)
    if not os.path.isdir(proj_dir):
        print(f"[!] Project '{slug}' not found.")
        return False

    config_path = os.path.join(proj_dir, "config.json")
    proj_title = slug
    proj_author = "Chưa rõ"
    is_dropped = False
    drop_reason = ""
    config_arcs = []

    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                proj_title = cfg.get("title", proj_title)
                proj_author = cfg.get("author", proj_author)
                is_dropped = cfg.get("is_dropped") is True or cfg.get("status") == "dropped"
                drop_reason = cfg.get("drop_reason", "")
                config_arcs = cfg.get("arcs", [])
        except Exception as e:
            pass

    if is_dropped and skip_dropped:
        print(f"[SKIP DROPPED] '{slug}' (Reason: {drop_reason or 'Marked dropped'})")
        return False

    chapters_dir = os.path.join(proj_dir, "chapters")
    chapter_folders = []
    if os.path.exists(chapters_dir):
        chapter_folders = [f for f in os.listdir(chapters_dir) if os.path.isdir(os.path.join(chapters_dir, f))]
        chapter_folders.sort(key=natural_sort_key)

    index_json_path = os.path.join(proj_dir, "chapters_index.json")
    toc_md_path = os.path.join(proj_dir, "TOC.md")

    existing_index: Dict[str, Any] = {}
    if os.path.exists(index_json_path):
        try:
            with open(index_json_path, "r", encoding="utf-8") as f:
                existing_index = json.load(f)
        except Exception:
            existing_index = {}

    existing_chapters_map = {ch.get("id"): ch for ch in existing_index.get("chapters", []) if isinstance(ch, dict)}

    stats = {k: 0 for k in STATUS_MAP.keys()}
    chapters_data: List[Dict[str, Any]] = []

    if not chapter_folders:
        # No chapters crawled yet
        stats["pending"] = 0
        index_payload = {
            "project_slug": slug,
            "title": proj_title,
            "author": proj_author,
            "total_chapters": 0,
            "stats": stats,
            "arcs": [],
            "chapters": [],
            "generated_at": datetime.now().isoformat(),
            "note": "Chưa có dữ liệu chương trong thư mục chapters/"
        }
        with open(index_json_path, "w", encoding="utf-8") as f:
            json.dump(index_payload, f, ensure_ascii=False, indent=2)

        toc_lines = [
            f"# 📖 MỤC LỤC: {proj_title}",
            f"> **Tác giả:** {proj_author} | **Tiến độ:** 0/0 chương (0.0%) | **Cập nhật:** {datetime.now().strftime('%d/%m/%Y')}",
            f"> **Trạng thái:** ⚪ Chưa cào raw vào hệ thống",
            "",
            "---",
            "",
            "*Dự án hiện chưa có dữ liệu chương trong thư mục `chapters/`. Hãy nạp raw vào để bắt đầu quy trình.*",
            ""
        ]
        with open(toc_md_path, "w", encoding="utf-8") as f:
            f.write("\n".join(toc_lines))

        print(f"[OK] {slug}: Synchronized (0 chapters - pending raw)")
        return True

    for order_idx, folder_name in enumerate(chapter_folders, start=1):
        ch_path = os.path.join(chapters_dir, folder_name)
        source_path = os.path.join(ch_path, "source.md")
        trans_path = os.path.join(ch_path, "translation.md")
        meta_path = os.path.join(ch_path, "meta.json")
        qa_path = os.path.join(ch_path, "qa_clarifications.md")
        qc_path = os.path.join(ch_path, "qc_report.md")

        meta: Dict[str, Any] = {}
        if os.path.exists(meta_path):
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)
            except Exception:
                meta = {}

        has_source = os.path.exists(source_path) and os.path.getsize(source_path) > 0
        has_trans = os.path.exists(trans_path) and os.path.getsize(trans_path) > 0
        has_qa = os.path.exists(qa_path) and os.path.getsize(qa_path) > 0
        has_qc = os.path.exists(qc_path) and os.path.getsize(qc_path) > 0

        # Chapter number parsing
        num_match = re.search(r'\d+', folder_name)
        ch_num = int(num_match.group()) if num_match else order_idx
        if "chapter" in meta and isinstance(meta["chapter"], int):
            ch_num = meta["chapter"]

        # Paragraph count and word count
        p_count = meta.get("paragraph_count") or meta.get("translated_paragraphs") or meta.get("source_paragraphs") or meta.get("n_paragraphs") or 0
        word_count = meta.get("word_count", 0)

        # Title Detection
        detected_title_vi = meta.get("title_vi", "")
        detected_title_zh = meta.get("original_header", "")

        meta_title = meta.get("title", "")
        if meta_title:
            if contains_hanzi(meta_title):
                if not detected_title_zh:
                    detected_title_zh = meta_title
            else:
                if not detected_title_vi:
                    detected_title_vi = meta_title

        # Read translation header if present
        if has_trans:
            try:
                with open(trans_path, "r", encoding="utf-8") as f:
                    lines = [line.strip() for line in f if line.strip()]
                    if p_count == 0:
                        p_count = len(lines)
                    text = " ".join(lines)
                    word_count = len(text.split())
                    if not detected_title_vi and lines and lines[0].startswith("#"):
                        detected_title_vi = lines[0].lstrip("#").strip()
            except Exception:
                pass
        elif has_source and p_count == 0:
            try:
                with open(source_path, "r", encoding="utf-8") as f:
                    lines = [line.strip() for line in f if line.strip()]
                    p_count = len(lines)
                    if not detected_title_zh and lines and ("第" in lines[0] or "章" in lines[0]):
                        detected_title_zh = lines[0].strip()
            except Exception:
                pass

        if not detected_title_zh:
            detected_title_zh = f"第{ch_num}章"

        if not detected_title_vi:
            detected_title_vi = f"Chương {ch_num}"

        # Status determination
        status = meta.get("status")
        if not status or status not in STATUS_MAP:
            if not has_source:
                status = "pending"
            elif has_qc or (has_trans and meta.get("status") == "translated"):
                status = "qc_approved" if has_qc else "translated"
            elif has_trans:
                status = "translated"
            elif has_qa:
                status = "prescanned"
            else:
                status = "raw_ready"

        stats[status] += 1

        old_entry = existing_chapters_map.get(folder_name, {})
        arc_id = meta.get("arc") or meta.get("arc_id") or old_entry.get("arc_id")
        arc_name = meta.get("arc_name") or old_entry.get("arc_name", "")

        entry = {
            "id": folder_name,
            "order": order_idx,
            "chapter_no": ch_num,
            "sub_index": meta.get("sub_index", old_entry.get("sub_index")),
            "arc_id": arc_id,
            "arc_name": arc_name,
            "title_zh": detected_title_zh,
            "title_vi": detected_title_vi,
            "status": status,
            "paragraph_count": p_count,
            "word_count": word_count,
            "source_url": meta.get("source_url", old_entry.get("source_url", "")),
            "updated_at": meta.get("updated_at", old_entry.get("updated_at", datetime.now().isoformat()))
        }
        chapters_data.append(entry)

    # Arc propagation for consistency
    first_known_arc = next((c for c in chapters_data if c["arc_id"] is not None), None)
    curr_arc_id = first_known_arc["arc_id"] if first_known_arc else 1
    curr_arc_name = first_known_arc["arc_name"] if first_known_arc and first_known_arc["arc_name"] else "Chính Văn"

    for c in chapters_data:
        if c["arc_id"] is not None:
            curr_arc_id = c["arc_id"]
            if c["arc_name"]:
                curr_arc_name = c["arc_name"]
            else:
                c["arc_name"] = curr_arc_name
        else:
            c["arc_id"] = curr_arc_id
            c["arc_name"] = curr_arc_name

    # Arcs extraction
    arcs_map = {}
    for ch in chapters_data:
        aid = ch.get("arc_id", 1)
        aname = ch.get("arc_name") or f"Arc {aid}"
        if aid not in arcs_map:
            arcs_map[aid] = {
                "arc_id": aid,
                "arc_name": aname,
                "folders": []
            }
        arcs_map[aid]["folders"].append(ch["id"])

    arcs_list = []
    for aid in sorted(arcs_map.keys(), key=lambda x: (str(x).isdigit(), int(x) if str(x).isdigit() else str(x))):
        folders = arcs_map[aid]["folders"]
        arcs_list.append({
            "arc_id": aid,
            "arc_name": arcs_map[aid]["arc_name"],
            "folder_range": [folders[0], folders[-1]] if folders else []
        })

    index_payload = {
        "project_slug": slug,
        "title": proj_title,
        "author": proj_author,
        "total_chapters": len(chapters_data),
        "stats": stats,
        "arcs": arcs_list,
        "chapters": chapters_data,
        "generated_at": datetime.now().isoformat()
    }

    with open(index_json_path, "w", encoding="utf-8") as f:
        json.dump(index_payload, f, ensure_ascii=False, indent=2)

    # Render TOC.md
    total_done = stats.get("qc_approved", 0) + stats.get("translated", 0) + stats.get("published", 0)
    pct = (total_done / len(chapters_data) * 100) if chapters_data else 0

    lines_md = [
        f"# 📖 MỤC LỤC: {proj_title}",
        f"> **Tác giả:** {proj_author} | **Tiến độ:** {total_done}/{len(chapters_data)} chương ({pct:.1f}%) | **Cập nhật:** {datetime.now().strftime('%d/%m/%Y')}",
        f"> **Trạng thái:** 🟢 Đã duyệt QC ({stats.get('qc_approved', 0)}) | 🔵 Đã dịch ({stats.get('translated', 0)}) | ⚪ Chưa dịch ({stats.get('raw_ready', 0) + stats.get('pending', 0)})",
        "",
        "---",
        ""
    ]

    for arc in arcs_list:
        aid = arc["arc_id"]
        aname = arc["arc_name"]
        header_title = aname.upper() if aname else f"ARC {aid}"
        lines_md.append(f"## 🌌 {header_title}")
        lines_md.append("")
        lines_md.append("| STT | Mã thư mục | Tiêu đề chương (Tiếng Việt) | Nguyên tác | Số đoạn | Trạng thái |")
        lines_md.append("| :---: | :---: | :--- | :--- | :---: | :---: |")

        arc_chs = [c for c in chapters_data if c.get("arc_id") == aid]
        for c in arc_chs:
            st = c.get("status", "raw_ready")
            icon, label = STATUS_MAP.get(st, ("⚪", st))
            cid = c['id']
            if st in ["translated", "qc_approved", "published"]:
                target_link = f"chapters/{cid}/translation.md"
            else:
                target_link = f"chapters/{cid}/source.md"

            title_vi_clean = c['title_vi'].replace("|", "-")
            title_vi_display = f"[{title_vi_clean}]({target_link})"
            lines_md.append(f"| {c['order']} | `{cid}` | {title_vi_display} | {c['title_zh']} | {c['paragraph_count']} | {icon} {label} |")

        lines_md.append("")

    with open(toc_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines_md))

    print(f"[OK] {slug}: Synchronized {len(chapters_data)} chapters (Done: {total_done})")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", help="Project slug to sync")
    parser.add_argument("--all", action="store_true", help="Sync all novel projects")
    parser.add_argument("--include-dropped", action="store_true", help="Include dropped projects")
    args = parser.parse_args()

    skip_dropped = not args.include_dropped

    if args.all:
        count = 0
        skipped = 0
        for item in sorted(os.listdir(NOVEL_PROJECTS_DIR)):
            p = os.path.join(NOVEL_PROJECTS_DIR, item)
            if os.path.isdir(p):
                res = sync_project(item, skip_dropped=skip_dropped)
                if res:
                    count += 1
                else:
                    skipped += 1
        print(f"\n==========================================")
        print(f"Batch synchronization complete!")
        print(f"Total synchronized projects: {count}")
        print(f"Total skipped (dropped): {skipped}")
        print(f"==========================================")
    elif args.slug:
        sync_project(args.slug, skip_dropped=skip_dropped)
    else:
        print("Please provide --slug <project_slug> or --all")

if __name__ == "__main__":
    main()
