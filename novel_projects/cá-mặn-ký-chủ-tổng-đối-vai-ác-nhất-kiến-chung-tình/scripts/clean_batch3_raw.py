import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\cá-mặn-ký-chủ-tổng-đối-vai-ác-nhất-kiến-chung-tình\chapters"

garbage_keywords = [
    "推荐阅读", "亡灵法师他会治疗", "换嫁小夫郎", "虐主文的NPC消极怠工了",
    "嫁给铁哥们", "两界种田大亨", "恋爱脑重生日常", "穿越之家有赘婿",
    "海岛求生：生活玩家种田囤货", "改嫁京圈太子爷后，竹马们气疯了", "寡夫郎家的小酒楼",
    "咸鱼攻救赎反派boss指南 第", "document.write", "耽美小说", "搜索",
    "近代现代古代架空", "高分榜单", "function isMainlandChinaUser",
    "navigator.language", "timeZone", "Intl.DateTimeFormat",
    "isMainlandTZ", "return isZhCN", "function isMac", "navigator.platform",
    "navigator.userAgent", "vipmember", "vipread", "需要VIP权限", "history.back()",
    "404.html", "isgood", "首页 > 穿越重生", "作者：梅子清汤", "标签:",
    "强强", "情有独钟", "系统", "甜文", "快穿", "爽文", "穿越重生"
]

for c_num in range(21, 31):
    c_dir = os.path.join(base_dir, f"c{c_num}")
    src_path = os.path.join(c_dir, "source.md")
    meta_path = os.path.join(c_dir, "meta.json")
    
    if not os.path.exists(src_path):
        continue
        
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    paras = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]
    cleaned_paras = []
    
    for p in paras:
        # Nếu đoạn văn chứa bất kỳ keyword rác nào trên thì bỏ qua
        is_garbage = False
        # Nếu đoạn chỉ chứa đúng 1 tag hoặc là code
        for kw in garbage_keywords:
            if kw in p:
                is_garbage = True
                break
        if not is_garbage:
            cleaned_paras.append(p)
            
    clean_text = "\n\n".join(cleaned_paras) + "\n"
    with open(src_path, "w", encoding="utf-8") as f:
        f.write(clean_text)
        
    if os.path.exists(meta_path):
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        meta["paragraphs_count"] = len(cleaned_paras)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
            
    print(f"✅ c{c_num}: Đã dọn sạch -> Còn lại {len(cleaned_paras)} đoạn văn chuẩn")
