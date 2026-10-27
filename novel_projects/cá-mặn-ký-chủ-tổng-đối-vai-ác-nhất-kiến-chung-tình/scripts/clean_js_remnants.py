import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\cá-mặn-ký-chủ-tổng-đối-vai-ác-nhất-kiến-chung-tình\chapters"

def is_js_or_garbage(p):
    # Dòng chỉ chứa ngoặc nhọn hoặc if/else/try/catch
    if re.search(r'[{}\(\);]|try|catch|else|if|isMainland|isMac|function', p) and len(re.findall(r'[\u4e00-\u9fa5]', p)) < 2:
        return True
    return False

for i in range(21, 31):
    src_path = os.path.join(base_dir, f"c{i}", "source.md")
    meta_path = os.path.join(base_dir, f"c{i}", "meta.json")
    if not os.path.exists(src_path):
        continue
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
    paras = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]
    cleaned = [p for p in paras if not is_js_or_garbage(p)]
    
    clean_text = "\n\n".join(cleaned) + "\n"
    with open(src_path, "w", encoding="utf-8") as f:
        f.write(clean_text)
        
    if os.path.exists(meta_path):
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        meta["paragraphs_count"] = len(cleaned)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
            
    print(f"c{i}: {len(cleaned)} đoạn văn chuẩn")
