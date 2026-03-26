@echo off
echo ========================================
echo        CareerCraft Setup & Launch       
echo ========================================

echo 1. Installing Python Packages...
pip install -r requirements.txt

echo.
echo 2. Initializing MySQL Database...
python init_db.py

echo.
echo 3. Training AI Recommendation Model...
python model\train_model.py

echo.
echo 4. Starting Flask Application...
python app.py

pause
