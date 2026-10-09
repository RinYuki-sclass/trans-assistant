import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

cdir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_038"
trans_file = os.path.join(cdir, "translation.md")

with open(trans_file, 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('---\n\n', 1)
header = parts[0] + '---\n\n'
paras = [p.strip() for p in parts[1].split('\n\n') if p.strip()]

# First 100 paras (indices 0 to 99)
clean_paras_first_100 = paras[:100]

# Paras 101 to 120 (indices 100 to 119)
fixed_last_20 = [
    "Cố Xuyên bị câu hỏi này của Sở Niên Niên làm cho tỉnh táo lại đôi chút, anh day day mắt, nhìn Sở Niên Niên thêm lần nữa.",
    "“Không có gì…” Anh xoa xoa huyệt thái dương để xoa dịu cơn đau đầu, nói: “Không chú ý nên nhìn nhầm cậu thành cô ấy.”",
    "…",
    "Sở Niên Niên bất động giữ nguyên tư thế cũ, tựa như một con rối gỗ mất đi linh hồn.",
    "Bên tai là chất giọng loli Đông Bắc của Mật Bảo.",
    "【Phát hiện kích hoạt điểm tình tiết tương ứng của kịch bản yêu đương, kịch bản đang tải——】",
    "【Thật quá quắt! Anh ta lại dám coi cậu thành bạch nguyệt quang, chẳng lẽ, chẳng lẽ sự đặc biệt anh ta dành cho cậu chỉ vì người chị gái kia thôi sao?! Cậu là ai chứ? Cậu chính là một trong những ứng viên xuất sắc nhất toàn vị diện mà Mật Bảo khổ công tìm kiếm, sao anh ta dám chứ?!! Cậu giận sôi máu, cậu quyết định phải bắt anh ta nhận rõ cậu rốt cuộc là ai!】",
    "【…】",
    "【Gương mặt tuấn tú lạnh lùng của anh ta vỡ vụn vì động tác của cậu, cậu nhìn chằm chằm anh ta, cười lạnh nguy hiểm, ngậm lấy bờ môi anh ta: Cố Xuyên, anh chỉ có thể nhìn một mình tôi.】",
    "Một đoạn chữ kích thích và nóng bỏng biến mất trước mắt Sở Niên Niên, cậu từ đầu đến cuối không hề có bất kỳ biến đổi cảm xúc nào, vẫn duy trì nguyên động tác cũ.",
    "Nhận thấy phản ứng khác quá xa so với ký chủ trước, Mật Bảo chết sững tại chỗ, ngầm hiểu là Sở Niên Niên từ chối diễn kịch bản, đang định làm theo cách đồng nghiệp chỉ dạy, bắt đầu vừa đe dọa vừa dụ dỗ thì Sở Niên Niên đã động đậy.",
    "Đầu ngón tay trắng nõn của cậu chậm rãi trèo lên cổ Cố Xuyên, tựa như một con rắn lặng lẽ không một tiếng động, siết chết con mồi trong lòng vào giây phút cuối cùng.",
    "Cố Xuyên bị động tác của Sở Niên Niên làm cho sặc tỉnh, anh cảm thấy khó thở, khi mở mắt ra thì vừa vặn đối diện với một đôi mắt hồ ly đen láy.",
    "“Cố Xuyên, nhìn cho rõ, tôi là ai?”",
    "Lực trên tay lại tăng thêm vài phần, khóe môi Sở Niên Niên từ từ nhếch lên.",
    "“Khụ khụ, khụ, Sở Niên Niên cậu——”",
    "Hai chữ “tìm chết” còn chưa kịp nói ra khỏi miệng, bàn tay trên cổ đã đột ngột buông lỏng.",
    "Ngay sau đó, bờ môi anh đã bị Sở Niên Niên hung hăng cắn lấy.",
    "“Tôi đúng là quá ngu xuẩn.”",
    "Anh nghe thấy Sở Niên Niên tự giễu cười khẩy một tiếng."
]

final_paras = clean_paras_first_100 + fixed_last_20

print(f"Total paragraphs: {len(final_paras)}")
assert len(final_paras) == 120

with open(trans_file, 'w', encoding='utf-8') as f:
    f.write(header + "\n\n".join(final_paras) + "\n")

print("ch_038 translation.md fixed successfully with exactly 120 paragraphs!")
