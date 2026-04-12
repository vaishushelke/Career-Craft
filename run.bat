@echo off
setlocal
cls
echo ========================================
echo        CareerCraft Setup ^& Launch       
echo ========================================

echo 1. Checking Python Installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your PATH. 
    echo Please install Python and try again.
    pause
    exit /b
)

echo 2. Installing Required Packages...
pip install -r requirements.txt --quiet

echo.
echo 3. Initializing Database (SQLite)...
python init_db.py

echo.
echo 4. Training AI AI Recommendation Model...
python model\train_model.py

echo.
echo 5. Starting CareerCraft Flask Application...
echo Access the site at: http://127.0.0.1:8000
python app.py

pause
