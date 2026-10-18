@echo off
chcp 65001 >nul
echo.
echo ========================================================
echo   🔄 DONG BO TRUYEN MANHWA LEN HOSTING (RENDER)
echo ========================================================
echo.

git status -s data/cubari_library >nul 2>&1
echo [1/3] Dang chuan bi cac bo truyen moi...
git add data/cubari_library .gitignore

echo [2/3] Dang tao ban commit cap nhat...
git commit -m "sync: cap nhat truyen manhwa len hosting" 2>nul
if errorlevel 1 (
    echo [INFO] Thu vien truyen da duoc dong bo moi nhat, khong co chuong moi nao can push!
) else (
    echo [3/3] Dang dong bo len GitHub de Render tu dong cap nhat...
    git push origin main
    echo.
    echo ========================================================
    echo   🎉 DONG BO THANH CONG!
    echo   Hosting se cap nhat trong khoang 1-2 phut tai:
    echo   👉 https://reader-assistant.onrender.com/
    echo ========================================================
)

echo.
pause
