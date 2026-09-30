import os, json, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r"d:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters"
for i in range(26, 34):
    ch = f"ch_{i:03d}"
    meta_path = os.path.join(base, ch, "meta.json")
    src_path = os.path.join(base, ch, "source.md")
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(src_path, "r", encoding="utf-8") as f:
        src = f.read()
    # Remove frontmatter
    import re
    body = re.sub(r"^---[\s\S]*?---\s*", "", src, count=1).strip()
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    print(f"{ch}: title='{meta.get('title')}', n_paras_meta={meta.get('n_paragraphs')}, actual_paras={len(paras)}")
