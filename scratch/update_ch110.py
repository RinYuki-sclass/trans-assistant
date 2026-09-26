import sys

path = r'd:\Nhung\trans-tool\novel_projects\công-vai-chính-công\chapters\ch_110\translation.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('anh chỉ khàn giọng đáp: “Tôi biết.”', 'anh chỉ khàn giọng đáp: “Em biết.”'),
    ('“Điện hạ, đương nhiên là tôi biết đau.”', '“Điện hạ, đương nhiên là anh biết đau.”'),
    ('“Điện hạ, lúc này trông cậu thật sự rất đẹp.”', '“Điện hạ, lúc này trông em thật sự rất đẹp.”'),
    ('“Hoa hồng nhỏ, mở Linh Cảnh của cậu cho tôi.”', '“Hoa hồng nhỏ, mở Linh Cảnh của em cho anh.”'),
    ('“Đừng có nói như thể tôi đáng sợ lắm vậy.”', '“Đừng có nói như thể em đáng sợ lắm vậy.”'),
    ('“Trì Chước, tôi đau quá.”', '“Trì Chước, em đau quá.”'),
    ('“Tôi sẽ nới lỏng thêm một chút.”', '“Anh sẽ nới lỏng thêm một chút.”'),
]

for old, new in replacements:
    if old not in text:
        print(f"FAILED TO FIND: {old}")
    else:
        text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated ch_110 successfully!")
