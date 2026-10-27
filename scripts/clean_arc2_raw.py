import os

project_dir = r"D:\Nhung\RIDI\trans-assistant\novel_projects\kieu-khi-diem-cong-luon-bi-phan-dien-nham-vao"
chapters_dir = os.path.join(project_dir, "chapters")

# Remove p79 folder as it belongs to Arc 1
p79_dir = os.path.join(chapters_dir, "p79")
if os.path.exists(p79_dir):
    import shutil
    shutil.rmtree(p79_dir)

# Re-write raw_arc2_abo_full.md with pages 80 to 144
full_md = os.path.join(project_dir, "raw_arc2_abo_full.md")
with open(full_md, "w", encoding="utf-8") as out:
    out.write("# 《Kiều Khí Điềm Công Luôn Bị Phản Diện Nhắm Vào [Khoái Xuyên]》- Thế Giới 2: ABO (Raw Toàn Bộ Arc 2)\n\n")
    out.write("- **Tên gốc:** 《娇气甜攻总被反派盯上[快穿]》\n")
    out.write("- **Tác giả:** Điềm Đáo Manh Nha (甜到萌芽)\n")
    out.write("- **Thế giới 2:** Tinh tế ABO (Trang 80 - Trang 144 / Tương ứng ABO 1 - ABO 24)\n")
    out.write("- **Nhân vật:** Đồng Tuế (Alpha kiều khí) x Dạ Lâm Uyên (Alpha đỉnh cấp phân hóa lần hai thành Omega)\n\n---\n\n")

    for p in range(80, 145):
        p_file = os.path.join(chapters_dir, f"p{p}", "source.md")
        if os.path.exists(p_file):
            with open(p_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                out.write(content + "\n\n---\n\n")

print("Updated raw_arc2_abo_full.md successfully.")
