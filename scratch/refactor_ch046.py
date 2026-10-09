import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_046\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_046\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 103, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 2: Thẩm Từ -> anh
p[2] = "Thẩm Từ lại châm một điếu thuốc, giữa làn khói vây quanh, anh đưa tay kéo chàng trai ham chơi xuống khỏi máy chém."

# Para 3: Thẩm Từ -> Anh
p[3] = "“Tôi thấy cậu ấy sẽ không đâu.” Anh nói."

# Para 9: Thẩm Từ -> Anh, Sở Tư Thừa -> cậu
p[9] = "Anh có thể phối hợp với màn biểu diễn của chàng trai, nhưng điều đó không có nghĩa là anh có thể chấp nhận lời nói dối ngọt ngào của cậu."

# Para 13: Thẩm Từ -> anh, Sở Tư Thừa -> cậu
p[13] = "Sở Tư Thừa biết anh đang đợi cậu đưa ra lời giải thích cho mười phút đến muộn kia."

# Para 14: Sở Tư Thừa -> cậu
p[14] = "Ngay cả thời gian cũng nhớ rõ mười mươi, vậy mà còn nói bản thân không hề muốn cậu gọi điện tới."

# Para 16: Thẩm Từ -> anh
p[16] = "Tuy nhiên, thấy anh đã tặng mình một chiếc điện thoại mới, Sở Tư Thừa không tiếp tục trêu chọc anh nữa, mà trực tiếp trả lời:"

# Para 21: Thẩm Từ -> anh
p[21] = "Đầu ngón tay Thẩm Từ siết chặt, nhưng ngay sau đó anh nghe thấy chàng trai nói:"

# Para 25: Sở Tư Thừa -> cậu
p[25] = "Thẩm Từ nghe cậu nói: “Thế nào, anh thấy câu trả lời này của tôi đáng giá một triệu không?”"

# Para 27: Thẩm Từ -> Anh, anh
p[27] = "Anh rất rõ, chàng trai đang câu dẫn anh."

# Para 28: Thẩm Từ -> anh
p[28] = "Dù đối phương luôn thêm một câu hỏi vào cuối mỗi câu nói, tỏ ra như rất quan tâm đến ý kiến của anh."

# Para 29: Thẩm Từ -> anh
p[29] = "Nhưng Thẩm Từ biết, chàng trai căn bản không hề quan tâm đến câu trả lời của anh."

# Para 30: Thẩm Từ -> anh
p[30] = "Hay nói cách khác, chàng trai tin chắc câu trả lời của anh sẽ nằm trong dự liệu của mình."

# Para 31: Thẩm Từ -> anh
p[31] = "Có lẽ lúc này đối phương đang tùy ý nằm trên giường, khi hỏi anh, tay cũng đang buồn chán nghịch ngợm thứ gì đó khác."

# Para 32: Thẩm Từ -> anh
p[32] = "Trong cái ao cá trong vắt thấy đáy kia vốn đã sớm giăng sẵn lưới, bất kể anh bơi về hướng nào cũng không tránh khỏi kết cục bị tóm gọn."

# Para 34: Thẩm Từ -> Anh
p[34] = "Anh sớm nên biết rằng, vào khoảnh khắc công tắc mất kiểm soát được bật lên, cánh cửa lớn sẽ chẳng bao giờ đóng lại được nữa."

# Para 47: Hệ thống gọi Sở Tư Thừa -> cậu, Thẩm Từ -> anh ấy
p[47] = "【Ký chủ, có phải vì phản diện trông giống Alex nên cậu mới mập mờ với anh ấy như vậy không?】"

# Para 56: Sở Tư Thừa -> cậu
p[56] = "Sở Tư Thừa muốn hỏi, trên thế giới này, có ai thực sự tốt với nhân vật chính, xứng đáng để cậu thân cận hay không?"

# Para 58: Sở Tư Thừa -> cậu, Thẩm Từ -> anh
p[58] = "Đêm đầu tiên sau khi nhận ra thân phận của cậu, anh đã không giao cậu cho Lệ Yến Trạch, đồng thời còn chu đáo nhường lại căn phòng tổng thống này để cho cậu một nơi trú chân tạm thời."

