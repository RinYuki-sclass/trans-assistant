"""
Module chuyển đổi Hán-Việt & Từ điển Tag / Cụm từ Đam Mỹ Tấn Giang (JJWXC)
Hoạt động 100% Offline, tốc độ tức thì (< 0.1ms/câu), không gọi API ngoài.
"""
import os
import re
import json
from typing import Dict, List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANVIET_DICT_PATH = os.path.join(BASE_DIR, "data", "hanviet_dict.json")

_CHAR_MAP: Dict[str, str] = {}

# Từ điển Tag chuẩn của Tấn Giang (JJWXC) -> Tiếng Việt / Hán Việt chuẩn Đam Mỹ
JJWXC_TAG_MAP: Dict[str, str] = {
    "穿书": "Xuyên thư",
    "快穿": "Khoái xuyên",
    "甜文": "Điềm văn",
    "强强": "Cường cường",
    "爽文": "Sảng văn",
    "系统": "Hệ thống",
    "仙侠修真": "Tiên hiệp tu chân",
    "重生": "Trọng sinh",
    "正剧": "Chính kịch",
    "星际": "Tinh tế",
    "豪门世家": "Hào môn thế gia",
    "娱乐圈": "Giới giải trí",
    "升级流": "Thăng cấp lưu",
    "破镜重圆": "Phá kính trùng viên",
    "年下": "Niên hạ",
    "生子": "Sinh tử",
    "情有独钟": "Tình hữu độc chung",
    "天作之合": "Thiên tác chi hợp",
    "穿越时空": "Xuyên việt thời không",
    "无限流": "Vô hạn lưu",
    "末世": "Mạt thế",
    "机甲": "Cơ giáp",
    "虫族": "Trùng tộc",
    "ABO": "ABO",
    "打脸": "Vả mặt",
    "逆袭": "Nghịch tập",
    "轻松": "Nhẹ nhàng",
    "爆笑": "Bạo tiếu (Hài)",
    "沙雕": "Sa điêu (Lầy lội)",
    "治愈": "Chữa lành",
    "救赎": "Cứu rỗi",
    "暗恋": "Thầm mến",
    "先婚后爱": "Cưới trước yêu sau",
    "欢喜冤家": "Oan gia ngõ hẹp",
    "近水楼台": "Cận thủy lâu đài",
    "青梅竹马": "Thanh mai trúc mã",
    "竹马竹马": "Trúc mã trúc mã",
    "天之骄子": "Thiên chi kiêu tử",
    "业界精英": "Tinh anh trong ngành",
    "都市": "Đô thị",
    "都市情缘": "Đô thị tình duyên",
    "幻想空间": "Không gian ảo tưởng",
    "未来架空": "Tương lai giá không",
    "异世大陆": "Dị thế đại lục",
    "奇幻魔幻": "Kỳ ảo ma pháp",
    "灵异神怪": "Linh dị thần quái",
    "宫廷侯爵": "Cung đình hầu tước",
    "布衣生活": "Bố y sinh hoạt",
    "种田文": "Chủng điền văn",
    "美食": "Mỹ thực",
    "基建": "Làm giàu / Xây dựng",
    "竞技": "Cạnh kỹ (Thi đấu)",
    "游戏网游": "Võng du / Game",
    "全息": "Toàn tức (Thực tế ảo)",
    "直播": "Livestream",
    "网配": "Võng phối",
    "校园": "Vườn trường",
    "悬疑推理": "Huyền nghi phá án",
    "江湖": "Giang hồ",
    "三教九流": "Tam giáo cửu lưu",
    "朝堂": "Triều堂 (Chính trường)",
    "朝堂之上": "Chốn triều đường",
    "权谋": "Quyền mưu",
    "日常": "Đời thường",
    "团宠": "Đoàn sủng",
    "万人迷": "Vạn nhân mê",
    "炮灰": "Pháo hôi",
    "反派": "Phản diện",
    "白月光": "Bạch nguyệt quang",
    "替身": "Thế thân",
    "火葬场": "Hỏa táng tràng",
    "追爱火葬场": "Truy thê/truy phu hỏa táng tràng",
    "高岭之花": "Cao lãnh chi hoa",
    "美强惨": "Mỹ cường thảm",
    "龙傲天": "Long Ngạo Thiên",
    "马甲文": "Áo choàng (Mãnh giáp)",
    "失忆": "Mất trí nhớ",
    "萌宠": "Thú cưng đáng yêu",
    "玄学": "Huyền học",
    "赛博朋克": "Cyberpunk",
    "废土": "Phế thổ",
    "克苏鲁": "Cthulhu",
    "规则怪谈": "Quy tắc quái đàm",
    "哨向": "Lính gác - Dẫn đường",
    "第四天灾": "Đệ tứ thiên tai",
    "群像": "Quần tượng",
    "单元文": "Đơn nguyên văn",
    "读心术": "Thuật đọc tâm",
    "忠犬": "Trung khuyển",
    "傲娇": "Ngạo kiều",
    "腹黑": "Phúc hắc",
    "毒舌": "Độc miệng",
    "高冷": "Cao lãnh",
    "禁欲": "Cấm dục",
    "病娇": "Bệnh kiều",
    "疯批": "Điên phê",
    "切片": "Cắt lát (Thiết phiến)",
    "日久生情": "Lửa gần rơm lâu ngày cũng bén",
    "相爱相杀": "Tương ái tương sát",
    "强取豪夺": "Cường thủ hào đoạt",
    "虐文": "Ngược văn",
    "悲剧": "Bi kịch",
    "HE": "HE",
    "BE": "BE",
    "1V1": "1v1",
}

