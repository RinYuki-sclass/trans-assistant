import os
import re

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_040\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_040\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 85, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 1: Một mặt là vì cậu và người đàn ông trong lòng đều không muốn kẻ đã hạ thuốc mình và anh được như ý nguyện, mặt khác là vì trước đó cậu cũng đã nói qua, cậu vốn không phải hạng người tùy tiện.
p[1] = "Một mặt là vì cậu và người đàn ông trong lòng đều không muốn kẻ đã hạ thuốc mình và anh được như ý nguyện, mặt khác là vì trước đó cậu cũng đã nói qua, cậu vốn không phải hạng người tùy tiện."

# Para 2: Cho dù cậu cần phát tiết, thì cũng không phải cứ vớ đại một người là được.
p[2] = "Cho dù cậu cần phát tiết, thì cũng không phải cứ vớ đại một người là được."

# Para 4: Ngay cả khi bên trong cơ thể người đàn ông cậu đang ôm thực sự ẩn chứa linh hồn của Alex, cậu cũng không thể để lần đầu tiên của hai người diễn ra trong tình cảnh tồi tệ như thế này.
p[4] = "Ngay cả khi bên trong cơ thể người đàn ông cậu đang ôm thực sự ẩn chứa linh hồn của Alex, cậu cũng không thể để lần đầu tiên của hai người diễn ra trong tình cảnh tồi tệ như thế này."

# Para 6: Dòng nước men theo đường ống chảy ngược lên trên, cuối cùng vỡ òa thành những tia nước lạnh buốt từ vòi hoa sen, làm ướt đẫm mái tóc đen của người đàn ông, cũng thấm thấu bộ vest xám mà anh vẫn chưa kịp cởi ra.
p[6] = "Dòng nước men theo đường ống chảy ngược lên trên, cuối cùng vỡ òa thành những tia nước lạnh buốt từ vòi hoa sen, làm ướt đẫm mái tóc đen của người đàn ông, cũng thấm thấu bộ vest xám mà anh vẫn chưa kịp cởi ra."

# Para 7: Sở Tư Thừa dùng tay vốc chút nước lạnh vỗ vỗ lên gò má nóng bừng của mình, trong lúc sự giãy giụa của người đàn ông dần yếu đi, cậu cuối cùng cũng có thời gian để sắp xếp lại cốt truyện trong đầu.
p[7] = "Sở Tư Thừa dùng tay vốc chút nước lạnh vỗ vỗ lên gò má nóng bừng của mình, trong lúc sự giãy giụa của người đàn ông dần yếu đi, cậu cuối cùng cũng có thời gian để sắp xếp lại cốt truyện trong đầu."

# Para 8: Chắc chẳng có nhân viên nào của Cục Quản lý tận tụy với công việc hơn cậu đâu nhỉ.
p[8] = "Chắc chẳng có nhân viên nào của Cục Quản lý tận tụy với công việc hơn cậu đâu nhỉ."

# Para 11: Thế giới cậu đang ở lúc này là một cuốn tiểu thuyết thuần ái cẩu huyết đời đầu.
p[11] = "Thế giới cậu đang ở lúc này là một cuốn tiểu thuyết thuần ái cẩu huyết đời đầu."

# Para 12: Nhân vật chính mà cậu sắm vai có tên là Tống Lạc An, thân thế vô cùng điển hình với một người cha nghiện rượu, một người mẹ bệnh tật, hai đứa em đang tuổi ăn học và một bản thân vụn vỡ.
p[12] = "Nhân vật chính mà cậu sắm vai có tên là Tống Lạc An, thân thế vô cùng điển hình với một người cha nghiện rượu, một người mẹ bệnh tật, hai đứa em đang tuổi ăn học và một bản thân vụn vỡ."

# Para 13: Vì viện phí đắt đỏ của mẹ, cậu đã chấp nhận sự bao nuôi của tổng tài bá đạo Lệ Yến Trạch, trở thành một chú chim hoàng yến bị nuôi nhốt bên cạnh đối phương, sau đó liên tục bị đối phương ngược thân ngược tâm.
p[13] = "Vì viện phí đắt đỏ của mẹ, cậu đã chấp nhận sự bao nuôi của tổng tài bá đạo Lệ Yến Trạch, trở thành một chú chim hoàng yến bị nuôi nhốt bên cạnh đối phương, sau đó liên tục bị đối phương ngược thân ngược tâm."

