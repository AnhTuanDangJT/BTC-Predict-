# ⚡ Quick Start Guide - Windows

## 🚀 Fastest Way to Run (Using PowerShell Scripts)

### Option 1: Use the Provided Scripts (Easiest)

1. **Open PowerShell in the project root directory**

2. **Run Backend (Terminal 1):**
```powershell
.\run-backend.ps1
```

3. **Open a NEW PowerShell window and run Frontend (Terminal 2):**
```powershell
.\run-frontend.ps1
```

4. **Open your browser:** `http://localhost:3000`

---

## 📝 Manual Setup (Step by Step)

### Step 1: Setup Backend

**Open PowerShell and run:**

```powershell
# Navigate to backend
cd smart-career-ai-platform\backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

✅ Backend will run on `http://localhost:5000`

### Step 2: Setup Frontend (New Terminal)

**Open a NEW PowerShell window:**

```powershell
# Navigate to frontend
cd smart-career-ai-platform\frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

✅ Frontend will run on `http://localhost:3000`

### Step 3: Use the Application

1. Open browser: `http://localhost:3000`
2. Upload a PDF resume OR enter your skills
3. View career recommendations!

---

## 🔍 Troubleshooting

### If PowerShell script execution is blocked:

```powershell
# Run this first to allow script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### If port 5000 is already in use:

```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace <PID> with the actual process ID)
taskkill /PID <PID> /F
```

### If npm install fails:

```powershell
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
Remove-Item -Recurse -Force node_modules
npm install
```

### If Python modules are missing:

```powershell
# Make sure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Reinstall requirements
pip install -r requirements.txt
```

---

## ✅ Success Checklist

- [ ] Backend shows: `Running on http://127.0.0.1:5000`
- [ ] Frontend shows: `Local: http://localhost:3000/`
- [ ] Browser opens the application
- [ ] You can upload a resume or enter skills
- [ ] Recommendations appear after processing

---

## 📚 More Information

- See `RUN.md` for detailed instructions
- See `README.md` for full documentation
- See `SETUP.md` for setup details

---

## 🆘 Need Help?

1. Check both terminal windows for error messages
2. Check browser console (F12 → Console tab)
3. Verify Python version: `python --version` (need 3.8+)
4. Verify Node.js version: `node --version` (need 16+)

