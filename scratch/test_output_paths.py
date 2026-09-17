import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant"

def _nw_get_output_dir(input_rel_path: str, default_sub: str = 'trans') -> str:
    if input_rel_path and not input_rel_path.startswith('('):
        norm = os.path.normpath(input_rel_path).replace('\\', '/')
        parts = norm.split('/')
        if len(parts) > 1 and parts[0] == 'input':
            sub_dir = '/'.join(parts[1:-1])
            if sub_dir:
                return os.path.join(BASE_DIR, 'output', *sub_dir.split('/'))
    return os.path.join(BASE_DIR, 'output', default_sub)

# Test 1: input/trans/354-kr.md
t1 = _nw_get_output_dir("input/trans/354-kr.md", default_sub="trans")
expected_1 = os.path.join(BASE_DIR, 'output', 'trans')
assert t1 == expected_1, f"Test 1 failed: {t1} != {expected_1}"
print("✅ Test 1 Passed: input/trans/354-kr.md ->", os.path.relpath(t1, BASE_DIR))

# Test 2: input/qc/338-vi.md
t2 = _nw_get_output_dir("input/qc/338-vi.md", default_sub="qc")
expected_2 = os.path.join(BASE_DIR, 'output', 'qc')
assert t2 == expected_2, f"Test 2 failed: {t2} != {expected_2}"
print("✅ Test 2 Passed: input/qc/338-vi.md ->", os.path.relpath(t2, BASE_DIR))

# Test 3: input/trans/series_a/chap1.md
t3 = _nw_get_output_dir("input/trans/series_a/chap1.md", default_sub="trans")
expected_3 = os.path.join(BASE_DIR, 'output', 'trans', 'series_a')
assert t3 == expected_3, f"Test 3 failed: {t3} != {expected_3}"
print("✅ Test 3 Passed: nested subfolder ->", os.path.relpath(t3, BASE_DIR))

# Test 4: input/solo.md (directly in input)
t4 = _nw_get_output_dir("input/solo.md", default_sub="trans")
assert t4 == expected_1, f"Test 4 failed: {t4} != {expected_1}"
print("✅ Test 4 Passed: root input with default trans ->", os.path.relpath(t4, BASE_DIR))

# Test 5: Fallback when None or placeholder
t5 = _nw_get_output_dir("(Chưa có file trong input/trans/)", default_sub="trans")
assert t5 == expected_1, f"Test 5 failed: {t5} != {expected_1}"
print("✅ Test 5 Passed: placeholder ->", os.path.relpath(t5, BASE_DIR))

# Check files moved
trans_files = os.listdir(os.path.join(BASE_DIR, 'output', 'trans'))
qc_files = os.listdir(os.path.join(BASE_DIR, 'output', 'qc'))
print("\n📁 output/trans files:", trans_files)
print("📁 output/qc files:", qc_files)
assert "result_354-kr.txt" in trans_files
assert "result_qc_336-vi.txt" in qc_files
print("\n🎉 ALL UNIT TESTS & VERIFICATIONS PASSED SUCCESSFULLY!")
