import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\cá-mặn-ký-chủ-tổng-đối-vai-ác-nhất-kiến-chung-tình\chapters"

titles_vi = {
    21: "Đêm khuya",
    22: "Thăm dò",
    23: "Lý sự cùn",
    24: "Theo đuổi",
    25: "Gốm sứ",
    26: "Tai nạn xe",
    27: "Hợp pháp",
    28: "Bầu không khí",
    29: "Cẩu huyết",
    30: "Quả cam"
}

for i in range(21, 31):
    meta_path = os.path.join(base_dir, f"c{i}", "meta.json")
    if os.path.exists(meta_path):
        with open(meta_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        data["status"] = "translated"
        data["title_vi"] = titles_vi.get(i, "")
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated c{i}/meta.json to status: translated, title_vi: {data['title_vi']}")