# Para 59: Thẩm Từ -> anh
p[59] = "Sau đó anh lại càng là kiểu người quyết đoán ít lời, chuyển thẳng một triệu vào bệnh viện để giải quyết vấn đề viện phí của mẹ Tống."

# Para 60: Thẩm Từ -> anh
p[60] = "Thấy chiếc điện thoại nát sắp nổ tung của Tống Lạc An, anh liền trực tiếp gửi một chiếc bản đặt riêng đến, thuận tiện còn gia hạn luôn tiền phòng."

# Para 61: Thẩm Từ -> anh
p[61] = "Cho dù anh làm những việc này đều có mục đích, nhưng ít nhất người ta thực sự làm được việc, chứ không giống vị tổng tài bá đạo ngồi xe lăn kia, mở miệng là đe dọa, ngậm miệng là chèn ép."

# Para 65: Sở Tư Thừa -> cậu
p[65] = "Việc này trong mắt Sở Tư Thừa chỉ là một công việc, ai lại tươi cười với ông chủ khi đang làm việc bao giờ, huống chi cậu bây giờ đã nộp đơn nghỉ việc, lại càng lười để ý đến đối phương."

# Para 67: Hệ thống gọi Thẩm Từ -> anh ấy, Sở Tư Thừa -> cậu
p[67] = "【Cho nên ký chủ không hề bận tâm đến việc tên phản diện và Alex có ngoại hình giống nhau, mà chỉ vì anh ấy làm việc khá vừa ý cậu sao?】"

# Para 70: Thoại với hệ thống
p[70] = "“Cậu thấy sao thì là vậy đi.”"

# Para 72: Sở Tư Thừa -> cậu
p[72] = "Huống hồ, cậu quả thực cũng không quá để tâm đến phương diện ngoại hình."

# Para 74: Sở Tư Thừa -> cậu
p[74] = "Cho nên đối với Sở Tư Thừa mà nói, ngoại hình quả thực không quá quan trọng, thứ cậu coi trọng hơn chính là linh hồn ẩn giấu bên dưới lớp vỏ bọc ấy."

# Para 75: Sở Tư Thừa -> cậu
p[75] = "Thật ra cậu có chút tò mò, tại sao đối phương lại xuất hiện ở thế giới này."

# Para 76: Sở Tư Thừa -> cậu
p[76] = "Chẳng lẽ đối phương cũng là người thực hiện nhiệm vụ giống cậu, chỉ là tình cờ gặp nhau hai lần?"

# Para 78: Sở Tư Thừa -> cậu
p[78] = "Hoặc nếu tự luyến một chút, liệu có phải đối phương đã đi theo cậu đến đây không?"

# Para 80: Sở Tư Thừa -> cậu
p[80] = "Chỉ tiếc là, Cục quản lý không hề cung cấp nút bỏ qua nhiệm vụ cho người thực hiện, cậu muốn tiến vào thế giới tiếp theo thì chỉ có thể ngoan ngoãn hoàn thành nhiệm vụ trước mắt mà thôi."

# Para 81: Sở Tư Thừa -> cậu
p[81] = "Sở Tư Thừa lướt qua bảng nhiệm vụ, nhìn thanh tiến độ hào quang đáng thương chỉ mới đạt hai mươi phần trăm, cậu thu hồi ảo tưởng trong một giây, quay về với thực tại rồi bắt đầu nghịch điện thoại."

# Para 82: Hệ thống gọi Sở Tư Thừa -> cậu
p[82] = "【Ký chủ, cậu đang làm gì thế?】 Hệ thống thấy cậu vẻ mặt nghiêm túc liền tò mò hỏi."

# Para 95: Thẩm Từ -> anh
p[95] = "Thẩm Từ nghĩ, quyết định hủy bỏ kỳ nghỉ trước đó có lẽ là sai lầm, hiệu suất làm việc gần đây của anh quả thực có chút quá thấp."

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_046 updated successfully. Total paragraphs:", len(p))
