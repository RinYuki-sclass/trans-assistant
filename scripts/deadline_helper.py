"""
Deadline Helper for Trans-Assistant
===================================
Module kết nối Google Sheets & Google Drive để theo dõi tiến độ Deadline,
phát hiện file mất, cảnh báo quá hạn và hiển thị trực tiếp trên giao diện Streamlit.
"""

import os
import re
import sys
import json
import io
from datetime import datetime, timezone, timedelta
from typing import Optional
from dataclasses import dataclass, field
import streamlit as st

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False


# ============================================================================
# CONFIGURATION
# ============================================================================

@dataclass
class DeadlineConfig:
    """Cấu hình cho deadline tracker"""
    credentials_path: str = ""
    spreadsheet_id: str = "1Rm6BLnW6yj019GMLHxxsQGDYCHQdz8z-cALrmdCfdro"
    sheet_name: str = "Mục lục chương truyện"
    assignment_range: str = "P1:W13"
    master_range: str = "A1:L871"
    trans_folder_id: str = "1Gsignn6UF7nHnSiwG8SIJUHnsbIiQ_Hp"
    beta_folder_id: str = "1KcGW2xOHVYS0Sll4eaS0frCkPUmAcdT7"
    scopes: list = field(default_factory=lambda: [
        'https://www.googleapis.com/auth/spreadsheets.readonly',
        'https://www.googleapis.com/auth/drive'
    ])


