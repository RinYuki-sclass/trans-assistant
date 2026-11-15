---
description: "Quy chuẩn bắt buộc chuyển đổi tên truyện sang tiếng Việt thuần thục (Pure Vietnamese Novel Naming Mandate) khi thêm mới hoặc khởi tạo bất kỳ dự án tiểu thuyết nào trong novel_projects"
globs: "novel_projects/**"
alwaysApply: true
---

# RULES ĐẶT TÊN TRUYỆN THUẦN VIỆT KHI THÊM MỚI VÀO NOVEL PROJECT

> 🚨 **QUY TẮC BẮT BUỘC:**  
> Mọi dự án tiểu thuyết mới khi thêm vào `novel_projects/` (khởi tạo qua Agent, import từ nguồn raw 52shuku, JJWXC, hoặc cào từ web) **BẮT BUỘC PHẢI DỊCH VÀ CHUYỂN ĐỔI TÊN TRUYỆN SANG TIẾNG VIỆT THUẦN THỤC, DỄ HIỂU VÀ TỰ NHIÊN**.

---

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

1. **Thuần Việt & Tự Nhiên (Natural & Fluent Vietnamese):**
   - Tên truyện là bộ mặt của tác phẩm trên giao diện Web Reader, Thư viện và Mục lục.
   - Bắt buộc phải diễn đạt trọn vẹn ý nghĩa của tiêu đề gốc bằng tiếng Việt trong sáng, thu hút độc giả, đúng phong vị tiểu thuyết mạng.
   - Tuyệt đối không giữ nguyên bản dịch thô (convert máy) chứa ngữ pháp hoặc từ nối tiếng Trung.

2. **Cấm Convert Hán-Việt Thô & Ngữ Pháp Tiếng Trung:**
   - ❌ **CẤM:** Các từ ngữ pháp tiếng Trung bị phiên âm thô:
     - `... Liễu na cá ...` (了那个) $\rightarrow$ Đổi thành `... Tên ... kia` / `... Kẻ ... ấy`
     - `Hoán cá tân lão bà ...` (换个新老婆) $\rightarrow$ Đổi thành `Đổi vợ mới ...`
     - `... Đích phát tiểu ...` (的发小) $\rightarrow$ Đổi thành `Bạn nối khố của ...`
     - `... Hữu thoại yếu thuyết` (有话要说) $\rightarrow$ Đổi thành `... có điều muốn nói`
     - `Tằng vi ... đản hạ nhất tử` (曾为...诞下一子) $\rightarrow$ Đổi thành `Từng sinh con cho ...`
     - `Oan chủng công tha ...` (冤种攻他) $\rightarrow$ Đổi thành `Anh công xui xẻo ...`
     - `Phản phái nhượng ... hoài tử hậu` (反派让...怀崽后) $\rightarrow$ Đổi thành `Sau khi kẻ phản diện khiến ... mang thai`
     - `... Hòa ... HE liễu` (和...HE了) $\rightarrow$ Đổi thành `Thành đôi với ...` / `Về chung một nhà với ...`
     - `... Chích tưởng nã tiền bào lộ` (只想拿钱跑路) $\rightarrow$ Đổi thành `... chỉ muốn ôm tiền bỏ trốn`
     - `... Dã hội bị cường thủ hào đoạt ma` (也会被强取豪夺吗) $\rightarrow$ Đổi thành `... cũng bị cưỡng ép chiếm đoạt sao?`
     - `... Kháo mại manh công lược sở hữu nhân` (靠卖萌攻略所有人) $\rightarrow$ Đổi thành `... dựa vào làm nũng đốn tim mọi người`
     - `Nhật nhật tưởng sát ngã` (日日想杀我) $\rightarrow$ Đổi thành `Ngày nào cũng muốn lấy mạng tôi`
     - `Cán điệu ... bất thị giá cán pháp` (干掉...不是这干法) $\rightarrow$ Đổi thành `Trừ khử ... không phải làm kiểu này đâu`
     - `Nhất thai tam bảo sinh bất đình` (一胎三宝生不停) $\rightarrow$ Đổi thành `Một thai ba con sinh không ngừng`

