@echo off
chcp 65001 >nul
title Đồng bộ 52Shuku Tracker qua Git
cd /d "%~dp0"

echo ========================================================
echo    ĐỒNG BỘ DỮ LIỆU 52SHUKU TRACKER QUA GITHUB
echo ========================================================
echo.
echo  [1] ĐẨY dữ liệu lên Git (Push: Lưu đọc sau, Blacklist, Đã đọc, Vị trí)
echo  [2] KÉO dữ liệu mới về từ Git (Pull về máy này)
echo.
set /p choice="Nhập lựa chọn (1 hoặc 2): "

if "%choice%"=="1" (
    echo.
    echo [1/3] Đang sao lưu dữ liệu trạng thái ra JSON...
    python -c "import scripts.shuku_tracker_server as s; s.dump_user_data_to_json()"
    echo [2/3] Đang thêm file và commit...
    git add .gitignore scripts/shuku_tracker_server.py DONG_BO_52SHUKU_GIT.bat data/shuku_tracker.db data/shuku_user_data.json
    git commit -m "sync: cập nhật dữ liệu 52shuku tracker"
    echo [3/3] Đang đẩy lên GitHub (git push)...
    git push origin main
    if errorlevel 1 (
        echo.
        echo [!] GitHub co ban cap nhat moi. Dang tu dong gop va day lai...
        git pull --rebase origin main
        git push origin main
    )
    echo.
    echo === ĐÃ ĐẨY DỮ LIỆU LÊN GITHUB THÀNH CÔNG ===
) else if "%choice%"=="2" (
    echo.
    echo (Lưu ý: Nếu đang mở cửa sổ CHAY_52SHUKU_TRACKER.bat, hãy tắt nó trước khi Pull)
    echo.
    echo [1/2] Đang tải dữ liệu từ GitHub (git pull)...
    git pull origin main
    echo [2/2] Đang nạp dữ liệu vào cơ sở dữ liệu...
    python -c "import scripts.shuku_tracker_server as s; s.init_db()"
    echo.
    echo === ĐÃ CẬP NHẬT DỮ LIỆU MỚI VỀ MÁY NÀY THÀNH CÔNG ===
) else (
    echo.
    echo Lựa chọn không hợp lệ.
)

echo.
pause
