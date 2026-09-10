import gspread
import os
import json
import pandas as pd
import sys
import argparse

# Đảm bảo output hỗ trợ UTF-8
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LOCAL_SERVICE_ACCOUNT_PATH = "service-account.json"
LOCAL_SHEET_URL = "https://docs.google.com/spreadsheets/d/1Rm6BLnW6yj019GMLHxxsQGDYCHQdz8z-cALrmdCfdro/edit?usp=sharing"

def get_sheet_connection():
    """Khởi tạo kết nối gspread tới Google Spreadsheet."""
    service_account_str = os.environ.get("GOOGLE_SERVICE_ACCOUNT")
    sheet_url = os.environ.get("GOOGLE_SHEET_URL") or LOCAL_SHEET_URL
    
    if os.path.exists(LOCAL_SERVICE_ACCOUNT_PATH):
        gc = gspread.service_account(filename=LOCAL_SERVICE_ACCOUNT_PATH)
    elif service_account_str:
        service_account_info = json.loads(service_account_str)
        gc = gspread.service_account_from_dict(service_account_info)
    else:
        raise ValueError("Thiếu file xác thực service-account.json hoặc biến môi trường GOOGLE_SERVICE_ACCOUNT.")
        
    sh = gc.open_by_url(sheet_url)
    return gc, sh

