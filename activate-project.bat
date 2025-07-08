@echo off

if "%VIRTUAL_ENV_DIR%"=="" (
  echo Error: VIRTUAL_ENV_DIR environment variable is not set.
  exit /b 1
)

set project_name=md2mm
set venv_dir=%VIRTUAL_ENV_DIR%\%project_name%

if exist "%venv_dir%" (
  call "%venv_dir%\Scripts\activate"
) else (
  echo Virtual environment not found. Run setup_project.bat first.
)
