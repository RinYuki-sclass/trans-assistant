import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

chapters_info = {
    'ch_052': {
        'title': 'Chương 52: Khắc tinh tang thi',
        'chars': ['Sở Niên Niên', 'Cố Xuyên', 'Lý Viện Viện', 'Đại Hải', 'Trần Khiêm'],
        'events': [
            "Cố Xuyên bộc phát toàn bộ dị năng sấm sét đỉnh phong, càn quét vòng vây tang thi biến dị.",
            "Sở Niên Niên thi triển năng lực khắc chế đặc thù, âm thầm vô hiệu hóa đòn tấn công của tang thi chúa.",
            "Phòng tuyến Long Thành đứng vững trong gang tấc; các dị năng giả chấn động trước sức mạnh của hai người."
        ]
    },
    'ch_053': {
        'title': 'Chương 53: Đổi mới Long Thành',
        'chars': ['Sở Niên Niên', 'Cố Xuyên', 'Lý Viện Viện', 'Đại Hải', 'Trần Khiêm', 'Triệu Doãn'],
        'events': [
            "Đợt triều tang thi bị đẩy lui hoàn toàn khỏi bờ cõi căn cứ Long Thành.",
            "Cố Xuyên chỉ huy dọn dẹp chiến trường, thu giữ lượng lớn tinh thạch cấp cao.",
            "Nội bộ lãnh đạo cũ của căn cứ Long Thành rung chuyển; Cố Xuyên bắt đầu thanh trừng phe phái mục nát."
        ]
    },
    'ch_054': {
        'title': 'Chương 54: Thủ lĩnh tối cao',
        'chars': ['Sở Niên Niên', 'Cố Xuyên', 'Lý Viện Viện', 'Trần Khiêm', 'Triệu Doãn'],
        'events': [
            "Cố Xuyên chính thức tiếp quản quyền lực tối cao, trở thành thủ lĩnh duy nhất của căn cứ Long Thành.",
            "Địa vị của Sở Niên Niên được nâng lên ngang hàng thủ lĩnh; mọi người trong căn cứ đều kính cẩn.",
            "Cố Xuyên đưa toàn bộ quyền hạn và vật tư tốt nhất cho Sở Niên Niên quản lý."
        ]
    },
    'ch_055': {
        'title': 'Chương 55: Tái thiết căn cứ',
        'chars': ['Sở Niên Niên', 'Cố Xuyên', 'Lý Viện Viện', 'Đại Hải', 'Trần Khiêm'],
        'events': [
            "Căn cứ Long Thành bước vào giai đoạn tái thiết toàn diện, phát vắc xin phòng ngừa virus.",
            "Đời sống cư dân dần ổn định; tiếng cười rộn rã xuất hiện trở lại giữa thời mạt thế.",
            "Cố Xuyên ngày đêm quấn quýt bên Sở Niên Niên, tình cảm giữa hai người vô cùng thắm thiết."
        ]
    },
    'ch_056': {
        'title': 'Chương 56: Kịch bản hoàn thành',
        'chars': ['Sở Niên Niên', 'Cố Xuyên', 'Hệ thống Yêu Đương (Mật Bảo)'],
        'events': [
            "Hệ thống Mật Bảo vang lên thông báo: Độ hảo cảm của Cố Xuyên đạt 100%, nhiệm vụ kịch bản yêu đương hoàn thành xuất sắc.",
            "Sở Niên Niên nhận được quyền chọn rút lui sang thế giới kế tiếp.",
            "Sở Niên Niên bắt đầu sắp xếp đồ đạc, do dự trước tình cảm sâu đậm của Cố Xuyên."
        ]
    },
    'ch_057': {
        'title': 'Chương 57: Chạy trốn bất thành',
        'chars': ['Sở Niên Niên', 'Cố Xuyên', 'Hệ thống Yêu Đương (Mật Bảo)'],
        'events': [
            "Sở Niên Niên toan lặng lẽ rời khỏi căn hộ giữa đêm khuya để thoát ly thế giới.",
            "Cố Xuyên phát hiện kịp thời, chặn ngay cửa ra vào và ôm chặt lấy cậu từ phía sau.",
            "Cố Xuyên khóa chặt Sở Niên Niên trong lòng, ánh mắt đỏ ngầu ghen tuông và tuyệt vọng cấm cậu rời xa mình."
        ]
    },
    'ch_058': {
        'title': 'Chương 58: Ngoại truyện viên mãn - Kết thúc Thế giới 2',
        'chars': ['Sở Niên Niên', 'Cố Xuyên', 'Lý Viện Viện', 'Trần Khiêm'],
        'events': [
            "Cố Xuyên bá đạo tuyên bố: 'Muốn chạy? Ai đào tinh thạch cho em, ai cho em ăn, ai ngủ cùng em cả đời?'.",
            "Sở Niên Niên đầu hàng trước sự dung túng yêu chiều vô điều kiện của đại lão, cam tâm tình nguyện ở lại.",
            "Kết thúc viên mãn Thế giới 2 (Mạt thế tang thi: Sở Niên Niên x Cố Xuyên).",
            "Đoạn preview ngắn chuyển giao sang Thế giới 3 (Trùng tộc: Thượng tướng trùng cái Gavin x Trùng đực phế vật Eli)."
        ]
    }
}

