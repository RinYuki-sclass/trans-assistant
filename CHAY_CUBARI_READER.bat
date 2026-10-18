@echo off
chcp 65001 >nul
echo.
echo ========================================================
echo   📖 CUBARI MANHWA READER (AD-FREE ^& LOCAL CRAWLER)
echo ========================================================
echo.

python -c "import starlette, uvicorn" 2>nul
if errorlevel 1 (
    echo [INFO] Dang cai dat thu vien Starlette va Uvicorn...
    python -m pip install starlette uvicorn
)

echo Dang khoi dong Web Reader tai http://localhost:8585...
echo Nhan Ctrl+C de thoat.
echo.

set PORT=8585
start "" "http://localhost:8585"
python scripts/reader_server.py
pause
