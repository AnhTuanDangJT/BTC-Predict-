# Frontend Startup Script for Windows PowerShell
Write-Host "🎨 Starting Smart Career AI Platform - Frontend" -ForegroundColor Green

# Navigate to frontend directory
Set-Location frontend

# Check if node_modules exists
if (-Not (Test-Path "node_modules")) {
    Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
    npm install
}

# Run the development server
Write-Host "✅ Starting development server on http://localhost:3000" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
npm run dev

