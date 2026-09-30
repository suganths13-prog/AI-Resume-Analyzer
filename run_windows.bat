@echo off
echo ==========================================
echo AI Resume Analyzer - Windows Launcher
echo ==========================================
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
call venv\Scripts\activate.bat
echo Installing/updating dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Applying database migrations...
python manage.py migrate
echo.
echo Starting Django server...
echo Open http://127.0.0.1:8000/ in your browser.
python manage.py runserver
pause
