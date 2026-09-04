import os

BASE_DIR = r"d:\Nhung\RIDI\trans-assistant"
time_path = os.path.join(BASE_DIR, 'memory', 'timeline_summary.md')

def append_timeline_entry(chap_id, title, location, plot, status):
    entry = f"\n\n### [{chap_id}] {title}\n- **Địa điểm & Bối cảnh:** {location}\n- **Diễn biến chính:** {plot}\n- **Trạng thái nhân vật:** {status}"
    return entry

sample = append_timeline_entry("Chap 327", "Hồi kết", "Hồ bơi", "Yoojin tìm cách liên lạc Dokkaebi", "Chân Yoojin gãy, cần nạng")
assert "Chap 327" in sample
print("Timeline entry helper test passed!")
