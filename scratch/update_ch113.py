import sys

path = r'd:\Nhung\trans-tool\novel_projects\công-vai-chính-công\chapters\ch_113\translation.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('“Hệ thống phòng thủ của bọn chúng khá kiên cố, tôi không thể xâm nhập và đột phá từ xa được.”',
     '“Hệ thống phòng thủ của bọn chúng khá kiên cố, em không thể xâm nhập và đột phá từ xa được.”'),
    ('Quý Thần Hi khẽ lắc đầu: “Tôi muốn đánh nhanh thắng nhanh. Phần khó nhằn nhất có lẽ là định vị và vô hiệu hóa tường lửa phòng thủ. Tôi đã thử khống chế toàn bộ các thể sống cơ khí bên trong căn cứ đó—tín hiệu có phản hồi, nhưng quả thực không tài nào xuyên thủng được lớp bảo vệ cốt lõi.”',
     'Quý Thần Hi khẽ lắc đầu: “Em muốn đánh nhanh thắng nhanh. Phần khó nhằn nhất có lẽ là định vị và vô hiệu hóa tường lửa phòng thủ. Em đã thử khống chế toàn bộ các thể sống cơ khí bên trong căn cứ đó—tín hiệu có phản hồi, nhưng quả thực không tài nào xuyên thủng được lớp bảo vệ cốt lõi.”'),
    ('“Vậy anh nghĩ tôi là người đang nóng lòng muốn quay về sao?”',
     '“Vậy anh nghĩ em là người đang nóng lòng muốn quay về sao?”'),
    ('“Đương nhiên là không. Tôi đang rất vội quay về đấy chứ, tốt nhất là giải quyết xong xuôi mọi việc trong vòng ba đến năm ngày.”',
     '“Đương nhiên là không. Em đang rất vội quay về đấy chứ, tốt nhất là giải quyết xong xuôi mọi việc trong vòng ba đến năm ngày.”'),
    ('“Gấp gáp như vậy, cậu vội vã quay về làm gì?”',
     '“Gấp gáp như vậy, em vội vã quay về làm gì?”'),
    ('“Về để cho mèo cưng của tôi ăn chứ sao.”',
     '“Về để cho mèo cưng của em ăn chứ sao.”'),
    ('Trì Chước thoáng lộ vẻ ngạc nhiên: “Cậu chắc chứ? Tôi cứ nghĩ cậu sẽ thích một nơi nào đó mới mẻ hoặc kỳ vĩ hơn.”',
     'Trì Chước thoáng lộ vẻ ngạc nhiên: “Em chắc chứ? Anh cứ nghĩ em sẽ thích một nơi nào đó mới mẻ hoặc kỳ vĩ hơn.”'),
    ('Trì Chước nói: “Cậu cứ chọn nơi nào mình thích là được.”',
     'Trì Chước nói: “Em cứ chọn nơi nào mình thích là được.”'),
    ('Vừa làm, anh vừa thong thả đáp: “Tôi thích mà. Đã là chuyến đi của hai chúng ta thì nên đến một nơi mà cả hai đều thấy thoải mái. Không cần phải quá ồn ào hay kịch tính, chỉ cần cùng nhau tản bộ và phơi nắng cũng đủ để thư giãn rồi.”',
     'Vừa làm, anh vừa thong thả đáp: “Em thích mà. Đã là chuyến đi của hai chúng ta thì nên đến một nơi mà cả hai đều thấy thoải mái. Không cần phải quá ồn ào hay kịch tính, chỉ cần cùng nhau tản bộ và phơi nắng cũng đủ để thư giãn rồi.”'),
    ('“Nếu anh Trì Chước có ý tưởng nào khác, anh cứ việc nói cho tôi biết.”',
     '“Nếu anh Trì Chước có ý tưởng nào khác, anh cứ việc nói cho em biết.”'),
    ('“Vậy là cậu đang nhân nhượng tôi đấy à?”',
     '“Vậy là em đang nhân nhượng anh đấy à?”'),
    ('“Cậu đến đây là để tìm kiếm thứ gì đó.”',
     '“Em đến đây là để tìm kiếm thứ gì đó.”'),
    ('Quý Thần Hi khẽ gật đầu: “Quả thực chẳng giấu nổi anh điều gì. Tôi đến đây đúng là để tìm một thứ.”',
     'Quý Thần Hi khẽ gật đầu: “Quả thực chẳng giấu nổi anh điều gì. Em đến đây đúng là để tìm một thứ.”'),
    ('“Thực ra, tập tài liệu này cũng có liên quan mật thiết đến anh. Tôi chỉ muốn đích thân kiểm chứng xem đó có phải là sự thật hay không.”',
     '“Thực ra, tập tài liệu này cũng có liên quan mật thiết đến anh. Em chỉ muốn đích thân kiểm chứng xem đó có phải là sự thật hay không.”'),
    ('Tôi chỉ muốn biết... rốt cuộc chuyện gì đã xảy ra với vật thí nghiệm trốn thoát năm đó?',
     'Em chỉ muốn biết... rốt cuộc chuyện gì đã xảy ra với vật thí nghiệm trốn thoát năm đó?'),
    ('“Hóa ra cậu lại tò mò đến vậy.”',
     '“Hóa ra em lại tò mò đến vậy.”'),
    ('“Cũng không hẳn. Tôi vốn chẳng có quá nhiều hiếu kỳ về chuyện thiên hạ. Tôi chỉ nghĩ anh rất có thể chính là đứa trẻ năm xưa nên mới để tâm hơn một chút thôi. Nhưng thành thật mà nói, dẫu cho thân phận thực sự của anh có là gì đi chăng nữa... anh vẫn là Alpha của tôi.”',
     '“Cũng không hẳn. Em vốn chẳng có quá nhiều hiếu kỳ về chuyện thiên hạ. Em chỉ nghĩ anh rất có thể chính là đứa trẻ năm xưa nên mới để tâm hơn một chút thôi. Nhưng thành thật mà nói, dẫu cho thân phận thực sự của anh có là gì đi chăng nữa... anh vẫn là Alpha của em.”'),
    ('“Được rồi, giờ thì tôi hiểu rồi. Anh đơn giản chỉ là muốn hôn tôi mà thôi.”',
     '“Được rồi, giờ thì em hiểu rồi. Anh đơn giản chỉ là muốn hôn em mà thôi.”'),
    ('“Cậu muốn chơi trò này thật à?” Trì Chước thoáng lộ vẻ kinh ngạc.',
     '“Em muốn chơi trò này thật à?” Trì Chước thoáng lộ vẻ kinh ngạc.'),
    ('“Sao thế? Anh Trì Chước chê trò này trẻ con ư? Trông vui lắm mà. Nào, vào chơi với tôi đi~”',
     '“Sao thế? Anh Trì Chước chê trò này trẻ con ư? Trông vui lắm mà. Nào, vào chơi với em đi~”'),
]

for old, new in replacements:
    if old not in text:
        print(f"FAILED TO FIND: {old}")
    else:
        text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated ch_113 successfully!")