def find_credentials_path() -> str:
    """Tìm đường dẫn file credentials / service-account.json nếu có trên đĩa"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    candidates = [
        os.path.join(base_dir, "service-account.json"),
        os.path.join(base_dir, "credentials.json"),
        os.path.join(os.path.dirname(base_dir), "howl-manager", "credentials.json"),
        os.path.join(os.path.dirname(base_dir), "howl-manager", "service-account.json"),
        "service-account.json",
        "credentials.json"
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return os.path.join(base_dir, "service-account.json")


def get_service_account_credentials_info() -> dict | None:
    """
    Lấy dictionary thông tin Service Account từ nhiều nguồn:
    1. st.secrets (Streamlit Cloud Secrets)
    2. Biến môi trường GOOGLE_SERVICE_ACCOUNT / GCP_SERVICE_ACCOUNT (JSON string)
    3. File JSON trên đĩa cục bộ
    """
    # 1. Thử lấy từ st.secrets (Streamlit Cloud)
    try:
        if hasattr(st, "secrets"):
            for sec_key in ["gcp_service_account", "google_service_account", "service_account", "GOOGLE_SERVICE_ACCOUNT", "credentials"]:
                if sec_key in st.secrets:
                    val = st.secrets[sec_key]
                    if isinstance(val, dict) or hasattr(val, "to_dict"):
                        return dict(val)
                    elif isinstance(val, str) and val.strip().startswith("{"):
                        return json.loads(val.strip())
    except Exception:
        pass

    # 2. Thử lấy từ biến môi trường
    for env_key in ["GOOGLE_SERVICE_ACCOUNT", "GCP_SERVICE_ACCOUNT", "GOOGLE_CREDENTIALS"]:
        env_val = os.environ.get(env_key, "").strip()
        if env_val.startswith("{"):
            try:
                return json.loads(env_val)
            except Exception:
                pass

    # 3. Thử đọc từ file cục bộ
    creds_path = find_credentials_path()
    if creds_path and os.path.exists(creds_path):
        try:
            with open(creds_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    return None


def get_service_account_credentials(scopes=None):
    """Khởi tạo Google Credentials object từ service account info (hỗ trợ cả Secrets, Env & File)"""
    if not GOOGLE_AVAILABLE:
        return None
    if scopes is None:
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets.readonly',
            'https://www.googleapis.com/auth/drive'
        ]
    info = get_service_account_credentials_info()
    if info:
        try:
            return service_account.Credentials.from_service_account_info(info, scopes=scopes)
        except Exception:
            pass
    return None


def get_service_account_email() -> str:
    """Lấy email của service account từ secrets, env hoặc file JSON"""
    info = get_service_account_credentials_info()
    if info:
        return info.get('client_email', 's-class@s-class-488908.iam.gserviceaccount.com')
    return "s-class@s-class-488908.iam.gserviceaccount.com"


def get_authenticated_drive_service():
    """Trả về Google Drive service v3 với đầy đủ quyền thao tác file"""
    if not GOOGLE_AVAILABLE:
        return None
    try:
        creds = get_service_account_credentials()
        if not creds:
            return None
        return build('drive', 'v3', credentials=creds, cache_discovery=False)
    except Exception:
        return None


def get_upload_webhook_url() -> str:
    """Lấy Webhook URL từ Streamlit session_state, Streamlit secrets, hoặc .env"""
    if 'google_upload_webhook_url' in st.session_state and st.session_state['google_upload_webhook_url']:
        return st.session_state['google_upload_webhook_url'].strip()
    try:
        if 'GOOGLE_UPLOAD_WEBHOOK_URL' in st.secrets:
            return st.secrets['GOOGLE_UPLOAD_WEBHOOK_URL'].strip()
    except Exception:
        pass
    return os.environ.get('GOOGLE_UPLOAD_WEBHOOK_URL', '').strip()


def save_upload_webhook_url(url: str):
    """Lưu Webhook URL vào session_state và file .env"""
    clean_url = url.strip()
    st.session_state['google_upload_webhook_url'] = clean_url
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(base_dir, '.env')
    try:
        lines = []
        found = False
        if os.path.exists(env_path):
            with open(env_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        
        new_lines = []
        for line in lines:
            if line.startswith('GOOGLE_UPLOAD_WEBHOOK_URL='):
                new_lines.append(f"GOOGLE_UPLOAD_WEBHOOK_URL={clean_url}\n")
                found = True
            else:
                new_lines.append(line)
        if not found:
            new_lines.append(f"\nGOOGLE_UPLOAD_WEBHOOK_URL={clean_url}\n")
            
        with open(env_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    except Exception as e:
        print(f"Error saving webhook to .env: {e}")


def get_github_pat() -> str:
    """Lấy GitHub Personal Access Token từ session_state, Streamlit secrets, hoặc .env"""
    if 'github_pat' in st.session_state and st.session_state['github_pat']:
        return st.session_state['github_pat'].strip()
    try:
        if hasattr(st, "secrets") and "GITHUB_PAT" in st.secrets:
            return st.secrets["GITHUB_PAT"].strip()
    except Exception:
        pass
    token = os.environ.get("GITHUB_PAT", "").strip()
    if token:
        return token
    # Đọc trực tiếp từ file .env nếu chưa được load vào os.environ
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(base_dir, '.env')
    if os.path.exists(env_path):
        try:
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith("GITHUB_PAT="):
                        val = line.strip().split("=", 1)[1].strip()
                        return val.strip('"').strip("'")
        except Exception:
            pass
    return ""


def get_howl_manager_repo() -> str:
    """Lấy tên repo howl-manager mục tiêu (mặc định RinYuki-sclass/howl-manager)"""
    if 'github_howl_repo' in st.session_state and st.session_state['github_howl_repo']:
        return st.session_state['github_howl_repo'].strip()
    try:
        if hasattr(st, "secrets") and "GITHUB_HOWL_REPO" in st.secrets:
            return st.secrets["GITHUB_HOWL_REPO"].strip()
    except Exception:
        pass
    repo = os.environ.get("GITHUB_HOWL_REPO", "").strip()
    if repo:
        return repo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(base_dir, '.env')
    if os.path.exists(env_path):
        try:
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith("GITHUB_HOWL_REPO="):
                        val = line.strip().split("=", 1)[1].strip()
                        return val.strip('"').strip("'")
        except Exception:
            pass
    return "RinYuki-sclass/howl-manager"


def trigger_daily_report_workflow() -> tuple[bool, str]:
    """
    Gửi lệnh workflow_dispatch tới GitHub Actions để chạy daily_report.yml:
    - Quét Google Drive
    - Cập nhật Google Sheets / Excel
    - Gửi thông báo Discord & Google Chat
    """
    import requests
    token = get_github_pat()
    if not token:
        return False, "Chưa cấu hình GITHUB_PAT trong .env hoặc st.secrets!"

    repo = get_howl_manager_repo()
    workflow_file = "daily_report.yml"
    url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_file}/dispatches"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    payload = {
        "ref": "main"
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=15)
        if resp.status_code == 204:
            return True, "Đã kích hoạt daily_report.yml trên GitHub Actions thành công!"
        elif resp.status_code == 401:
            return False, "GITHUB_PAT không hợp lệ hoặc đã hết hạn (401 Unauthorized)."
        elif resp.status_code == 403:
            return False, f"GITHUB_PAT không đủ quyền Actions: Read and write cho repo {repo} (403 Forbidden)."
        elif resp.status_code == 404:
            return False, f"Không tìm thấy repo hoặc file workflow ({url})."
        else:
            return False, f"GitHub API trả về lỗi ({resp.status_code}): {resp.text}"
    except Exception as e:
        return False, f"Lỗi kết nối khi gọi GitHub API: {str(e)}"


def get_latest_daily_report_run() -> dict:
    """Lấy trạng thái lần chạy gần nhất của daily_report.yml trên GitHub Actions"""
    import requests
    token = get_github_pat()
    if not token:
        return {}

    repo = get_howl_manager_repo()
    workflow_file = "daily_report.yml"
    url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_file}/runs?per_page=1"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    try:
        resp = requests.get(url, headers=headers, timeout=8)
        if resp.status_code == 200:
            runs = resp.json().get("workflow_runs", [])
            if runs:
                r = runs[0]
                created_dt_str = r.get("created_at", "")
                created_vn = created_dt_str
                if created_dt_str:
                    try:
                        dt = datetime.strptime(created_dt_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                        created_vn = (dt + timedelta(hours=7)).strftime("%H:%M:%S %d/%m/%Y")
                    except Exception:
                        pass
                return {
                    "id": r.get("id"),
                    "status": r.get("status"), # in_progress, completed, queued
                    "conclusion": r.get("conclusion"), # success, failure
                    "event": r.get("event"),
                    "html_url": r.get("html_url"),
                    "created_at": created_vn
                }
    except Exception:
        pass
    return {}


def upload_file_to_google_drive(file_data: bytes, original_filename: str, target_filename: str, folder_id: str, convert_to_gdoc: bool = True) -> tuple[bool, str, str]:
    """
    Tải tập tin lên Google Drive vào folder_id chỉ định.
    Ưu tiên 1: Gửi qua Webhook Apps Script (Tài khoản B) để tránh 100% lỗi Quota.
    Ưu tiên 2: Sử dụng Google Drive API trực tiếp qua Service Account.
    """
    ext = os.path.splitext(original_filename)[1].lower()
    mime_map = {
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".doc": "application/msword",
        ".txt": "text/plain",
        ".md": "text/plain",
        ".pdf": "application/pdf",
        ".zip": "application/zip",
        ".rar": "application/x-rar-compressed",
        ".html": "text/html",
    }
def parse_webhook_response(resp) -> tuple[bool, str, str]:
    """Phân tích phản hồi từ Apps Script Webhook với hướng dẫn chẩn đoán thân thiện."""
    if resp is None:
        return False, "Không nhận được phản hồi từ Webhook.", ""
    
    # Kiểm tra nếu bị chuyển hướng sang trang đăng nhập Google (Do chưa set quyền Anyone)
    if "accounts.google.com" in resp.url or "ServiceLogin" in resp.url or "Sign in - Google Accounts" in resp.text:
        return False, (
            "🔒 **Google Webhook bị chặn do chưa đặt quyền 'Bất kỳ ai (Anyone)'!**\n\n"
            "👉 **Cách khắc phục trong 10 giây:**\n"
            "1. Mở [script.google.com](https://script.google.com) trên Tài khoản B.\n"
            "2. Bấm **Triển khai (Deploy)** ➔ **Quản lý tùy chọn triển khai (Manage deployments)**.\n"
            "3. Bấm **Cây bút chì (Chỉnh sửa)** ➔ Mục **Người có quyền truy cập (Who has access)** đổi thành **Bất kỳ ai (Anyone)**.\n"
            "4. Bấm **Triển khai (Deploy)** để hoàn tất."
        ), ""

    # Kiểm tra nếu URL là link edit/dev thay vì /exec
    if "/edit" in resp.url or "/dev" in resp.url:
        return False, (
            "⚠️ **URL Webhook chưa chính xác!**\n"
            "URL Webhook phải kết thúc bằng `/exec` (lấy từ Deploy ➔ Web app URL), không dùng link trình duyệt (/edit hoặc /dev)."
        ), ""

    try:
        data = resp.json()
        if data.get("status") == "success":
            return True, data.get("url", ""), data.get("id", "")
        else:
            return False, f"Lỗi từ Apps Script: {data.get('message', 'Không xác định')}", ""
    except Exception:
        raw_text = resp.text.strip()
        if len(raw_text) > 250:
            raw_text = raw_text[:250] + "..."
        return False, f"Webhook trả về phản hồi không hợp lệ (HTTP {resp.status_code}): {raw_text}", ""


def upload_file_to_google_drive(file_data: bytes, original_filename: str, target_filename: str, folder_id: str, convert_to_gdoc: bool = True) -> tuple[bool, str, str]:
    """
    Tải tập tin lên Google Drive vào folder_id chỉ định.
    Ưu tiên 1: Gửi qua Webhook Apps Script (Tài khoản B) để tránh 100% lỗi Quota.
    Ưu tiên 2: Sử dụng Google Drive API trực tiếp qua Service Account.
    """
    ext = os.path.splitext(original_filename)[1].lower()
    mime_map = {
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".doc": "application/msword",
        ".txt": "text/plain",
        ".md": "text/plain",
        ".pdf": "application/pdf",
        ".zip": "application/zip",
        ".rar": "application/x-rar-compressed",
        ".html": "text/html",
    }
    input_mime = mime_map.get(ext, "application/octet-stream")

    # 1. Thử gửi qua Webhook Apps Script nếu đã cấu hình
    webhook_url = get_upload_webhook_url()
    if webhook_url:
        import requests
        import base64
        try:
            payload = {
                "folderId": folder_id,
                "filename": target_filename if target_filename.endswith(ext) else f"{target_filename}{ext}",
                "content": base64.b64encode(file_data).decode('utf-8'),
                "isBase64": True,
                "mimeType": input_mime,
                "convertToDoc": convert_to_gdoc
            }
            resp = requests.post(
                webhook_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                allow_redirects=True,
                timeout=60
            )
            return parse_webhook_response(resp)
        except Exception as e:
            return False, f"Lỗi gọi Webhook Apps Script: {str(e)}", ""

    # 2. Dự phòng: Gửi trực tiếp qua Google Drive API
    try:
        drive_service = get_authenticated_drive_service()
        if not drive_service:
            return False, "Không tìm thấy file credentials hợp lệ để kết nối Google Drive API.", ""

        from googleapiclient.http import MediaIoBaseUpload

        file_metadata = {
            'name': target_filename,
            'parents': [folder_id]
        }

        if convert_to_gdoc and ext in [".docx", ".doc", ".txt", ".md", ".html"]:
            file_metadata['mimeType'] = 'application/vnd.google-apps.document'

        media = MediaIoBaseUpload(io.BytesIO(file_data), mimetype=input_mime, resumable=True)
        uploaded = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink',
            supportsAllDrives=True
        ).execute()

        web_link = uploaded.get('webViewLink') or f"https://drive.google.com/file/d/{uploaded.get('id')}"
        return True, web_link, uploaded.get('id', '')

    except Exception as e:
        err_str = str(e)
        if "storageQuotaExceeded" in err_str or "storage quota" in err_str.lower():
            return False, "QUOTA_ERROR", ""
        elif "insufficientParentPermissions" in err_str or "Insufficient permissions" in err_str:
            sa_email = get_service_account_email()
            return False, f"PERMISSION_ERROR:{sa_email}", ""
        elif "403" in err_str:
            sa_email = get_service_account_email()
            return False, f"PERMISSION_ERROR:{sa_email}", ""
        return False, f"Lỗi khi tải file lên: {err_str}", ""


def upload_text_to_google_drive(text_content: str, target_filename: str, folder_id: str) -> tuple[bool, str, str]:
    """
    Tạo trực tiếp một Google Doc từ nội dung văn bản thuần trên Drive.
    """
    webhook_url = get_upload_webhook_url()
    if webhook_url:
        import requests
        try:
            payload = {
                "folderId": folder_id,
                "filename": target_filename,
                "content": text_content,
                "isBase64": False,
                "convertToDoc": True
            }
            resp = requests.post(
                webhook_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                allow_redirects=True,
                timeout=60
            )
            return parse_webhook_response(resp)
        except Exception as e:
            return False, f"Lỗi gọi Webhook Apps Script: {str(e)}", ""

    return upload_file_to_google_drive(
        file_data=text_content.encode('utf-8'),
        original_filename=f"{target_filename}.txt",
        target_filename=target_filename,
        folder_id=folder_id,
        convert_to_gdoc=True
    )


def normalize_chapter_filename(name: str, fallback_chap_num: str = "") -> str:
    """
    Chuẩn hóa tên file theo quy chuẩn chuẩn của Team: 'Chương XXX'
    Ví dụ:
      - 'Chap298' -> 'Chương 298'
      - 'chap 298' -> 'Chương 298'
      - 'chapter 298' -> 'Chương 298'
      - 'ch298' -> 'Chương 298'
      - '298' -> 'Chương 298'
      - 'Chap298-Tiêu đề' -> 'Chương 298 - Tiêu đề'
      - 'Chap 347 - Tôi ra ngoài một lát (3)' -> 'Chương 347 - Tôi ra ngoài một lát (3)'
      - '[Trans] Chap298' -> 'Chương 298'
      - '[Beta] Chap 298' -> 'Chương 298'
    """
    if not name and fallback_chap_num:
        return f"Chương {fallback_chap_num.strip()}"
    
    text = name.strip()
    if not text:
        return f"Chương {fallback_chap_num.strip()}" if fallback_chap_num else ""

    # Tách phần mở rộng nếu có
    base, ext = os.path.splitext(text)
    known_exts = {".docx", ".doc", ".txt", ".md", ".pdf", ".zip", ".rar", ".html"}
    if ext.lower() in known_exts:
        target_text = base
        file_ext = ext
    else:
        target_text = text
        file_ext = ""

    # Loại bỏ tiền tố [Trans], [Beta] nếu có
    target_text = re.sub(r'^\s*\[(Trans|Beta)\]\s*', '', target_text, flags=re.IGNORECASE)
    # Loại bỏ tiền tố 'Bản sao của' nếu có
    target_text = re.sub(r'^\s*Bản sao của\s+', '', target_text, flags=re.IGNORECASE)

    # 1. Biến thể Chap/Chapter/Chuong/Chương/Ch/C + số -> 'Chương X'
    def replace_chap(m):
        return f"Chương {m.group(1)}"

    target_text = re.sub(r'(?i)\b(?:chapter|chap|chuong|chương|ch|c)\s*(\d+)', replace_chap, target_text)

    # 2. Nếu chuỗi bắt đầu trực tiếp bằng số (chưa có chữ 'Chương ')
    if re.match(r'^\d+', target_text):
        target_text = re.sub(r'^(\d+)', r'Chương \1', target_text)

    # 3. Chuẩn hóa dấu gạch nối tiêu đề
    target_text = re.sub(r'(Chương\s+\d+)\s*[-_–—:]\s*', r'\1 - ', target_text)

    # 4. Chuẩn hóa khoảng trắng thừa
    target_text = re.sub(r'\s+', ' ', target_text).strip()

    if not target_text and fallback_chap_num:
        target_text = f"Chương {fallback_chap_num.strip()}"

    return target_text + file_ext


def normalize_text_spacing(text: str) -> str:
    """Chuẩn hóa ký tự xuống dòng và khoảng trắng đặc biệt (NBSP, Zero-width, CRLF)."""
    if not text:
        return ""
    # Chuẩn hóa CRLF / CR thành LF
    t = text.replace('\r\n', '\n').replace('\r', '\n')
    # Chuẩn hóa khoảng trắng đặc biệt (NBSP, Zero-width, Ideographic space)
    t = t.replace('\u00a0', ' ').replace('\u200b', '').replace('\ufeff', '').replace('\u3000', ' ')
    return t


def standardize_paragraphs_spacing(text: str) -> str:
    """
    Loại bỏ toàn bộ dòng trống thừa và định dạng lại để các đoạn cách nhau đúng 1 dòng trống chuẩn.
    """
    clean_t = normalize_text_spacing(text)
    if not clean_t.strip():
        return ""
    lines = [l.strip() for l in clean_t.splitlines() if l.strip()]
    return "\n\n".join(lines)


def split_paragraphs_for_merge(text: str, mode: str = "line") -> list[str]:
    """
    Tách văn bản thành danh sách các đoạn văn bản chuẩn.
    Mỗi đoạn có chữ là 1 phần tử (đã chuẩn hóa loại bỏ dòng trống dư thừa).
    """
    clean_t = normalize_text_spacing(text)
    if not clean_t.strip():
        return []

    if mode == "block":
        blocks = re.split(r'\n\s*\n+', clean_t.strip())
        paras = []
        for b in blocks:
            b_clean = " ".join([l.strip() for l in b.split('\n') if l.strip()])
            if b_clean:
                paras.append(b_clean)
        return paras
    else:
        lines = [l.strip() for l in clean_t.splitlines()]
        paras = [l for l in lines if l]
        return paras


def merge_interleaved_text(raw_text: str, trans_text: str, custom_raw_tag: str = "Raw:", split_mode: str = "line") -> tuple[str, int, int, str]:
    """
    Ghép song ngữ xen kẽ 1:1 theo định dạng:
    Raw: <câu/đoạn raw>
    <câu/đoạn dịch>
    
    Trả về: (nội_dung_ghép, số_đoạn_raw, số_đoạn_trans, thông_báo_cảnh_báo)
    """
    raw_paras = split_paragraphs_for_merge(raw_text, mode=split_mode)
    trans_paras = split_paragraphs_for_merge(trans_text, mode=split_mode)
    
    num_raw = len(raw_paras)
    num_trans = len(trans_paras)
    
    if num_raw == 0 and num_trans == 0:
        return "", 0, 0, "Chưa nhập nội dung Raw hoặc Bản dịch."
    
    tag = custom_raw_tag.strip()
    if not tag.endswith(":"):
        tag = f"{tag}:"
    
    merged_lines = []
    warning_msg = ""
    
    max_len = max(num_raw, num_trans)
    if num_raw != num_trans and num_raw > 0 and num_trans > 0:
        warning_msg = f"⚠️ Lệch số đoạn: Raw có {num_raw} đoạn, Bản dịch có {num_trans} đoạn (chênh lệch {abs(num_raw - num_trans)} đoạn)."
    
    for i in range(max_len):
        r = raw_paras[i] if i < num_raw else ""
        t = trans_paras[i] if i < num_trans else ""
        
        if r:
            # Nếu r đã có tag Raw: hoặc KR: thì chuẩn hóa lại
            clean_r = re.sub(r'^(?:\[\s*)?(?:raw|kr|en|kor|eng)\s*(?:\]\s*)?:?\s*', '', r, flags=re.IGNORECASE).strip()
            merged_lines.append(f"{tag} {clean_r}")
        
        if t:
            merged_lines.append(t)
            
        merged_lines.append("")  # Dòng trống ngăn cách các cặp đoạn
        
    return "\n".join(merged_lines).strip(), num_raw, num_trans, warning_msg


def clean_interleaved_raw_text(text: str) -> str:
    """
    Loại bỏ tất cả các dòng bắt đầu bằng 'Raw:', 'KR:', 'EN:', 'KOR:', 'ENG:', '[Raw]', '[KR]'...
    để trích xuất bản dịch Tiếng Việt sạch 100%.
    """
    if not text:
        return ""
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        stripped = line.strip()
        # Bỏ qua các dòng gắn tag Raw: hoặc KR:, EN:, vv
        if re.match(r'^(?:\[\s*)?(?:raw|kr|en|kor|eng)\s*(?:\]\s*)?:?', stripped, flags=re.IGNORECASE):
            continue
        clean_lines.append(line)
    
    res = "\n".join(clean_lines)
    res = re.sub(r'\n{3,}', '\n\n', res)
    return res.strip()


def extract_chapter_title_from_text(text: str) -> str:
    """
    Trích xuất và chuẩn hóa tên chương từ các dòng đầu tiên của nội dung văn bản.
    Hỗ trợ cả trường hợp dòng đầu tiên có tiền tố 'Raw:', 'KR:', 'Chương...', 'Chap...'
    VD:
      'Raw: Chương 347: Tôi ra ngoài một lát (3)' -> 'Chương 347 - Tôi ra ngoài một lát (3)'
      'Chap 298' -> 'Chương 298'
    """
    lines = [l.strip() for l in text.strip().split('\n') if l.strip()]
    for line in lines[:8]:
        clean_l = re.sub(r'^(?:raw|kr|en|kor|eng)\s*:\s*', '', line, flags=re.IGNORECASE).strip()
        if re.search(r'(?:chương|chuong|chapter|chap|ch|c)?\s*\d+', clean_l, flags=re.IGNORECASE):
            norm = normalize_chapter_filename(clean_l)
            if norm.startswith("Chương "):
                return norm
    return ""


# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class ChapterAssignment:
    """Thông tin phân công cho 1 người"""
    name: str
    priority_chapter: str
    will_do_chapters: str
    role: str
    assigned_date: str = ""

    DAYS_NORMAL = 7
    DAYS_WARNING = 14

    def _extract_numbers(self, text: str) -> list[int]:
        if not text:
            return []
        text = str(text).replace(' ', '')
        matches = re.findall(r'(\d+)', text)
        return [int(m) for m in matches]

    def get_priority_numbers(self) -> list[int]:
        return self._extract_numbers(self.priority_chapter)

    def get_will_do_numbers(self) -> list[int]:
        return self._extract_numbers(self.will_do_chapters)

    def get_assigned_date(self) -> Optional[datetime]:
        if not self.assigned_date:
            return None
        formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"]
        for fmt in formats:
            try:
                return datetime.strptime(self.assigned_date.strip(), fmt)
            except ValueError:
                continue
        return None

    def get_days_elapsed(self) -> Optional[int]:
        dt = self.get_assigned_date()
        if not dt:
            return None
        return (datetime.now() - dt).days

    def get_urgency_level(self) -> tuple[str, str, str]:
        """Trả về (badge, level_code, color)"""
        diff = self.get_days_elapsed()
        if diff is None:
            return ("", "unknown", "#8c8273")
        if diff <= self.DAYS_NORMAL:
            return (f"🟢 Đang làm ({diff} ngày)", "normal", "#2e7d32")
        elif diff <= self.DAYS_WARNING:
            return (f"🟡 Hơi chậm ({diff} ngày)", "warning", "#f39c12")
        else:
            return (f"🔴 Quá lâu! ({diff} ngày)", "danger", "#c62828")


@dataclass
class ChapterItemStatus:
    chapter_number: int
    assigned_to: str
    role: str
    status: str  # "found" hoặc "not_found"
    file_name: str = ""
    file_link: str = ""
    modified_time: str = ""
    urgency_badge: str = ""
    urgency_color: str = ""
    assigned_date: str = ""
    days_elapsed: Optional[int] = None


def find_howl_team_raw_docs_path() -> str:
    """Tìm đường dẫn tới thư mục docs của howl-team-raw"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    candidates = [
        os.path.join(os.path.dirname(base_dir), "howl-team-raw", "docs"),
        "d:/Nhung/RIDI/howl-team-raw/docs",
        os.path.join(base_dir, "howl-team-raw", "docs"),
    ]
    for p in candidates:
        if os.path.exists(p):
            return os.path.abspath(p)
    return ""


