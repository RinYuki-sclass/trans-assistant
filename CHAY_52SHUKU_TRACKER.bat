@echo off
chcp 65001 >nul
title 52Shuku Series Tracker - Chu Cong BL (Full Raw)
cd /d "%~dp0"

echo ========================================================
echo    52SHUKU SERIES TRACKER - DAM MY CHU CONG (FULL RAW)
echo    URL: http://localhost:8688
echo ========================================================
echo.

start "" "http://localhost:8688"
python scripts/shuku_tracker_server.py --port 8688
pause
