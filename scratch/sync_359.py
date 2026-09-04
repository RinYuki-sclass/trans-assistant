import sys
import os
sys.path.insert(0, os.path.abspath("."))
from scripts.update_glossary import append_terms_to_sheet

terms = [
    {"chap": "359", "korean": "황림", "english": "Hwang Rim", "vietnamese": "Hoàng Lâm", "category": "Tên nhân vật", "note": "Thợ săn cấp S Trung Quốc"},
    {"chap": "359", "korean": "초화운", "english": "Cho Hwa-woon", "vietnamese": "Sở Hoa Vân", "category": "Tên nhân vật", "note": "Thợ săn cấp S Trung Quốc"},
    {"chap": "359", "korean": "운이", "english": "Woon-ie", "vietnamese": "A Vân", "category": "Tên nhân vật", "note": "Cách Hoàng Lâm gọi Sở Hoa Vân"},
    {"chap": "359", "korean": "관 낭자", "english": "Guan Lang-ja", "vietnamese": "Quan Nương Tử", "category": "Tên nhân vật", "note": "Nữ thợ săn cấp S Trung Quốc"},
    {"chap": "359", "korean": "수룡", "english": "Water Dragon", "vietnamese": "Thủy Long", "category": "Tên ma thú", "note": "Rồng nước ở bể nuôi"},
    {"chap": "359", "korean": "무림맹", "english": "Murim Alliance", "vietnamese": "Võ Lâm Minh", "category": "Địa điểm", "note": "Thế lực bang hội đối lập tại TQ"},
    {"chap": "359", "korean": "김 서방", "english": "Kim Seobang", "vietnamese": "đại ca Kim", "category": "Thuật ngữ", "note": "Dokkaebi gọi Yoojin"},
    {"chap": "359", "korean": "도깨비왕", "english": "Dokkaebi King", "vietnamese": "Vua Dokkaebi", "category": "Tên nhân vật", "note": "Danh hiệu của Yoon Yoon"}
]

if __name__ == "__main__":
    count, skipped = append_terms_to_sheet(terms, is_qc_flow=False)
    print(f"Done: added {count}, skipped: {skipped}")