# Cụm từ thông dụng trong tiêu đề truyện Đam Mỹ Xuyên Thư giúp tiêu đề dễ hiểu ngay lập tức
TITLE_PHRASE_MAP: List[tuple] = [
    ("穿进总受文的炮灰和正牌攻1v1了", "Xuyên Vào Pháo Hôi Truyện Tổng Thụ Và Chính Bài Công 1v1"),
    ("伪装直男", "Ngụy Trang Trai Thẳng"),
    ("穿书后", "Sau Khi Xuyên Thư"),
    ("穿书之", "Xuyên Thư Chi "),
    ("［穿书］", " [Xuyên Thư]"),
    ("[穿书]", " [Xuyên Thư]"),
    ("（穿书）", " (Xuyên Thư)"),
    ("(穿书)", " (Xuyên Thư)"),
    ("［快穿］", " [Khoái Xuyên]"),
    ("[快穿]", " [Khoái Xuyên]"),
    ("（快穿）", " (Khoái Xuyên)"),
    ("(快穿)", " (Khoái Xuyên)"),
    ("主角攻", "Nhân Vật Chính Công"),
    ("主角受", "Nhân Vật Chính Thụ"),
    ("正牌攻", "Chính Bài Công"),
    ("正牌受", "Chính Bài Thụ"),
    ("炮灰攻", "Pháo Hôi Công"),
    ("炮灰受", "Pháo Hôi Thụ"),
    ("渣攻", "Tra Công"),
    ("贱受", "Tiện Thụ"),
    ("总受", "Tổng Thụ"),
    ("总攻", "Tổng Công"),
    ("直男", "Trai Thẳng"),
    ("万人迷", "Vạn Nhân Mê"),
    ("白月光", "Bạch Nguyệt Quang"),
    ("朱砂痣", "Chu Sa Chí"),
    ("火葬场", "Hỏa Táng Tràng"),
    ("龙傲天", "Long Ngạo Thiên"),
    ("高岭之花", "Cao Lãnh Chi Hoa"),
    ("美强惨", "Mỹ Cường Thảm"),
    ("小可怜", "Tiểu Đáng Thương"),
    ("工具人", "Người Công Cụ"),
    ("反派", "Phản Diện"),
    ("炮灰", "Pháo Hôi"),
    ("恶毒男配", "Nam Phụ Độc Ác"),
    ("男配", "Nam Phụ"),
    ("男主", "Nam Chính"),
    ("女主", "Nữ Chính"),
    ("主角", "Nhân Vật Chính"),
    ("路人甲", "Người Qua Đường Giáp"),
    ("路人", "Người Qua Đường"),
    ("师尊", "Sư Tôn"),
    ("师兄", "Sư Huynh"),
    ("师弟", "Sư Đệ"),
    ("师叔", "Sư Thúc"),
    ("师父", "Sư Phụ"),
    ("徒弟", "Đồ Đệ"),
    ("仙尊", "Tiên Tôn"),
    ("魔尊", "Ma Tôn"),
    ("暴君", "Bạo Quân"),
    ("太子", "Thái Tử"),
    ("摄政王", "Nhiếp Chính Vương"),
    ("皇帝", "Hoàng Đế"),
    ("霸总", "Bá Tổng"),
    ("总裁", "Tổng Tài"),
    ("大佬", "Đại Lão"),
    ("金主", "Kim Chủ"),
    ("替身", "Thế Thân"),
    ("前夫", "Chồng Trước"),
    ("前男友", "Bạn Trai Cũ"),
    ("死对头", "Đối Đầu"),
    ("宿敌", "Túc Địch"),
    ("竹马", "Trúc Mã"),
    ("天菜", "Thiên Thái"),
    ("雄虫", "Hùng Trùng"),
    ("雌虫", "Thư Trùng"),
    ("虫族", "Trùng Tộc"),
    ("哨兵", "Lính Gác"),
    ("向导", "Dẫn Đường"),
    ("信息素", "Tin Tức Tố"),
    ("标记", "Đánh Dấu"),
    ("恋爱脑", "Não Yêu Đương"),
    ("修真界", "Tu Chân Giới"),
    ("修仙界", "Tu Tiên Giới"),
    ("娱乐圈", "Giới Giải Trí"),
    ("恋综", "Show Hẹn Hò"),
    ("直播", "Livestream"),
    ("穿成", "Xuyên Thành "),
    ("穿进", "Xuyên Vào "),
    ("重生", "Trọng Sinh "),
    ("拯救", "Cứu Rỗi "),
    ("攻略", "Công Lược "),
    ("绑定", "Trói Định "),
    ("系统", "Hệ Thống "),
    ("剧本", "Kịch Bản "),
    ("人设", "Thiết Lập "),
    ("崩了", "Sụp Đổ Rồi"),
    ("怎么办", "Phải Làm Sao"),
    ("的日子", "Những Ngày "),
    ("指南", "Chỉ Nam"),
    ("手册", "Sổ Tay"),
    ("日常", "Đời Thường"),
]

