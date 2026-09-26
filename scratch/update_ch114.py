import sys

path = r'd:\Nhung\trans-tool\novel_projects\công-vai-chính-công\chapters\ch_114\translation.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('“Tôi đâu có lén lút, tôi làm việc này đường đường chính chính đấy chứ. Chỉ cần anh chịu ghé qua cung điện một lần thôi là đã sớm biết rồi. Đằng này có kẻ vô tâm nào đó chẳng thèm đến tìm tôi lấy một lần.”',
     '“Em đâu có lén lút, em làm việc này đường đường chính chính đấy chứ. Chỉ cần anh chịu ghé qua cung điện một lần thôi là đã sớm biết rồi. Đằng này có kẻ vô tâm nào đó chẳng thèm đến tìm em lấy một lần.”'),
    ('“Tôi không hề né tránh cậu. Tôi chỉ không muốn quấy rầy cậu, và muốn cho cậu một khoảng không gian riêng mà thôi.”',
     '“Anh không hề né tránh em. Anh chỉ không muốn quấy rầy em, và muốn cho em một khoảng không gian riêng mà thôi.”'),
    ('“Nếu tôi không biết anh đã phái người điều tra tôi, thậm chí còn lén mò về trang viên đọc trộm cuốn sách kia của tôi, thì tôi đã thực sự tưởng anh chẳng mảy may để tâm rồi đấy.”',
     '“Nếu em không biết anh đã phái người điều tra em, thậm chí còn lén mò về trang viên đọc trộm cuốn sách kia của em, thì em đã thực sự tưởng anh chẳng mảy may để tâm rồi đấy.”'),
    ('“Thực ra tôi đã hiểu nội dung cuốn sách kia của cậu rồi.”',
     '“Thực ra anh đã hiểu nội dung cuốn sách kia của em rồi.”'),
    ('“Đó chẳng qua chỉ là một cuốn sách thôi mà. Nếu có người phải lo lắng thì người đó đáng lẽ phải là tôi mới đúng chứ. Trong sách, anh và cậu ấy mới là một đôi, còn tôi chỉ là một kẻ qua đường chẳng có chút trọng lượng nào.”',
     '“Đó chẳng qua chỉ là một cuốn sách thôi mà. Nếu có người phải lo lắng thì người đó đáng lẽ phải là em mới đúng chứ. Trong sách, anh và cậu ấy mới là một đôi, còn em chỉ là một kẻ qua đường chẳng có chút trọng lượng nào.”'),
    ('“Đây xem như lời thú tội thành thật của tôi nhé. Ban đầu tôi chủ động tiếp cận anh quả thực là vì cuốn sách đó,”',
     '“Đây xem như lời thú tội thành thật của em nhé. Ban đầu em chủ động tiếp cận anh quả thực là vì cuốn sách đó,”'),
    ('“Thú tội chuyện này ngay trước thềm hôn lễ… cậu không sợ tôi sẽ bỏ chạy sao?”',
     '“Thú tội chuyện này ngay trước thềm hôn lễ… em không sợ anh sẽ bỏ chạy sao?”'),
    ('“Bởi vì tôi biết tỏng anh sẽ không bao giờ chạy trốn.”',
     '“Bởi vì em biết tỏng anh sẽ không bao giờ chạy trốn.”'),
    ('“Tôi không quan tâm lý do ban đầu cậu tiếp cận tôi là gì, tôi chỉ để tâm đến tương lai sau này mà thôi. Một khi đã kết hôn, cậu đừng hòng chạy thoát. Dục vọng chiếm hữu của tôi mạnh mẽ hơn cậu tưởng tượng nhiều đấy.”',
     '“Anh không quan tâm lý do ban đầu em tiếp cận anh là gì, anh chỉ để tâm đến tương lai sau này mà thôi. Một khi đã kết hôn, em đừng hòng chạy thoát. Dục vọng chiếm hữu của anh mạnh mẽ hơn em tưởng tượng nhiều đấy.”'),
    ('“Vậy thì cứ để tôi chứng kiến xem nào.”',
     '“Vậy thì cứ để em chứng kiến xem nào.”'),
    ('“Tôi thực sự muốn ăn sạch cậu ngay lúc này đấy, đóa hồng nhỏ của tôi,”',
     '“Anh thực sự muốn ăn sạch em ngay lúc này đấy, đóa hồng nhỏ của anh,”'),
    ('“Anh Trì Chước, nhìn đuôi của tôi này.”',
     '“Anh Trì Chước, nhìn đuôi của em này.”'),
    ('“Tân nương của tôi ơi, đến giờ dậy rồi.”',
     '“Tân nương của em ơi, đến giờ dậy rồi.”'),
    ('“Vậy thì cứ muộn đi, tiểu thê tử của tôi.”',
     '“Vậy thì cứ muộn đi, tiểu thê tử của anh.”'),
]

for old, new in replacements:
    if old not in text:
        print(f"FAILED TO FIND: {old}")
    else:
        text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated ch_114 successfully!")
