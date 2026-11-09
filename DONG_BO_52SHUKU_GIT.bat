@echo off
title Dong bo 52Shuku Tracker qua Git
cd /d "%~dp0"

echo ========================================================
echo    DONG BO DU LIEU 52SHUKU TRACKER QUA GITHUB
echo ========================================================
echo.
echo  [1] DAY du lieu len Git (Push: Da doc, Blacklist, Luu, Vi tri)
echo  [2] KEO du lieu moi ve tu Git (Pull ve may nay)
echo.
set "choice="
set /p choice="Nhap lua chon [1 hoac 2]: "

if "%choice%"=="1" goto do_push
if "%choice%"=="2" goto do_pull
echo.
echo Lua chon khong hop le.
goto do_end

:do_push
echo.
echo [1/3] Dang sao luu du lieu trang thai ra JSON...
python -c "import scripts.shuku_tracker_server as s; s.dump_user_data_to_json()"
echo [2/3] Dang them file va commit...
git add .gitignore scripts/shuku_tracker_server.py DONG_BO_52SHUKU_GIT.bat data/shuku_tracker.db data/shuku_user_data.json
git commit -m "sync: cap nhat du lieu 52shuku tracker"
echo [3/3] Dang day len GitHub (git push)...
git push origin main
if errorlevel 1 (
    echo.
    echo [!] GitHub co ban cap nhat moi. Dang tu dong gop va day lai...
    git pull --rebase origin main
    git push origin main
)
echo.
echo === DA DAY DU LIEU LEN GITHUB THANH CONG ===
goto do_end

:do_pull
echo.
echo [!] Luu y: Neu dang mo CHAY_52SHUKU_TRACKER.bat, hay tat no truoc khi Pull
echo.
echo [1/2] Dang tai du lieu tu GitHub (git pull)...
git pull origin main
echo [2/2] Dang nap du lieu vao co so du lieu...
python -c "import scripts.shuku_tracker_server as s; s.init_db()"
echo.
echo === DA CAP NHAT DU LIEU MOI VE MAY NAY THANH CONG ===
goto do_end

:do_end
echo.
pause
