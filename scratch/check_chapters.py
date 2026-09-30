import os

base = r"d:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters"
for i in range(16, 26):
    ch = f"ch_{i:03d}"
    p = os.path.join(base, ch)
    if os.path.exists(p):
        print(f"{ch}: {os.listdir(p)}")
    else:
        print(f"{ch}: NOT FOUND")
