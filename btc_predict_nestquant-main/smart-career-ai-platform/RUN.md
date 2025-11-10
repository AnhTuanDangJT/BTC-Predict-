# 🚀 How to Run the Smart Career AI Platform

## Step-by-Step Instructions

### Prerequisites Check
- ✅ Python 3.8 or higher installed
- ✅ Node.js 16 or higher installed
- ✅ npm or yarn installed

### Step 1: Backend Setup

1. **Open a terminal and navigate to the backend directory:**
```bash
cd smart-career-ai-platform/backend
```

2. **Create a virtual environment (recommended):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

4. **Initialize the database (optional - will be created automatically):**
```bash
python setup_db.py
```

5. **Start the Flask backend server:**
```bash
python app.py
```

✅ **Backend is now running on `http://localhost:5000`**

You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 2: Frontend Setup

1. **Open a NEW terminal window** (keep the backend running)

2. **Navigate to the frontend directory:**
```bash
cd smart-career-ai-platform/frontend
```

3. **Install Node.js dependencies:**
```bash
npm install
```

4. **Start the development server:**
```bash
npm run dev
```

✅ **Frontend is now running on `http://localhost:3000`**

You should see output like:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

### Step 3: Access the Application

1. **Open your web browser**
2. **Navigate to:** `http://localhost:3000`
3. **You should see the Smart Career AI Platform homepage**

### Step 4: Test the Application

1. **Upload a Resume:**
   - Click on "Upload Resume" tab
   - Select a PDF file
   - Click "Upload and Analyze"
   - Wait for recommendations to appear

2. **Or Enter Skills:**
   - Click on "Enter Skills" tab
   - Type your skills and experience
   - Click "Get Recommendations"

3. **View Dashboard:**
   - Click on "Dashboard" in the navigation
   - Enter your user ID (from the upload/input response)
   - View your stored recommendations

## 🔧 Troubleshooting

### Backend Issues

**Problem: Port 5000 already in use**
```bash
# Windows - Find and kill process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux - Find and kill process using port 5000
lsof -ti:5000 | xargs kill -9
```

**Problem: Module not found errors**
```bash
# Make sure you're in the virtual environment
# Reinstall dependencies
pip install -r requirements.txt
```

**Problem: Database errors**
```bash
# Delete the database file and restart
# SQLite database will be recreated automatically
rm smart_career_db.db  # Mac/Linux
del smart_career_db.db  # Windows
python app.py
```

### Frontend Issues

**Problem: Port 3000 already in use**
```bash
# The Vite dev server will automatically use the next available port
# Or modify vite.config.js to use a different port
```

**Problem: npm install fails**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules  # Mac/Linux
rmdir /s node_modules  # Windows
npm install
```

**Problem: Cannot connect to backend**
```bash
# Make sure backend is running on port 5000
# Check backend/backend/app.py is running
# Check CORS is enabled in backend
```

### Common Issues

**Problem: PDF upload fails**
- Ensure PDF file is not corrupted
- Check file size is under 16MB
- Verify pdfminer.six is installed: `pip install pdfminer.six`

**Problem: No recommendations appear**
- Check browser console for errors (F12)
- Verify backend is running
- Check backend terminal for error messages
- Ensure jobs_dataset.csv exists in backend directory

**Problem: Database errors**
- For SQLite: Ensure write permissions in backend directory
- For PostgreSQL: Check DATABASE_URL environment variable
- Run `python setup_db.py` to recreate tables

## 🎯 Quick Start Commands (All-in-One)

### Windows (PowerShell)
```powershell
# Terminal 1 - Backend
cd smart-career-ai-platform\backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

# Terminal 2 - Frontend (new window)
cd smart-career-ai-platform\frontend
npm install
npm run dev
```

### Mac/Linux (Bash)
```bash
# Terminal 1 - Backend
cd smart-career-ai-platform/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

# Terminal 2 - Frontend (new window)
cd smart-career-ai-platform/frontend
npm install
npm run dev
```

## 📝 Notes

- **Keep both terminals open** - Backend and frontend need to run simultaneously
- **Backend must run first** - Frontend depends on the backend API
- **Database is created automatically** - No manual database setup needed for SQLite
- **Hot reload is enabled** - Changes to code will automatically refresh

## ✅ Success Indicators

You know everything is working when:
1. ✅ Backend shows "Running on http://127.0.0.1:5000"
2. ✅ Frontend shows "Local: http://localhost:3000/"
3. ✅ Browser opens and shows the Smart Career AI Platform homepage
4. ✅ You can upload a resume or enter skills
5. ✅ Recommendations appear after processing

## 🆘 Need Help?

If you encounter any issues:
1. Check the error messages in the terminal
2. Check the browser console (F12 → Console tab)
3. Verify all dependencies are installed
4. Ensure both servers are running
5. Check the README.md for more information