def update_glossary():
    """Tải dữ liệu từ Google Sheets về file local glossary/glossary.md (Chiều Tải)."""
    print("[INFO] Đang tải dữ liệu từ Google Sheets về local...")
    try:
        _, sh = get_sheet_connection()
        print(f"[OK] Đã kết nối thành công với: {sh.title}")
        
        output_md = 'glossary/glossary.md'
        os.makedirs('glossary', exist_ok=True)

        with open(output_md, 'w', encoding='utf-8') as f:
            f.write("# TAI LIEU THAM KHAO DICH THUAT\n\n")

            def get_ws(name):
                try:
                    return sh.worksheet(name)
                except:
                    for w in sh.worksheets():
                        if w.title.lower().strip() == name.lower().strip():
                            return w
                    return None

            # --- 1. XỬ LÝ SHEET XƯNG HÔ ---
            print("- Đang xử lý sheet 'Xưng hô'...")
            ws_xh = get_ws("Xưng hô")
            if ws_xh:
                try:
                    data_xh = ws_xh.get_all_values()
                    df_xh = pd.DataFrame(data_xh[1:], columns=data_xh[0])
                    df_xh.set_index(df_xh.columns[0], inplace=True)
                    
                    f.write("## 1. QUY TAC XUNG HO\n")
                    
                    # Gom nhóm đại từ khi kể chuyện (Third-person)
                    narration_pronouns = []
                    for name in df_xh.index:
                        if name in df_xh.columns:
                            val = df_xh.loc[name, name]
                            if val and str(val).strip() and val != '-':
                                narration_pronouns.append(f"{name}: {val}")
                    
                    if narration_pronouns:
                        f.write("### Dai tu khi ke chuyen (Ngoi thu 3):\n")
                        f.write(", ".join(narration_pronouns) + "\n\n")

                    f.write("### Cách gọi nhau trong đối thoại (Ngôi 1 gọi Ngôi 2):\n")
                    for speaker in df_xh.index:
                        for listener in df_xh.columns:
                            if speaker == listener: continue
                            call_name = str(df_xh.loc[speaker, listener]).strip()
                            if call_name and call_name != '-' and call_name.lower() != 'nan':
                                lines_raw = call_name.split('\n')
                                processed_lines = []
                                for ln in lines_raw:
                                    ln = ln.strip()
                                    if not ln:
                                        continue
                                    if ' - ' in ln:
                                        parts = ln.split(' - ', 1)
                                        processed_lines.append(f"xưng {parts[0].strip()} gọi {parts[1].strip()}")
                                    elif '-' in ln:
                                        parts = ln.split('-', 1)
                                        processed_lines.append(f"xưng {parts[0].strip()} gọi {parts[1].strip()}")
                                    else:
                                        processed_lines.append(ln)
                                final_call = ", ".join(processed_lines)
                                f.write(f"- {speaker} gọi {listener} là: {final_call}\n")
                    f.write("\n")
                except Exception as e: print(f"Lỗi sheet Xưng hô: {e}")

            # --- 2. XỬ LÝ SHEET NHÂN VẬT ---
            print("- Đang xử lý sheet 'Nhân vật'...")
            ws_nv = get_ws("Nhân vật")
            if ws_nv:
                try:
                    data_nv = ws_nv.get_all_values()
                    if len(data_nv) > 1:
                        df_nv = pd.DataFrame(data_nv[1:], columns=data_nv[0])
                        f.write("## 2. THONG TIN NHAN VAT\n")
                        for _, row in df_nv.iterrows():
                            ten = str(row.get('Tên', '')).strip()
                            tuoi = str(row.get('Tuổi', '')).strip()
                            ghi_chu = str(row.get('Ghi chú', '')).strip()
                            sk_raw = str(row.get('Skill (raw)', '')).strip()
                            sk_eng = str(row.get('Skill (eng)', '')).strip()
                            sk_vn = str(row.get('Skill (vn)', '')).strip()
                            
                            if ten and ten != 'nan' and ten != '':
                                line = f"- {ten}"
                                if tuoi and tuoi != 'nan': line += f" ({tuoi} tuổi)"
                                if ghi_chu and ghi_chu != 'nan': line += f": {ghi_chu}"
                                
                                skills = []
                                if sk_raw and sk_raw != 'nan': skills.append(sk_raw)
                                if sk_eng and sk_eng != 'nan': skills.append(sk_eng)
                                if sk_vn and sk_vn != 'nan': skills.append(f"-> {sk_vn}")
                                
                                if skills:
                                    line += " [Skill: " + " / ".join(skills) + "]"
                                
                                f.write(line + "\n")
                        f.write("\n")
                except Exception as e: print(f"Lỗi sheet Nhân vật: {e}")

            # --- 3. XỬ LÝ SHEET THUẬT NGỮ (PHÂN TẦNG QC-CHỐT VÀ THEO THỨ TỰ CHAP) ---
            print("- Đang xử lý sheet 'Thuật ngữ chi tiết'...")
            ws_tn = get_ws("Thuật ngữ chi tiết")
            if ws_tn:
                try:
                    data_tn = ws_tn.get_all_values()
                    if len(data_tn) > 1:
                        df_tn = pd.DataFrame(data_tn[1:], columns=data_tn[0])
                        f.write("## 3. THUAT NGU VA TEN RIENG (SAP XEP THEO THU TU CHAP)\n")
                        f.write("> 💡 **Quy tắc thứ tự Chap:** Khi dịch hoặc QC cho Chap N, hệ thống sẽ ưu tiên tối đa các thuật ngữ có Chap <= N đã được QC Chốt.\n\n")
                        
                        official_terms = []
                        draft_terms = []
                        
                        for _, row in df_tn.iterrows():
                            chap = str(row.get('Chap', '')).strip()
                            han = str(row.get('Tiếng hàn', '')).strip()
                            anh = str(row.get('Tiếng anh', '')).strip()
                            dich = str(row.get('Dịch', '')).strip()
                            cat = str(row.get('Phân loại', '')).strip()
                            chot = str(row.get('Chốt', '')).strip().upper()
                            note = str(row.get('Ghi chú', '')).strip()
                            
                            if not han and not anh and not dich:
                                continue
                                
                            chap_prefix = f"[Chap {chap}] " if chap and chap != 'nan' else ""
                            cat_tag = f" ({cat})" if cat and cat != 'nan' else ""
                            note_tag = f" - {note}" if note and note != 'nan' else ""
                            
                            term_line = f"- {chap_prefix}{han} | {anh} -> {dich}{cat_tag}{note_tag}"
                            
                            if chot == "TRUE":
                                official_terms.append((chap, term_line))
                            else:
                                draft_terms.append((chap, term_line))
                                
                        # Sắp xếp thuật ngữ theo thứ tự số của Chap (tăng dần)
                        def parse_chap_num(c_str):
                            try:
                                import re
                                m = re.search(r'\d+', str(c_str))
                                return int(m.group()) if m else 999999
                            except:
                                return 999999
                                
                        official_terms.sort(key=lambda x: parse_chap_num(x[0]))
                        draft_terms.sort(key=lambda x: parse_chap_num(x[0]))
                                
                        if official_terms:
                            f.write("### 3.1. Thuật ngữ Chính thức (Đã qua QC duyệt - Chốt = TRUE):\n")
                            for _, line in official_terms:
                                f.write(line + "\n")
                            f.write("\n")
                            
                        if draft_terms:
                            f.write("### 3.2. Thuật ngữ Dự thảo (Do Trans tạm đặt ở các chap đi trước - Chờ QC duyệt):\n")
                            for _, line in draft_terms:
                                f.write(line + "\n")
                            f.write("\n")
                except Exception as e: print(f"Lỗi sheet Thuật ngữ: {e}")


        print(f"[OK] Đã cập nhật thành công {output_md} từ Google Sheets!")
        return True

    except Exception as e:
        import traceback
        print(f"[ERROR] Lỗi khi kết nối Google Sheets: {e}")
        traceback.print_exc()
        return False

