#!/usr/bin/env python3
"""
Phân tích hệ thống tab trong rin_mode vs howl_mode
"""

MENU_ITEMS_RIN = [
    '🏠 Hướng Dẫn Rin Tool',
    '📖 Novel Workflow',
    '🤖 Novel Agent',
    '🎨 Truyện Tranh',
    '✂️ Cắt Ảnh',
    '🎧 Audio Converter',
    '📋 Reformat Script',
    '🌐 Đăng WordPress',
    '🔀 Ghép Xen Kẽ Song Ngữ',
    '🧹 Xóa Raw',
    '🦉 Howl Team Tracker'
]

TAB_NAMES_MAP_RIN = {
    0: '🏠 Hướng Dẫn Rin Tool',
    1: '📝 Dịch Thuật',
    2: '🔍 QC Review',
    3: '📊 So Sánh',
    4: '📖 Đối Chiếu',
    5: '🎨 Truyện Tranh',
    6: '📥 Tải Truyện',
    7: '📚 Glossary',
    8: '✂️ Cắt Ảnh',
    9: '📋 Reformat Script',
    10: '🔎 QC Diff',
    11: '🤖 Novel Agent',
    12: '🎧 Audio Converter',
    13: '🌐 Đăng WordPress',
    14: '📖 Novel Workflow',
    15: '🦉 Howl Team Tracker',
    16: '🔀 Ghép Xen Kẽ Song Ngữ',
    17: '📤 Nộp File Lên Drive',
    18: '🧹 Xóa Raw'
}

_tab_dict_keys = set(MENU_ITEMS_RIN)

print("=" * 60)
print("RIN MODE — STATUS CỦA TỪNG TAB INDEX")
print("=" * 60)
active_tabs = []
inactive_tabs = []

for idx in sorted(TAB_NAMES_MAP_RIN.keys()):
    name = TAB_NAMES_MAP_RIN[idx]
    active = name in _tab_dict_keys
    status = "✅ ACTIVE" if active else "❌ không hiển thị"
    print(f"  tabs.is_active({idx:2d}) = {status:20s} | '{name}'")
    if active:
        active_tabs.append(idx)
    else:
        inactive_tabs.append(idx)

print()
print("=" * 60)
print("CÁC TAB ĐƯỢC HIỂN THỊ TRONG RIN MODE:")
print("=" * 60)
for idx in active_tabs:
    name = TAB_NAMES_MAP_RIN[idx]
    # Find position in MENU_ITEMS
    pos = MENU_ITEMS_RIN.index(name) if name in MENU_ITEMS_RIN else -1
    print(f"  Tab #{idx} → Tab UI #{pos} '{name}'")

print()
print("=" * 60)
print("CÁC TAB KHÔNG HIỂN THỊ (Dùng st.container() làm fallback):")
print("=" * 60)
for idx in inactive_tabs:
    print(f"  Tab #{idx} | '{TAB_NAMES_MAP_RIN[idx]}'")

print()
print("=" * 60)
print("MENU ITEMS KHÔNG CÓ TAB CONTENT:")
print("=" * 60)
all_mapped = set(TAB_NAMES_MAP_RIN.values())
for name in MENU_ITEMS_RIN:
    if name not in all_mapped:
        print(f"  ORPHAN (no content): '{name}'")
