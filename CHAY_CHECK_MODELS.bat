@echo off
pushd "%~dp0"
python scripts/check_models_new.py
set "EXIT_CODE=%ERRORLEVEL%"
popd
pause
exit /b %EXIT_CODE%
