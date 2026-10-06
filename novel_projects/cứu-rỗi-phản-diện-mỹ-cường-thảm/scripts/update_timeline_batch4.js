const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '../memory/timeline.json');
const data = JSON.parse(fs.readFileSync(file, 'utf8'));

const newChapters = [
  {
    chapter: 'ch_069',
    title: 'Chương 69: Bạch thiếu gia, em thật tàn nhẫn',
    event: 'Thần Vũ và Hoàng Khiếu Thiên giao nộp toàn bộ chứng cứ cho cảnh sát; Lục Đảo Phong bị bắt khẩn cấp ngay tại hội nghị cổ đông. Thần Vũ một mình tới biệt thự Bạch gia đội mưa chờ suốt 3 tiếng dưới cổng. Dữ Nhĩ phát hiện bèn lao xuống sân che ô; Thần Vũ ôm chặt lấy cậu vào lòng, nghẹn ngào hỏi tội sao lại lừa anh và thốt lên: "Bạch thiếu gia, em thật tàn nhẫn". Hắc hóa tăng lên 86 do Thần Vũ tự ti về khoảng cách thân phận hào môn.',
    blackening_value: 86
  },
  {
    chapter: 'ch_070',
    title: 'Chương 70: Vậy em có thể ngoan ngoãn một chút không?',
    event: 'Dữ Nhĩ ôm Thần Vũ và giải thích mọi hiểu lầm, khuyên anh không được bỏ rơi mình. Thần Vũ ngậm chặt ngón tay Dữ Nhĩ, hôn lên khóe môi cậu và nghẹn ngào bảo "Vậy em có thể ngoan ngoãn một chút không?". Thần Vũ đưa Dữ Nhĩ về nhà ổ chuột, cởi đồ ướt sấy tóc dỗ dành cậu ngủ. Tại Lục gia, Lục Tử Nghi cùng đường bị anh em đuổi khỏi nhà, ôm hận thù điên cuồng lên kế hoạch trả thù Thần Vũ.',
    blackening_value: 86
  },
  {
    chapter: 'ch_071',
    title: 'Chương 71: Đồ vô lương tâm',
    event: 'Thần Vũ thức dậy thấy Dữ Nhĩ biến mất, hoảng loạn đi tìm khắp nơi (hắc hóa lên 89); hóa ra Dữ Nhĩ biến thành cún Maltese chạy ra chợ mua bánh bao và sườn heo mang về cho anh. Thần Vũ bế cún vào lòng xót xa mắng yêu "đồ vô lương tâm". Dữ Nhĩ biến lại thành người ôm anh. Thần Vũ đưa Dữ Nhĩ vào bệnh viện thăm sư phụ Trần Cận; Trần Cận vui mừng khi thấy Thần Vũ đã tìm được người mình yêu thương.',
    blackening_value: 89
  },
  {
    chapter: 'ch_072',
    title: 'Chương 72: Em làm',
    event: 'Trần Cận qua đời thanh thản trong bệnh viện sau khi dặn dò Thần Vũ phải sống tốt; Thần Vũ nén đau thương tổ chức tang lễ cho sư phụ, hắc hóa tăng lên 90. Trở về nhà cũ, Thần Vũ uống say suy sụp, Dữ Nhĩ ôm lấy anh an ủi. Thần Vũ kéo Dữ Nhĩ lên giường, đưa cho cậu chai dầu bôi trơn và thì thầm "Em làm"; Dữ Nhĩ đỏ mặt đè Thần Vũ xuống giường, cả hai phát sinh quan hệ thân mật sâu sắc đầu tiên (Dữ Nhĩ làm công).',
    blackening_value: 90
  },
  {
    chapter: 'ch_073',
    title: 'Chương 73: Vậy em mau lớn lên đi',
    event: 'Sáng hôm sau, Thần Vũ thức dậy với tấm lưng đầy vết cào cấu của Dữ Nhĩ; anh nấu bữa sáng cho cậu ăn và trêu ghẹo chuyện giường chiếu tối qua, dỗ dành "Vậy em mau lớn lên đi". Bộ phim võ hiệp của đạo diễn Mã chính thức công chiếu, tạo nên cơn sốt phòng vé kỷ lục; vai diễn Cừu Vũ của Thần Vũ bùng nổ diễn xuất chấn động toàn quốc, nhận vô số đề cử giải thưởng điện ảnh danh giá.',
    blackening_value: 90
  },
  {
    chapter: 'ch_074',
    title: 'Chương 74: Em là chú cún con ngoan nhất',
    event: 'Lễ trao giải điện ảnh Kim Chi khai mạc. Thần Vũ và Dữ Nhĩ cùng nhau sải bước trên thảm đỏ. Lục Tử Nghi xuất hiện với bộ dạng tiều tụy bẩn thỉu rắp tâm gây chuyện nhưng bị bảo vệ tống cổ. Thần Vũ được xướng tên đoạt giải Nam diễn viên chính xuất sắc nhất (Ảnh đế). Đứng trên bục nhận giải, Thần Vũ nghẹn ngào cảm ơn người quan trọng nhất cuộc đời mình và nhìn xuống Dữ Nhĩ; hắc hóa tăng lên 93 do cảm xúc dâng trào và Lục Tử Nghi lén rình rập ngoài hội trường.',
    blackening_value: 93
  },
  {
    chapter: 'ch_075',
    title: 'Chương 75: Tôi chỉ có mình em thôi',
    event: 'Sau đêm nhận giải, Thần Vũ đưa Dữ Nhĩ về nhà và cả hai quấn quýt nồng nàn. Thần Vũ thổ lộ anh chẳng còn người thân nào trên đời nữa, "Tôi chỉ có mình em thôi", khiến hắc hóa bùng nổ lên 98 do tâm lý phụ thuộc và chiếm hữu tột độ. Lục Tử Nghi liên hệ với đám côn đồ cho vay nặng lãi và lên kế hoạch bắt cóc Bạch Dữ Nhĩ để tống tiền và hủy hoại Thần Vũ.',
    blackening_value: 98
  },
  {
    chapter: 'ch_076',
    title: 'Chương 76: Cậu ấy đâu rồi?',
    event: 'Dữ Nhĩ đi siêu thị mua nguyên liệu nấu lẩu cho Thần Vũ thì bị Lục Tử Nghi cùng đám giang hồ đánh thuốc mê bắt cóc đến nhà xưởng bỏ hoang ngoại ô. Thần Vũ ở nhà đợi mãi không thấy Dữ Nhĩ về, gọi điện thuê bao, phát hiện túi đồ siêu thị rơi vãi ở ngõ; hắc hóa chạm đỉnh 98. Thần Vũ nhận được điện thoại tống tiền của Lục Tử Nghi, gã ép Thần Vũ phải đến một mình nếu không sẽ giết chết Dữ Nhĩ.',
    blackening_value: 98
  },
  {
    chapter: 'ch_077',
    title: 'Chương 77: Đừng động vào cậu ấy',
    event: 'Thần Vũ một mình lái xe như điên đến nhà xưởng bỏ hoang, trong tay chỉ cầm một thanh ống sắt. Lục Tử Nghi trói Dữ Nhĩ trên ghế cao và ra lệnh cho đám côn đồ cầm dao vây chém Thần Vũ. Thần Vũ liều mạng đánh bại từng tên giang hồ, cả người đầm đìa vết thương máu me nhưng ánh mắt kiên định gầm thét: "Đừng động vào cậu ấy!". Lục Tử Nghi hoảng loạn kề dao vào cổ Dữ Nhĩ ép Thần Vũ vứt vũ khí.',
    blackening_value: 98
  },
  {
    chapter: 'ch_078',
    title: 'Chương 78: Bỏ dao xuống',
    event: 'Vì bảo vệ tính mạng của Dữ Nhĩ, Thần Vũ vứt thanh sắt chịu trói. Lục Tử Nghi cười điên loạn lao vào dùng gậy sắt đánh gãy chân Thần Vũ và đập túi bụi vào đầu anh tóe máu. Dữ Nhĩ gào khóc thảm thiết van xin. Hệ thống cảnh báo hắc hóa của Thần Vũ chạm ngưỡng 99 - ranh giới sinh tử tuyệt vọng. Lục Tử Nghi tưới xăng khắp nhà xưởng chuẩn bị phóng hỏa thiêu sống cả hai.',
    blackening_value: 99
  },
  {
    chapter: 'ch_079',
    title: 'Chương 79: Cháy',
    event: 'Lục Tử Nghi châm lửa phóng hỏa rồi khóa chặt cửa sắt bỏ chạy. Ngọn lửa bùng cháy dữ dội bao trùm nhà xưởng, khói đặc nghẹt thở. Thần Vũ dùng chút sức tàn bò về phía Dữ Nhĩ, lấy thân mình che chắn mảnh xà gồ rực lửa rơi xuống. Thấy Thần Vũ vì mình mà sẵn sàng hy sinh tính mạng mà không một lời oán trách, giá trị hắc hóa bỗng sụp đổ thần kỳ từ 99 tụt thẳng xuống 10 điểm; Hệ thống Uông Uông reo hò thông báo nhiệm vụ hoàn thành!',
    blackening_value: 10
  },
  {
    chapter: 'ch_080',
    title: 'Chương 80: Đừng khóc',
    event: 'Giữa biển lửa, Dữ Nhĩ trong cơn tuyệt vọng bèn biến thân thành cún Maltese nhỏ bé tuột khỏi xích sắt. Cún con chạy lại liếm máu trên mắt Thần Vũ để anh nhìn thấy, rồi biến lại thành người tháo xích cứu anh. Thần Vũ thì thầm "Đừng khóc" và ngỡ ngàng nhận ra bí mật người yêu chính là chú cún Maltese. Cả hai dìu nhau tìm lối thoát giữa đống đổ nát rực cháy.',
    blackening_value: 10
  },
  {
    chapter: 'ch_081',
    title: 'Chương 81: Em có thật lòng thích tôi không?',
    event: 'Dữ Nhĩ vừa khóc vừa thú nhận toàn bộ sự thật: mình là chú cún Maltese số 23 và Thần Vũ vốn là nhân vật trong cuốn tiểu thuyết hắc hóa. Thần Vũ không hề sợ hãi hay oán trách, chỉ siết chặt lấy cổ tay cậu, đôi mắt đỏ ngầu nghẹn ngào hỏi câu duy nhất xuất phát từ tận đáy lòng: "Em có thật lòng thích tôi không?". Hệ thống cảnh báo thế giới logic sắp sụp đổ do tiết lộ thân phận.',
    blackening_value: 0
  },
  {
    chapter: 'ch_082',
    title: 'Chương 82: Em có thể gọi anh một tiếng chủ nhân được không? (Kết thúc thế giới 2)',
    event: 'Dữ Nhĩ khóc nức nở thổ lộ "Em thích anh", Thần Vũ lấy thân mình chịu đèn sắt rơi trúng lưng bảo vệ cậu trước khi bất tỉnh. Bạch gia cùng cảnh sát ập vào cứu cả hai; Lục Tử Nghi chết cháy trong tai nạn ô tô khi bỏ trốn. Bạch gia mở công ty giải trí cho Dữ Nhĩ quản lý và ký hợp đồng với Thần Vũ. Cả hai ngọt ngào trêu ghẹo nhau tại căn nhà cũ, Thần Vũ đòi Dữ Nhĩ gọi "chủ nhân" trên giường. Chấp hành quan và Hệ thống đến; Maltese quyết định ở lại thế giới này bên Thần Vũ trọn đời. Hệ thống chào tạm biệt chuẩn bị tiếp nhận ký chủ Border Collie ở Thế giới 3 (Cẩm Y Vệ Cố Thừa Minh).',
    blackening_value: 0
  }
];

newChapters.forEach(nc => {
  const idx = data.findIndex(c => (c.chapter || c.chapter_id) === nc.chapter);
  if (idx >= 0) {
    data[idx] = nc;
  } else {
    data.push(nc);
  }
});

fs.writeFileSync(file, JSON.stringify(data, null, 2), 'utf8');
console.log('Updated timeline.json successfully. Total chapters:', data.length);
