"""
☁️ Google Workspace Helper Module
Cung cấp authenticated Google Drive & Docs API clients,
dùng chung Service Account với hệ thống Glossary sync.
"""

import os
import json
import io
import re as _re


def _natural_sort_key(name: str):
    """
    Natural sort key: '2.jpg' trước '10.jpg'.
    Tương thích với get_windows_sort_key trong app.py.
    """
    return [int(c) if c.isdigit() else c.lower() for c in _re.split(r'(\d+)', name)]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================
# AUTH & CLIENT BUILDERS
# ============================================================

_SERVICE_ACCOUNT_PATH = os.path.join(BASE_DIR, "service-account.json")
_SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]


def _get_env(key: str, default=None):
    """Read env var, with Streamlit secrets fallback."""
    try:
        import streamlit as st
        return st.secrets[key]
    except Exception:
        return os.environ.get(key, default)


def get_credentials():
    """
    Return google.oauth2.service_account.Credentials.
    Priority: local JSON file → env var GOOGLE_SERVICE_ACCOUNT (JSON string).
    """
    from google.oauth2 import service_account

    if os.path.exists(_SERVICE_ACCOUNT_PATH):
        return service_account.Credentials.from_service_account_file(
            _SERVICE_ACCOUNT_PATH, scopes=_SCOPES
        )

    sa_json = _get_env("GOOGLE_SERVICE_ACCOUNT")
    if sa_json:
        info = json.loads(sa_json)
        return service_account.Credentials.from_service_account_info(info, scopes=_SCOPES)

    return None


def get_drive_service():
    """Return an authenticated Google Drive v3 service."""
    from googleapiclient.discovery import build

    creds = get_credentials()
    if not creds:
        raise RuntimeError("Không tìm thấy Service Account. Hãy đặt file service-account.json hoặc cấu hình env GOOGLE_SERVICE_ACCOUNT.")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def get_docs_service():
    """Return an authenticated Google Docs v1 service."""
    from googleapiclient.discovery import build

    creds = get_credentials()
    if not creds:
        raise RuntimeError("Không tìm thấy Service Account. Hãy đặt file service-account.json hoặc cấu hình env GOOGLE_SERVICE_ACCOUNT.")
    return build("docs", "v1", credentials=creds, cache_discovery=False)


def get_root_folder_id() -> str:
    """Return the configured root Google Drive folder ID."""
    fid = _get_env("GOOGLE_DRIVE_FOLDER_ID", "")
    if not fid:
        raise RuntimeError("Chưa cấu hình GOOGLE_DRIVE_FOLDER_ID trong .env")
    return fid.strip().strip('"').strip("'")


def is_configured() -> bool:
    """Check if Google API is properly configured."""
    try:
        creds = get_credentials()
        fid = _get_env("GOOGLE_DRIVE_FOLDER_ID", "")
        return creds is not None and bool(fid)
    except Exception:
        return False


# ============================================================
# GOOGLE DRIVE OPERATIONS
# ============================================================

def create_subfolder(parent_folder_id: str, folder_name: str) -> str:
    """
    Create a sub-folder inside parent_folder_id. Returns new folder's ID.
    If folder with same name already exists, returns existing ID.
    """
    service = get_drive_service()

    # Check if folder already exists
    query = (
        f"name='{folder_name}' and '{parent_folder_id}' in parents "
        f"and mimeType='application/vnd.google-apps.folder' and trashed=false"
    )
    results = service.files().list(q=query, fields="files(id, name)", spaces="drive").execute()
    existing = results.get("files", [])
    if existing:
        return existing[0]["id"]

    # Create new folder
    metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_folder_id],
    }
    folder = service.files().create(body=metadata, fields="id").execute()
    return folder["id"]


def upload_file_to_drive(local_path: str, parent_folder_id: str, filename: str = None) -> str:
    """
    Upload a local file to Google Drive inside parent_folder_id.
    Returns the file ID.
    """
    from googleapiclient.http import MediaFileUpload

    service = get_drive_service()
    fname = filename or os.path.basename(local_path)

    # Detect mime type
    ext = os.path.splitext(fname)[1].lower()
    mime_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".gif": "image/gif",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }
    mimetype = mime_map.get(ext, "application/octet-stream")

    file_metadata = {
        'name': fname,
        'parents': [parent_folder_id]
    }
    media = MediaFileUpload(local_path, mimetype=mimetype, resumable=True)
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id',
        supportsAllDrives=True
    ).execute()
    return file["id"]


