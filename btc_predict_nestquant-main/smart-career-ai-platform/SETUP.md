# Quick Setup Guide

## Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

## Step 1: Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database (optional - will be created automatically on first run)
python setup_db.py

# Run the Flask server
python app.py
```

The backend will be available at `http://localhost:5000`

## Step 2: Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Step 3: Test the Application

1. Open your browser and go to `http://localhost:3000`
2. Upload a PDF resume or enter your skills
3. View your career recommendations!

## Troubleshooting

### Backend won't start
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check if port 5000 is available
- Verify Python version: `python --version` (should be 3.8+)

### Frontend won't start
- Make sure all dependencies are installed: `npm install`
- Check if port 3000 is available
- Verify Node.js version: `node --version` (should be 16+)

### Database errors
- For SQLite (default): Ensure write permissions in the backend directory
- For PostgreSQL: Check database connection string and ensure PostgreSQL is running

### PDF upload errors
- Ensure the PDF file is not corrupted
- Check file size (max 16MB)
- Verify pdfminer.six is installed: `pip install pdfminer.six`

## Environment Variables

You can set the following environment variables:

- `DATABASE_URL`: Database connection string (default: SQLite)
  - Example: `postgresql://user:password@localhost/smart_career_db`
  - Or: `sqlite:///smart_career_db.db`

## Next Steps

- Add more jobs to `backend/jobs_dataset.csv`
- Customize the UI in `frontend/src/components/`
- Extend the recommendation engine in `backend/routes/recommend.py`

