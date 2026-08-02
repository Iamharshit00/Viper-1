@echo off
title Viper Chat Launcher

echo =====================================
echo        Viper Chat Launcher
echo =====================================
echo.

:: Check if Python 3.13 is installed
py -3.13 --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python 3.13 is not installed.
    echo Please install Python 3.13 from https://www.python.org/downloads/
    pause
    exit /b
)

:: Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    py -3.13 -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Upgrade pip
python -m pip install --upgrade pip

:: Install requirements
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    if exist requriments.txt (
        pip install -r requriments.txt
    ) else (
        echo No requirements file found.
    )
)

:: Run chat.py
echo.
echo Starting chat.py...
python chat.py

pause
