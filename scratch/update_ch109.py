import sys

path = r'd:\Nhung\trans-tool\novel_projects\công-vai-chính-công\chapters\ch_109\translation.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('“Cậu có vẻ rất hưởng thụ đấy nhỉ,”', '“Em có vẻ rất hưởng thụ đấy nhỉ,”'),
    ('“Tôi đau đầu,” Quý Thần Hi', '“Em đau đầu,” Quý Thần Hi'),
    ('hạ thấp giọng nói: “Chải vuốt thêm hai lần nữa là cậu sẽ ổn thôi.”', 'hạ thấp giọng nói: “Chải vuốt thêm hai lần nữa là em sẽ ổn thôi.”'),
    ('“Anh đột nhiên dịu dàng thế này... tôi thực sự không quen lắm,”', '“Anh đột nhiên dịu dàng thế này... em thực sự không quen lắm,”'),
    ('“Ồ? Hóa ra ngày thường trong mắt cậu, tôi đáng sợ lắm sao?”', '“Ồ? Hóa ra ngày thường trong mắt em, anh đáng sợ lắm sao?”'),
    ('ngày thường anh Trì Chước cũng đâu có tiếc ngọc thương hoa với bông hoa mỏng manh như tôi.”', 'ngày thường anh Trì Chước cũng đâu có tiếc ngọc thương hoa với bông hoa mỏng manh như em.”'),
    ('“Chẳng trách tôi được.', '“Chẳng trách em được.'),
    ('“Cậu không nói thì tôi cũng suýt quên mất cậu là một bông hoa mỏng manh đấy. Hửm? Bông hồng nhỏ.”', '“Em không nói thì anh cũng suýt quên mất em là một bông hoa mỏng manh đấy. Hửm? Bông hồng nhỏ.”'),
    ('“Tôi thực sự không thích cái biệt danh này chút nào. Hồi bé thì còn tạm được, chứ bây giờ? Nó chẳng hợp với một Alpha trưởng thành tẹo nào.”', '“Em thực sự không thích cái biệt danh này chút nào. Hồi bé thì còn tạm được, chứ bây giờ? Nó chẳng hợp với một Alpha trưởng thành tẹo nào.”'),
    ('“Vậy tôi chỉ cho phép anh gọi riêng khi chỉ có hai chúng ta thôi đấy.”', '“Vậy em chỉ cho phép anh gọi riêng khi chỉ có hai chúng ta thôi đấy.”'),
    ('“Tô Dục lúc nào cũng gọi cậu như thế còn gì.”', '“Tô Dục lúc nào cũng gọi em như thế còn gì.”'),
    ('“Cậu ấy gọi tôi như thế từ bé đến lớn rồi, tôi làm sao mà ép cậu ấy dừng lại được.”', '“Cậu ấy gọi em như thế từ bé đến lớn rồi, em làm sao mà ép cậu ấy dừng lại được.”'),
    ('“Vậy thì ngủ ngoan đi. Có chuyện gì xảy ra tôi sẽ lo liệu,”', '“Vậy thì ngủ ngoan đi. Có chuyện gì xảy ra anh sẽ lo liệu,”'),
    ('“Vậy tôi ngủ thật đấy nhé?”', '“Vậy em ngủ thật đấy nhé?”'),
    ('“Điện hạ thật đúng là vô tư lự. Không sợ trong lúc cậu ngủ say, tôi sẽ thừa cơ gạt phăng cậu sang một bên mà đoạt quyền sao?”', '“Điện hạ thật đúng là vô tư lự. Không sợ trong lúc em ngủ say, anh sẽ thừa cơ gạt phăng em sang một bên mà đoạt quyền sao?”'),
    ('“Anh cứ việc gạt tôi ra rìa đi. Đằng nào đống chuyện phiền phức kia tôi cũng chẳng muốn đụng tay vào.”', '“Anh cứ việc gạt em ra rìa đi. Đằng nào đống chuyện phiền phức kia em cũng chẳng muốn đụng tay vào.”'),
    ('“Tôi làm cậu thức giấc à?”', '“Anh làm em thức giấc à?”'),
    ('“Hay là... Điện hạ không nỡ để tôi đi?”', '“Hay là... Điện hạ không nỡ để anh đi?”'),
    ('“Tôi chỉ sợ trong lúc tôi ngủ, anh lại thừa cơ gạt phăng tôi sang một bên thôi,”', '“Em chỉ sợ trong lúc em ngủ, anh lại thừa cơ gạt phăng em sang một bên thôi,”'),
    ('“Cho nên anh cứ ở lại đây với tôi,”', '“Cho nên anh cứ ở lại đây với em,”'),
    ('“Hay là còn có lý do nào khác? Chẳng hạn như Điện hạ thực sự không nỡ xa rời tôi.”', '“Hay là còn có lý do nào khác? Chẳng hạn như Điện hạ thực sự không nỡ xa rời anh.”'),
    ('“Anh Trì Chước lại định nhân lúc tôi đang ngủ mà giở trò chiếm tiện nghi sao?”', '“Anh Trì Chước lại định nhân lúc em đang ngủ mà giở trò chiếm tiện nghi sao?”'),
    ('“Không sao đâu, tôi chỉ cần nghỉ ngơi một chút là được.”', '“Không sao đâu, em chỉ cần nghỉ ngơi một chút là được.”'),
    ('“Với tình trạng này của cậu, căn bản không thể nào nghỉ ngơi được,”', '“Với tình trạng này của em, căn bản không thể nào nghỉ ngơi được,”'),
    ('“Trì Chước, anh phiền phức thật đấy. Đừng ở cạnh tôi nữa.”', '“Trì Chước, anh phiền phức thật đấy. Đừng ở cạnh em nữa.”'),
    ('“Cậu thừa biết với sự nhạy cảm của tôi, muốn lừa gạt tôi là chuyện chẳng hề dễ dàng. Vậy mà cậu vẫn khăng khăng giữ tôi ở lại đây. Tại sao chứ? Muốn tôi giúp đỡ sao? Đó hoàn toàn không phải tác phong thường ngày của cậu. Cho nên... có phải là vì ở bên cạnh tôi sẽ khiến cậu cảm thấy dễ chịu hơn không?”',
     '“Em thừa biết với sự nhạy cảm của anh, muốn lừa gạt anh là chuyện chẳng hề dễ dàng. Vậy mà em vẫn khăng khăng giữ anh ở lại đây. Tại sao chứ? Muốn anh giúp đỡ sao? Đó hoàn toàn không phải tác phong thường ngày của em. Cho nên... có phải là vì ở bên cạnh anh sẽ khiến em cảm thấy dễ chịu hơn không?”'),
    ('“Đánh dấu tôi đi.”', '“Đánh dấu anh đi.”'),
    ('“Hiện tại tôi không thể khống chế được bản thân đâu.”', '“Hiện tại em không thể khống chế được bản thân đâu.”'),
    ('“Tôi tự chịu đựng được.”', '“Anh tự chịu đựng được.”'),
    ('“Anh thừa biết ý tôi không phải như vậy,”', '“Anh thừa biết ý em không phải như vậy,”'),
    ('“Đừng lo, có tôi ở đây.”', '“Đừng lo, có anh ở đây.”'),
    ('“Tôi đã nói rồi — đánh dấu tôi đi, tiểu điện hạ của tôi. Đánh dấu tôi, chiếm đoạt tôi. Những chuyện khác, cứ im lặng là được.”',
     '“Anh đã nói rồi — đánh dấu anh đi, tiểu điện hạ của anh. Đánh dấu anh, chiếm đoạt anh. Những chuyện khác, cứ im lặng là được.”'),
    ('“Điện hạ… cậu thắt nút rồi.”', '“Điện hạ… em thắt nút rồi.”'),
]

for old, new in replacements:
    if old not in text:
        print(f"FAILED TO FIND: {old}")
    else:
        text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated ch_109 successfully!")