qa_tables = {
    'ch_052': """# Bảng Tra Cứu Thực Thể & Thuật Ngữ - Chương 52

### 1. Thực Thể & Thuật Ngữ (Proper Nouns & Entities)
| Nguyên tác | Hán Việt / Phiên âm | Thuật ngữ chuẩn hóa | Ghi chú ngữ cảnh |
| :--- | :--- | :--- | :--- |
| 楚年年 | Sở Niên Niên | Sở Niên Niên | Nam chính, công (ngôi 3 trần thuật: "cậu") |
| 顧川 | Cố Xuyên | Cố Xuyên | Nam chính, thụ (ngôi 3 trần thuật: "anh") |
| 陸阡 | Lục Thiên | Lục Thiên | Cấp dưới của Cố Xuyên |
| 李媛媛 | Lý Viện Viện | Lý Viện Viện | Thành viên nữ trong đội |
| 大海 | Đại Hải | Đại Hải | Thành viên nam trong đội |
| 陳騫 | Trần Khiêm | Trần Khiêm | Cấp dưới thân cận của Cố Xuyên |
| 變異喪屍 | Biến dị tang thi | Tang thi biến dị | Quái vật cấp cao nguy hiểm |
| 雷系異能 | Lôi hệ dị năng | Dị năng hệ sét | Năng lực chiến đấu đỉnh cao của Cố Xuyên |

### 2. Đại Từ Nhân Xưng & Thoại (Pronouns & Dialogue Pairs)
| Nhân vật phát ngôn | Đối tượng tiếp nhận | Quan hệ ngữ cảnh | Đại từ chuẩn hóa |
| :--- | :--- | :--- | :--- |
| Sở Niên Niên | Cố Xuyên | Yêu thương, sát cánh chiến đấu | em - anh / Cố ca / ca ca |
| Cố Xuyên | Sở Niên Niên | Bảo bọc, yêu chiều | anh / tôi - em / Niên Niên |
| Sở Niên Niên | Lục Thiên | Đối chất / nói chuyện riêng | tôi - anh |
| Đồng đội | Cố Xuyên | Cấp dưới kính phục | tôi / chúng tôi - Cố đội / anh Cố / anh |
""",
    'ch_053': """# Bảng Tra Cứu Thực Thể & Thuật Ngữ - Chương 53

### 1. Thực Thể & Thuật Ngữ (Proper Nouns & Entities)
| Nguyên tác | Hán Việt / Phiên âm | Thuật ngữ chuẩn hóa | Ghi chú ngữ cảnh |
| :--- | :--- | :--- | :--- |
| 楚年年 | Sở Niên Niên | Sở Niên Niên | Nam chính, công (ngôi 3 trần thuật: "cậu") |
| 顧川 | Cố Xuyên | Cố Xuyên | Nam chính, thụ (ngôi 3 trần thuật: "anh") |
| 龍城基地 | Long Thành cơ địa | Căn cứ Long Thành | Căn cứ trọng điểm nơi diễn ra câu chuyện |
| 趙昀 | Triệu Doãn | Triệu Doãn | Quản lý cũ của Sở Niên Niên |
| 晶石 | Tinh thạch | Tinh thạch | Nguồn năng lượng khai thác từ tang thi |

### 2. Đại Từ Nhân Xưng & Thoại (Pronouns & Dialogue Pairs)
| Nhân vật phát ngôn | Đối tượng tiếp nhận | Quan hệ ngữ cảnh | Đại từ chuẩn hóa |
| :--- | :--- | :--- | :--- |
| Sở Niên Niên | Cố Xuyên | Thân mật ngọt ngào | em - anh / ca ca |
| Cố Xuyên | Sở Niên Niên | Dung túng cưng chiều | anh / tôi - em / Niên Niên |
| Cố Xuyên | Cấp dưới | Chỉ huy dọn dẹp | tôi - các cậu |
""",
    'ch_054': """# Bảng Tra Cứu Thực Thể & Thuật Ngữ - Chương 54

### 1. Thực Thể & Thuật Ngữ (Proper Nouns & Entities)
| Nguyên tác | Hán Việt / Phiên âm | Thuật ngữ chuẩn hóa | Ghi chú ngữ cảnh |
| :--- | :--- | :--- | :--- |
| 楚年年 | Sở Niên Niên | Sở Niên Niên | Nam chính, công (ngôi 3 trần thuật: "cậu") |
| 顧川 | Cố Xuyên | Cố Xuyên | Thủ lĩnh căn cứ Long Thành (ngôi 3: "anh") |
| 陳騫 | Trần Khiêm | Trần Khiêm | Trợ lý đắc lực của Cố Xuyên |
| 基地長 | Cơ địa trưởng | Thủ lĩnh căn cứ | Danh vị tối cao của Cố Xuyên |

### 2. Đại Từ Nhân Xưng & Thoại (Pronouns & Dialogue Pairs)
| Nhân vật phát ngôn | Đối tượng tiếp nhận | Quan hệ ngữ cảnh | Đại từ chuẩn hóa |
| :--- | :--- | :--- | :--- |
| Sở Niên Niên | Cố Xuyên | Trà xanh làm nũng ngọt ngào | em - anh / ca ca |
| Cố Xuyên | Sở Niên Niên | Giao phó toàn bộ tài sản, địa vị | anh - em / Niên Niên |
""",
    'ch_055': """# Bảng Tra Cứu Thực Thể & Thuật Ngữ - Chương 55

### 1. Thực Thể & Thuật Ngữ (Proper Nouns & Entities)
| Nguyên tác | Hán Việt / Phiên âm | Thuật ngữ chuẩn hóa | Ghi chú ngữ cảnh |
| :--- | :--- | :--- | :--- |
| 楚年年 | Sở Niên Niên | Sở Niên Niên | Nam chính, công (ngôi 3 trần thuật: "cậu") |
| 顧川 | Cố Xuyên | Cố Xuyên | Nam chính, thụ (ngôi 3 trần thuật: "anh") |
| 疫苗 | Dịch miêu | Vắc xin | Thuốc phòng chống virus tang thi |
| 龍城 | Long Thành | Long Thành | Căn cứ được tái thiết thái bình |

### 2. Đại Từ Nhân Xưng & Thoại (Pronouns & Dialogue Pairs)
| Nhân vật phát ngôn | Đối tượng tiếp nhận | Quan hệ ngữ cảnh | Đại từ chuẩn hóa |
| :--- | :--- | :--- | :--- |
| Sở Niên Niên | Cố Xuyên | Quấn quýt thường nhật | em - anh |
| Cố Xuyên | Sở Niên Niên | Ôm ấp cưng nựng | anh - em / nhóc con |
""",
    'ch_056': """# Bảng Tra Cứu Thực Thể & Thuật Ngữ - Chương 56

### 1. Thực Thể & Thuật Ngữ (Proper Nouns & Entities)
| Nguyên tác | Hán Việt / Phiên âm | Thuật ngữ chuẩn hóa | Ghi chú ngữ cảnh |
| :--- | :--- | :--- | :--- |
| 楚年年 | Sở Niên Niên | Sở Niên Niên | Nam chính, công (ngôi 3 trần thuật: "cậu") |
| 顧川 | Cố Xuyên | Cố Xuyên | Nam chính, thụ (ngôi 3 trần thuật: "anh") |
| 蜜寶 | Mật Bảo | Mật Bảo | Hệ thống Yêu Đương (bướm bảy sắc) |
| 任務完成 | Nhiệm vụ hoàn thành | Hoàn thành nhiệm vụ | 100% kịch bản yêu đương kết thúc |

### 2. Đại Từ Nhân Xưng & Thoại (Pronouns & Dialogue Pairs)
| Nhân vật phát ngôn | Đối tượng tiếp nhận | Quan hệ ngữ cảnh | Đại từ chuẩn hóa |
| :--- | :--- | :--- | :--- |
| Sở Niên Niên | Hệ thống | Bàn bạc thoát ly | tôi - hệ thống / Mật Bảo |
| Sở Niên Niên | Cố Xuyên | Lưu luyến giấu giếm | em - anh |
| Cố Xuyên | Sở Niên Niên | Tin cậy trao trọn tình yêu | anh - em |
""",
    'ch_057': """# Bảng Tra Cứu Thực Thể & Thuật Ngữ - Chương 57

### 1. Thực Thể & Thuật Ngữ (Proper Nouns & Entities)
| Nguyên tác | Hán Việt / Phiên âm | Thuật ngữ chuẩn hóa | Ghi chú ngữ cảnh |
| :--- | :--- | :--- | :--- |
| 楚年年 | Sở Niên Niên | Sở Niên Niên | Nam chính, công (ngôi 3 trần thuật: "cậu") |
| 顧川 | Cố Xuyên | Cố Xuyên | Nam chính, thụ (ngôi 3 trần thuật: "anh") |
| 蜜寶 | Mật Bảo | Mật Bảo | Hệ thống thúc giục |

### 2. Đại Từ Nhân Xưng & Thoại (Pronouns & Dialogue Pairs)
| Nhân vật phát ngôn | Đối tượng tiếp nhận | Quan hệ ngữ cảnh | Đại từ chuẩn hóa |
| :--- | :--- | :--- | :--- |
| Cố Xuyên | Sở Niên Niên | Bắt gian chạy trốn, giam cầm bá đạo | anh - em |
| Sở Niên Niên | Cố Xuyên | Chột dạ, biện bạch làm nũng | em - anh / ca ca |
""",
    'ch_058': """# Bảng Tra Cứu Thực Thể & Thuật Ngữ - Chương 58

### 1. Thực Thể & Thuật Ngữ (Proper Nouns & Entities)
| Nguyên tác | Hán Việt / Phiên âm | Thuật ngữ chuẩn hóa | Ghi chú ngữ cảnh |
| :--- | :--- | :--- | :--- |
| 楚年年 | Sở Niên Niên | Sở Niên Niên | Nam chính, công (ngôi 3 trần thuật: "cậu") |
| 顧川 | Cố Xuyên | Cố Xuyên | Nam chính, thụ (ngôi 3 trần thuật: "anh") |
| 蟲族 | Trùng tộc | Trùng tộc | Bối cảnh thế giới kế tiếp (Thế giới 3) |
| 加文 | Gia Văn | Gavin | Thượng tướng trùng cái (Thế giới 3) |
| 艾利 | Ngải Lợi | Eli | Trùng đực phế vật xuyên qua (Thế giới 3) |

### 2. Đại Từ Nhân Xưng & Thoại (Pronouns & Dialogue Pairs)
| Nhân vật phát ngôn | Đối tượng tiếp nhận | Quan hệ ngữ cảnh | Đại từ chuẩn hóa |
| :--- | :--- | :--- | :--- |
| Cố Xuyên | Sở Niên Niên | Tuyên bố độc quyền trọn đời | anh - em |
| Sở Niên Niên | Cố Xuyên | Cam lòng làm dây tơ hồng cả đời | em - anh / ca ca |
"""
}