def list_images_in_folder(folder_id: str) -> list:
    """
    List image files in a Google Drive folder.
    Returns list of dicts: [{"id": ..., "name": ..., "mimeType": ...}, ...]
    """
    service = get_drive_service()
    query = (
        f"'{folder_id}' in parents and trashed=false and ("
        f"mimeType='image/jpeg' or mimeType='image/png' or "
        f"mimeType='image/webp' or mimeType='image/gif'"
        f")"
    )
    results = service.files().list(
        q=query,
        fields="files(id, name, mimeType, size)",
        orderBy="name",
        pageSize=200,
        supportsAllDrives=True,
        includeItemsFromAllDrives=True
    ).execute()
    files = results.get("files", [])
    # Natural sort: '2.jpg' trước '10.jpg' (API trả alphabetical)
    files.sort(key=lambda f: _natural_sort_key(f.get("name", "")))
    return files


def list_subfolders(folder_id: str) -> list:
    """
    List sub-folders in a Google Drive folder.
    Returns list of dicts: [{"id": ..., "name": ...}, ...]
    """
    service = get_drive_service()
    query = (
        f"'{folder_id}' in parents and trashed=false and "
        f"mimeType='application/vnd.google-apps.folder'"
    )
    results = service.files().list(
        q=query,
        fields="files(id, name)",
        orderBy="name",
        pageSize=200,
        supportsAllDrives=True,
        includeItemsFromAllDrives=True
    ).execute()
    folders = results.get("files", [])
    folders.sort(key=lambda f: _natural_sort_key(f.get("name", "")))
    return folders


def download_file_to_bytes(file_id: str) -> bytes:
    """Download a file from Google Drive and return its contents as bytes."""
    service = get_drive_service()
    from googleapiclient.http import MediaIoBaseDownload

    request = service.files().get_media(fileId=file_id)
    buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return buffer.getvalue()


def download_file_to_path(file_id: str, dest_path: str):
    """Download a file from Google Drive to a local path."""
    data = download_file_to_bytes(file_id)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "wb") as f:
        f.write(data)


def get_folder_url(folder_id: str) -> str:
    """Return a direct link to a Google Drive folder."""
    return f"https://drive.google.com/drive/folders/{folder_id}"


def parse_folder_id_from_url(url_or_id: str) -> str:
    """
    Extract folder ID from a Google Drive URL or return as-is if already an ID.
    Supports: https://drive.google.com/drive/folders/XXXXX?...
    """
    import re
    url_or_id = url_or_id.strip()
    m = re.search(r"/folders/([a-zA-Z0-9_-]+)", url_or_id)
    if m:
        return m.group(1)
    # Assume it's already a folder ID (no slashes, reasonable length)
    if "/" not in url_or_id and len(url_or_id) > 10:
        return url_or_id
    raise ValueError(f"Không thể nhận diện Folder ID từ: {url_or_id}")


# ============================================================
# GOOGLE DOCS OPERATIONS
# ============================================================

def create_google_doc(title: str, content: str, folder_id: str = None) -> dict:
    """
    Create a new Google Doc with the given title and plain text content.
    Places it inside folder_id (or root Drive folder if None).
    
    Returns: {"doc_id": str, "doc_url": str}
    """
    docs_service = get_docs_service()
    service = get_drive_service()
    target_folder = folder_id or get_root_folder_id()

    # 1. Search for EXACT file title in this folder
    query = f"name = '{title}' and '{target_folder}' in parents and trashed = False"
    existing_files = service.files().list(
        q=query, 
        fields="files(id)",
        supportsAllDrives=True,
        includeItemsFromAllDrives=True
    ).execute().get('files', [])

    if not existing_files:
        raise RuntimeError(f"❌ Không tìm thấy file Google Doc mang tên '{title}' trong folder này. Hãy tự tạo file và share quyền Editor cho Service Account trước!")
    
    doc_id = existing_files[0]['id']

    # 2. Clear existing content (overwrite mode)
    try:
        doc = docs_service.documents().get(documentId=doc_id).execute()
        end_index = doc.get('body').get('content')[-1].get('endIndex')
        if end_index > 1:
            docs_service.documents().batchUpdate(documentId=doc_id, body={
                'requests': [{'deleteContentRange': {'range': {'startIndex': 1, 'endIndex': end_index - 1}}}]
            }).execute()
    except Exception as e:
        # If document is already empty or other issue, we just proceed
        pass

    # 3. Insert content using Docs API
    if content and content.strip():
        try:
            requests = [
                {
                    "insertText": {
                        "location": {"index": 1},
                        "text": content,
                    }
                }
            ]
            docs_service.documents().batchUpdate(
                documentId=doc_id, body={"requests": requests}
            ).execute()
        except Exception as e:
            # Nếu insert text lỗi, file Doc vẫn còn nhưng rỗng
            print(f"Lưu ý: Tạo file thành công nhưng không ghi được text: {e}")

    doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
    return {"doc_id": doc_id, "doc_url": doc_url}