# Para 17: Lúc này Lệ Yến Trạch vẫn còn đang ngồi xe lăn, một mặt được "chim hoàng yến" chăm sóc, một mặt lại hoài niệm bạch nguyệt quang. Vậy nên khi kẻ sau vừa về nước, nhân vật chính - "chim hoàng yến" này liền gặp họa.
p[17] = "Lúc này Lệ Yến Trạch vẫn còn đang ngồi xe lăn, một mặt được \"chim hoàng yến\" chăm sóc, một mặt lại hoài niệm bạch nguyệt quang. Vậy nên khi kẻ sau vừa về nước, nhân vật chính - \"chim hoàng yến\" này liền gặp họa."

# Para 20: Sở Tư Thừa vô thức nhướng mày, hàng mi khẽ run rẩy. Cậu mở mắt ra lần nữa, đặt tầm mắt vào Thẩm Từ đang ở trong bồn tắm, dù liên tục bị nước lạnh xối vào người nhưng vẫn không nhịn được mà xé rách cổ áo.
p[20] = "Sở Tư Thừa vô thức nhướng mày, hàng mi khẽ run rẩy. Cậu mở mắt ra lần nữa, đặt tầm mắt vào Thẩm Từ đang ở trong bồn tắm, dù liên tục bị nước lạnh xối vào người nhưng vẫn không nhịn được mà xé rách cổ áo."

# Para 22: Sở Tư Thừa nghe thấy anh nhíu mày lẩm bẩm một tiếng, dường như thật sự không thể chịu đựng nổi cái lạnh thấu xương do nước lạnh mang lại.
p[22] = "Sở Tư Thừa nghe thấy anh nhíu mày lẩm bẩm một tiếng, dường như thật sự không thể chịu đựng nổi cái lạnh thấu xương do nước lạnh mang lại."

# Para 23: Nhưng đồng thời, anh lại vô thức kéo mở cổ áo, để diện tích tiếp xúc trực tiếp giữa da thịt và dòng nước lớn hơn. Những ngón tay theo bản năng đưa xuống định tự giải quyết cứ liên tục nhấp nhô trong nước, chỉ là không biết do động tác của anh không chuẩn, hay là sau khi trúng thuốc thì tay không còn sức lực.
p[23] = "Nhưng đồng thời, anh lại vô thức kéo mở cổ áo, để diện tích tiếp xúc trực tiếp giữa da thịt và dòng nước lớn hơn. Những ngón tay theo bản năng đưa xuống định tự giải quyết cứ liên tục nhấp nhô trong nước, chỉ là không biết do động tác của anh không chuẩn, hay là sau khi trúng thuốc thì tay không còn sức lực."

# Para 24: Chỗ đó sau khi trải qua sự gột rửa của nước lạnh và sự giày vò như tự ngược đãi của anh, không những không có chút dấu hiệu bình lặng nào, mà lửa còn càng cháy càng vượng.
p[24] = "Chỗ đó sau khi trải qua sự gột rửa của nước lạnh và sự giày vò như tự ngược đãi của anh, không những không có chút dấu hiệu bình lặng nào, mà lửa còn càng cháy càng vượng."

# Para 26: Bây giờ anh nên làm gì đây?
p[26] = "Bây giờ anh nên làm gì đây?"

# Para 27: Lý trí bảo Thẩm Từ rằng, anh cần phải tiếp tục nhẫn nhịn, anh bắt buộc phải nhẫn nhịn!
p[27] = "Lý trí bảo Thẩm Từ rằng, anh cần phải tiếp tục nhẫn nhịn, anh bắt buộc phải nhẫn nhịn!"

# Para 28: Bởi vì đây rõ ràng là một cái bẫy, anh đã nhìn ra được thì càng không nên nhảy vào.
p[28] = "Bởi vì đây rõ ràng là một cái bẫy, anh đã nhìn ra được thì càng không nên nhảy vào."

# Para 29: Thế nhưng cơ thể anh lại không thể khống chế được.
p[29] = "Thế nhưng cơ thể anh lại không thể khống chế được."