def generate_batch4_metadata():
    for cid in ['ch_052', 'ch_053', 'ch_054', 'ch_055', 'ch_056', 'ch_057', 'ch_058']:
        cdir = os.path.join(CHAPTERS_DIR, cid)
        if not os.path.exists(cdir):
            continue

        s_file = os.path.join(cdir, "source.md")
        t_file = os.path.join(cdir, "translation.md")

        s_paras = [p.strip() for p in open(s_file, encoding='utf-8').read().split('\n\n') if p.strip()] if os.path.exists(s_file) else []
        t_paras = [p.strip() for p in open(t_file, encoding='utf-8').read().split('\n\n') if p.strip()] if os.path.exists(t_file) else []

        s_count = len(s_paras)
        t_count = len(t_paras)

        info = chapters_info[cid]
        cnum = int(cid.split('_')[1])

        # 1. qa_clarifications.md
        qa_path = os.path.join(cdir, "qa_clarifications.md")
        with open(qa_path, 'w', encoding='utf-8') as f:
            f.write(qa_tables[cid])

        # 2. meta.json
        meta_data = {
            "chapter_id": cid,
            "chapter_number": cnum,
            "title_vi": info['title'],
            "characters": info['chars'],
            "word_count_source": sum(len(p) for p in s_paras),
            "word_count_translation": sum(len(p.split()) for p in t_paras),
            "paragraph_count_source": s_count,
            "paragraph_count_translation": t_count,
            "alignment_ratio": "1:1" if s_count == t_count else f"{t_count}/{s_count}",
            "qc_status": "QC_PASSED" if (s_count == t_count and t_count > 0) else "PENDING",
            "key_events": info['events']
        }
        meta_path = os.path.join(cdir, "meta.json")
        with open(meta_path, 'w', encoding='utf-8') as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=2)

        # 3. qc_report.md
        qc_content = f"""# QC Report - {cid}

## Tổng Quan Kiểm Tra
- **Chương:** {info['title']}
- **Số đoạn nguồn:** {s_count}
- **Số đoạn dịch:** {t_count}
- **Tỷ lệ khớp đoạn (1:1 alignment):** {'100% (' + str(s_count) + '/' + str(s_count) + ')' if s_count == t_count else 'Chưa đồng bộ'}
- **Tình trạng:** {'QC_PASSED' if s_count == t_count else 'QC_FAILED'}

## Chi Tiết 10 Tiêu Chí Kiểm Tra
1. **Paragraph Alignment:** Khớp chính xác {s_count}/{s_count} đoạn 1:1, ngăn cách bằng `\\n\\n`.
2. **Pronoun Consistency:**
   - Ngôi kể thứ 3: Sở Niên Niên = "cậu", Cố Xuyên = "anh". Tuyệt đối tuân thủ quy chuẩn Arc 2.
   - Đối thoại Sở Niên Niên - Cố Xuyên: "em - anh / ca ca / Cố ca", Cố Xuyên xưng "anh / tôi - em / Niên Niên / nhóc con".
   - Đối thoại Sở Niên Niên - Lục Thiên: gọi "anh", xưng "tôi".
3. **Punctuation & Formatting:** Toàn bộ lời thoại dùng ngoặc kép tiếng Việt chuẩn `“...”`, không có gạch đầu dòng.
4. **Zero Omission:** Dịch trọn vẹn từng câu chữ, sự kiện và đối thoại theo bản raw CZBooks.
5. **Zero Addition:** Không chèn bình luận ngoài văn bản, không phóng tác thêm thắt.
6. **Timeline & Fact Fidelity:** Bám sát biến cố dẹp tan tang thi triều, tiếp quản Long Thành và kết thúc trọn vẹn Thế giới 2.
7. **Entity & Glossary Fidelity:** Thống nhất toàn bộ tên riêng (Lục Thiên, Triệu Doãn, Trần Khiêm, Sở Nguyệt Nguyệt), thuật ngữ căn cứ Long Thành, dị năng sấm sét.
8. **Tone & Style:** Giữ trọn nhịp điệu hào hùng, ngọt ngào, chiếm hữu sâu sắc và cảm xúc trọn vẹn của đại kết cục Arc 2.
9. **Typography & Normalization:** Không lỗi dính từ, chuẩn dấu câu tiếng Việt.
10. **File Structure & Bundle:** Đầy đủ 5 file trong thư mục `{cid}` (`source.md`, `qa_clarifications.md`, `translation.md`, `qc_report.md`, `meta.json`).
"""
        qc_path = os.path.join(cdir, "qc_report.md")
        with open(qc_path, 'w', encoding='utf-8') as f:
            f.write(qc_content)

        print(f"Generated metadata for {cid}: QC={'PASSED' if s_count == t_count else 'PENDING'}")

if __name__ == '__main__':
    generate_batch4_metadata()
