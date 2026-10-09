import json
import os

chars_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\memory\characters.json'
with open(chars_path, 'r', encoding='utf-8') as f:
    chars = json.load(f)

for c in chars:
    if c['name'] == 'Sở Tư Thừa':
        c['third_person_pronoun'] = 'anh (ở Arc 1) / cậu (ở Arc 2 & 3)'
        c['notes'] = 'Bình tĩnh, cơ trí, phong thái đại lão phản diện. Ngôi 3 trần thuật: Arc 1 dùng "anh"; Arc 2 & 3 dùng "cậu". Đối thoại Arc 2 & 3: xưng "cậu" (hoặc "tôi/em"), gọi Thụ là "anh".'
    elif c['name'] == 'Tống Lạc An':
        c['third_person_pronoun'] = 'cậu'
        c['notes'] = 'Thân xác nguyên tác thế giới 2. Trần thuật ngôi 3 dùng "cậu". Đối thoại: xưng "cậu" (hoặc "tôi/em"), gọi Thẩm Từ là "anh".'
    elif c['name'] == 'Thẩm Từ':
        c['third_person_pronoun'] = 'anh'
        c['notes'] = 'Tổng tài / Đại lão phản diện thế giới 2 (Thụ TG2). Đại từ ngôi 3 trần thuật từ Arc 2 dùng "anh". Đối thoại: xưng "anh", gọi Sở Tư Thừa là "cậu".'
    elif c['name'] == 'Lệ Yến Trạch':
        c['third_person_pronoun'] = 'hắn'
        c['notes'] = 'Tổng tài tra công nguyên tác TG2. Luôn dùng "hắn" (tuyệt đối KHÔNG dùng "anh" để tránh nhầm với Thẩm Từ).'

names = [c['name'] for c in chars]
if 'Khương Niệm An' not in names:
    chars.append({
        'name': 'Khương Niệm An',
        'hanviet_name': 'Khương Niệm An',
        'original_name': '姜念安',
        'pinyin': "Jiāng Niàn'ān",
        'gender': 'Nam',
        'third_person_pronoun': 'cậu',
        'role': 'Thân xác thế giới 3 của Sở Tư Thừa (Diễn viên tuyến 18)',
        'notes': 'Ngôi 3 trần thuật dùng "cậu". Đối thoại xưng "cậu", gọi Lộ Vũ Minh là "anh".'
    })

if 'Lộ Vũ Minh' not in names:
    chars.append({
        'name': 'Lộ Vũ Minh',
        'hanviet_name': 'Lộ Vũ Minh',
        'original_name': '路宇鸣',
        'pinyin': 'Lù Yǔmíng',
        'gender': 'Nam',
        'third_person_pronoun': 'anh',
        'role': 'Nam chính (Thụ TG3), học sinh lớp 12, con riêng của mẹ kế',
        'notes': 'Ngôi 3 trần thuật dùng "anh". Đối thoại xưng "anh", gọi Sở Tư Thừa là "cậu".'
    })

if 'Khương Lê' not in names:
    chars.append({
        'name': 'Khương Lê',
        'hanviet_name': 'Khương Lê',
        'original_name': '姜黎',
        'pinyin': 'Jiāng Lí',
        'gender': 'Nam',
        'third_person_pronoun': 'anh',
        'role': 'Linh hồn thực tại của Thụ tại Cục Quản Lý Thời Không (Hồi kết)',
        'notes': 'Nhân viên tổ Phản diện Cục Thời Không. Ngôi 3 dùng "anh". Đối thoại xưng "anh", gọi Sở Tư Thừa là "cậu".'
    })

if 'Tần Uyên' not in names:
    chars.append({
        'name': 'Tần Uyên',
        'hanviet_name': 'Tần Uyên',
        'original_name': '秦渊',
        'pinyin': 'Qín Yuān',
        'gender': 'Nam',
        'third_person_pronoun': 'hắn',
        'role': 'Kim chủ / tra công cũ phong sát Khương Niệm An',
        'notes': 'Ngôi 3 dùng "hắn" (tuyệt đối KHÔNG dùng "anh").'
    })

with open(chars_path, 'w', encoding='utf-8') as f:
    json.dump(chars, f, ensure_ascii=False, indent=2)

print('Updated characters.json successfully.')

# Update AGENTS.md
agents_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\AGENTS.md'
with open(agents_path, 'r', encoding='utf-8') as f:
    agents_content = f.read()