3. **Từ Điển Chuyển Đổi Thuật Ngữ Lóng & Hán-Việt Sang Thuần Việt:**
   > 💡 **Lưu ý đặc biệt:** Thuật ngữ **"Tang thi"** (丧尸) trong truyện mạt thế **VẪN GIỮ NGUYÊN LÀ "TANG THI"** vì đây là thuật ngữ kinh điển, quen thuộc hàng đầu với độc giả (không đổi thành "xác sống").

   | Cụm từ gốc / Hán Việt | Nghĩa tiếng Việt chuẩn hóa |
   | :--- | :--- |
   | `Tang thi` (丧尸) | **Giữ nguyên "Tang thi"** (VD: *Bạn trai tang thi của tôi*) |
   | `Cơ kiến` (基建) | **Khai khẩn / Lập quốc / Xây dựng đế quốc** (VD: *Ngai vàng khai khẩn lập quốc*) |
   | `Khoái xuyên` / `Mau xuyên` (快穿) | **[Xuyên Nhanh]** (đồng bộ tag đuôi `[Xuyên Nhanh]`) |
   | `Cá mặn` (咸鱼) | **Lười biếng / Nằm phơi** |
   | `Phong phê` (疯批) | **Điên cuồng / Điên rồ** |
   | `Luyến ái não` (恋爱脑) | **Kẻ lụy tình / Mê muội yêu đương** |
   | `Thủ sách` (手册) | **Cẩm nang** |
   | `Thoái biến ký` (蜕变记) | **Nhật ký lột xác** |
   | `Cường thủ hào đoạt` (强取豪夺) | **Cưỡng ép chiếm đoạt** |
   | `Bạch liên hoa` (白莲花) | **Hoa sen trắng** |
   | `Bạch nguyệt quang` (白月光) | **Ánh trăng sáng** |
   | `Tiểu cẩu` (小狗) | **Cún con / Chó cưng** |
   | `Đặc trợ` (特助) | **Trợ lý / Trợ lý tốt thí** |
   | `Phối giác` (配角) | **Nhân vật phụ / Kẻ làm nền** |
   | `Bi tình` (悲情) | **Bi thương / Đau khổ** |
   | `Tuyệt phối` (绝配) | **Đôi trời sinh / Cặp đôi hoàn hảo** |
   | `Cường chế ái` (强制爱) | **Cưỡng ép yêu / Ép yêu** |
   | `Thiểm cẩu` (舔狗) | **Kẻ liếm cẩu / Người si tình mù quáng** |
   | `Hồi đáng` (回档) | **Quay về điểm lưu / Về vạch xuất phát** |

---

## 2. QUY CHUẨN LƯU TRỮ TRONG HỆ THỐNG FILE DỰ ÁN

Mỗi khi tạo mới một thư mục dự án `novel_projects/<slug>/`:

1. **`config.json`:**
   - Trường `"title"`: BẮT BUỘC lưu **Tên tiếng Việt thuần thục** (VD: `"Bẻ Cong Tên Trai Thẳng Long Ngạo Thiên Kia"`).
   - Trường `"chinese_title"`: Lưu **Tên tiếng Trung gốc** (VD: `"攻了那个直男龙傲天"`).
   - Trường `"slug"`: Giữ dạng ký tự latin không dấu, ngăn cách bằng dấu gạch nối (VD: `"cong-lieu-na-ca-truc-nam-long-ngao-thien"` hoặc slug thuần Việt).

2. **`AGENTS.md`:**
   - Dòng tiêu đề H1: `# AGENT RULES: <TÊN THUẦN VIỆT IN HOA> (<Tên tiếng Trung gốc nếu có>)`
   - Dòng thông tin: `- **Tên truyện:** <Tên thuần Việt> (<Tên tiếng Trung gốc nếu có>).`

3. **`TOC.md`:**
   - Dòng tiêu đề H1: `# MỤC LỤC: <Tên thuần Việt> (<Tên tiếng Trung gốc nếu có>)`

---

## 3. CHECKLIST KIỂM TRA KHI THÊM TIỂU THUYẾT MỚI
- [ ] Tên truyện đã được chuyển đổi sang tiếng Việt tự nhiên chưa? Có còn dính cụm từ convert Hán-Việt ngô nghê không?
- [ ] Đã chuyển các tag `[Khoái Xuyên]` thành `[Xuyên Nhanh]` chưa?
- [ ] Đã dịch từ lóng gây khó hiểu (`luyến ái não` $\rightarrow$ `lụy tình`, `cơ kiến` $\rightarrow$ `khai khẩn lập quốc`...) và bảo toàn thuật ngữ quen thuộc (`tang thi` giữ nguyên)?
- [ ] Tên tiếng Trung gốc đã được lưu vào `"chinese_title"` trong `config.json` chưa?
- [ ] Tiêu đề trong `AGENTS.md` và `TOC.md` đã đồng bộ với tên thuần Việt chưa?
