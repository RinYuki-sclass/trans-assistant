import sys

path = r'd:\Nhung\trans-tool\novel_projects\công-vai-chính-công\chapters\ch_111\translation.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('“Tôi không biết cậu có chấp niệm gì sâu nặng về mẹ mình,” Trì Chước lạnh lùng nói. “Nhưng theo những gì tôi thấy,',
     '“Anh không biết em có chấp niệm gì sâu nặng về mẹ mình,” Trì Chước lạnh lùng nói. “Nhưng theo những gì anh thấy,'),
    ('“Có lẽ cha tôi đã làm tổn thương mẹ quá sâu đậm. Mỗi lần nhìn thấy tôi, mẹ lại nhớ đến ông ấy. Có lẽ tất cả những điều đó chỉ do tôi tự mình suy diễn mà thôi.”',
     '“Có lẽ cha em đã làm tổn thương mẹ quá sâu đậm. Mỗi lần nhìn thấy em, mẹ lại nhớ đến ông ấy. Có lẽ tất cả những điều đó chỉ do em tự mình suy diễn mà thôi.”'),
    ('“Cậu khao khát sự chú ý của bà ta, điều đó tôi hiểu. Nhưng một người mẹ thực sự yêu con mình sẽ không bao giờ trút hận thù của người khác lên đầu đứa trẻ. Bà ta giữ cậu bên cạnh, nhưng chưa từng trao cho cậu thứ mà cậu thực sự khao khát.”',
     '“Em khao khát sự chú ý của bà ta, điều đó anh hiểu. Nhưng một người mẹ thực sự yêu con mình sẽ không bao giờ trút hận thù của người khác lên đầu đứa trẻ. Bà ta giữ em bên cạnh, nhưng chưa từng trao cho em thứ mà em thực sự khao khát.”'),
    ('“Nhưng mẹ tôi chỉ là một Omega bị lừa gạt,” anh khẽ giọng. “Làm sao tôi có thể nhẫn tâm trách cứ bà ấy được chứ?”',
     '“Nhưng mẹ em chỉ là một Omega bị lừa gạt,” anh khẽ giọng. “Làm sao em có thể nhẫn tâm trách cứ bà ấy được chứ?”'),
    ('“Vậy nên cậu nghĩ tất cả là do lỗi của bản thân? Rằng cậu không đáp ứng được kỳ vọng của bà ta... rằng cậu không xứng đáng được yêu thương?”',
     '“Vậy nên em nghĩ tất cả là do lỗi của bản thân? Rằng em không đáp ứng được kỳ vọng của bà ta... rằng em không xứng đáng được yêu thương?”'),
    ('“Tôi không biết hạng người nào mới xứng đáng được yêu,” Trì Chước bình thản nói. “Kẻ lương thiện? Tôi thấy đôi khi bọn họ quá đỗi giả tạo.',
     '“Anh không biết hạng người nào mới xứng đáng được yêu,” Trì Chước bình thản nói. “Kẻ lương thiện? Anh thấy đôi khi bọn họ quá đỗi giả tạo.'),
    ('“Tôi chỉ biết duy nhất một điều: Tôi thích cậu.”',
     '“Anh chỉ biết duy nhất một điều: Anh thích em.”'),
    ('“Khi cậu nhìn ngắm người khác, tôi lại đang dõi theo cậu. Thứ mà kẻ khác gọi là thủ đoạn tàn nhẫn—tôi lại thấy cậu hệt như một chú mèo con đang xù lông giương móng vuốt sau khi bị bắt nạt. Tôi không thấy nó nhơ nhớp chút nào. Tôi thấy nó vô cùng đáng yêu.”',
     '“Khi em nhìn ngắm người khác, anh lại đang dõi theo em. Thứ mà kẻ khác gọi là thủ đoạn tàn nhẫn—anh lại thấy em hệt như một chú mèo con đang xù lông giương móng vuốt sau khi bị bắt nạt. Anh không thấy nó nhơ nhớp chút nào. Anh thấy nó vô cùng đáng yêu.”'),
    ('“Nhưng tôi không thấy thế. Bởi vì là cậu, nên mọi thứ thuộc về cậu đều khiến tôi thấy… đáng yêu. Nếu điều đó biến tôi thành kẻ biến thái thì cũng chẳng sao. Có lẽ tôi chỉ đơn giản là thích cậu nhiều hơn thôi.”',
     '“Nhưng anh không thấy thế. Bởi vì là em, nên mọi thứ thuộc về em đều khiến anh thấy… đáng yêu. Nếu điều đó biến anh thành kẻ biến thái thì cũng chẳng sao. Có lẽ anh chỉ đơn giản là thích em nhiều hơn thôi.”'),
    ('“Vì tôi thích cậu nhiều hơn… nên tôi chỉ muốn nhìn ngắm một mình cậu.”',
     '“Vì anh thích em nhiều hơn… nên anh chỉ muốn nhìn ngắm một mình em.”'),
]

for old, new in replacements:
    if old not in text:
        print(f"FAILED TO FIND: {old}")
    else:
        text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated ch_111 successfully!")
