@echo off

rem Ensure required packages are installed
py -3 -c "import pkgutil, sys; sys.exit(0 if pkgutil.find_loader('flask') else 1)" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Python dependencies...
    py -3 -m pip install -r requirements.txt
)

py -3 -m chess_game.web_app
pause
