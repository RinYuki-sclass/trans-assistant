@echo off
chcp 65001 >nul
echo.
echo ========================================================
echo   📚 NOVELUPDATES SERIES TRACKER (DANH SACH CO DINH)
echo ========================================================
echo.

python -c "import starlette, uvicorn, curl_cffi, bs4" 2>nul
if errorlevel 1 (
    echo [INFO] Dang kiem tra va cai dat thu vien can thiet...
    python -m pip install starlette uvicorn curl_cffi beautifulsoup4 lxml
)

echo Dang khoi dong NovelUpdates Tracker tai http://localhost:8686...
echo Nhan Ctrl+C de thoat.
echo.

set NU_PORT=8686
start "" "http://localhost:8686"
python scripts/nu_tracker_server.py
pause
