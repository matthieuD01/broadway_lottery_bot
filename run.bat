@echo off
REM Load variables from .env file
if exist "%~dp0.env" (
    for /f "usebackq tokens=1,* delims==" %%A in (`type "%~dp0.env" ^| findstr /v "^#"`) do set "%%A=%%B"
)

if "%CONDA_ENV%"=="" (
    echo CONDA_ENV not specified in .env
    exit /b 1
)

for /f "delims=" %%i in ('conda info --base') do set "CONDA_BASE=%%i"
call "%CONDA_BASE%\condabin\conda.bat" activate "%CONDA_ENV%"

python main.py
