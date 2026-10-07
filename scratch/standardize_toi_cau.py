import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Script to standardize Tan Diem <-> Bach Huan dialogue pronouns to "tôi - cậu" across ch_001 to ch_007

def update_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content
    for old, new in replacements:
        if old not in content:
            print(f"Warning in {os.path.basename(path)}: '{old}' not found!")
        content = content.replace(old, new)
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"No changes in {path}")

# ch_001 replacements
ch1_reps = [
    ('“Đệt mợ mày! Ông đây căn bản không hề đánh mày——”', '“Đệt mợ! Tôi căn bản không hề đánh cậu——”'),
    ('“Bạch Huân, ông đây thèm vào đấm mày, ông đây chê mày bẩn thỉu.”', '“Bạch Huân, tôi thèm vào đấm cậu, tôi chê cậu bẩn thỉu.”'),
    ('“Mày bốc phét ở trường rằng mày xuất thân từ gia đình trí thức, ai nấy đều đồn mày là công tử thanh cao nho nhã gì đó? Ha, Bạch Huân, sao mày giả tạo thế hả, chẳng qua chỉ là một thằng nhà quê mặc đồ nhái mà thôi, cũng chỉ có mấy đứa ngốc như Thư Ninh Ninh mới tin mày.”',
     '“Cậu bốc phét ở trường rằng cậu xuất thân từ gia đình trí thức, ai nấy đều đồn cậu là công tử thanh cao nho nhã gì đó? Ha, Bạch Huân, sao cậu giả tạo thế hả, chẳng qua chỉ là một kẻ nhà quê mặc đồ nhái mà thôi, cũng chỉ có mấy đứa ngốc như Thư Ninh Ninh mới tin cậu.”'),
    ('“Mẹ kiếp, mày thử nói thêm một câu nữa xem?”', '“Mẹ kiếp, cậu thử nói thêm một câu nữa xem?”'),
    ('“Ông đây không hề bỏ thuốc cô ta, cô ta bị người khác gài bẫy, ông đây hảo tâm đi ngang qua cứu cô ta một mạng, ai ngờ lại bị một tiểu nhân hèn hạ như mày nắm thóp, lấy mấy đoạn camera cắt ghép đi tung tin đồn bôi nhọ ông đây.”',
     '“Tôi không hề bỏ thuốc cô ta, cô ta bị người khác gài bẫy, tôi hảo tâm đi ngang qua cứu cô ta một mạng, ai ngờ lại bị một kẻ tiểu nhân hèn hạ như cậu nắm thóp, lấy mấy đoạn camera cắt ghép đi tung tin đồn bôi nhọ tôi.”'),
    ('“Rốt cuộc mày muốn cái gì?”', '“Rốt cuộc cậu muốn cái gì?”'),
    ('“Hừ, mày đừng hòng...” Tần Diễm cười nhạo một tiếng, nhưng nét mặt bỗng cứng đờ trong một giây, có chút khó tin mà nhíu mày, “Ờ, cái gì, mày vừa nói cái gì?”',
     '“Hừ, cậu đừng hòng...” Tần Diễm cười nhạo một tiếng, nhưng nét mặt bỗng cứng đờ trong một giây, có chút khó tin mà nhíu mày, “Ờ, cái gì, cậu vừa nói cái gì?”'),
    ('“Mày... Mày đây là, có ý gì hả.”', '“Cậu... Cậu đây là, có ý gì hả.”'),
    ('“Mẹ kiếp, Bạch Huân, cái đồ biến thái nhà mày, ông đây không tha cho mày đâu!”', '“Mẹ kiếp, Bạch Huân, cái đồ biến thái nhà cậu, tôi không tha cho cậu đâu!”'),
]
update_file(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_001\translation.md', ch1_reps)

# ch_003 replacements
ch3_reps = [
    ('“Sao lại là thằng thần kinh nhà mày nữa thế, lúc này còn mò tới là muốn ăn đòn à?”', '“Sao lại là tên thần kinh nhà cậu nữa thế, lúc này còn mò tới là muốn ăn đòn à?”'),
    ('“Đệt mợ, rốt cuộc mày muốn làm cái gì, tao khuyên mày nếu không muốn chết thì mau buông tay ra ngay cho tao...”', '“Mẹ kiếp, rốt cuộc cậu muốn làm cái gì, tôi khuyên cậu nếu không muốn chết thì mau buông tay ra ngay cho tôi...”'),
    ('“Bạch Huân, mày bị biến thái đúng không, mày đích thị là một thằng biến thái!”', '“Bạch Huân, cậu bị biến thái đúng không, cậu đích thị là một tên biến thái!”'),
    ('“Bạch Huân, mày tiêu đời thật rồi,”', '“Bạch Huân, cậu tiêu đời thật rồi,”'),
    ('“Đến cả mày còn biết, mày nghĩ tao không tra ra được chắc?”', '“Đến cả cậu còn biết, cậu nghĩ tôi không tra ra được chắc?”'),
    ('“Tao không phải loại đàn ông lấy điểm yếu của phụ nữ ra để ép họ làm việc, hơn nữa, làm chuyện này cũng chẳng phải do cô ta muốn, người nhà cô ta bị ung thư.”',
     '“Tôi không phải loại đàn ông lấy điểm yếu của phụ nữ ra để ép họ làm việc, hơn nữa, làm chuyện này cũng chẳng phải do cô ta muốn, người nhà cô ta bị ung thư.”'),
    ('Này, sao tự nhiên mày lại muốn giúp tao?', 'Này, sao tự nhiên cậu lại muốn giúp tôi?'),
]
update_file(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_003\translation.md', ch3_reps)

# ch_004 replacements
ch4_reps = [
    ('“Được thôi, chẳng phải mày muốn tìm tiểu gia đây sao, cho mày một phút, có rắm thì mau phóng.”',
     '“Được thôi, chẳng phải cậu muốn tìm tôi sao, cho cậu một phút, có rắm thì mau phóng.”'),
]
update_file(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_004\translation.md', ch4_reps)

# ch_005 replacements
ch5_reps = [
    ('“Tao ấy à, chẳng thiếu thứ gì cả, nếu thật sự nói thiếu cái gì đó thì bây giờ chỉ thiếu một tên sai vặt đi theo hầu đọc sách thôi.”',
     '“Tôi ấy à, chẳng thiếu thứ gì cả, nếu thật sự nói thiếu cái gì đó thì bây giờ chỉ thiếu một tên sai vặt đi theo hầu đọc sách thôi.”'),
    ('“Mày chắc chắn chứ?”', '“Cậu chắc chắn chứ?”'),
    ('Bạch Huân, mày cứ đợi đấy, xem tao có xử đẹp mày không.', 'Bạch Huân, cậu cứ đợi đấy, xem tôi có xử đẹp cậu không.'),
]
update_file(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_005\translation.md', ch5_reps)

# ch_006 replacements
ch6_reps = [
    ('“Sao mày đi lề mề thế hả.”', '“Sao cậu đi lề mề thế hả.”'),
    ('“Mày vào trước đã.”', '“Cậu vào trước đã.”'),
    ('“Mày quản việc tao muốn viết lúc nào làm gì, mày đừng quên hiện tại mày là thân phận gì, tao bảo mày làm gì thì mày làm nấy, không làm thì cút.”',
     '“Cậu quản việc tôi muốn viết lúc nào làm gì, cậu đừng quên hiện tại cậu là thân phận gì, tôi bảo cậu làm gì thì cậu làm nấy, không làm thì cút.”'),
    ('“Mày, mày nhìn tao chằm chằm như thế làm gì.” Tần Diễm bị ánh mắt của Bạch Huân dọa sợ, cậu nhận ra bản thân có phần hơi quá đáng, nhưng lại không thể hạ mình xin lỗi, chỉ đành ho khan hai tiếng để xoa dịu bầu không khí, “Dù sao thì mày cứ tùy tiện viết giúp tao đi, viết được bao nhiêu thì bấy nhiêu, buồn ngủ thì cứ ngủ ở chỗ tao...”',
     '“Cậu, cậu nhìn tôi chằm chằm như thế làm gì.” Tần Diễm bị ánh mắt của Bạch Huân dọa sợ, cậu nhận ra bản thân có phần hơi quá đáng, nhưng lại không thể hạ mình xin lỗi, chỉ đành ho khan hai tiếng để xoa dịu bầu không khí, “Dù sao thì cậu cứ tùy tiện viết giúp tôi đi, viết được bao nhiêu thì bấy nhiêu, buồn ngủ thì cứ ngủ ở chỗ tôi...”'),
]
update_file(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_006\translation.md', ch6_reps)

# ch_007 replacements
ch7_reps = [
    ('“Mày đi đi, tao đi theo sau lưng mày, nếu có chuyện gì tao sẽ báo cảnh sát.”', '“Cậu đi đi, tôi đi theo sau lưng cậu, nếu có chuyện gì tôi sẽ báo cảnh sát.”'),
    ('“Chuyện ngày hôm nay, nếu có người thứ ba biết được, mày chết chắc.”', '“Chuyện ngày hôm nay, nếu có người thứ ba biết được, cậu chết chắc.”'),
    ('“Mày có bệnh à.”', '“Cậu có bệnh à.”'),
    ('“Tao cảnh cáo mày, bất kể trong lòng mày rốt cuộc đang toan tính cái gì, những ngày này nếu mày hầu hạ tao vui vẻ thì chuyện mày hãm hại tao tao sẽ miễn cưỡng mở một mắt nhắm một mắt bỏ qua cho, bằng không mày tự hiểu đấy, tao có thể khiến mày cút xéo khỏi trường bất cứ lúc nào.”',
     '“Tôi cảnh cáo cậu, bất kể trong lòng cậu rốt cuộc đang toan tính cái gì, những ngày này nếu cậu hầu hạ tôi vui vẻ thì chuyện cậu hãm hại tôi tôi sẽ miễn cưỡng mở một mắt nhắm một mắt bỏ qua cho, bằng không cậu tự hiểu đấy, tôi có thể khiến cậu cút xéo khỏi trường bất cứ lúc nào.”'),
    ('“Muộn quá rồi, hôm nay mày tự tìm một phòng ngủ dành cho khách mà ngủ đi.”', '“Muộn quá rồi, hôm nay cậu tự tìm một phòng ngủ dành cho khách mà ngủ đi.”'),
    ('“Còn nữa, sáng mai không được làm phiền tao, có việc thì tự nhiên.”', '“Còn nữa, sáng mai không được làm phiền tôi, có việc thì tự nhiên.”'),
    ('“Thế nếu tao không dậy thì mày gọi tao.”', '“Thế nếu tôi không dậy thì cậu gọi tôi.”'),
    ('“Tùy mày tùy mày.”', '“Tùy cậu tùy cậu.”'),
    ('“Mày nấu mỗi món này thôi á?”', '“Cậu nấu mỗi món này thôi á?”'),
    ('“Đợi đó, ngồi xe tao.” Tần Diễm đảo mắt: “Mày đi bộ thế này làm tao thấy tao chẳng có phong độ gì cả.”',
     '“Đợi đó, ngồi xe tôi.” Tần Diễm đảo mắt: “Cậu đi bộ thế này làm tôi thấy tôi chẳng có phong độ gì cả.”'),
]
update_file(r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_007\translation.md', ch7_reps)

print("All chapters updated to tôi - cậu successfully!")