VALID_CATEGORIES = ['Tên nhân vật', 'Tên ma thú', 'Tên title/skill', 'Tên vật phẩm', 'Địa điểm', 'Thuật ngữ']

def normalize_category(cat_str: str) -> str:
    """Chuẩn hóa phân loại về đúng 6 danh mục chuẩn của Google Sheet."""
    c = str(cat_str).lower().strip()
    if any(k in c for k in ['nhân vật', 'người', 'thợ săn', 'hunter']):
        return 'Tên nhân vật'
    if any(k in c for k in ['ma thú', 'thú', 'quái', 'beast', 'monster', 'rồng']):
        return 'Tên ma thú'
    if any(k in c for k in ['skill', 'kỹ năng', 'title', 'danh hiệu', 'chiêu']):
        return 'Tên title/skill'
    if any(k in c for k in ['vật phẩm', 'item', 'vũ khí', 'trang bị', 'thuốc']):
        return 'Tên vật phẩm'
    if any(k in c for k in ['địa điểm', 'địa danh', 'dungeon', 'hầm ngục', 'rừng', 'núi', 'thành phố']):
        return 'Địa điểm'
    return 'Thuật ngữ'

def append_terms_to_sheet(terms: list[dict], is_qc_flow: bool = True, auto_sync_local: bool = True):
    """
    Đẩy danh sách thuật ngữ mới lên Google Sheet 'Thuật ngữ chi tiết' (Chiều Ghi).
    
    QUY TẮC BẢO VỆ DỮ LIỆU & THỨ TỰ CHAP:
    - Bất kỳ dòng nào có 'Chốt' = 'TRUE' đều là BẤT KHẢ XÂM PHẠM (không được sửa đổi).
    - Phân định rõ:
        + Nếu ghi từ QC Flow (is_qc_flow=True): Đặt Chốt = 'TRUE' (Khóa chính thức).
        + Nếu ghi từ Trans Flow (is_qc_flow=False): Đặt Chốt = 'FALSE' (Dự thảo chờ QC).
    - Tự động điền tiếp vào dòng trống đầu tiên (ví dụ dòng 601).
    - Tự động sắp xếp (Sort) lại bảng theo số thứ tự Chap tăng dần.
    """
    if not terms:
        print("[INFO] Danh sách thuật ngữ trống, bỏ qua.")
        return 0, []

    print(f"[INFO] Đang xử lý {len(terms)} thuật ngữ (QC flow: {is_qc_flow}) để đối chiếu và đẩy lên Google Sheets...")
    try:
        _, sh = get_sheet_connection()
        ws = sh.worksheet("Thuật ngữ chi tiết")
        
        all_vals = ws.get_all_values()
        
        # 1. Quét danh sách đã Chốt (Chốt == TRUE) và tìm dòng trống đầu tiên
        locked_kr = {}
        locked_vn = {}
        existing_kr = {}
        existing_vn = {}
        first_empty_row_idx = None  # 1-indexed
        
        for row_idx, r in enumerate(all_vals[1:], start=2):
            kr = r[1].strip() if len(r) > 1 else ""
            en = r[2].strip() if len(r) > 2 else ""
            vn = r[3].strip() if len(r) > 3 else ""
            chot = r[5].strip().upper() if len(r) > 5 else "FALSE"
            
            # Kiểm tra dòng trống thực sự (cả tiếng Hàn, tiếng Anh, Dịch đều trống)
            if not kr and not en and not vn:
                if first_empty_row_idx is None:
                    first_empty_row_idx = row_idx
                continue
            
            # Ghi nhận trạng thái đã Chốt
            if chot == "TRUE":
                if kr: locked_kr[kr.lower()] = row_idx
                if vn: locked_vn[vn.lower()] = row_idx
            else:
                if kr: existing_kr[kr.lower()] = row_idx
                if vn: existing_vn[vn.lower()] = row_idx

        if first_empty_row_idx is None:
            first_empty_row_idx = len(all_vals) + 1

        print(f"- Dòng trống đầu tiên để điền thuật ngữ mới: Dòng {first_empty_row_idx}")

        rows_to_insert = []
        skipped = []
        
        for item in terms:
            kr = str(item.get("korean", "")).strip()
            en = str(item.get("english", "")).strip()
            vn = str(item.get("vietnamese", "")).strip()
            chap = str(item.get("chap", "")).strip()
            cat = normalize_category(item.get("category", "Thuật ngữ"))
            note = str(item.get("note", "")).strip()

            if not kr and not vn:
                continue

            # NGUYÊN TẮC: Row có Chốt = TRUE tuyệt đối KHÔNG ĐƯỢC MODIFY
            if kr and kr.lower() in locked_kr:
                row_lock = locked_kr[kr.lower()]
                skipped.append(f"[ĐÃ CHỐT] '{kr}' (Dòng {row_lock}) - Không được phép sửa đổi")
                continue
            if vn and vn.lower() in locked_vn:
                row_lock = locked_vn[vn.lower()]
                skipped.append(f"[ĐÃ CHỐT] '{vn}' (Dòng {row_lock}) - Không được phép sửa đổi")
                continue

            # Tránh trùng lặp cả với các từ chưa chốt
            if (kr and kr.lower() in existing_kr) or (vn and vn.lower() in existing_vn):
                skipped.append(f"[ĐÃ CÓ] '{kr or vn}' - Đã tồn tại trong danh sách chờ duyệt")
                continue

            # Cột: ['Chap', 'Tiếng hàn', 'Tiếng anh', 'Dịch', 'Phân loại', 'Chốt', 'Ghi chú', 'Văn mẫu hệ thống']
            chot_status = True if is_qc_flow else False
            new_row = [chap, kr, en, vn, cat, chot_status, note, ""]
            rows_to_insert.append(new_row)
            
            if kr: existing_kr[kr.lower()] = first_empty_row_idx + len(rows_to_insert) - 1
            if vn: existing_vn[vn.lower()] = first_empty_row_idx + len(rows_to_insert) - 1

        if rows_to_insert:
            start_row = first_empty_row_idx
            end_row = first_empty_row_idx + len(rows_to_insert) - 1
            range_to_update = f"A{start_row}:H{end_row}"
            
            ws.update(values=rows_to_insert, range_name=range_to_update, value_input_option="USER_ENTERED")
            print(f"[OK] Đã điền thành công {len(rows_to_insert)} dòng mới vào vị trí {range_to_update}!")

            # Đảm bảo cột F luôn hiển thị dạng Checkbox chuẩn và căn giữa
            try:
                sh.batch_update({
                    "requests": [
                        {
                            "setDataValidation": {
                                "range": {
                                    "sheetId": ws.id,
                                    "startRowIndex": start_row - 1,
                                    "endRowIndex": end_row,
                                    "startColumnIndex": 5,
                                    "endColumnIndex": 6
                                },
                                "rule": {
                                    "condition": {
                                        "type": "BOOLEAN"
                                    },
                                    "showCustomUi": True
                                }
                            }
                        },
                        {
                            "repeatCell": {
                                "range": {
                                    "sheetId": ws.id,
                                    "startRowIndex": start_row - 1,
                                    "endRowIndex": end_row,
                                    "startColumnIndex": 5,
                                    "endColumnIndex": 6
                                },
                                "cell": {
                                    "userEnteredFormat": {
                                        "horizontalAlignment": "CENTER"
                                    }
                                },
                                "fields": "userEnteredFormat.horizontalAlignment"
                            }
                        }
                    ]
                })
            except Exception as e_chk:
                print(f"[WARN] Không thể gán format Checkbox tự động: {e_chk}")

            # Tự động sắp xếp lại theo cột Chap (Cột A) tăng dần
            try:
                ws.sort((1, 'asc'), range=f"A2:H{end_row}")
                print(f"[OK] Đã tự động sắp xếp lại Google Sheet theo thứ tự Chap tăng dần (A2:H{end_row})!")
            except Exception as e_sort:
                print(f"[WARN] Không thể tự động sort trên Google Sheet: {e_sort}")
            
            if auto_sync_local:
                print("[INFO] Đang tự động kéo dữ liệu mới về local glossary/glossary.md...")
                update_glossary()
        else:
            print("[INFO] Không có thuật ngữ mới nào cần ghi.")

        if skipped:
            print("\n[BẢO VỆ DỮ LIỆU & BỎ QUA]:")
            for msg in skipped[:10]:
                print(f"  * {msg}")

        return len(rows_to_insert), skipped

    except Exception as e:
        import traceback
        print(f"[ERROR] Không thể ghi lên Google Sheets: {e}")
        print("💡 Lưu ý: Hãy chắc chắn email 's-class@s-class-488908.iam.gserviceaccount.com' đã được cấp quyền 'Editor' trên Google Sheet.")
        traceback.print_exc()
        return 0, []