# Các dấu hiệu nhận diện truyện Khoái Xuyên ẩn (dù tác giả không gắn tag 快穿)
QUICK_TRANS_INDICATORS = [
    "快穿",
    "慢穿",
    "穿成各个世界",
    "第一个世界",
    "第二个世界",
    "第三个世界",
    "世界一：",
    "世界二：",
    "世界三：",
    "世界1：",
    "世界2：",
    "暂定世界",
    "小世界",
    "任务世界",
    "位面",
    "单元剧快穿",
]


def _load_char_map():
    global _CHAR_MAP
    if _CHAR_MAP:
        return
    if os.path.exists(HANVIET_DICT_PATH):
        try:
            with open(HANVIET_DICT_PATH, "r", encoding="utf-8") as f:
                _CHAR_MAP = json.load(f)
        except Exception:
            _CHAR_MAP = {}


def to_hanviet(text: str, capitalize_words: bool = True) -> str:
    """
    Chuyển chuỗi tiếng Trung sang phiên âm Hán-Việt chuẩn.
    """
    if not text:
        return ""
    _load_char_map()

    punct_map = {
        "《": "«",
        "》": "»",
        "【": "[",
        "】": "]",
        "［": "[",
        "］": "]",
        "（": "(",
        "）": ")",
        "，": ", ",
        "。": ". ",
        "！": "! ",
        "？": "? ",
        "：": ": ",
        "；": "; ",
        "、": ", ",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
    }

    tokens: List[str] = []
    ascii_buf: List[str] = []

    def flush_ascii():
        if ascii_buf:
            s = "".join(ascii_buf).strip()
            if s:
                tokens.append(s)
            ascii_buf.clear()

    for ch in text:
        if ch in punct_map:
            flush_ascii()
            tokens.append(punct_map[ch])
        elif ch in _CHAR_MAP:
            flush_ascii()
            hv = _CHAR_MAP[ch]
            if capitalize_words and hv:
                hv = hv.capitalize()
            tokens.append(hv)
        elif "\u4e00" <= ch <= "\u9fff":
            flush_ascii()
            tokens.append(ch)
        else:
            ascii_buf.append(ch)

    flush_ascii()

    out = " ".join(tokens)
    out = re.sub(r"\s+([,.:;!?\]»)])", r"\1", out)
    out = re.sub(r"([\[«(])\s+", r"\1", out)
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out