# Replace character table section and pronoun section
old_sec2_marker = '### Bảng nhân vật Thế giới 2 (Hào môn thế gia - từ Chương 43 trở đi):'
new_sec2_content = '''### Bối cảnh Thế giới 2 & 3 (Hào môn thế gia & Giới giải trí - từ Chương 40 trở đi):
> [!IMPORTANT]
> **THAY ĐỔI ĐẠI TỪ CỐT LÕI TỪ ARC 2 & ARC 3:**
> - **CÔNG (Sở Tư Thừa / Tống Lạc An / Khương Niệm An):** Ngôi 3 trần thuật dùng **"cậu"**. Đối thoại xưng **"cậu"** (hoặc *"tôi / em"*), gọi Thụ là **"anh"**.
> - **THỤ (Thẩm Từ / Lộ Vũ Minh / Khương Lê):** Ngôi 3 trần thuật dùng **"anh"**. Đối thoại xưng **"anh"**, gọi Công là **"cậu"**.
> - **PHẢN DIỆN / TRA NAM (Lệ Yến Trạch, Tần Uyên):** Dùng **"hắn"** (tuyệt đối KHÔNG dùng "anh" để tránh nhầm lẫn với Thụ).

| Tên tiếng Trung | Tên chuẩn trong bản dịch | Đại từ ngôi 3 | Vai trò / Thân phận | Quy chuẩn đối thoại |
| :--- | :--- | :--- | :--- | :--- |
| **宋乐安** | **Tống Lạc An** | **cậu** | Thân xác của Sở Tư Thừa ở TG2 | Xưng **cậu** (hoặc *tôi / em*), gọi Thẩm Từ là **anh** |
| **沈辞** | **Thẩm Từ** | **anh** | Tổng tài Thẩm thị (Thụ TG2) | Xưng **anh**, gọi Sở Tư Thừa là **cậu** |
| **厉晏泽** | **Lệ Yến Trạch** | **hắn** | Tổng tài tra công nguyên tác | ❌ CẤM dùng "anh" |
| **周洛洛** | **Chu Lạc Lạc** | **gã** | Kẻ trọng sinh mang Bug đọc tâm | ❌ CẤM dùng "anh" |
| **姜念安** | **Khương Niệm An** | **cậu** | Thân xác của Sở Tư Thừa ở TG3 | Xưng **cậu**, gọi Thụ là **anh** |
| **路宇鸣 / 姜黎** | **Lộ Vũ Minh / Khương Lê** | **anh** | Nam chính (Thụ TG3 / Hồi kết) | Xưng **anh**, gọi Sở Tư Thừa là **cậu** |
| **秦渊** | **Tần Uyên** | **hắn** | Tra công kim chủ cũ của Khương Niệm An | ❌ CẤM dùng "anh" |'''

# Replace from old_sec2_marker up to ## 3. THUẬT NGỮ
idx_start = agents_content.find(old_sec2_marker)
idx_end = agents_content.find('## 3. THUẬT NGỮ THẾ GIỚI TRÙNG TỘC (WORLD 1)')

if idx_start != -1 and idx_end != -1:
    agents_content = agents_content[:idx_start] + new_sec2_content + '\n\n---\n\n' + agents_content[idx_end:]

