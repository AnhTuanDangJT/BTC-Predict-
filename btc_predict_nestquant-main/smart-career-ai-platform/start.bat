@echo off
REM Start script for Smart Career AI Platform (Windows)
REM This script starts both backend and frontend servers

echo 🚀 Starting Smart Career AI Platform...

REM Check if backend directory exists
if not exist "backend" (
    echo ❌ Backend directory not found!
    exit /b 1
)

REM Check if frontend directory exists
if not exist "frontend" (
    echo ❌ Frontend directory not found!
    exit /b 1
)

REM Start backend
echo 📦 Starting backend server...
cd backend
if not exist "venv" (
    echo ⚠️  Virtual environment not found. Please create one first:
    echo    python -m venv venv
    echo    venv\Scripts\activate
    echo    pip install -r requirements.txt
    exit /b 1
)

call venv\Scripts\activate.bat
start "Backend Server" cmd /k "python app.py"
cd ..

REM Wait for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend
echo 🎨 Starting frontend server...
cd frontend
if not exist "node_modules" (
    echo ⚠️  Node modules not found. Installing...
    call npm install
)

start "Frontend Server" cmd /k "npm run dev"
cd ..

echo ✅ Servers started!
echo    Backend: http://localhost:5000
echo    Frontend: http://localhost:3000
echo.
echo Press any key to exit...
pause >nul