@st.cache_data(ttl=86400, show_spinner=False)
def get_cached_raw_catalog() -> dict:
    """Xây dựng và cache chỉ mục link Raw EN và Raw KR từ howl-team-raw/docs"""
    import glob
    docs_dir = find_howl_team_raw_docs_path()
    en_slug_map = {}
    kr_index = {}

    if docs_dir and os.path.exists(docs_dir):
        # 1. EN docs: docs/*.md
        for file_path in glob.glob(os.path.join(docs_dir, "*.md")):
            fname = os.path.basename(file_path)
            doc_slug = os.path.splitext(fname)[0]
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if line.startswith('## '):
                            m = re.search(r'##\s*(\d+)\s*:\s*(.+)', line)
                            if m:
                                chap_num = int(m.group(1))
                                title = m.group(2).strip()
                                clean_title = re.sub(r'[^a-zA-Z0-9\s-]', '', title).lower()
                                slug = re.sub(r'\s+', '-', clean_title)
                                en_slug_map[chap_num] = f"https://howl-team-raw.vercel.app/docs/{doc_slug}#{chap_num}-{slug}"
            except Exception:
                pass

        # 2. KR docs: docs/kr/s-class/vol-*/*.md
        for kf in glob.glob(os.path.join(docs_dir, "kr", "s-class", "**", "*.md"), recursive=True):
            rel = os.path.relpath(kf, docs_dir).replace('\\', '/')
            m_vol = re.search(r'vol-(\d+)', rel)
            if not m_vol:
                continue
            vol_num = int(m_vol.group(1))
            url = f"https://howl-team-raw.vercel.app/docs/{os.path.splitext(rel)[0]}"
            try:
                with open(kf, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if line.startswith('title:'):
                            m_par = re.findall(r'\((.+?)\)', line)
                            for p in m_par:
                                clean_p = re.sub(r'\s*\(\d+\)\s*$', '', p).strip().lower()
                                kr_index[(vol_num, clean_p)] = url
                            break
            except Exception:
                pass

    return {
        "en_map": en_slug_map,
        "kr_map": kr_index
    }


def _is_exact_chapter_match(filename: str, chapter_number: int) -> bool:
    nums = re.findall(r'\d+', filename)
    for n in nums:
        if int(n) == chapter_number:
            return True
    return False


def resolve_chapter_links(chap_num: int, master_lookup: dict, raw_catalog: dict, trans_drive_files: list) -> dict:
    """Trả về dict chứa raw_en_url, raw_kr_url, trans_doc_url cho 1 chapter"""
    en_map = raw_catalog.get("en_map", {})
    kr_map = raw_catalog.get("kr_map", {})

    # 1. Raw EN URL
    raw_en_url = en_map.get(chap_num, "")
    if not raw_en_url:
        group_start = ((chap_num - 1) // 10) * 10 + 1
        group_end = ((chap_num - 1) // 10 + 1) * 10
        raw_en_url = f"https://howl-team-raw.vercel.app/docs/{group_start}-{group_end}#{chap_num}"

    # 2. Raw KR URL
    info = master_lookup.get(chap_num, {})
    vol_num = info.get("vol", 1)
    vn_title = info.get("title", "")
    clean_vn = re.sub(r'\s*\(\d+\)\s*$', '', vn_title).strip().lower()

    raw_kr_url = kr_map.get((vol_num, clean_vn), "")
    if not raw_kr_url and clean_vn:
        for (v, t), u in kr_map.items():
            if v == vol_num and (clean_vn in t or t in clean_vn):
                raw_kr_url = u
                break
    if not raw_kr_url and vol_num:
        raw_kr_url = f"https://howl-team-raw.vercel.app/docs/kr/s-class/vol-{vol_num:02d}"

    # 3. Trans Doc URL
    trans_doc_url = ""
    for f in trans_drive_files:
        if _is_exact_chapter_match(f.get('name', ''), chap_num):
            trans_doc_url = f.get('webViewLink', f"https://docs.google.com/document/d/{f.get('id')}/edit")
            break

    return {
        "raw_en": raw_en_url,
        "raw_kr": raw_kr_url,
        "trans_doc": trans_doc_url
    }


def get_action_buttons_html(role: str, raw_en_url: str, raw_kr_url: str, trans_doc_url: str) -> str:
    """Tạo cụm button Raw EN, Raw KR, và File Trans (cho Beta)"""
    btns = []
    if raw_en_url:
        btns.append(f'<a href="{raw_en_url}" target="_blank" class="dl-action-pill dl-pill-en">🌐 Raw EN</a>')
    if raw_kr_url:
        btns.append(f'<a href="{raw_kr_url}" target="_blank" class="dl-action-pill dl-pill-kr">🇰🇷 Raw KR</a>')
    if role.lower() == "beta":
        if trans_doc_url:
            btns.append(f'<a href="{trans_doc_url}" target="_blank" class="dl-action-pill dl-pill-trans">📄 File Trans</a>')
        else:
            btns.append('<span class="dl-action-pill dl-pill-trans-disabled" title="Trans chưa nộp file lên Drive">⏳ Chưa có file Trans</span>')
    return " ".join(btns)


@st.cache_data(ttl=43200, show_spinner=False)
def get_cached_deadline_data(cache_key: str, spreadsheet_id: str, trans_fid: str, beta_fid: str) -> dict:
    """Hàm lấy dữ liệu từ Google APIs có cache 12 giờ trong Streamlit"""
    if not GOOGLE_AVAILABLE:
        return {"error": "Chưa cài đặt thư viện `google-api-python-client` hoặc `google-auth`."}

    creds = get_service_account_credentials()
    if not creds:
        return {
            "error": (
                "Chưa tìm thấy thông tin xác thực Google Service Account!\n\n"
                "👉 **Nếu deploy trên Streamlit Cloud:** Vào **App Settings ➔ Secrets**, tạo mục `[gcp_service_account]` và dán toàn bộ nội dung file `service-account.json` (hoặc `credentials.json`) vào đó.\n"
                "👉 **Nếu chạy Local:** Hãy đảm bảo file `service-account.json` hoặc `credentials.json` nằm ở thư mục gốc của project."
            )
        }

    try:
        sheets_service = build('sheets', 'v4', credentials=creds, cache_discovery=False)
        drive_service = build('drive', 'v3', credentials=creds, cache_discovery=False)
    except Exception as e:
        return {"error": f"Lỗi xác thực Google Service Account: {str(e)}"}

    # 1. Đọc Assignment Range
    try:
        res_assign = sheets_service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range="Mục lục chương truyện!P1:W13"
        ).execute()
        rows = res_assign.get('values', [])
    except Exception as e:
        return {"error": f"Lỗi đọc dữ liệu phân công Google Sheet: {str(e)}"}

    assignments: list[ChapterAssignment] = []
    if rows and len(rows) > 1:
        for row in rows[1:]:
            def safe(idx): return row[idx].strip() if len(row) > idx else ""
            trans_name, trans_p, trans_w, trans_d = safe(0), safe(1), safe(2), safe(3)
            if trans_name:
                assign_t = ChapterAssignment(
                    name=trans_name, priority_chapter=trans_p,
                    will_do_chapters=trans_w, role="trans", assigned_date=trans_d
                )
                if assign_t.get_priority_numbers() or assign_t.get_will_do_numbers():
                    assignments.append(assign_t)

            beta_name, beta_p, beta_w, beta_d = safe(4), safe(5), safe(6), safe(7)
            if beta_name:
                assign_b = ChapterAssignment(
                    name=beta_name, priority_chapter=beta_p,
                    will_do_chapters=beta_w, role="beta", assigned_date=beta_d
                )
                if assign_b.get_priority_numbers() or assign_b.get_will_do_numbers():
                    assignments.append(assign_b)

    # 2. Đọc Master Table
    master_rows = []
    try:
        res_master = sheets_service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range="Mục lục chương truyện!A1:L871"
        ).execute()
        master_rows = res_master.get('values', [])
    except Exception as e:
        print(f"Lỗi đọc master table: {e}")

    # Tạo bảng tra cứu Volume và Tiêu đề từ Master Table
    master_lookup = {}
    if master_rows:
        current_vol = 1
        for row in master_rows[1:]:
            if not row or not row[0]:
                continue
            nums = re.findall(r'\d+', str(row[0]))
            if not nums:
                continue
            cn = int(nums[0])
            title_vn = str(row[1]).strip() if len(row) > 1 else ""
            vol_cell = str(row[4]).strip() if len(row) > 4 else ""
            if vol_cell:
                m_v = re.search(r'\d+', vol_cell)
                if m_v:
                    current_vol = int(m_v.group(0))
            master_lookup[cn] = {
                "vol": current_vol,
                "title": title_vn
            }

    raw_catalog = get_cached_raw_catalog()

    # 3. Quét danh sách file trong 2 folder Drive
    drive_files = {'trans': [], 'beta': []}
    for role, fid in [('trans', trans_fid), ('beta', beta_fid)]:
        if fid:
            try:
                q = f"'{fid}' in parents and trashed = false"
                res_files = drive_service.files().list(
                    q=q, spaces='drive', fields='files(id, name, webViewLink, modifiedTime)', pageSize=1000
                ).execute()
                drive_files[role] = res_files.get('files', [])
            except Exception as e:
                print(f"Lỗi đọc folder Drive {role}: {e}")

    # 4. Phân tích trạng thái từng chapter ưu tiên
    items = []
    for a in assignments:
        badge, code, color = a.get_urgency_level()
        for chap_num in a.get_priority_numbers():
            links = resolve_chapter_links(chap_num, master_lookup, raw_catalog, drive_files['trans'])
            matched = [f for f in drive_files[a.role] if _is_exact_chapter_match(f.get('name', ''), chap_num)]
            if matched:
                f_item = matched[0]
                mtime_str = f_item.get('modifiedTime', '')
                f_time = ""
                if mtime_str:
                    try:
                        dt = datetime.strptime(mtime_str.split('.')[0].replace('Z', ''), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
                        f_time = (dt + timedelta(hours=7)).strftime("%d/%m %H:%M")
                    except:
                        f_time = mtime_str
                items.append({
                    "chapter_number": chap_num,
                    "assigned_to": a.name,
                    "role": a.role,
                    "status": "found",
                    "file_name": f_item.get('name', ''),
                    "file_link": f_item.get('webViewLink', f"https://drive.google.com/file/d/{f_item.get('id')}"),
                    "modified_time": f_time,
                    "urgency_badge": badge,
                    "urgency_color": color,
                    "assigned_date": a.assigned_date,
                    "days_elapsed": a.get_days_elapsed(),
                    "raw_en_url": links['raw_en'],
                    "raw_kr_url": links['raw_kr'],
                    "trans_doc_url": links['trans_doc']
                })
            else:
                items.append({
                    "chapter_number": chap_num,
                    "assigned_to": a.name,
                    "role": a.role,
                    "status": "not_found",
                    "file_name": "",
                    "file_link": "",
                    "modified_time": "",
                    "urgency_badge": badge,
                    "urgency_color": color,
                    "assigned_date": a.assigned_date,
                    "days_elapsed": a.get_days_elapsed(),
                    "raw_en_url": links['raw_en'],
                    "raw_kr_url": links['raw_kr'],
                    "trans_doc_url": links['trans_doc']
                })

    # 5. Phân tích cảnh báo (Overdue & Duplicate)
    warnings = []
    # Duplicate
    for r in ['trans', 'beta']:
        c_map = {}
        for a in assignments:
            if a.role != r:
                continue
            for cn in a.get_priority_numbers() + a.get_will_do_numbers():
                c_map.setdefault(cn, []).append(a.name)
        for cn, names in c_map.items():
            u_names = list(set(names))
            if len(u_names) > 1:
                warnings.append(f"Chap {cn} ({r.upper()}) đang được phân cho nhiều người: {', '.join(u_names)}")

    # Overdue
    for a in assignments:
        diff = a.get_days_elapsed()
        if diff and diff > a.DAYS_WARNING:
            warnings.append(f"🔴 QUÁ HẠN ({a.role.upper()}): **{a.name}** - giao ngày {a.assigned_date} ({diff} ngày chưa xong)")

    # 6. Phát hiện file Trans mất trên Drive
    missing_drive = []
    if master_rows:
        trans_files_names = [f.get('name', '') for f in drive_files['trans']]
        for i, row in enumerate(master_rows):
            if i < 299:
                continue
            row = row + [''] * (12 - len(row))
            trans_status = str(row[9]).strip().lower()
            beta_status = str(row[11]).strip().lower()
            if trans_status == "đã xong" and beta_status != "đã xong":
                nums = re.findall(r'\d+', str(row[0]))
                if not nums:
                    continue
                chap_num = int(nums[0])
                if not any(_is_exact_chapter_match(fn, chap_num) for fn in trans_files_names):
                    missing_drive.append({
                        'chapter': chap_num,
                        'assignee': str(row[8]).strip() if len(row) > 8 else "???"
                    })

    # 7. Lịch Release 4 tuần tới
    release_schedule = []
    if master_rows:
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        future_limit = today + timedelta(weeks=4)
        last_valid_date = None
        for i, row in enumerate(master_rows):
            if i == 0 or len(row) < 7:
                continue
            row = row + [''] * (12 - len(row))
            date_cell = str(row[6]).strip()
            chap_num_raw = str(row[0]).strip()
            if not chap_num_raw:
                continue
            cur_date = None
            if date_cell:
                for fmt in ["%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"]:
                    try:
                        cur_date = datetime.strptime(date_cell, fmt)
                        last_valid_date = cur_date
                        break
                    except ValueError:
                        pass
            elif last_valid_date:
                cur_date = last_valid_date

            if cur_date and today <= cur_date <= future_limit:
                nums = re.findall(r'\d+', chap_num_raw)
                chap_num = int(nums[0]) if nums else 0

                # Trạng thái & Tên Trans
                trans_name = str(row[8]).strip() if len(row) > 8 else ""
                trans_status = str(row[9]).strip().lower() if len(row) > 9 else ""
                trans_done = trans_status == "đã xong"

                # Trạng thái & Tên Beta
                beta_name = str(row[10]).strip() if len(row) > 10 else ""
                beta_status = str(row[11]).strip().lower() if len(row) > 11 else ""
                beta_done = beta_status == "đã xong"

                # Tìm link file Beta trên Drive hoặc cột H
                beta_link = ""
                matched_beta = [f for f in drive_files['beta'] if _is_exact_chapter_match(f.get('name', ''), chap_num)] if chap_num else []
                if matched_beta:
                    beta_link = matched_beta[0].get('webViewLink', f"https://drive.google.com/file/d/{matched_beta[0].get('id')}")
                elif len(row) > 7 and "http" in str(row[7]):
                    m_link = re.search(r'https?://[^\s",;)]+', str(row[7]))
                    if m_link:
                        beta_link = m_link.group(0)

                release_schedule.append({
                    'chapter': chap_num_raw,
                    'chap_num': chap_num,
                    'date': cur_date.strftime("%d/%m/%Y"),
                    'weekday': ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"][cur_date.weekday()],
                    'dt': cur_date,
                    'trans_name': trans_name,
                    'trans_done': trans_done,
                    'beta_name': beta_name,
                    'beta_done': beta_done,
                    'beta_link': beta_link
                })

    found_count = len([i for i in items if i['status'] == 'found'])
    not_found_count = len([i for i in items if i['status'] == 'not_found'])

    # Xây dựng danh sách assignments chi tiết kèm trạng thái thực tế từng chap ưu tiên
    processed_assignments = []
    for a in assignments:
        p_nums = a.get_priority_numbers()
        p_items = []
        all_p_done = True if p_nums else False

        for cn in p_nums:
            links = resolve_chapter_links(cn, master_lookup, raw_catalog, drive_files['trans'])
            matched = [f for f in drive_files[a.role] if _is_exact_chapter_match(f.get('name', ''), cn)]
            if matched:
                f_item = matched[0]
                mtime_str = f_item.get('modifiedTime', '')
                f_time = ""
                if mtime_str:
                    try:
                        dt = datetime.strptime(mtime_str.split('.')[0].replace('Z', ''), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
                        f_time = (dt + timedelta(hours=7)).strftime("%d/%m %H:%M")
                    except:
                        f_time = mtime_str
                p_items.append({
                    "chapter": cn,
                    "done": True,
                    "file_name": f_item.get('name', ''),
                    "file_link": f_item.get('webViewLink', f"https://drive.google.com/file/d/{f_item.get('id')}"),
                    "time": f_time,
                    "raw_en_url": links['raw_en'],
                    "raw_kr_url": links['raw_kr'],
                    "trans_doc_url": links['trans_doc']
                })
            else:
                all_p_done = False
                p_items.append({
                    "chapter": cn,
                    "done": False,
                    "file_name": "",
                    "file_link": "",
                    "time": "",
                    "raw_en_url": links['raw_en'],
                    "raw_kr_url": links['raw_kr'],
                    "trans_doc_url": links['trans_doc']
                })

        # Trạng thái tổng thể của người này
        if p_nums and all_p_done:
            status_badge = "✅ Đã xong (Đã nộp Drive)"
            status_color = "#2e7d32"
            is_done = True
        elif not p_nums:
            status_badge = "📝 Chờ nhận chap ưu tiên"
            status_color = "#3b82f6"
            is_done = False
        else:
            urgency_badge, _, urgency_color = a.get_urgency_level()
            status_badge = urgency_badge
            status_color = urgency_color
            is_done = False

        # HTML hiển thị cho các chap ưu tiên kèm action buttons (Raw EN, Raw KR, File Trans)
        p_rows = []
        for pi in p_items:
            if pi['done']:
                time_lbl = f" ({pi['time']})" if pi['time'] else ""
                status_lbl = f"<span style='background: rgba(46,125,50,0.12); color: #2e7d32; padding: 2px 7px; border-radius: 4px; font-weight: 600;'>Chap {pi['chapter']} ✅ Đã nộp{time_lbl}</span>"
            else:
                status_lbl = f"<span style='background: rgba(198,40,40,0.1); color: #c62828; padding: 2px 7px; border-radius: 4px; font-weight: 600;'>Chap {pi['chapter']} ⏳ Chưa nộp</span>"
            
            action_btns = get_action_buttons_html(a.role, pi['raw_en_url'], pi['raw_kr_url'], pi['trans_doc_url'])
            p_rows.append(
                f"<div style='display: flex; align-items: center; justify-content: space-between; gap: 8px; background: #ffffff; padding: 6px 10px; border-radius: 6px; border: 1px solid #E2E8F0; margin-top: 5px; flex-wrap: wrap;'>"
                f"<div>{status_lbl}</div>"
                f"<div style='display: flex; gap: 5px; align-items: center; flex-wrap: wrap;'>{action_btns}</div>"
                f"</div>"
            )
        priority_html = "".join(p_rows) if p_rows else "<i>(Trống)</i>"

        processed_assignments.append({
            "name": a.name,
            "role": a.role,
            "priority": a.priority_chapter,
            "priority_html": priority_html,
            "will_do": a.will_do_chapters,
            "date": a.assigned_date,
            "days": a.get_days_elapsed(),
            "status_badge": status_badge,
            "status_color": status_color,
            "is_done": is_done,
            "priority_items": p_items
        })

    # Sắp xếp thứ tự: Đã xong lên đầu tiên, các chap đang làm sắp xếp tăng dần theo số ngày (1 ngày -> 3 ngày -> 11 ngày)
    processed_assignments.sort(
        key=lambda x: (not x.get('is_done', False), x.get('days') if x.get('days') is not None else 9999)
    )

    return {
        "timestamp": datetime.now(timezone(timedelta(hours=7))).strftime("%H:%M:%S %d/%m/%Y"),
        "total": len(items),
        "found_count": found_count,
        "not_found_count": not_found_count,
        "items": items,
        "assignments": processed_assignments,
        "warnings": warnings,
        "missing_drive": missing_drive,
        "release_schedule": sorted(release_schedule, key=lambda x: x['dt']),
        "drive_files": drive_files
    }


def fetch_deadline_data(force_refresh: bool = False) -> dict:
    """Wrapper lấy data, hỗ trợ force refresh xóa cache"""
    info = get_service_account_credentials_info()
    cache_key = info.get('client_email', '') if info else "no_creds"
    cfg = DeadlineConfig(credentials_path=cache_key)
    if force_refresh:
        get_cached_deadline_data.clear()
    return get_cached_deadline_data(
        cache_key, cfg.spreadsheet_id, cfg.trans_folder_id, cfg.beta_folder_id
    )


# ============================================================================
# STREAMLIT UI COMPONENTS
# ============================================================================

def get_role_badge_html(role: str) -> str:
    """Tạo badge màu sắc & icon phân biệt cho ✍️ TRANS (Xanh lam) và 🔍 BETA (Tím)"""
    r = str(role).strip().lower()
    if r == "trans":
        return (
            '<span style="background: rgba(2, 132, 199, 0.12); color: #0284c7; '
            'border: 1px solid rgba(2, 132, 199, 0.35); padding: 2px 9px; '
            'border-radius: 6px; font-size: 11.5px; font-weight: 700; letter-spacing: 0.5px;">'
            '✍️ TRANS</span>'
        )
    elif r == "beta":
        return (
            '<span style="background: rgba(147, 51, 234, 0.12); color: #7e22ce; '
            'border: 1px solid rgba(147, 51, 234, 0.35); padding: 2px 9px; '
            'border-radius: 6px; font-size: 11.5px; font-weight: 700; letter-spacing: 0.5px;">'
            '🔍 BETA</span>'
        )
    return f'<span style="background: #eee; color: #555; padding: 2px 6px; border-radius: 4px; font-size: 11px;">{role.upper()}</span>'


def render_deadline_alert_banner():
    """Hiển thị banner cảnh báo ngắn gọn ở đầu trang web nếu có deadline quá hạn hoặc mất file"""
    try:
        data = fetch_deadline_data(force_refresh=False)
        if data.get("error"):
            return

        missing = data.get("missing_drive", [])
        warnings = data.get("warnings", [])
        overdue_items = [w for w in warnings if "QUÁ HẠN" in w]

        if overdue_items or missing:
            with st.container():
                st.markdown("""
                <div style="background: rgba(198, 40, 40, 0.08); border-left: 5px solid #c62828; padding: 12px 18px; border-radius: 8px; margin-bottom: 15px;">
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                        <span style="color: #c62828; font-weight: 700; font-size: 14.5px;">🚨 CẢNH BÁO TIẾN ĐỘ DEADLINE</span>
                        <span style="font-size: 12px; color: #7f1d1d;">(Xem chi tiết tại tab ⏰ Deadline & Tiến Độ)</span>
                    </div>
                """, unsafe_allow_html=True)
                
                if overdue_items:
                    for ov in overdue_items[:3]:
                        st.markdown(f"<span style='color: #991b1b; font-size: 13px;'>• {ov}</span>", unsafe_allow_html=True)
                if missing:
                    st.markdown(f"<span style='color: #991b1b; font-size: 13px;'>• <b>{len(missing)} chương</b> hoàn thành trên Sheet nhưng chưa có file trong folder Trans.</span>", unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
    except Exception:
        pass


def render_deadline_dashboard():
    """Hiển thị toàn bộ giao diện quản lý Deadline trên Tab riêng"""
    st.markdown("""
    <style>
    .dl-btn-read {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        background-color: #0D9488 !important;
        color: #FFFFFF !important;
        text-decoration: none !important;
        padding: 8px 18px !important;
        border-radius: 6px !important;
        font-size: 13.5px !important;
        font-weight: 700 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.12) !important;
        transition: all 0.2s ease !important;
        border: none !important;
    }
    .dl-btn-read:hover {
        background-color: #0F766E !important;
        color: #FFFFFF !important;
        text-decoration: none !important;
        transform: translateY(-1px);
    }
    .dl-btn-read:visited, .dl-btn-read:active, .dl-btn-read:focus {
        color: #FFFFFF !important;
        text-decoration: none !important;
    }
    .dl-btn-read span {
        color: #FFFFFF !important;
    }
    .dl-action-pill {
        display: inline-flex !important;
        align-items: center !important;
        gap: 4px !important;
        padding: 4px 10px !important;
        border-radius: 5px !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        transition: all 0.15s ease-in-out !important;
        white-space: nowrap !important;
        line-height: 1.2 !important;
    }
    .dl-action-pill:hover {
        transform: translateY(-1px) !important;
        text-decoration: none !important;
    }
    .dl-pill-en {
        background-color: #EFF6FF !important;
        color: #1D4ED8 !important;
        border: 1px solid #BFDBFE !important;
    }
    .dl-pill-en:visited, .dl-pill-en:active, .dl-pill-en:focus {
        color: #1D4ED8 !important;
    }
    .dl-pill-en:hover {
        background-color: #DBEAFE !important;
        color: #1E40AF !important;
    }
    .dl-pill-kr {
        background-color: #FEF2F2 !important;
        color: #B91C1C !important;
        border: 1px solid #FECACA !important;
    }
    .dl-pill-kr:visited, .dl-pill-kr:active, .dl-pill-kr:focus {
        color: #B91C1C !important;
    }
    .dl-pill-kr:hover {
        background-color: #FEE2E2 !important;
        color: #991B1B !important;
    }
    .dl-pill-trans {
        background-color: #F5F3FF !important;
        color: #6D28D9 !important;
        border: 1px solid #DDD6FE !important;
    }
    .dl-pill-trans:visited, .dl-pill-trans:active, .dl-pill-trans:focus {
        color: #6D28D9 !important;
    }
    .dl-pill-trans:hover {
        background-color: #EDE9FE !important;
        color: #5B21B6 !important;
    }
    .dl-pill-trans-disabled {
        background-color: #F1F5F9 !important;
        color: #94A3B8 !important;
        border: 1px dashed #CBD5E1 !important;
        cursor: not-allowed !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## ⏰ Báo Cáo & Quản Lý Tiến Độ Deadline")
    st.caption("Dữ liệu được đồng bộ trực tiếp từ Google Sheet 'Mục lục chương truyện' và 2 folder Google Drive (Trans & Beta).")

    c_top1, c_top2 = st.columns([2.6, 1.4])
    with c_top1:
        st.write("💡 *Dữ liệu được lưu trong 12–24h. Bấm nút bên cạnh để làm mới dữ liệu, đồng thời kích hoạt GitHub Action cập nhật Excel & gửi báo cáo.*")
    with c_top2:
        if st.button("🔄 Quét & Cập Nhật tiến độ", type="primary", use_container_width=True, help="Làm mới bảng tiến độ và gọi daily_report.yml trên GitHub Actions để cập nhật trạng thái 'Đã xong' vào Google Sheet"):
            import time
            prev_run = get_latest_daily_report_run()
            with st.spinner("⏳ Đang gửi lệnh cập nhật tiến độ tới GitHub Actions..."):
                ok, msg = trigger_daily_report_workflow()
                if ok:
                    st.session_state["polling_github_action"] = True
                    st.session_state["polling_start_time"] = time.time()
                    st.session_state["polling_prev_run_id"] = prev_run.get("id") if prev_run else None
                else:
                    st.session_state["workflow_dispatch_status"] = (
                        "warning",
                        f"⚠️ Đã làm mới giao diện nhưng không thể kích hoạt GitHub Action: {msg}"
                    )
            st.rerun()

    # Xử lý Auto-Polling để tự động làm mới giao diện khi GitHub Action hoàn tất
    if st.session_state.get("polling_github_action", False):
        import time
        start_time = st.session_state.get("polling_start_time", time.time())
        prev_id = st.session_state.get("polling_prev_run_id")
        elapsed = int(time.time() - start_time)

        if elapsed > 120:
            st.session_state["polling_github_action"] = False
            st.warning("⚠️ Đã chờ hơn 2 phút. GitHub Action có thể vẫn đang xử lý, bạn có thể kiểm tra trực tiếp trên tab Actions của GitHub.")
        else:
            latest_run = get_latest_daily_report_run()
            curr_id = latest_run.get("id") if latest_run else None
            r_status = latest_run.get("status") if latest_run else None
            r_conc = latest_run.get("conclusion") if latest_run else None

            # Trường hợp 1: Run mới chưa kịp xuất hiện trên GitHub API
            if curr_id == prev_id and elapsed < 12:
                st.info(
                    f"⏳ **Đang khởi tạo GitHub Action ({elapsed}s)...** Runner đang được cấp phát trên GitHub.",
                    icon="🔄"
                )
                time.sleep(3)
                st.rerun()

            # Trường hợp 2: Run mới đang chạy (in_progress / queued)
            elif r_status in ["in_progress", "queued"]:
                st.info(
                    f"⏳ **GitHub Action đang thực thi ({elapsed}s)...** Đang quét Drive, cập nhật Google Sheet & gửi báo cáo. "
                    "**Màn hình sẽ tự động làm mới ngay khi hoàn tất!**",
                    icon="🔄"
                )
                time.sleep(4)
                st.rerun()

            # Trường hợp 3: Đã hoàn tất!
            elif r_status == "completed":
                st.session_state["polling_github_action"] = False
                fetch_deadline_data(force_refresh=True)
                if r_conc == "success":
                    st.session_state["action_completed_msg"] = (
                        "success",
                        "🎉 **GitHub Action đã hoàn tất!** Dữ liệu Excel mới nhất đã được ghi vào Google Sheet và cập nhật ngay lên giao diện web."
                    )
                else:
                    st.session_state["action_completed_msg"] = (
                        "warning",
                        f"⚠️ GitHub Action đã kết thúc với trạng thái: `{r_conc}`. Vui lòng xem chi tiết trên GitHub."
                    )
                st.rerun()

    if "action_completed_msg" in st.session_state:
        msg_type, msg_text = st.session_state.pop("action_completed_msg")
        if msg_type == "success":
            st.success(msg_text, icon="✅")
            st.toast("🎉 Đã cập nhật Excel & Giao diện thành công!", icon="✅")
        else:
            st.warning(msg_text)

    if "workflow_dispatch_status" in st.session_state:
        status_type, status_text = st.session_state.pop("workflow_dispatch_status")
        if status_type == "success":
            st.success(status_text, icon="⚡")
        else:
            st.warning(status_text)


    data = fetch_deadline_data(force_refresh=False)

    if data.get("error"):
        st.error(f"❌ {data['error']}")
        st.info("📌 Hãy đảm bảo file `service-account.json` hoặc `credentials.json` đã được đặt ở thư mục gốc của project.")
        return

    # Metrics Overview
    st.markdown("---")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("📝 Tổng Chap Đang Làm", f"{data['total']} chap")
    m2.metric("✅ Đã Xong Trên Drive", f"{data['found_count']} chap")
    m3.metric("⏳ Chưa Xong (Pending)", f"{data['not_found_count']} chap")
    m4.metric("🚨 File Mất Trên Drive", f"{len(data['missing_drive'])} chap", delta_color="inverse")

    # Status row: Lần quét giao diện + Trạng thái GitHub Action
    c_status1, c_status2 = st.columns([1, 1])
    with c_status1:
        st.caption(f"🕒 Giao diện web cập nhật lúc: **{data.get('timestamp', 'N/A')}**")
    with c_status2:
        latest_run = get_latest_daily_report_run()
        if latest_run:
            r_status = latest_run.get("status")
            r_conc = latest_run.get("conclusion")
            r_time = latest_run.get("created_at")
            r_url = latest_run.get("html_url", "https://github.com/RinYuki-sclass/howl-manager/actions/workflows/daily_report.yml")
            if r_status in ["in_progress", "queued"]:
                st.caption(f"🟡 **GitHub Action:** Đang chạy cập nhật Excel... ({r_time}) • [Xem log ↗]({r_url})")
            elif r_conc == "success":
                st.caption(f"🟢 **GitHub Action:** Excel & Báo cáo đã cập nhật lúc **{r_time}** • [Xem log ↗]({r_url})")
            elif r_conc == "failure":
                st.caption(f"🔴 **GitHub Action:** Lỗi lúc **{r_time}** • [Xem chi tiết ↗]({r_url})")
            else:
                st.caption(f"🤖 **GitHub Action:** Lần chạy gần nhất: **{r_time}** • [Xem log ↗]({r_url})")
        else:
            st.caption("🤖 **GitHub Action:** Sẵn sàng kết nối")


    # Accordion Guide
    with st.expander("📖 Hướng Dẫn Nhanh: Cách Xem Bảng Phân Công & Tiến Độ", expanded=False):
        st.markdown("""
        - **📋 Bảng Phân Công**:
          - Dùng ô **🔍 Tìm theo tên hoặc số chap** để lọc nhanh chương của mình (`Chap đang làm` ⭐ và `Chap sẽ làm` 📝).
          - Bấm vào nút **Link EN / Link KR** để mở bản gốc hoặc **Google Docs** để mở file dịch.
        - **⏳ Các Chap Đang Làm**:
          - Theo dõi các chương đang được thực hiện (chia theo cột **✍️ Trans** và **🔍 Beta**).
          - Ý nghĩa huy hiệu thời gian: 🟢 *Bình thường (0 - 7 ngày)* &nbsp;|&nbsp; 🟡 *Cận hạn (8 - 14 ngày)* &nbsp;|&nbsp; 🔴 *Quá hạn (> 14 ngày)*.
        - **✅ Các Chap Đã Xong**: Danh sách các chương đã nộp file lên Drive. Bấm nút **📖 Đọc chap** để kiểm tra nội dung.
        - **📅 Lịch Release Dự Kiến**: Lịch phát hành dự kiến theo tuần để nắm bắt ngày ra chương của Team.
        """)

    # Warnings Section (nếu có)
    if data.get("warnings"):
        with st.expander("⚠️ CẢNH BÁO PHÂN CÔNG & QUÁ HẠN", expanded=True):
            for w in data["warnings"]:
                st.markdown(f"- {w}")

    # Missing Files on Drive
    if data.get("missing_drive"):
        with st.expander("🚨 CẢNH BÁO: CHƯƠNG ĐÃ XONG TRÊN SHEET NHƯNG THIẾU FILE TRÊN DRIVE", expanded=True):
            st.warning("Các chương dưới đây được đánh dấu **'Đã xong'** trên Master Table nhưng **không tìm thấy** file tương ứng trong folder Trans:")
            cols = st.columns(3)
            for idx, item in enumerate(data["missing_drive"]):
                with cols[idx % 3]:
                    st.markdown(f"• **Chap {item['chapter']}** ({item['assignee']})")

    # 4 Sub-Tabs for Howl Tracker
    t_assign, t_pending, t_done, t_release = st.tabs([
        "📋 Bảng Phân Công",
        "⏳ Các Chap Đang Làm",
        "✅ Các Chap Đã Xong",
        "📅 Lịch Release Dự Kiến"
    ])

    # Tab 1: Bảng Phân Công Thành Viên
    with t_assign:
        st.markdown("#### 📋 Bảng Phân Công Thành Viên")
        # Filters
        f1, f2, f3 = st.columns([1, 1, 2])
        with f1:
            role_filter = st.selectbox("Lọc theo vai trò:", ["Tất cả", "Trans", "Beta"], key="dl_role_filter")
        with f2:
            status_filter = st.selectbox("Lọc trạng thái:", ["Tất cả", "Chưa xong (Pending)", "Đã xong (Done)"], key="dl_status_filter")
        with f3:
            search_query = st.text_input("🔍 Tìm theo tên hoặc số chap:", placeholder="Nhập tên người làm hoặc số chương...", key="dl_search")

        assignments = data.get("assignments", [])
        if role_filter != "Tất cả":
            assignments = [a for a in assignments if a['role'].lower() == role_filter.lower()]
        if status_filter == "Chưa xong (Pending)":
            assignments = [a for a in assignments if not a.get('is_done', False)]
        elif status_filter == "Đã xong (Done)":
            assignments = [a for a in assignments if a.get('is_done', False)]
        if search_query.strip():
            sq = search_query.strip().lower()
            assignments = [
                a for a in assignments 
                if sq in a['name'].lower() or sq in a['priority'].lower() or sq in a['will_do'].lower()
            ]

        def _render_assign_card(a):
            role_tag = get_role_badge_html(a['role'])
            c_card = st.container()
            with c_card:
                card_html = f"""<div style="border: 1px solid #D1CFC7; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px; background: #F8F6F0;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
<div style="display: flex; align-items: center; gap: 8px;">
{role_tag}
<span style="font-size: 15.5px; font-weight: 700; color: #1e293b;">{a['name']}</span>
</div>
<span style="font-size: 13px; font-weight: 600; color: {a['status_color']};">{a['status_badge']}</span>
</div>
<div style="font-size: 13.5px; color: #333; line-height: 1.8;">
<b>⭐ Chap đang làm:</b> {a['priority_html']}<br>
<b>📝 Chap sẽ làm:</b> <code>{a['will_do'] or '(Trống)'}</code><br>
<b>📅 Ngày giao:</b> {a['date'] or 'Chưa ghi nhận'}
</div>
</div>"""
                st.markdown(card_html, unsafe_allow_html=True)

        trans_assigns = [a for a in assignments if a['role'].lower() == 'trans']
        beta_assigns = [a for a in assignments if a['role'].lower() == 'beta']

        if not trans_assigns and not beta_assigns:
            st.info("Không tìm thấy phân công phù hợp với bộ lọc.")
        elif role_filter == "Trans":
            st.markdown("##### ✍️ PHÂN CÔNG TRANS")
            for a in trans_assigns:
                _render_assign_card(a)
        elif role_filter == "Beta":
            st.markdown("##### 🔍 PHÂN CÔNG BETA")
            for a in beta_assigns:
                _render_assign_card(a)
        else:
            col_trans, col_beta = st.columns(2)
            with col_trans:
                st.markdown("##### ✍️ PHÂN CÔNG TRANS")
                if not trans_assigns:
                    st.info("Không có phân công Trans nào.")
                else:
                    for a in trans_assigns:
                        _render_assign_card(a)
            with col_beta:
                st.markdown("##### 🔍 PHÂN CÔNG BETA")
                if not beta_assigns:
                    st.info("Không có phân công Beta nào.")
                else:
                    for a in beta_assigns:
                        _render_assign_card(a)

    # Tab 2: Các Chap Đang Làm
    with t_pending:
        st.markdown("#### ⏳ Danh Sách Chap Đang Làm (Chưa Có File Trên Drive)")
        pending_trans = [i for i in data.get("items", []) if i['status'] == 'not_found' and i['role'] == 'trans']
        pending_beta = [i for i in data.get("items", []) if i['status'] == 'not_found' and i['role'] == 'beta']
        
        pending_trans.sort(key=lambda x: x.get('days_elapsed') if x.get('days_elapsed') is not None else 9999)
        pending_beta.sort(key=lambda x: x.get('days_elapsed') if x.get('days_elapsed') is not None else 9999)
        
        if not pending_trans and not pending_beta:
            st.success("🎉 Tuyệt vời! Tất cả các chương đang làm đều đã có file trên Drive!")
        else:
            col_trans, col_beta = st.columns(2)
            with col_trans:
                st.markdown("##### ✍️ CÁC CHAP TRANS ĐANG LÀM")
                if not pending_trans:
                    st.info("Không có chap Trans nào đang tồn đọng.")
                else:
                    for item in pending_trans:
                        role_tag = get_role_badge_html('trans')
                        action_btns = get_action_buttons_html('trans', item['raw_en_url'], item['raw_kr_url'], item['trans_doc_url'])
                        trans_html = f"""<div style="border-left: 4px solid {item['urgency_color']}; background: #FFF9F5; padding: 12px 16px; margin-bottom: 12px; border-radius: 8px; border: 1px solid #fed7aa; border-left-width: 4px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
<span style="font-size: 15px; font-weight: 700; color: #1e293b;">⏳ Chap {item['chapter_number']}</span>
{role_tag}
</div>
<div style="font-size: 13.5px; color: #444; margin-bottom: 8px;">
👤 Người làm: <b>{item['assigned_to']}</b> &nbsp;&nbsp;|&nbsp;&nbsp; 
<span style="color: {item['urgency_color']}; font-weight: 600;">{item['urgency_badge']}</span>
</div>
<div style="display: flex; gap: 6px; flex-wrap: wrap; padding-top: 6px; border-top: 1px dashed #fed7aa;">
{action_btns}
</div>
</div>"""
                        st.markdown(trans_html, unsafe_allow_html=True)

            with col_beta:
                st.markdown("##### 🔍 CÁC CHAP BETA ĐANG LÀM")
                if not pending_beta:
                    st.info("Không có chap Beta nào đang tồn đọng.")
                else:
                    for item in pending_beta:
                        role_tag = get_role_badge_html('beta')
                        action_btns = get_action_buttons_html('beta', item['raw_en_url'], item['raw_kr_url'], item['trans_doc_url'])
                        beta_html = f"""<div style="border-left: 4px solid {item['urgency_color']}; background: #FFF9F5; padding: 12px 16px; margin-bottom: 12px; border-radius: 8px; border: 1px solid #e9d5ff; border-left-width: 4px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
<span style="font-size: 15px; font-weight: 700; color: #1e293b;">⏳ Chap {item['chapter_number']}</span>
{role_tag}
</div>
<div style="font-size: 13.5px; color: #444; margin-bottom: 8px;">
👤 Người làm: <b>{item['assigned_to']}</b> &nbsp;&nbsp;|&nbsp;&nbsp; 
<span style="color: {item['urgency_color']}; font-weight: 600;">{item['urgency_badge']}</span>
</div>
<div style="display: flex; gap: 6px; flex-wrap: wrap; padding-top: 6px; border-top: 1px dashed #e9d5ff;">
{action_btns}
</div>
</div>"""
                        st.markdown(beta_html, unsafe_allow_html=True)

    # Tab 3: Các Chap Đã Xong
    with t_done:
        st.markdown("#### ✅ Danh Sách Chap Đã Nộp File Lên Google Drive")
        found_items = [i for i in data.get("items", []) if i['status'] == 'found']
        if not found_items:
            st.info("Chưa có chương nào nộp file lên Drive.")
        else:
            f_cols = st.columns(2)
            for idx, item in enumerate(found_items):
                with f_cols[idx % 2]:
                    role_tag = get_role_badge_html(item['role'])
                    read_btn = f'<a href="{item["file_link"]}" target="_blank" class="dl-btn-read" style="color: #ffffff !important;"><span style="color: #ffffff !important;">📖 Đọc chap {item["chapter_number"]}</span></a>'
                    item_html = f"""<div style="border-left: 4px solid #2e7d32; background: rgba(46,125,50,0.05); padding: 12px 16px; margin-bottom: 12px; border-radius: 8px; border: 1px solid #bbf7d0; border-left-width: 4px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
<span style="font-size: 15.5px; font-weight: 700; color: #1e293b;">✅ Chap {item['chapter_number']}</span>
{role_tag}
</div>
<div style="font-size: 13px; color: #475569; margin-bottom: 10px;">
👤 Người làm: <b>{item['assigned_to']}</b> &nbsp;&nbsp;|&nbsp;&nbsp; 🕒 Đã nộp: <b>{item['modified_time'] or 'Mới đây'}</b>
</div>
<div>
{read_btn}
</div>
</div>"""
                    st.markdown(item_html, unsafe_allow_html=True)

    # Tab 4: Lịch Release Dự Kiến
    with t_release:
        st.markdown("#### 📅 Lịch Release Dự Kiến (4 Tuần Tới)")
        sched = data.get("release_schedule", [])
        if not sched:
            st.info("Chưa có lịch phát hành dự kiến trong 4 tuần tới từ Master Table.")
        else:
            date_groups = {}
            for sc in sched:
                date_key = f"{sc['weekday']} ({sc['date']})"
                date_groups.setdefault(date_key, []).append(sc)

            for d_str, ch_list in date_groups.items():
                items_html = []
                for ch in ch_list:
                    t_status_tag = (
                        "<span style='color: #2e7d32; font-weight: 600;'>✅ Đã xong</span>" 
                        if ch['trans_done'] else 
                        "<span style='color: #c62828; font-weight: 600;'>⏳ Chưa xong</span>"
                    )
                    t_name_str = f" ({ch['trans_name']})" if ch['trans_name'] else ""
                    
                    b_status_tag = (
                        "<span style='color: #2e7d32; font-weight: 600;'>✅ Đã xong</span>" 
                        if ch['beta_done'] else 
                        "<span style='color: #c62828; font-weight: 600;'>⏳ Chưa xong</span>"
                    )
                    b_name_str = f" ({ch['beta_name']})" if ch['beta_name'] else ""

                    if ch.get('beta_link'):
                        chap_label = ch['chap_num'] or ch['chapter']
                        read_btn_html = f'<a href="{ch["beta_link"]}" target="_blank" class="dl-btn-read" style="color: #ffffff !important; padding: 6px 16px !important; font-size: 13px !important;"><span style="color: #ffffff !important;">📖 Đọc chap {chap_label}</span></a>'
                    elif ch.get('beta_done'):
                        read_btn_html = "<span style='font-size: 12px; color: #2e7d32; font-weight: 600; background: rgba(46,125,50,0.12); padding: 5px 10px; border-radius: 4px; border: 1px solid #bbf7d0;'>✅ Sẵn sàng đăng</span>"
                    else:
                        read_btn_html = "<span style='font-size: 12px; color: #64748b; background: #f1f5f9; padding: 5px 10px; border-radius: 4px;'>Chưa có file</span>"

                    item_block = f"""<div style="display: flex; justify-content: space-between; align-items: center; background: #ffffff; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px 16px; margin-bottom: 8px;">
<div>
<span style="font-weight: 700; font-size: 15px; color: #1e293b;">📖 Chap {ch['chapter']}</span> &nbsp;&nbsp;|&nbsp;&nbsp; 
<span style="font-size: 13px; color: #475569;">
✍️ <b>Trans:</b> {t_status_tag}{t_name_str} &nbsp;&nbsp;•&nbsp;&nbsp; 
🔍 <b>Beta:</b> {b_status_tag}{b_name_str}
</span>
</div>
<div>
{read_btn_html}
</div>
</div>"""
                    items_html.append(item_block)

                all_items_str = "\n".join(items_html)
                group_card = f"""<div style="background: #F8F6F0; border: 1px solid #D1CFC7; border-radius: 10px; padding: 14px 18px; margin-bottom: 16px;">
<div style="font-weight: 700; color: #0D9488; font-size: 15.5px; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
<span>📅 {d_str}</span>
<span style="font-size: 12px; background: rgba(13,148,136,0.12); color: #0D9488; padding: 2px 8px; border-radius: 10px; font-weight: 600;">{len(ch_list)} chương</span>
</div>
{all_items_str}
</div>"""
                st.markdown(group_card, unsafe_allow_html=True)


def render_drive_uploader_tool(data: dict = None):
    """
    Giao diện công cụ nộp file lên Google Drive của Howl Team.
    Có thể render độc lập dưới dạng 1 Tab chính.
    """
    if data is None:
        data = fetch_deadline_data()

    st.markdown("### 📤 Nộp Bản Dịch / Bản Beta Lên Google Drive")
    st.caption("Hỗ trợ tải lên file bản dịch (Trans) hoặc bản duyệt (Beta) trực tiếp vào các folder Google Drive của Team.")

    # Accordion Guide
    with st.expander("📖 Hướng Dẫn Thao Tác: Cách Nộp File Bản Dịch / Beta Lên Drive", expanded=False):
        st.markdown("""
        1. **Chọn Thư Mục Đích**:
           - **✍️ Trans (Folder Trans)**: Dành cho Translator nộp file bản dịch thô sau khi hoàn thành.
           - **🔍 Beta (Folder Dl)**: Dành cho Beta nộp bản duyệt đã trau chuốt hoàn chỉnh.
        2. **Chọn File Bản Dịch**:
           - Bấm chọn hoặc kéo thả file từ máy tính (`.docx`, `.txt`, `.md`, `.doc`, `.pdf`...).
           - Hệ thống sẽ **tự động nhận diện số chương và chuẩn hóa tên file** (VD: `Chương 347 - Tiêu đề`).
        3. **Tải Lên & Chuyển Đổi Google Docs**:
           - Bấm nút **🚀 Tải File Lên Google Drive**. File văn bản sẽ tự động chuyển thành định dạng **Google Docs** để nhóm có thể đọc và chỉnh sửa trực tiếp.
           - Sau khi tải xong, bấm **📖 Mở file trên Google Drive** để kiểm tra lại bài nộp.
        """)

    # Quick access cards
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown(f"""
        <div style="background: #FFF9F5; border: 1px solid #FED7AA; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">
            <div style="font-weight: 700; color: #EA580C; font-size: 15px; margin-bottom: 4px;">✍️ Thư Mục Trans</div>
            <div style="font-size: 13px; color: #64748B; margin-bottom: 8px;">Dành cho Trans nộp file bản dịch thô sau khi hoàn thành.</div>
            <a href="https://drive.google.com/drive/folders/{DeadlineConfig.trans_folder_id}" target="_blank" class="dl-action-pill dl-pill-trans" style="padding: 6px 14px; font-size: 12.5px;">📂 Mở Folder Trans trên Drive ↗</a>
        </div>
        """, unsafe_allow_html=True)
    with col_f2:
        st.markdown(f"""
        <div style="background: #FAF5FF; border: 1px solid #E9D5FF; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">
            <div style="font-weight: 700; color: #7C3AED; font-size: 15px; margin-bottom: 4px;">🔍 Thư Mục Beta (Dl)</div>
            <div style="font-size: 13px; color: #64748B; margin-bottom: 8px;">Dành cho Beta nộp file đã kiểm tra, trau chuốt hoàn chỉnh.</div>
            <a href="https://drive.google.com/drive/folders/{DeadlineConfig.beta_folder_id}" target="_blank" class="dl-action-pill dl-pill-en" style="padding: 6px 14px; font-size: 12.5px;">📂 Mở Folder Beta trên Drive ↗</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Configuration expander for Google Apps Script Webhook
    current_webhook = get_upload_webhook_url()
    with st.expander("⚙️ Cấu hình Tải Tự Động 1-Click (Tài khoản B - Google Apps Script)", expanded=not bool(current_webhook)):
        if current_webhook:
            st.markdown('<span style="color: #16A34A; font-weight: 600;">🟢 Đã kết nối Webhook tải file tự động</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span style="color: #D97706; font-weight: 600;">🟡 Chưa cấu hình Webhook</span> (Hiện tại cần nộp bằng cách kéo thả vào Drive)', unsafe_allow_html=True)
        
        st.caption("Dán URL Web App Google Apps Script triển khai từ Tài khoản B (người có quyền Biên tập viên) để nộp file 1-click không bị giới hạn Quota.")
        
        col_wh1, col_wh2 = st.columns([3, 1])
        with col_wh1:
            wh_input = st.text_input("Google Apps Script Webhook URL:", value=current_webhook, placeholder="https://script.google.com/macros/s/.../exec", label_visibility="collapsed", key="dl_webhook_url_input")
        with col_wh2:
            if st.button("💾 Lưu Webhook", key="dl_btn_save_webhook", use_container_width=True):
                save_upload_webhook_url(wh_input.strip())
                st.success("Đã lưu Webhook thành công!")
                st.rerun()

        with st.expander("📄 Xem mã nguồn Google Apps Script (Hỗ trợ Drive API v3 & v2)", expanded=False):
            st.markdown("""
            **Các bước cài đặt trên Tài khoản B (1 lần duy nhất):**
            1. Mở [script.google.com](https://script.google.com) và bấm **Dự án mới (New Project)**.
            2. Xóa hết code cũ và dán đoạn code bên dưới vào file `Code.gs`.
            3. Ở cột bên trái, bấm vào dấu **+** cạnh mục **Dịch vụ (Services)** ➔ Chọn **Drive API** ➔ Bấm **Thêm (Add)**.
            4. Bấm **Triển khai (Deploy)** ➔ **Tùy chọn triển khai mới (New deployment)**.
            5. Loại: **Ứng dụng web (Web app)** ➔ *Người có quyền truy cập:* **Bất kỳ ai (Anyone)**.
            6. Copy link **URL ứng dụng web** (kết thúc bằng `/exec`) và dán vào ô Webhook ở trên.
            """)
            gas_template_code = """function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const folderId = data.folderId;
    const filename = data.filename || "Bản_dịch_mới";
    const isBase64 = data.isBase64 || false;
    const content = data.content || "";
    const mimeType = data.mimeType || "text/plain";
    const convertToDoc = data.convertToDoc !== false;

    // 1. Tạo Blob dữ liệu
    let blob;
    if (isBase64) {
      const decodedBytes = Utilities.base64Decode(content);
      blob = Utilities.newBlob(decodedBytes, mimeType, filename);
    } else {
      blob = Utilities.newBlob(content, "text/plain", filename);
    }

    let fileId = "";
    let fileUrl = "";

    // 2. Tự động chuyển đổi sang Google Docs (hỗ trợ cả Drive API v3 và v2)
    if (convertToDoc && (filename.endsWith('.docx') || filename.endsWith('.doc') || filename.endsWith('.txt') || filename.endsWith('.md'))) {
      const cleanName = filename.replace(/\\.(docx|doc|txt|md)$/i, '');
      
      if (typeof Drive !== 'undefined' && Drive.Files) {
        if (typeof Drive.Files.create === 'function') {
          // Drive API v3 (Chuẩn mới)
          const resource = {
            name: cleanName,
            mimeType: 'application/vnd.google-apps.document',
            parents: [folderId]
          };
          const createdFile = Drive.Files.create(resource, blob, { supportsAllDrives: true });
          fileId = createdFile.id;
          fileUrl = 'https://docs.google.com/document/d/' + fileId + '/edit';
        } else if (typeof Drive.Files.insert === 'function') {
          // Drive API v2 (Phiên bản cũ)
          const resource = {
            title: cleanName,
            mimeType: 'application/vnd.google-apps.document',
            parents: [{ id: folderId }]
          };
          const createdFile = Drive.Files.insert(resource, blob, { supportsAllDrives: true });
          fileId = createdFile.id;
          fileUrl = createdFile.alternateLink || ('https://docs.google.com/document/d/' + fileId + '/edit');
        }
      }
    }

    // 3. Fallback: Nếu không dùng Drive Service hoặc tải file zip, pdf...
    if (!fileId) {
      const folder = DriveApp.getFolderById(folderId);
      const createdFile = folder.createFile(blob);
      fileId = createdFile.getId();
      fileUrl = createdFile.getUrl();
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      id: fileId,
      url: fileUrl,
      message: "Tải file lên thành công"
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}"""
            st.code(gas_template_code, language="javascript")

    # Select Role
    u_role = st.radio(
        "1. Chọn vai trò & Thư mục đích:",
        ["✍️ Trans (Folder Trans)", "🔍 Beta (Folder Dl - nộp dl ở đây)"],
        horizontal=True,
        key="dl_upload_role"
    )
    is_trans = "Trans" in u_role
    target_folder_id = DeadlineConfig.trans_folder_id if is_trans else DeadlineConfig.beta_folder_id
    target_role_str = "trans" if is_trans else "beta"

    # Suggested chapters from current pending assignments
    pending_chaps = [i['chapter_number'] for i in data.get("items", []) if i['status'] == 'not_found' and i['role'] == target_role_str]
    pending_labels = [f"Chương {c}" for c in sorted(pending_chaps)] if pending_chaps else []
    if pending_labels:
        st.caption(f"💡 **Các chương đang làm dở:** {', '.join(pending_labels)}")

    # Upload file section
    uploaded_file = st.file_uploader(
        "Chọn hoặc kéo thả file từ máy tính của bạn (.docx, .doc, .txt, .md, .pdf):",
        type=["docx", "doc", "txt", "md", "pdf", "zip", "rar"],
        key="dl_uploader_file"
    )
    convert_gdoc = True

    if uploaded_file:
        auto_name = normalize_chapter_filename(os.path.splitext(uploaded_file.name)[0])
        st.markdown(f"""
        <div style="font-size: 13.5px; color: #0D9488; background: rgba(13,148,136,0.08); padding: 8px 14px; border-radius: 6px; margin: 10px 0; border: 1px solid rgba(13,148,136,0.2);">
            ✨ <b>File đã chọn:</b> <code>{uploaded_file.name}</code> &nbsp;➔&nbsp; <b>Tự động chuẩn hóa lưu trên Drive:</b> <code>{auto_name}</code>
        </div>
        """, unsafe_allow_html=True)

    if st.button("🚀 Tải File Lên Google Drive", type="primary", key="dl_btn_upload_file"):
        if not uploaded_file:
            st.warning("⚠️ Vui lòng chọn một file để tải lên.")
        else:
            raw_base = os.path.splitext(uploaded_file.name)[0]
            final_name = normalize_chapter_filename(raw_base)

            with st.spinner(f"Đang tải '{final_name}' lên Google Drive..."):
                file_bytes = uploaded_file.getvalue()
                success, res_link, fid = upload_file_to_google_drive(
                    file_data=file_bytes,
                    original_filename=uploaded_file.name,
                    target_filename=final_name,
                    folder_id=target_folder_id,
                    convert_to_gdoc=convert_gdoc
                )

            if success:
                st.success(f"🎉 **Đã tải lên thành công:** `{final_name}`")
                st.markdown(f"""
                <div style="margin: 12px 0;">
                    <a href="{res_link}" target="_blank" class="dl-btn-read" style="color: #ffffff !important; font-size: 14px !important; padding: 10px 22px !important;">
                        <span style="color: #ffffff !important;">📖 Mở file trên Google Drive</span>
                    </a>
                </div>
                """, unsafe_allow_html=True)
                st.info("🔄 Hệ thống đã tự động làm mới dữ liệu để cập nhật trạng thái chương.")
                fetch_deadline_data(force_refresh=True)
            else:
                if res_link == "QUOTA_ERROR":
                    st.warning("⚠️ **Hạn chế chính sách lưu trữ của Google Drive đối với Service Account:**")
                    st.markdown(f"""
                    <div style="background: #FFFBEB; border: 1px solid #FDE68A; border-radius: 8px; padding: 14px 18px; margin-top: 8px;">
                        <div style="font-weight: 700; color: #B45309; margin-bottom: 6px;">📂 Thư mục Drive cá nhân yêu cầu tải lên bằng tài khoản Google:</div>
                        <div style="font-size: 13.5px; color: #4B5563; margin-bottom: 12px; line-height: 1.6;">
                            Hãy cấu hình <b>Google Apps Script Webhook (Tài khoản B)</b> ở mục cài đặt phía trên để tải tự động 1-click không bao giờ bị giới hạn dung lượng.<br>
                            👉 <b>Hoặc nộp nhanh:</b> Bấm nút mở thư mục bên dưới và kéo thả file <code>{final_name}</code> vào Drive.
                        </div>
                        <a href="https://drive.google.com/drive/folders/{target_folder_id}" target="_blank" class="dl-action-pill dl-pill-en" style="padding: 8px 18px; font-size: 13px; font-weight: 700;">📂 Mở Thư Mục Trên Google Drive Để Kéo Thả File ↗</a>
                    </div>
                    """, unsafe_allow_html=True)
                elif res_link.startswith("PERMISSION_ERROR:"):
                    sa_email = res_link.split(":", 1)[1]
                    st.error("❌ **Chưa có quyền ghi vào thư mục Google Drive!**")
                    st.markdown(f"""
                    <div style="background: #FEF2F2; border: 1px solid #FECACA; border-radius: 8px; padding: 14px 18px; margin-top: 10px;">
                        <div style="font-weight: 700; color: #991B1B; margin-bottom: 6px;">📋 Hướng dẫn cấp quyền 1 lần duy nhất:</div>
                        <ol style="font-size: 13.5px; color: #374151; margin-bottom: 12px; padding-left: 20px; line-height: 1.6;">
                            <li>Mở thư mục trên Google Drive: <a href="https://drive.google.com/drive/folders/{target_folder_id}" target="_blank"><b>Link Thư Mục</b></a></li>
                            <li>Bấm nút <b>Chia sẻ (Share)</b> ở góc trên bên phải</li>
                            <li>Nhập email Service Account sau vào ô thêm người dùng:</li>
                            <div style="margin: 6px 0;"><code style="background: #ffffff; padding: 4px 8px; border: 1px solid #CBD5E1; border-radius: 4px; font-weight: 600; color: #1E293B;">{sa_email}</code></div>
                            <li>Chọn vai trò: <b>Người chỉnh sửa (Editor)</b> rồi bấm <b>Gửi (Send)</b>.</li>
                        </ol>
                        <a href="https://drive.google.com/drive/folders/{target_folder_id}" target="_blank" class="dl-action-pill dl-pill-kr" style="padding: 8px 16px; font-size: 13px;">📂 Mở thư mục để kéo thả file trực tiếp</a>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"❌ {res_link}")

    # List existing files in this folder
    st.markdown("---")
    st.markdown(f"##### 📂 Danh Sách File Hiện Có Trong Thư Mục {'Trans' if is_trans else 'Beta (Dl)'}")
    target_files_list = data.get("drive_files", {}).get(target_role_str, [])
    if not target_files_list:
        target_files_list = [i for i in data.get("items", []) if i['role'] == target_role_str and i['status'] == 'found']
        
    if not target_files_list:
        st.info("Thư mục hiện tại chưa có file nào.")
    else:
        search_f = st.text_input("🔍 Tìm file trong thư mục:", placeholder="Nhập tên file hoặc số chap...", key="dl_search_folder_files")
        filtered_f = target_files_list
        if search_f.strip():
            sf = search_f.strip().lower()
            filtered_f = [
                f for f in target_files_list 
                if sf in f.get('name', '').lower() or sf in f.get('file_name', '').lower() or sf in str(f.get('chapter_number', ''))
            ]
        
        st.caption(f"Hiển thị {len(filtered_f)} file")
        cols_f = st.columns(2)
        for idx, f in enumerate(filtered_f):
            with cols_f[idx % 2]:
                f_name = f.get('name') or f.get('file_name') or f"Chap {f.get('chapter_number', '')}"
                f_link = f.get('webViewLink') or f.get('file_link') or f"https://drive.google.com/file/d/{f.get('id', '')}"
                f_time = f.get('modifiedTime') or f.get('modified_time') or ""
                display_time = ""
                if f_time:
                    if 'T' in str(f_time):
                        try:
                            dt = datetime.strptime(str(f_time).split('.')[0].replace('Z', ''), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
                            display_time = (dt + timedelta(hours=7)).strftime("%d/%m/%Y %H:%M")
                        except Exception:
                            display_time = str(f_time)
                    else:
                        display_time = str(f_time)
                st.markdown(f"""
                <div style="background: #ffffff; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 12px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                    <div style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 70%;">
                        <span style="font-weight: 600; font-size: 13.5px; color: #1E293B;">📄 {f_name}</span><br>
                        <span style="font-size: 11.5px; color: #64748B;">🕒 {display_time or 'N/A'}</span>
                    </div>
                    <a href="{f_link}" target="_blank" class="dl-action-pill dl-pill-en" style="padding: 4px 10px; font-size: 12px;">Mở File ↗</a>
                </div>
                """, unsafe_allow_html=True)


def render_interleaved_merger_tool():
    """
    Giao diện công cụ ghép song ngữ xen kẽ (Raw: ... / Bản dịch).
    Flow độc lập chuyên ghép văn bản gốc và bản dịch thành từng cặp đoạn có tag Raw:.
    """
    st.markdown("#### 🔀 Ghép Xen Kẽ Song Ngữ (Raw: ... / Bản Dịch)")
    st.caption("Công cụ ghép văn bản gốc (Raw / KR / EN) và bản dịch tiếng Việt thành từng cặp đoạn xen kẽ có tiền tố `Raw:` chuẩn để đối chiếu và gửi duyệt.")

    # Accordion Guide
    with st.expander("📖 Hướng Dẫn Thao Tác: Cách Ghép Song Ngữ Xen Kẽ", expanded=False):
        st.markdown("""
        1. **Dán Nội Dung Song Song**:
           - **Ô bên trái (Raw)**: Dán toàn bộ văn bản gốc (Tiếng Hàn hoặc Tiếng Anh).
           - **Ô bên phải (Dịch)**: Dán toàn bộ bản dịch Tiếng Việt tương ứng.
        2. **Thao Tác Điều Khiển**:
           - **`🔀 Ghép Xen Kẽ Ngay`**: Bấm để hệ thống ghép cặp 1:1 và hiển thị kết quả.
           - **`⚡ Đồng Bộ Format 2 Bên`**: Tự động xóa mọi dòng trống thừa và căn chỉnh các đoạn cách nhau đúng 1 dòng trống chuẩn.
           - **`🗑️ Xóa Trắng`**: Xóa trắng dữ liệu cả 2 ô để làm chương mới.
           - *Tính năng **Cuộn song song (Sync Scroll)** luôn tự động kích hoạt ngầm để bạn cuộn đối chiếu 2 bên cùng lúc.*
        3. **Tải File Xuất**:
           - Bấm nút **`⬇️ Tải file xen kẽ (.txt)`** để tải về tệp hoàn chỉnh có gắn tag `Raw:` chuẩn.
        """)

    col_r, col_t = st.columns(2)
    with col_r:
        raw_in = st.text_area(
            "1. Dán văn bản gốc (Raw / KR / EN):",
            height=280,
            placeholder="Dán các đoạn văn bản tiếng gốc tại đây...\nVD:\n347 - Tôi ra ngoài một lát (3)\n어제 밤에 무슨 일이 있었는지...\n그는 조용히 문을 열었다.",
            key="dl_tab6_raw_input"
        )
    with col_t:
        trans_in = st.text_area(
            "2. Dán bản dịch (Tiếng Việt):",
            height=280,
            placeholder="Dán các đoạn bản dịch tiếng Việt tương ứng tại đây...\nVD:\nChương 347: Tôi ra ngoài một lát (3)\nKhông một ai biết chuyện gì đã xảy ra vào đêm qua...\nHắn lặng lẽ mở cánh cửa.",
            key="dl_tab6_trans_input"
        )

    # Action Buttons Toolbar
    col_btn1, col_btn2, col_btn3 = st.columns([1.6, 1.6, 1.2])
    with col_btn1:
        btn_do_merge = st.button("🔀 Ghép Xen Kẽ Ngay", type="primary", use_container_width=True, help="Bấm để tiến hành ghép từng cặp đoạn Raw và Bản dịch")
    with col_btn2:
        btn_do_sync = st.button("⚡ Đồng Bộ Format 2 Bên", type="secondary", use_container_width=True, help="Xóa mọi dòng trống thừa và format lại để mỗi đoạn cách nhau đúng 1 dòng trống chuẩn")
    with col_btn3:
        btn_clear = st.button("🗑️ Xóa Trắng", type="secondary", use_container_width=True, help="Xóa trắng 2 ô nhập liệu để nhập lại từ đầu")

    if btn_do_sync:
        curr_r = st.session_state.get("dl_tab6_raw_input", "")
        curr_t = st.session_state.get("dl_tab6_trans_input", "")
        st.session_state["dl_tab6_raw_input"] = standardize_paragraphs_spacing(curr_r)
        st.session_state["dl_tab6_trans_input"] = standardize_paragraphs_spacing(curr_t)
        st.toast("✅ Đã đồng bộ format các đoạn cách nhau 1 dòng trống!")
        st.rerun()

    if btn_clear:
        st.session_state["dl_tab6_raw_input"] = ""
        st.session_state["dl_tab6_trans_input"] = ""
        st.session_state.pop("dl_merged_result", None)
        st.session_state.pop("dl_has_merged", None)
        st.session_state.pop("dl_tab6_preview_merged_area", None)
        st.rerun()

    # Handle Merge Logic on Click
    if btn_do_merge:
        curr_r = st.session_state.get("dl_tab6_raw_input", "").strip()
        curr_t = st.session_state.get("dl_tab6_trans_input", "").strip()
        if not curr_r and not curr_t:
            st.warning("⚠️ Vui lòng dán văn bản gốc và bản dịch trước khi bấm ghép.")
        else:
            raw_tag = "Raw:"
            merged_text, num_r, num_t, warn_m = merge_interleaved_text(curr_r, curr_t, custom_raw_tag=raw_tag, split_mode="line")
            
            st.session_state["dl_merged_result"] = merged_text
            st.session_state["dl_merge_num_r"] = num_r
            st.session_state["dl_merge_num_t"] = num_t
            st.session_state["dl_merge_warn"] = warn_m
            st.session_state["dl_tab6_preview_merged_area"] = merged_text
            st.session_state["dl_has_merged"] = True

    # JavaScript sync scroll injection (always active)
    sync_scroll_code = """
    <script>
    (function() {
        function initSync() {
            try {
                const doc = window.parent.document;
                const textareas = doc.querySelectorAll('textarea');
                let rawTa = null;
                let transTa = null;

                textareas.forEach(ta => {
                    const container = ta.closest('.stTextArea');
                    if (!container) return;
                    const label = container.querySelector('label');
                    if (!label) return;
                    const text = label.innerText || '';
                    if (text.includes('1. Dán văn bản gốc')) {
                        rawTa = ta;
                    } else if (text.includes('2. Dán bản dịch')) {
                        transTa = ta;
                    }
                });

                if (!rawTa || !transTa) return;
                if (rawTa.dataset.synced === 'true') return;
                rawTa.dataset.synced = 'true';
                transTa.dataset.synced = 'true';

                let isSyncing = false;

                function doSync(source, target) {
                    if (isSyncing) return;
                    isSyncing = true;
                    const srcMax = source.scrollHeight - source.clientHeight;
                    const tgtMax = target.scrollHeight - target.clientHeight;
                    if (srcMax > 0 && tgtMax > 0) {
                        const ratio = source.scrollTop / srcMax;
                        target.scrollTop = ratio * tgtMax;
                    } else {
                        target.scrollTop = source.scrollTop;
                    }
                    requestAnimationFrame(() => {
                        isSyncing = false;
                    });
                }

                rawTa.addEventListener('scroll', function() {
                    doSync(rawTa, transTa);
                }, { passive: true });

                transTa.addEventListener('scroll', function() {
                    doSync(transTa, rawTa);
                }, { passive: true });
            } catch(e) {
                // ignore
            }
        }
        setInterval(initSync, 600);
    })();
    </script>
    """
    import streamlit.components.v1 as components
    components.html(sync_scroll_code, height=0)

    # If merged result is available, render metrics, warnings and preview
    if st.session_state.get("dl_has_merged") and st.session_state.get("dl_merged_result"):
        merged_text = st.session_state.get("dl_merged_result", "")
        num_r = st.session_state.get("dl_merge_num_r", 0)
        num_t = st.session_state.get("dl_merge_num_t", 0)
        warn_m = st.session_state.get("dl_merge_warn", "")

        st.session_state["dl_tab6_preview_merged_area"] = merged_text

        st.markdown("---")
        # Metrics status
        c_st1, c_st2, c_st3 = st.columns(3)
        c_st1.metric("Số đoạn Bản Gốc (Raw)", f"{num_r} đoạn")
        c_st2.metric("Số đoạn Bản Dịch (VI)", f"{num_t} đoạn")
        if num_r > 0 and num_t > 0:
            if num_r == num_t:
                c_st3.success(f"✅ Đã khớp hoàn toàn ({num_r} cặp đoạn)")
            else:
                c_st3.warning(f"⚠️ Lệch {abs(num_r - num_t)} đoạn")

        if warn_m:
            st.warning(warn_m)
            with st.expander(f"🔍 Bảng Đối Chiếu So Sánh Từng Đoạn (Raw: {num_r} vs Dịch: {num_t})", expanded=False):
                st.caption("Kiểm tra đối chiếu từng vị trí đoạn để tìm điểm lệch:")
                r_paras = split_paragraphs_for_merge(raw_in, mode="line")
                t_paras = split_paragraphs_for_merge(trans_in, mode="line")
                max_l = max(len(r_paras), len(t_paras))
                for idx in range(max_l):
                    rp = r_paras[idx] if idx < len(r_paras) else "⚠️ [THIẾU ĐOẠN RAW]"
                    tp = t_paras[idx] if idx < len(t_paras) else "⚠️ [THIẾU ĐOẠN DỊCH]"
                    is_missing = (idx >= min(len(r_paras), len(t_paras)))
                    bg_col = "#FEF2F2" if is_missing else "#ffffff"
                    st.markdown(f"""
                    <div style="background: {bg_col}; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 12px; margin-bottom: 6px; font-size: 13px;">
                        <b>[Đoạn {idx+1}]</b><br>
                        <span style="color: #64748B;">• Raw:</span> {rp[:140]}{'...' if len(rp) > 140 else ''}<br>
                        <span style="color: #0D9488;">• Dịch:</span> {tp[:140]}{'...' if len(tp) > 140 else ''}
                    </div>
                    """, unsafe_allow_html=True)

        # Detect Title
        detected_name = extract_chapter_title_from_text(trans_in) or extract_chapter_title_from_text(raw_in) or extract_chapter_title_from_text(merged_text) or "Bản_dịch_xen_kẽ"
        clean_filename = normalize_chapter_filename(detected_name) or "Chuong_moi"

        if detected_name and detected_name != "Bản_dịch_xen_kẽ":
            st.markdown(f"""
            <div style="font-size: 13.5px; color: #0D9488; background: rgba(13,148,136,0.08); padding: 8px 14px; border-radius: 6px; margin: 10px 0; border: 1px solid rgba(13,148,136,0.2);">
                ✨ <b>Tự động nhận diện tiêu đề chương:</b> <code>{clean_filename}</code>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("##### 👁️ Nội dung song ngữ xen kẽ hoàn chỉnh:")
        st.text_area("Nội dung song ngữ xen kẽ hoàn chỉnh:", value=merged_text, height=320, key="dl_tab6_preview_merged_area", label_visibility="collapsed")
        st.download_button(
            label=f"⬇️ Tải file xen kẽ: {clean_filename}.txt",
            data=merged_text,
            file_name=f"{clean_filename}.txt",
            mime="text/plain",
            type="primary",
            key="dl_tab6_btn_dl_merged"
        )


def render_clean_raw_tool():
    """
    Giao diện công cụ bóc tách làm sạch văn bản, loại bỏ toàn bộ tag/dòng Raw (Raw:, KR:, EN:, vv)
    để xuất ra 100% bản dịch tiếng Việt sạch.
    Flow độc lập riêng biệt.
    """
    st.markdown("#### 🧹 Bóc Tách Bản Dịch Sạch (Loại Bỏ Dòng Raw / Tag)")
    st.caption("Công cụ chuyên dụng để bóc tách, loại bỏ toàn bộ các dòng `Raw:`, `KR:`, `EN:`, `[Raw]`, `[KR]`... khỏi bản dịch để thu được 100% tiếng Việt thuần sạch.")

    with st.expander("📖 Hướng Dẫn Thao Tác: Cách Bóc Tách Bản Dịch Sạch", expanded=False):
        st.markdown("""
        1. **Dán Văn Bản**: Dán toàn bộ file/văn bản song ngữ còn dính dòng `Raw:`, `KR:`, `EN:` hoặc các tiền tố gốc.
        2. **Thao Tác Điều Khiển**:
           - Bấm **`🧹 Bóc Tách Bản Dịch Sạch`** để lọc bỏ toàn bộ các dòng Raw và giữ lại 100% bản dịch tiếng Việt.
           - Bấm **`⚡ Đồng Bộ Format`** nếu muốn chuẩn hóa các đoạn cách nhau đúng 1 dòng trống.
           - Bấm **`🗑️ Xóa Trắng`** để làm sạch khung nhập và bắt đầu lại.
        3. **Tải File**: Bấm nút **`⬇️ Tải bản dịch tiếng Việt sạch`** để tải về file `.txt`.
        """)

    dirty_input = st.text_area(
        "Dán văn bản cần bóc tách / loại bỏ dòng Raw:",
        height=300,
        placeholder="Dán nội dung có gắn các tag Raw: / KR: / EN: tại đây...\nVD:\nRaw: 어제 밤에 무슨 일이 있었는지...\nKhông một ai biết chuyện gì đã xảy ra vào đêm qua...\n\nRaw: 그는 조용히 문을 열었다.\nHắn lặng lẽ mở cánh cửa.",
        key="dl_standalone_dirty_raw_input"
    )

    col_c1, col_c2, col_c3 = st.columns([1.6, 1.6, 1.2])
    with col_c1:
        btn_do_clean = st.button("🧹 Bóc Tách Bản Dịch Sạch", type="primary", use_container_width=True, key="btn_clean_standalone_do")
    with col_c2:
        btn_clean_sync_fmt = st.button("⚡ Đồng Bộ Format (1 Dòng Trống)", type="secondary", use_container_width=True, key="btn_clean_sync_fmt")
    with col_c3:
        btn_clean_clear = st.button("🗑️ Xóa Trắng", type="secondary", use_container_width=True, key="btn_clean_clear")

    if btn_clean_sync_fmt:
        curr_txt = st.session_state.get("dl_standalone_dirty_raw_input", "")
        st.session_state["dl_standalone_dirty_raw_input"] = standardize_paragraphs_spacing(curr_txt)
        st.toast("✅ Đã đồng bộ format các đoạn cách nhau 1 dòng trống!")
        st.rerun()

    if btn_clean_clear:
        st.session_state["dl_standalone_dirty_raw_input"] = ""
        st.session_state.pop("dl_standalone_clean_output", None)
        st.session_state.pop("dl_has_cleaned_flag", None)
        st.session_state.pop("dl_clean_num_raw_removed", None)
        st.session_state.pop("dl_clean_num_trans_kept", None)
        st.rerun()

    if btn_do_clean:
        curr_txt = st.session_state.get("dl_standalone_dirty_raw_input", "").strip()
        if not curr_txt:
            st.warning("⚠️ Vui lòng dán văn bản cần làm sạch vào ô trên.")
        else:
            cleaned_txt = clean_interleaved_raw_text(curr_txt)
            total_lines = len([l for l in curr_txt.splitlines() if l.strip()])
            clean_paras = split_paragraphs_for_merge(cleaned_txt, mode="line")
            raw_lines_removed = total_lines - len(clean_paras)
            
            st.session_state["dl_standalone_clean_output"] = cleaned_txt
            st.session_state["dl_clean_num_raw_removed"] = max(0, raw_lines_removed)
            st.session_state["dl_clean_num_trans_kept"] = len(clean_paras)
            st.session_state["dl_has_cleaned_flag"] = True

    if st.session_state.get("dl_has_cleaned_flag") and st.session_state.get("dl_standalone_clean_output") is not None:
        cleaned_result = st.session_state.get("dl_standalone_clean_output", "")
        num_removed = st.session_state.get("dl_clean_num_raw_removed", 0)
        num_kept = st.session_state.get("dl_clean_num_trans_kept", 0)
        dirty_txt = st.session_state.get("dl_standalone_dirty_raw_input", "")

        detected_clean_name = extract_chapter_title_from_text(dirty_txt) or extract_chapter_title_from_text(cleaned_result) or "Ban_dich_sach"
        clean_title_fn = normalize_chapter_filename(detected_clean_name) or "Ban_dich_sach"

        st.markdown("---")
        c_m1, c_m2, c_m3 = st.columns(3)
        c_m1.metric("Số dòng Raw đã lọc bỏ", f"{num_removed} dòng")
        c_m2.metric("Số đoạn Bản Dịch sạch", f"{num_kept} đoạn")
        c_m3.success("✨ Đã bóc tách 100% Tiếng Việt sạch")

        if detected_clean_name and detected_clean_name != "Ban_dich_sach":
            st.markdown(f"""
            <div style="font-size: 13.5px; color: #0D9488; background: rgba(13,148,136,0.08); padding: 8px 14px; border-radius: 6px; margin: 10px 0; border: 1px solid rgba(13,148,136,0.2);">
                ✨ <b>Tự động nhận diện tiêu đề chương:</b> <code>{clean_title_fn}</code>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("##### ✅ Kết quả Bản dịch tiếng Việt sạch (100% không còn dòng Raw):")
        st.text_area("Bản dịch tiếng Việt sạch:", value=cleaned_result, height=320, key="dl_standalone_clean_output_view", label_visibility="collapsed")
        st.download_button(
            label=f"⬇️ Tải bản dịch tiếng Việt sạch: {clean_title_fn}_clean.txt",
            data=cleaned_result,
            file_name=f"{clean_title_fn}_clean.txt",
            mime="text/plain",
            type="primary",
            key="btn_dl_clean_standalone_txt"
        )



