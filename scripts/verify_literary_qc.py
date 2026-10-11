import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'xuyên-thư-xong-tôi-giả-gay-trong-truyện-bá-tổng')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')

def verify_chapter(ch_num):
    ch_id = f"ch_{ch_num:03d}"
    ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
    src_path = os.path.join(ch_dir, 'source.md')
    trans_path = os.path.join(ch_dir, 'translation.md')

    if not os.path.exists(src_path) or not os.path.exists(trans_path):
        return False, f"Missing files for {ch_id}"

    with open(src_path, 'r', encoding='utf-8') as f:
        src_raw = f.read().strip()
    with open(trans_path, 'r', encoding='utf-8') as f:
        trans_raw = f.read().strip()

    # Source paragraphs
    src_paras = [p.strip() for p in re.split(r'\n\s*\n', src_raw) if p.strip()]
    if src_paras and src_paras[0].startswith('#'):
        src_paras = src_paras[1:]

    # Trans paragraphs
    trans_clean = re.sub(r'^---\n.*?\n---\n*', '', trans_raw, flags=re.DOTALL).strip()
    trans_paras = [p.strip() for p in re.split(r'\n\s*\n', trans_clean) if p.strip()]

    # 1. Paragraph count check
    if len(src_paras) != len(trans_paras):
        return False, f"{ch_id}: Paragraph mismatch! src={len(src_paras)}, trans={len(trans_paras)}"

    # 2. Check for double quotes instead of single or code blocks
    issues = []
    for idx, p in enumerate(trans_paras):
        if '```' in p:
            issues.append(f"Para {idx+1} contains code fence")

    return (True, f"{ch_id}: OK ({len(src_paras)} paras)") if not issues else (False, f"{ch_id}: Issues: {'; '.join(issues)}")

if __name__ == '__main__':
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 58
    
    all_ok = True
    for c in range(start, end + 1):
        ok, msg = verify_chapter(c)
        print(f"[{'PASS' if ok else 'FAIL'}] {msg}")
        if not ok:
            all_ok = False
            
    print("\nResult:", "ALL PASSED" if all_ok else "SOME FAILED")
