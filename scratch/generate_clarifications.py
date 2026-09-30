import glob
import json
import os
from datetime import datetime

dir_path = glob.glob('d:/Nhung/RIDI/trans-assistant/novel_projects/*khi*')[0]

mapping = {
    "楚司承": "Sở Tư Thừa",
    "Chu Si Cheng": "Sở Tư Thừa",
    "Chu Sicheng": "Sở Tư Thừa",
    "楚司承 (ngôi thứ 3)": "anh",
    "Chu Sicheng (ngôi thứ 3)": "anh",
    "瑞安": "Ryan",
    "Rui An": "Ryan",
    "瑞安 (ngôi thứ 3)": "cậu",
    "Rui An (ngôi thứ 3)": "cậu",
    "艾利克斯萨克森": "Alex Sachsen",
    "艾利克斯薩克森": "Alex Sachsen",
    "艾利克斯萨克森 (ngôi thứ 3)": "hắn",
    "艾利克斯薩克森 (ngôi thứ 3)": "hắn",
    "艾利克斯": "Alex",
    "Alex": "Alex",
    "艾利克斯 (ngôi thứ 3)": "hắn",
    "Alex (ngôi thứ 3)": "hắn",
    "萨克森将军": "Tướng quân Sachsen",
    "萨克森将军 (ngôi thứ 3)": "hắn",
    "费洛": "Felo",
    "Felo": "Felo",
    "費洛閣下": "Các hạ Felo",
    "费洛 (ngôi thứ 3)": "gã",
    "Felo (ngôi thứ 3)": "gã",
    "弗德里希": "Friedrich",
    "弗德裡希": "Friedrich",
    "Friedrich": "Friedrich",
    "弗德里希 (ngôi thứ 3)": "hắn",
    "Friedrich (ngôi thứ 3)": "hắn",
    "系统": "Hệ thống",
    "系统 (của Felo)": "Hệ thống",
    "系统 (của Chu Sicheng)": "Hệ thống",
    "系统 (ngôi thứ 3)": "nó",
    "系统 (của Felo) (ngôi thứ 3)": "nó",
    "系统 (của Chu Sicheng) (ngôi thứ 3)": "nó",
    "骷髅": "Hư ảnh đầu lâu",
    "骷髅头虚影": "Hư ảnh đầu lâu",
    "骷髅 (ngôi thứ 3)": "nó",
    "骷髅头虚影 (ngôi thứ 3)": "nó",
    "Bộ xương": "Hư ảnh đầu lâu",
    "Bộ xương (ngôi thứ 3)": "nó",
    "海德曼": "Heideman",
    "海德曼 (ngôi thứ 3)": "ông ta",
    "法官大人": "Đại pháp quan",
    "法官大人 (ngôi thứ 3)": "ông ta",
    "引导老师": "Giáo viên hướng dẫn",
    "引导老师 (ngôi thứ 3)": "người này",
    "闯入者": "Kẻ xông vào",
    "闯入者 (ngôi thứ 3)": "anh ta",
    "穿越者": "Kẻ xuyên không",
    "穿越者 (ngôi thứ 3)": "hắn",
    "姜黎": "Khương Lê",
    "姜黎 (ngôi thứ 3)": "hắn",
    "主角受對照組": "Nhóm đối chiếu của nhân vật thụ chính",
    "紋刀": "Văn đao",
}

for ch in ['ch_001', 'ch_002', 'ch_003', 'ch_004', 'ch_005']:
    analysis_file = f'{dir_path}/chapters/{ch}/analysis.json'
    if not os.path.exists(analysis_file):
        continue
    with open(analysis_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    ambiguous = data.get('ambiguous', [])
    answers = {}
    for amb in ambiguous:
        aid = amb.get('id')
        orig = amb.get('original', '').strip()
        opts = amb.get('options', [])
        choice = None
        # Check mapping
        if orig in mapping:
            choice = mapping[orig]
        elif 'ngôi thứ 3' in orig and ('楚司承' in orig or 'Chu Sicheng' in orig):
            choice = "anh"
        elif 'ngôi thứ 3' in orig and ('瑞安' in orig or 'Rui' in orig):
            choice = "cậu"
        elif 'ngôi thứ 3' in orig and ('艾利克斯' in orig or 'Alex' in orig or '弗德里希' in orig):
            choice = "hắn"
        elif 'ngôi thứ 3' in orig and '系统' in orig:
            choice = "nó"
        elif 'xưng' in amb.get('suggested', ''):
            choice = amb.get('suggested')
        else:
            choice = amb.get('suggested') or (opts[0] if opts else None)
        answers[aid] = {
            "choice": choice,
            "custom": None
        }

    clar_data = {
        "chapter_id": ch,
        "questions": ambiguous,
        "answers": answers,
        "answered_at": datetime.now().isoformat()
    }
    clar_file = f'{dir_path}/chapters/{ch}/clarifications.json'
    with open(clar_file, 'w', encoding='utf-8') as f:
        json.dump(clar_data, f, ensure_ascii=False, indent=2)
    print(f"Generated clarifications for {ch}: {len(answers)} answers")
