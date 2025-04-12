@echo off
echo This script will reset the MongoDB database, removing all data.
echo The next time you start the application, it will reload all data from CSV files.
echo.

call venv\Scripts\activate
python reset_database.py
pause