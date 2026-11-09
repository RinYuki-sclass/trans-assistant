@echo off
chcp 65001 >nul
title Đồng bộ Trackers qua Git (52Shuku + NovelUpdates)
cd /d "%~dp0"

echo ========================================================
echo   ĐỒNG BỘ DỮ LIỆU TRACKERS QUA GITHUB
echo   (52Shuku Tracker + NovelUpdates Tracker)
echo ========================================================
echo.
echo  [1] ĐẨY dữ liệu (Push) cả 52Shuku & NovelUpdates lên Git
echo  [2] KÉO dữ liệu (Pull) cả 2 Tracker từ Git về máy này
echo  [3] Chỉ đồng bộ 52Shuku Tracker
echo  [4] Chỉ đồng bộ NovelUpdates Tracker
echo.
set /p choice="Nhập lựa chọn (1, 2, 3 hoặc 4): "

if "%choice%"=="1" (
    echo.
    echo [1/3] Đang xuất dữ liệu trạng thái ra JSON...
    python -c "import scripts.shuku_tracker_server as s; s.dump_user_data_to_json()"
    python -c "import scripts.nu_tracker_server as n; n.dump_user_data_to_json()"
    echo [2/3] Đang thêm file và commit...
    git add .gitignore scripts/shuku_tracker_server.py scripts/nu_tracker_server.py DONG_BO_52SHUKU_GIT.bat DONG_BO_NU_GIT.bat DONG_BO_TRACKERS_GIT.bat data/shuku_tracker.db data/shuku_user_data.json data/nu_tracker.db data/nu_user_data.json
    git commit -m "sync: cập nhật dữ liệu 52shuku và novelupdates trackers"
    echo [3/3] Đang đẩy lên GitHub (git push)...
    git push origin main
    echo.
    echo === ĐÃ ĐẨY DỮ LIỆU CẢ 2 TRACKER LÊN GITHUB THÀNH CÔNG ===
) else if "%choice%"=="2" (
    echo.
    echo (Lưu ý: Nếu đang mở cửa sổ CHAY_52SHUKU_TRACKER.bat hoặc CHAY_NU_TRACKER.bat, hãy tắt trước khi Pull)
    echo.
    echo [1/2] Đang tải dữ liệu từ GitHub (git pull)...
    git pull origin main
    echo [2/2] Đang nạp dữ liệu vào cơ sở dữ liệu...
    python -c "import scripts.shuku_tracker_server as s; s.init_db()"
    python -c "import scripts.nu_tracker_server as n; n.init_db()"
    echo.
    echo === ĐÃ CẬP NHẬT DỮ LIỆU CẢ 2 TRACKER VỀ MÁY NÀY THÀNH CÔNG ===
) else if "%choice%"=="3" (
    call DONG_BO_52SHUKU_GIT.bat
) else if "%choice%"=="4" (
    call DONG_BO_NU_GIT.bat
) else (
    echo.
    echo Lựa chọn không hợp lệ.
)

echo.
pause