# Para 42: Cậu hơi cúi mắt, nhìn người đàn ông trong nước đang chìa tay về phía mình, đôi mắt đen láy dưới ánh đèn khẽ lấp lánh,
p[42] = "Cậu hơi cúi mắt, nhìn người đàn ông trong nước đang chìa tay về phía mình, đôi mắt đen láy dưới ánh đèn khẽ lấp lánh,"

# Para 43: “Anh muốn tôi giúp chỉ đạo bằng lời, hay là, trực tiếp ra tay?”
p[43] = "“Anh muốn tôi giúp chỉ đạo bằng lời, hay là, trực tiếp ra tay?”"

# Para 45: Bộ não bị dược lực khống chế khiến Thẩm Từ không thể suy nghĩ nhiều, chỉ dựa vào trực giác của một thương nhân mà chọn ra giải pháp tối ưu nhất cho mình vào lúc này.
p[45] = "Bộ não bị dược lực khống chế khiến Thẩm Từ không thể suy nghĩ nhiều, chỉ dựa vào trực giác của một thương nhân mà chọn ra giải pháp tối ưu nhất cho mình vào lúc này."

# Para 46: Bộ vest của anh đã hoàn toàn ướt đẫm, dán chặt vào người, tuy không để lộ quá nhiều da thịt nhưng cũng chính vì thế, mảng da thịt lộ ra trên nền vải xám lại càng thêm nổi bật.
p[46] = "Bộ vest của anh đã hoàn toàn ướt đẫm, dán chặt vào người, tuy không để lộ quá nhiều da thịt nhưng cũng chính vì thế, mảng da thịt lộ ra trên nền vải xám lại càng thêm nổi bật."

# Para 48: Sở Tư Thừa dùng đầu lưỡi khẽ đẩy vào lớp thịt mềm trong khoang miệng, ngồi xổm xuống giữa sự lôi kéo ngày một gấp gáp của Thẩm Từ, nhưng cậu không hề như Thẩm Từ mong muốn mà bước vào trong nước để cùng đối phương rơi vào đại dương dục vọng.
p[48] = "Sở Tư Thừa dùng đầu lưỡi khẽ đẩy vào lớp thịt mềm trong khoang miệng, ngồi xổm xuống giữa sự lôi kéo ngày một gấp gáp của Thẩm Từ, nhưng cậu không hề như Thẩm Từ mong muốn mà bước vào trong nước để cùng đối phương rơi vào đại dương dục vọng."

# Para 49: Thay vào đó, cậu vẫn đứng bên rìa bồn tắm, chỉ nhúng ngón tay vào nước, khuấy động mặt hồ vốn chỉ thuộc về một mình Thẩm Từ.
p[49] = "Thay vào đó, cậu vẫn đứng bên rìa bồn tắm, chỉ nhúng ngón tay vào nước, khuấy động mặt hồ vốn chỉ thuộc về một mình Thẩm Từ."

# Para 51: Đặc biệt là khi đầu ngón tay của Sở Tư Thừa chạm vào da thịt anh, cảm giác khô nóng phát ra từ bên trong cơ thể lại càng thêm rõ rệt.
p[51] = "Đặc biệt là khi đầu ngón tay của Sở Tư Thừa chạm vào da thịt anh, cảm giác khô nóng phát ra từ bên trong cơ thể lại càng thêm rõ rệt."

# Para 52: Anh giống như một lữ khách đang đi trong rừng rậm nhiệt đới, môi trường xung quanh ẩm ướt và oi bức không chỉ thấm đẫm quần áo mà còn tước đoạt lượng oxy xung quanh, khiến anh vô thức há miệng thở dốc, dường như chỉ có như vậy mới không làm anh mất đi toàn bộ ý thức giữa những đợt khoái cảm dâng trào như sóng vỗ.
p[52] = "Anh giống như một lữ khách đang đi trong rừng rậm nhiệt đới, môi trường xung quanh ẩm ướt và oi bức không chỉ thấm đẫm quần áo mà còn tước đoạt lượng oxy xung quanh, khiến anh vô thức há miệng thở dốc, dường như chỉ có như vậy mới không làm anh mất đi toàn bộ ý thức giữa những đợt khoái cảm dâng trào như sóng vỗ."

