"""
Utility script for Novel Pipeline Orchestrator to inspect chapter progress and state.
Usage: python scripts/inspect_chapter_state.py --slug <project_slug> --chapter <ch_xxx>
"""
import os
import sys
import json
import argparse

def inspect_chapter(base_dir: str, slug: str, chapter_id: str):
    proj_dir = os.path.join(base_dir, 'novel_projects', slug)
    if not os.path.exists(proj_dir):
        return {"error": f"Project '{slug}' not found."}
    
    ch_dir = os.path.join(proj_dir, 'chapters', chapter_id)
    if not os.path.exists(ch_dir):
        return {"error": f"Chapter '{chapter_id}' not found in project '{slug}'."}

    source_path = os.path.join(ch_dir, 'source.md')
    trans_path = os.path.join(ch_dir, 'translation.md')
    meta_path = os.path.join(ch_dir, 'meta.json')
    summary_path = os.path.join(ch_dir, 'summary.json')
    chunks_dir = os.path.join(ch_dir, 'chunks')
    qa_path = os.path.join(ch_dir, 'qa_clarifications.md')
    qc_path = os.path.join(ch_dir, 'qc_report.md')

    has_source = os.path.exists(source_path) and os.path.getsize(source_path) > 0
    has_qa = os.path.exists(qa_path) and os.path.getsize(qa_path) > 0
    has_trans = os.path.exists(trans_path) and os.path.getsize(trans_path) > 0
    has_qc = os.path.exists(qc_path) and os.path.getsize(qc_path) > 0
    has_meta = os.path.exists(meta_path)
    has_summary = os.path.exists(summary_path)

    # Determine state
    if not has_source:
        state = "EMPTY_NEEDS_SOURCE"
        next_action = "Nạp raw vào source.md"
        recommended_skill = None
    elif not has_qa:
        state = "NEEDS_PRESCAN"
        next_action = "Chạy quét tiền trạm để lập bảng QA xưng hô & glossary"
        recommended_skill = "novel-prescan-extractor"
    elif not has_trans:
        state = "NEEDS_TRANSLATION"
        next_action = "Dịch nội dung 1:1 theo QA đã duyệt"
        recommended_skill = "novel-chunk-translator"
    elif not has_qc:
        state = "NEEDS_QC"
        next_action = "Chạy kiểm định chất lượng bản dịch (QC audit)"
        recommended_skill = "novel-qc-auditor"
    elif not has_summary or not has_meta:
        state = "NEEDS_POST_PROCESS"
        next_action = "Cập nhật memory dài hạn và định dạng xuất bản"
        recommended_skill = "novel-lorekeeper / novel-publisher-formatter"
    else:
        state = "COMPLETED"
        next_action = "Chương đã hoàn tất sẵn sàng xuất bản"
        recommended_skill = "novel-publisher-formatter"

    return {
        "slug": slug,
        "chapter_id": chapter_id,
        "state": state,
        "files": {
            "source": has_source,
            "qa": has_qa,
            "translation": has_trans,
            "qc_report": has_qc,
            "meta": has_meta,
            "summary": has_summary
        },
        "next_action": next_action,
        "recommended_skill": recommended_skill
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--slug', required=True)
    parser.add_argument('--chapter', required=True)
    args = parser.parse_args()

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    res = inspect_chapter(base_dir, args.slug, args.chapter)
    print(json.dumps(res, ensure_ascii=False, indent=2))
