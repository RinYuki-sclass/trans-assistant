import sys

path = r'd:\Nhung\trans-tool\novel_projects\công-vai-chính-công\chapters\ch_112\translation.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('Làm sao tôi biết được lời anh vừa nói không phải là một lời dối trá khác chứ?',
     'Làm sao em biết được lời anh vừa nói không phải là một lời dối trá khác chứ?'),
    ('thì ít nhất Điện hạ cũng nên ổn định Linh Cảnh của mình trước đã rồi hẵng từ từ kiểm chứng, cậu thấy có đúng không?',
     'thì ít nhất Điện hạ cũng nên ổn định Linh Cảnh của mình trước đã rồi hẵng từ từ kiểm chứng, em thấy có đúng không?'),
    ('“Điện hạ, đây là Linh Cảnh của cậu. Chỉ cần cậu muốn, cậu có thể khôi phục mọi thứ trở lại bình thường ngay tức khắc.”',
     '“Điện hạ, đây là Linh Cảnh của em. Chỉ cần em muốn, em có thể khôi phục mọi thứ trở lại bình thường ngay tức khắc.”'),
    ('“Chào mừng đến với Linh Cảnh của tôi. Anh có muốn đi trượt tuyết không?”',
     '“Chào mừng đến với Linh Cảnh của em. Anh có muốn đi trượt tuyết không?”'),
    ('“So với trượt tuyết, tôi thà…”',
     '“So với trượt tuyết, anh thà…”'),
    ('“Đây vốn chẳng phải là môi trường sống tự nhiên của loài đom đóm. Tôi rất hiếm khi trông thấy chúng xuất hiện trong hoàng cung. Lần cuối cùng tôi nhìn thấy đom đóm là khi mẫu thân đưa tôi đến công viên rừng rậm ở một tinh cầu lân cận.”',
     '“Đây vốn chẳng phải là môi trường sống tự nhiên của loài đom đóm. Em rất hiếm khi trông thấy chúng xuất hiện trong hoàng cung. Lần cuối cùng em nhìn thấy đom đóm là khi mẫu thân đưa em đến công viên rừng rậm ở một tinh cầu lân cận.”'),
    ('“Nếu cậu muốn ngắm chúng, từ nay về sau năm nào tôi cũng có thể đi cùng cậu.”',
     '“Nếu em muốn ngắm chúng, từ nay về sau năm nào anh cũng có thể đi cùng em.”'),
    ('“Giờ đây tôi đã là Hoàng đế của Đế quốc rồi đấy nhé.”',
     '“Giờ đây em đã là Hoàng đế của Đế quốc rồi đấy nhé.”'),
    ('“Thế lỡ như tôi quên mất thì sao?”',
     '“Thế lỡ như anh quên mất thì sao?”'),
    ('“Tôi đùa thôi. Nếu anh lỡ quên, tôi sẽ nhắc nhở anh. Dù sao đi nữa, lời hứa hẹn này là chuyện của cả hai chúng ta.”',
     '“Em đùa thôi. Nếu anh lỡ quên, em sẽ nhắc nhở anh. Dù sao đi nữa, lời hứa hẹn này là chuyện của cả hai chúng ta.”'),
]

for old, new in replacements:
    if old not in text:
        print(f"FAILED TO FIND: {old}")
    else:
        text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated ch_112 successfully!")
