@echo off
chcp 65001 >nul
title Đồng bộ NovelUpdates Tracker qua Git
cd /d "%~dp0"

echo ========================================================
echo    ĐỒNG BỘ DỮ LIỆU NOVELUPDATES TRACKER QUA GITHUB
echo ========================================================
echo.
echo  [1] ĐẨY dữ liệu lên Git (Push: Lưu đọc sau, Blacklist, Vị trí)
echo  [2] KÉO dữ liệu mới về từ Git (Pull về máy này)
echo.
set /p choice="Nhập lựa chọn (1 hoặc 2): "

if "%choice%"=="1" (
    echo.
    echo [1/3] Đang sao lưu dữ liệu trạng thái ra JSON...
    python -c "import scripts.nu_tracker_server as n; n.dump_user_data_to_json()"
    echo [2/3] Đang thêm file và commit...
    git add .gitignore scripts/nu_tracker_server.py DONG_BO_NU_GIT.bat data/nu_tracker.db data/nu_user_data.json
    git commit -m "sync: cập nhật dữ liệu novelupdates tracker"
    echo [3/3] Đang đẩy lên GitHub (git push)...
    git push origin main
    echo.
    echo === ĐÃ ĐẨY DỮ LIỆU LÊN GITHUB THÀNH CÔNG ===
) else if "%choice%"=="2" (
    echo.
    echo (Lưu ý: Nếu đang mở cửa sổ CHAY_NU_TRACKER.bat, hãy tắt nó trước khi Pull)
    echo.
    echo [1/2] Đang tải dữ liệu từ GitHub (git pull)...
    git pull origin main
    echo [2/2] Đang nạp dữ liệu vào cơ sở dữ liệu...
    python -c "import scripts.nu_tracker_server as n; n.init_db()"
    echo.
    echo === ĐÃ CẬP NHẬT DỮ LIỆU MỚI VỀ MÁY NÀY THÀNH CÔNG ===
) else (
    echo.
    echo Lựa chọn không hợp lệ.
)

echo.
pause