def filter_glossary_content(glossary_text: str, max_chap: int = None, search_keywords: list = None) -> str:
    """
    Lọc nội dung glossary.md để chống tràn token (overflow) khi nạp vào LLM Prompt.
    - Luôn bảo toàn Phần 1 (Xưng hô) và Phần 2 (Nhân vật).
    - Phần 3.1: Chỉ nạp các thuật ngữ có Chap <= max_chap.
    - Phần 3.2: Lọc các thuật ngữ dự thảo theo từ khóa thực tế hoặc tinh giản.
    """
    if not glossary_text or (max_chap is None and not search_keywords):
        return glossary_text

    import re
    lines = glossary_text.split('\n')
    filtered_lines = []
    current_section = None

    for line in lines:
        if line.startswith('## 1.') or line.startswith('## 2.'):
            current_section = 'header'
            filtered_lines.append(line)
            continue
        elif line.startswith('### 3.1.'):
            current_section = 'official'
            filtered_lines.append(line)
            continue
        elif line.startswith('### 3.2.'):
            current_section = 'draft'
            filtered_lines.append(line)
            continue
        elif line.startswith('## '):
            current_section = 'other'
            filtered_lines.append(line)
            continue

        if current_section in ['header', 'other', None]:
            filtered_lines.append(line)
        elif current_section == 'official':
            if line.startswith('- [Chap '):
                m = re.search(r'\[Chap\s+(\d+)\]', line)
                if m and max_chap is not None:
                    ch_num = int(m.group(1))
                    if ch_num > max_chap:
                        continue
            filtered_lines.append(line)
        elif current_section == 'draft':
            if search_keywords and line.startswith('- '):
                line_lower = line.lower()
                if not any(kw.lower() in line_lower for kw in search_keywords if len(kw) > 1):
                    continue
            filtered_lines.append(line)

    return '\n'.join(filtered_lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Sheets Glossary Sync Tool (2-way)")
    parser.add_argument("--sync", action="store_true", help="Tải toàn bộ từ Google Sheets về local glossary.md")
    parser.add_argument("--append", type=str, help="JSON chuỗi hoặc file chứa danh sách terms để đẩy lên Google Sheets")
    parser.add_argument("--trans-flow", action="store_true", help="Ghi từ luồng Trans (đặt Chốt=FALSE thay vì TRUE)")
    
    args = parser.parse_args()

    if args.append:
        raw_input = args.append.strip()
        if os.path.exists(raw_input):
            with open(raw_input, 'r', encoding='utf-8') as f:
                terms_data = json.load(f)
        else:
            terms_data = json.loads(raw_input)
        is_qc = not args.trans_flow
        append_terms_to_sheet(terms_data, is_qc_flow=is_qc)
    else:
        # Mặc định chạy sync
        update_glossary()
