@echo off

if "%VIRTUAL_ENV_DIR%"=="" (
  echo Error: VIRTUAL_ENV_DIR environment variable is not set.
  exit /b 1
)

set python_version=3.12.6
REM Check if Python version is installed.  pyenv-win doesn't have a great way to check,
REM so we'll just try to run it and check the error code.
pyenv local %python_version% >nul 2>&1
if errorlevel 1 (
  echo Error: Python %python_version% is not installed. Please install it using pyenv-win.
  exit /b 1
)
python -m venv "%venv_dir%"

set project_name=md2mm
set venv_dir=%VIRTUAL_ENV_DIR%\%project_name%

if exist "%venv_dir%" (
  echo Virtual environment already exists: %venv_dir%
) else (
  python -m venv "%venv_dir%"
  echo Virtual environment created: %venv_dir%

  REM Install dependencies (optional)
  call "%venv_dir%\Scripts\activate"
  pip install -r requirements.txt
  deactivate
)
