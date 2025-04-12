@echo off
echo Installing dependencies...
call venv\Scripts\activate
pip install -r requirements.txt
echo Dependencies installed successfully!

echo.
echo Testing Gemini API connection...
python test_gemini.py

echo.
echo If the test was successful, you can now run the application with:
echo uvicorn app.main:app --reload
pause