@echo off
title Dong bo Trackers qua Git (52Shuku + NovelUpdates)
cd /d "%~dp0"

echo ========================================================
echo   DONG BO DU LIEU TRACKERS QUA GITHUB
echo   (52Shuku Tracker + NovelUpdates Tracker)
echo ========================================================
echo.
echo  [1] DAY du lieu (Push) ca 52Shuku va NovelUpdates len Git
echo  [2] KEO du lieu (Pull) ca 2 Tracker tu Git ve may nay
echo  [3] Chi dong bo 52Shuku Tracker
echo  [4] Chi dong bo NovelUpdates Tracker
echo.
set "choice="
set /p choice="Nhap lua chon [1, 2, 3 hoac 4]: "

if "%choice%"=="1" goto do_push_all
if "%choice%"=="2" goto do_pull_all
if "%choice%"=="3" goto do_shuku
if "%choice%"=="4" goto do_nu
echo.
echo Lua chon khong hop le.
goto do_end

:do_push_all
echo.
echo [1/3] Dang xuat du lieu trang thai ra JSON...
python -c "import scripts.shuku_tracker_server as s; s.dump_user_data_to_json()"
python -c "import scripts.nu_tracker_server as n; n.dump_user_data_to_json()"
echo [2/3] Dang them file va commit...
git add .gitignore scripts/shuku_tracker_server.py scripts/nu_tracker_server.py DONG_BO_52SHUKU_GIT.bat DONG_BO_NU_GIT.bat DONG_BO_TRACKERS_GIT.bat data/shuku_tracker.db data/shuku_user_data.json data/nu_tracker.db data/nu_user_data.json
git commit -m "sync: cap nhat du lieu 52shuku va novelupdates trackers"
echo [3/3] Dang day len GitHub (git push)...
git push origin main
if errorlevel 1 (
    echo.
    echo [!] GitHub co ban cap nhat moi. Dang tu dong gop va day lai...
    git pull --rebase origin main
    git push origin main
)
echo.
echo === DA DAY DU LIEU CA 2 TRACKER LEN GITHUB THANH CONG ===
goto do_end

:do_pull_all
echo.
echo [!] Luu y: Neu dang mo CHAY_52SHUKU_TRACKER.bat hoac CHAY_NU_TRACKER.bat, hay tat truoc khi Pull
echo.
echo [1/2] Dang tai du lieu tu GitHub (git pull)...
git pull origin main
echo [2/2] Dang nap du lieu vao co so du lieu...
python -c "import scripts.shuku_tracker_server as s; s.init_db()"
python -c "import scripts.nu_tracker_server as n; n.init_db()"
echo.
echo === DA CAP NHAT DU LIEU CA 2 TRACKER VE MAY NAY THANH CONG ===
goto do_end

:do_shuku
call DONG_BO_52SHUKU_GIT.bat
goto do_end

:do_nu
call DONG_BO_NU_GIT.bat
goto do_end

:do_end
echo.
pause