# Para 53: Có lẽ vì tâm lý trốn tránh nào đó, Thẩm Từ không hỏi tên của Sở Tư Thừa, đồng thời răng cũng cắn chặt môi, ngoại trừ những âm thanh không thể kiềm chế tràn ra từ khóe môi, anh cơ bản không hề phát ra tiếng động nào.
p[53] = "Có lẽ vì tâm lý trốn tránh nào đó, Thẩm Từ không hỏi tên của Sở Tư Thừa, đồng thời răng cũng cắn chặt môi, ngoại trừ những âm thanh không thể kiềm chế tràn ra từ khóe môi, anh cơ bản không hề phát ra tiếng động nào."

# Para 54: Anh dường như không có ý định giao lưu quá nhiều với Sở Tư Thừa.
p[54] = "Anh dường như không có ý định giao lưu quá nhiều với Sở Tư Thừa."

# Para 55: Nhưng Sở Tư Thừa lại không cho anh cơ hội trốn tránh.
p[55] = "Nhưng Sở Tư Thừa lại không cho anh cơ hội trốn tránh."

# Para 56: Đầu ngón tay hơi dùng lực, giống như đang chơi đàn piano, dễ dàng khơi dậy một trận run rẩy trên cơ thể Thẩm Từ, khiến anh không kìm được mà cong người lên.
p[56] = "Đầu ngón tay hơi dùng lực, giống như đang chơi đàn piano, dễ dàng khơi dậy một trận run rẩy trên cơ thể Thẩm Từ, khiến anh không kìm được mà cong người lên."

# Para 65: Nhưng người đàn ông bên cạnh lại như thể sinh ra để đối nghịch với anh, vẫn không ngừng suy đoán, “Đợi lát nữa nếu bọn họ thật sự xông vào thì phải làm sao đây…”
p[65] = "Nhưng người đàn ông bên cạnh lại như thể sinh ra để đối nghịch với anh, vẫn không ngừng suy đoán, “Đợi lát nữa nếu bọn họ thật sự xông vào thì phải làm sao đây…”"

# Para 66: Cậu nói: “Ngài có bị chụp ảnh không?”
p[66] = "Cậu nói: “Ngài có bị chụp ảnh không?”"

# Para 67: Cậu nói: “Ngài có bị hiểu lầm không?”
p[67] = "Cậu nói: “Ngài có bị hiểu lầm không?”"

# Para 68: Dòng nước xoáy tròn trôi xuống cống, sự tiếp xúc trên đầu ngón tay càng trở nên rõ ràng, điểm trống rỗng trong đại não của anh cũng theo âm thanh bên cạnh ngày càng lớn.
p[68] = "Dòng nước xoáy tròn trôi xuống cống, sự tiếp xúc trên đầu ngón tay càng trở nên rõ ràng, điểm trống rỗng trong đại não của anh cũng theo âm thanh bên cạnh ngày càng lớn."

# Para 69: Cuối cùng, trong tầm mắt mơ hồ, Thẩm Từ nhìn thấy người đàn ông từ từ đưa tay về phía mình, có thứ gì đó dính nhớp dính vào mặt anh.
p[69] = "Cuối cùng, trong tầm mắt mơ hồ, Thẩm Từ nhìn thấy người đàn ông từ từ đưa tay về phía mình, có thứ gì đó dính nhớp dính vào mặt anh."

# Para 70: Sau đó, kèm theo một tiếng đập cửa lớn bên ngoài phòng tắm, anh lại nghe thấy người đàn ông nói: “Làm sao bây giờ? Ngài trông bộ dạng này bị nhìn thấy thì có lẽ không ổn lắm đâu…”
p[70] = "Sau đó, kèm theo một tiếng đập cửa lớn bên ngoài phòng tắm, anh lại nghe thấy người đàn ông nói: “Làm sao bây giờ? Ngài trông bộ dạng này bị nhìn thấy thì có lẽ không ổn lắm đâu…”"

# Para 79: Chu Lạc Lạc
p[79] = "Người sáng mắt đều có thể nhìn ra lúc này tâm trạng hắn tệ đến cực điểm, thế mà Chu Lạc Lạc lại như người mù màu trời sinh, khi Lệ Yến Trạch rõ ràng đang lạnh lùng không muốn nói chuyện, gã vẫn cứ mon men lại gần đổ thêm dầu vào lửa."

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_040 updated successfully. Total paragraphs:", len(p))
