@echo off
chcp 65001 >nul
echo.
echo ====================================================================
echo   🏮 TAN GIANG (JJWXC) TRACKER - CHU CONG XUYEN THU (HOAN CHINH VAN)
echo ====================================================================
echo.

python -c "import starlette, uvicorn, curl_cffi, bs4" 2>nul
if errorlevel 1 (
    echo [INFO] Dang kiem tra va cai dat thu vien can thiet...
    python -m pip install starlette uvicorn curl_cffi beautifulsoup4 lxml
)

echo Dang khoi dong Tan Giang (JJWXC) Tracker tai http://localhost:8687...
echo Nhan Ctrl+C de thoat.
echo.

set JJWXC_PORT=8687
start "" "http://localhost:8687"
python scripts/jjwxc_tracker_server.py
pause