def to_smart_title_vi(title_cn: str) -> str:
    """
    Chuyển tên truyện sang dạng Hán-Việt kết hợp cụm từ tiếng Việt thông dụng
    để người đọc nhận diện ngay ý nghĩa tên truyện.
    """
    if not title_cn:
        return ""
    work = title_cn
    for cn_phrase, vi_phrase in TITLE_PHRASE_MAP:
        if cn_phrase in work:
            work = work.replace(cn_phrase, f" {vi_phrase} ")
    return to_hanviet(work, capitalize_words=True)


def translate_tag(tag_cn: str) -> str:
    """
    Dịch tag Tấn Giang sang dạng chuẩn tiếng Việt + gốc Trung: VD '穿书' -> 'Xuyên thư (穿书)'
    hoặc trả về tên tiếng Việt ngắn gọn.
    """
    tag_cn = (tag_cn or "").strip()
    if not tag_cn:
        return ""
    if tag_cn in JJWXC_TAG_MAP:
        return JJWXC_TAG_MAP[tag_cn]
    return to_hanviet(tag_cn, capitalize_words=True)


def translate_category(cat_cn: str) -> str:
    """
    Dịch chuỗi phân loại của JJWXC: VD '原创-纯爱-近代现代-爱情-主攻' -> 'Nguyên sang - Thuần ái - Hiện đại - Tình cảm - Chủ công'
    """
    if not cat_cn:
        return ""
    part_map = {
        "原创": "Nguyên sang",
        "衍生": "Diễn sinh",
        "纯爱": "Thuần ái",
        "言情": "Ngôn tình",
        "无CP": "Vô CP",
        "百合": "Bách hợp",
        "多元": "Đa nguyên",
        "近代现代": "Hiện đại",
        "古色古香": "Cổ đại",
        "架空历史": "Giá không lịch sử",
        "幻想未来": "Ảo tưởng tương lai",
        "爱情": "Tình cảm",
        "仙侠": "Tiên hiệp",
        "奇幻": "Kỳ ảo",
        "科幻": "Khoa học viễn tưởng",
        "游戏": "Võng du/Game",
        "悬疑": "Huyền nghi",
        "剧情": "Cốt truyện",
        "轻小说": "Light Novel",
        "武侠": "Võ hiệp",
        "传奇": "Truyền kỳ",
        "主攻": "Chủ công",
        "主受": "Chủ thụ",
        "互攻": "Hỗ công",
        "双视角": "Song thị giác",
    }
    parts = [p.strip() for p in cat_cn.split("-") if p.strip()]
    translated = [part_map.get(p, to_hanviet(p)) for p in parts]
    return " • ".join(translated)


def detect_is_quick_trans(title_cn: str, tags: List[str], short_desc: str = "", full_desc: str = "") -> bool:
    """
    Kiểm tra truyện có phải Khoái Xuyên hay không:
    1. Có tag '快穿' trong danh sách tag
    2. Hoặc tiêu đề / văn án chứa từ khóa nhận diện Khoái xuyên ('[快穿]', '第一个世界', '世界一：'...)
    """
    if "快穿" in (tags or []):
        return True
    combined = f"{title_cn or ''}\n{short_desc or ''}\n{full_desc or ''}"
    for kw in QUICK_TRANS_INDICATORS:
        if kw in combined:
            return True
    return False


def detect_is_sweet(tags: List[str], desc_text: str = "") -> bool:
    """
    Kiểm tra truyện có gắn các tag bị loại bỏ vĩnh viễn:
    - Điềm văn ('甜文', '甜宠文', '甜宠', '小甜饼', '无虐甜文')
    - Chủng điền ('种田文', '种田')
    - Mỹ thực ('美食', '美食文')
    """
    banned_tags = {"甜文", "甜宠文", "甜宠", "小甜饼", "无虐甜文", "种田文", "种田", "美食", "美食文"}
    for t in (tags or []):
        if t in banned_tags:
            return True
    if desc_text:
        for kw in ("小甜饼", "甜宠文", "无虐甜文", "1v1甜文", "主攻甜文", "种田文", "美食文"):
            if kw in desc_text:
                return True
    return False
