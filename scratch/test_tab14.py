import os, re

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant"

def _nw_get_input_files():
    files = []
    for root in [os.path.join(BASE_DIR, 'input'), os.path.join(BASE_DIR, 'input', 'qc')]:
        if os.path.exists(root):
            for f in sorted(os.listdir(root)):
                if f.endswith(('.txt', '.md')) and not f.startswith('.'):
                    rel = os.path.relpath(os.path.join(root, f), BASE_DIR).replace('\\', '/')
                    files.append(rel)
    return files

def _nw_clean_vi(result_text):
    if not result_text:
        return ""
    lines = result_text.splitlines()
    clean = []
    for l in lines:
        s = l.strip()
        if s.startswith('KR:') or s.startswith('EN:'):
            continue
        clean.append(l)
    res = '\n'.join(clean)
    res = re.sub(r'\n{3,}', '\n\n', res).strip()
    return res

print("Input files:", _nw_get_input_files()[:4])

sample = """KR: 'S급 헌터인가.'
'Thợ săn cấp S sao.'

KR: 이곳에는 S급 이상 헌터가 셋 이상 상주한다고 했었다.
Nghe nói ở đây có từ ba Thợ săn cấp S trở lên thường trực."""

cleaned = _nw_clean_vi(sample)
assert "Thợ săn cấp S sao." in cleaned
assert "KR:" not in cleaned
print(f"Cleaned lines: {len(cleaned.splitlines())}")
print("ALL TESTS PASSED!")
