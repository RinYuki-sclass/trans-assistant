import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\cá-mặn-ký-chủ-tổng-đối-vai-ác-nhất-kiến-chung-tình\chapters"

def get_paragraphs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    paras = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]
    return paras

all_matched = True
total_raw = 0
total_trans = 0

print("=" * 60)
print("KIỂM TRA ĐỐI ỨNG ĐOẠN VĂN 1:1 BATCH 3 (CHƯƠNG 21 - 30)")
print("=" * 60)

for c_num in range(21, 31):
    c_dir = os.path.join(base_dir, f"c{c_num}")
    src_file = os.path.join(c_dir, "source.md")
    trans_file = os.path.join(c_dir, "translation.md")
    
    if not os.path.exists(src_file) or not os.path.exists(trans_file):
        print(f"❌ c{c_num}: Thiếu file!")
        all_matched = False
        continue
        
    src_p = get_paragraphs(src_file)
    trans_p = get_paragraphs(trans_file)
    
    total_raw += len(src_p)
    total_trans += len(trans_p)
    
    if len(src_p) == len(trans_p):
        print(f"✅ c{c_num}: KHỚP TUYỆT ĐỐI 1:1 ({len(src_p)}/{len(trans_p)} đoạn)")
    else:
        print(f"❌ c{c_num}: LỆCH SỐ ĐOẠN! Raw: {len(src_p)} != Trans: {len(trans_p)}")
        all_matched = False

print("-" * 60)
print(f"Tổng số đoạn Raw: {total_raw} | Tổng số đoạn Trans: {total_trans}")
if all_matched and total_raw == total_trans:
    print("🎯 KẾT QUẢ: 10/10 CHƯƠNG BATCH 3 ĐẠT CHUẨN 1:1 HOÀN HẢO!")
else:
    print("⚠️ CẦN CHỈNH SỬA LẠI ĐOẠN VĂN LỆCH!")
