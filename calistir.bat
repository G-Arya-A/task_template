@echo off
echo ==========================================
echo   Proje Sablonu - Calistirici
echo ==========================================
echo.

set VENV_PYTHON=%~dp0venv\Scripts\python.exe
set PROJECT_DIR=%~dp0

echo [1/4] Testler calistiriliyor...
"%VENV_PYTHON%" -m pytest "%PROJECT_DIR%tests" -v
echo.

echo [2/4] Lint kontrolu yapiliyor...
"%VENV_PYTHON%" -m ruff check "%PROJECT_DIR%src" "%PROJECT_DIR%tests"
echo.

echo [3/4] Format kontrolu yapiliyor...
"%VENV_PYTHON%" -m black --check "%PROJECT_DIR%src" "%PROJECT_DIR%tests"
echo.

echo ==========================================
echo   Tamamlandi!
echo ==========================================
pause
