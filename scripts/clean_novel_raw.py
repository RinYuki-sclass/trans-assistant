import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'xuyên-thư-xong-tôi-giả-gay-trong-truyện-bá-tổng')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')

clean_pattern = re.compile(r'^\s*目录[\s\xa0]*上一页[\s\xa0]*下一页[\s\xa0]*尾页\s*$', re.MULTILINE)

total_cleaned = 0

for root, dirs, files in os.walk(PROJECT_DIR):
    for f in files:
        if f.endswith('.md') or f.endswith('.txt'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            cleaned, n = clean_pattern.subn('', content)
            # Normalize excessive newlines
            cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
            
            if n > 0:
                total_cleaned += n
                with open(fpath, 'w', encoding='utf-8') as file:
                    file.write(cleaned.strip() + '\n')

                # Update meta.json n_paragraphs if inside chapters/
                meta_json_path = os.path.join(root, 'meta.json')
                if os.path.exists(meta_json_path):
                    with open(meta_json_path, 'r', encoding='utf-8') as mf:
                        meta = json.load(mf)
                    # count paragraphs
                    paras = [p for p in cleaned.split('\n\n') if p.strip() and not p.strip().startswith('# ')]
                    meta['n_paragraphs'] = len(paras)
                    with open(meta_json_path, 'w', encoding='utf-8') as mf:
                        json.dump(meta, mf, ensure_ascii=False, indent=2)

print(f"Cleaned {total_cleaned} instances of navigation boilerplate across all files!")
