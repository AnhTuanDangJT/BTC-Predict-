# Backend Startup Script for Windows PowerShell
Write-Host "🚀 Starting Smart Career AI Platform - Backend" -ForegroundColor Green

# Navigate to backend directory
Set-Location backend

# Check if virtual environment exists
if (-Not (Test-Path "venv")) {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "🔧 Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Check if requirements are installed
if (-Not (Test-Path "venv\Lib\site-packages\flask")) {
    Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

# Run the Flask server
Write-Host "✅ Starting Flask server on http://localhost:5000" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
python app.py