# Replace section 4, 5, 6
old_sec4_marker = '## 4. QUY TẮC ĐẠI TỪ NGÔI KỂ THỨ 3'
new_tail = '''## 4. QUY TẮC ĐẠI TỪ NGÔI KỂ THỨ 3 (VĂN TỰ SỰ / TRẦN THUẬT) & VĂN PHONG
1. **Phân hóa đại từ ngôi 3 theo từng Arc (QUAN TRỌNG NHẤT):**
   - **Arc 1 (Trùng tộc - `ch_001` $\\rightarrow$ `ch_039`):**
     - **Sở Tư Thừa (Công):** DUY NHẤT dùng **"anh"**.
     - **Alex Sachsen (Thụ):** Dùng **"hắn"** (tuyệt đối KHÔNG dùng "anh").
     - **Friedrich, Felo, Elio:** Dùng **"hắn / gã"**.
   - **Arc 2 & Arc 3 (Hào môn thế gia & Giới giải trí - từ `ch_040` $\\rightarrow$ `ch_103`):**
     - **Công (Sở Tư Thừa / Tống Lạc An / Khương Niệm An):** Dùng đại từ **"cậu"**.
     - **Thụ (Thẩm Từ / Lộ Vũ Minh / Khương Lê):** Dùng đại từ **"anh"**.
     - **Phản diện / Tra nam (Lệ Yến Trạch, Tần Uyên, Chu Lạc Lạc):** Dùng **"hắn / gã"** (Tuyệt đối CẤM dùng "anh" để tránh nhầm lẫn chủ thể với Thụ).
2. **Quy tắc nhập xác:** Khi Sở Tư Thừa nhập vào thân xác nào thì toàn bộ ngôi 3 của nhân vật chính đồng bộ theo quy tắc của Arc đó (Arc 1: "anh", Arc 2 & 3: "cậu").
3. **Đoạn thoại và trần thuật:** Tách đoạn rõ ràng, không gộp thoại và văn trần thuật chung một đoạn.
4. **Quy tắc định dạng đoạn văn khi Dịch & QC (BẮT BUỘC):**
   - **Các đoạn phải cách nhau đúng 1 dòng:** Giữa hai đoạn văn trần thuật hoặc lời thoại bất kỳ **bắt buộc phải có đúng 1 dòng trống (`\\n\\n`)**.
   - Tuyệt đối không để các đoạn văn dính liền kề trên hai dòng liên tiếp (`\\n`) mà không có dòng trống ngăn cách.
   - Không để thừa nhiều dòng trống liên tiếp (chỉ giữ đúng 1 dòng trống).

---

## 5. QUY TẮC XƯNG HÔ ĐỐI THOẠI CÔNG - THỤ
### Bối cảnh Thế giới 1 (Trùng tộc - Sở Tư Thừa & Alex):
1. **Thường ngày:** Sở Tư Thừa xưng *"tôi"*, gọi *"anh / Alex / Tướng quân"*; Alex xưng *"tôi"*, gọi *"cậu"*.
2. **Quy phục / Thân mật:** Alex gọi *"Trùng chủ / Chủ nhân / ngài"*, xưng *"tôi / em"*.

### Bối cảnh Thế giới 2 & Thế giới 3 (Hào môn & Giới giải trí - Sở Tư Thừa x Thẩm Từ / Lộ Vũ Minh):
1. **Thụ (Thẩm Từ / Lộ Vũ Minh / Khương Lê):**
   - Xưng **"anh"** (hoặc *"tôi"* trong bối cảnh công việc), gọi Công là **"cậu"**.
2. **Công (Sở Tư Thừa):**
   - Gọi Thụ là **"anh"** / tên riêng / *"Ông chủ"*.
   - Xưng **"cậu"** (khi đối thoại bình đẳng) hoặc **"tôi / em"** (khi làm nũng/thân mật).

---

## 6. CHECKLIST BẮT BUỘC KHI DỊCH VÀ QC MỖI CHƯƠNG
1. **Kiểm tra định dạng đoạn văn:** Tất cả các đoạn văn và lời thoại phải cách nhau đúng 1 dòng trống (`\\n\\n`).
2. **Kiểm tra tên riêng:** Tên phương Tây (Alex, Ryan, Friedrich, Felo, Heideman, Sachsen...) phải giữ nguyên tiếng Anh, không dịch Hán Việt.
3. **Kiểm tra đại từ ngôi 3 tự sự:**
   - **Arc 1:** Công = **"anh"**, Thụ = **"hắn"**.
   - **Arc 2 & 3:** Công = **"cậu"**, Thụ = **"anh"**. Tra nam (Lệ Yến Trạch, Tần Uyên) = **"hắn"** (CẤM dùng "anh").
4. **Kiểm tra xưng hô đối thoại Công - Thụ:**
   - **Arc 1:** Công xưng "tôi" - gọi "anh"; Thụ xưng "tôi" - gọi "cậu".
   - **Arc 2 & 3:** Thụ xưng "anh" - gọi "cậu"; Công gọi "anh" - xưng "cậu" (hoặc "tôi / em").
5. **Kiểm tra danh xưng Trùng tộc (ở Arc 1):** Tuyệt đối không dùng "con thư trùng", "con hùng trùng", "con quân thư".
6. **Kiểm tra bảo toàn đoạn 1:1:** Không bỏ sót câu thoại hay đoạn văn, số đoạn khớp 1:1 với nguyên tác.
'''

idx_sec4 = agents_content.find(old_sec4_marker)
if idx_sec4 != -1:
    agents_content = agents_content[:idx_sec4] + new_tail

with open(agents_path, 'w', encoding='utf-8') as f:
    f.write(agents_content)

print('Updated AGENTS.md successfully.')
