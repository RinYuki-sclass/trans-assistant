import sys

path = r'd:\Nhung\trans-tool\novel_projects\công-vai-chính-công\chapters\ch_115\translation.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

old = '“Báo tuyết nhỏ… khẩn cấp… yến tiệc của Bạch Hân Khả… tôi bị chuốc thuốc rồi.”'
new = '“Báo tuyết nhỏ… khẩn cấp… yến tiệc của Bạch Hân Khả… anh bị chuốc thuốc rồi.”'

if old in text:
    text = text.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated ch_115 successfully!")
else:
    print("Could not find line in ch_115")
