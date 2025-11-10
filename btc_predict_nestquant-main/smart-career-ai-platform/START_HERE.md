# 🎯 START HERE - How to Run the Project

## ⚡ Quick Commands (Copy & Paste)

### Terminal 1 - Backend (Flask Server)

```powershell
cd smart-career-ai-platform\backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

**Wait until you see:** `Running on http://127.0.0.1:5000`

---

### Terminal 2 - Frontend (React Server)

**Open a NEW PowerShell window** and run:

```powershell
cd smart-career-ai-platform\frontend
npm install
npm run dev
```

**Wait until you see:** `Local: http://localhost:3000/`

---

### Step 3 - Open Browser

1. Open your web browser
2. Go to: **http://localhost:3000**
3. Start using the application! 🎉

---

## 📋 Detailed Instructions

### Backend Setup (First Time)

1. **Open PowerShell**
2. **Navigate to backend folder:**
   ```powershell
   cd smart-career-ai-platform\backend
   ```

3. **Create virtual environment:**
   ```powershell
   python -m venv venv
   ```

4. **Activate virtual environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   You should see `(venv)` in your prompt.

5. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
   This may take a few minutes.

6. **Start the server:**
   ```powershell
   python app.py
   ```

7. **You should see:**
   ```
   * Running on http://127.0.0.1:5000
   * Debug mode: on
   ```
   **Keep this terminal open!** ⚠️

---

### Frontend Setup (First Time)

1. **Open a NEW PowerShell window** (keep backend running)

2. **Navigate to frontend folder:**
   ```powershell
   cd smart-career-ai-platform\frontend
   ```

3. **Install dependencies:**
   ```powershell
   npm install
   ```
   This may take a few minutes.

4. **Start the development server:**
   ```powershell
   npm run dev
   ```

5. **You should see:**
   ```
   VITE v5.x.x  ready in xxx ms
   ➜  Local:   http://localhost:3000/
   ```

6. **Keep this terminal open too!** ⚠️

---

### Using the Application

1. **Open your browser** and go to: `http://localhost:3000`

2. **You'll see the Smart Career AI Platform homepage**

3. **To get recommendations:**
   - **Option A:** Upload a PDF resume
     - Click "Upload Resume" tab
     - Select a PDF file
     - Click "Upload and Analyze"
   
   - **Option B:** Enter your skills
     - Click "Enter Skills" tab
     - Type your skills and experience
     - Click "Get Recommendations"

4. **View recommendations** - They'll appear on the right side with charts and scores

5. **Check Dashboard** - Click "Dashboard" in the navigation to view all your recommendations

---

## 🔧 Troubleshooting

### "Execution Policy" Error when running scripts:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Port 5000 already in use:

```powershell
# Find what's using port 5000
netstat -ano | findstr :5000

# Kill the process (replace <PID> with the number from above)
taskkill /PID <PID> /F
```

### "Module not found" errors:

```powershell
# Make sure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Reinstall requirements
pip install -r requirements.txt
```

### Frontend won't start:

```powershell
# Delete node_modules and reinstall
Remove-Item -Recurse -Force node_modules
npm install
npm run dev
```

### Cannot connect to backend:

- Make sure backend is running on port 5000
- Check backend terminal for errors
- Make sure both servers are running simultaneously

---

## ✅ Success Checklist

- [ ] Backend terminal shows: `Running on http://127.0.0.1:5000`
- [ ] Frontend terminal shows: `Local: http://localhost:3000/`
- [ ] Browser opens the application successfully
- [ ] You can upload a resume or enter skills
- [ ] Recommendations appear after processing

---

## 🚀 Next Steps After Setup

1. **Upload a resume** or **enter your skills**
2. **View your career recommendations**
3. **Check the Dashboard** to see all recommendations
4. **Explore the code** to customize it for your needs

---

## 📚 Additional Resources

- **RUN.md** - Detailed running instructions
- **README.md** - Full project documentation
- **SETUP.md** - Setup guide
- **QUICK_START.md** - Quick reference

---

## 🆘 Still Having Issues?

1. Check both terminal windows for error messages
2. Open browser console (F12 → Console tab) for frontend errors
3. Verify Python version: `python --version` (need 3.8+)
4. Verify Node.js version: `node --version` (need 16+)
5. Make sure both servers are running at the same time

---

**Happy Coding! 🎉**

