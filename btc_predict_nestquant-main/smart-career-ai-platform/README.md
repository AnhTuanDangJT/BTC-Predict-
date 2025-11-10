# Smart Career AI Platform

A full-stack AI-powered career recommendation platform where users upload their resumes or enter skills to receive personalized career path suggestions using machine learning.

## 🚀 Features

- **Resume Upload**: Upload PDF resumes and extract text automatically
- **Skill Input**: Enter skills and experience directly as text
- **AI Recommendations**: Get personalized career recommendations using TF-IDF and cosine similarity
- **Visual Analytics**: View recommendations with interactive charts using Recharts
- **User Dashboard**: Track and view all your career recommendations

## 🧱 Tech Stack

### Backend
- Flask - Web framework
- SQLAlchemy - ORM for database management
- PostgreSQL/SQLite - Database
- scikit-learn - Machine learning (TF-IDF, cosine similarity)
- pdfminer.six - PDF text extraction
- Flask-CORS - Cross-origin resource sharing

### Frontend
- React - UI library
- Vite - Build tool
- TailwindCSS - Styling
- Axios - HTTP client
- Recharts - Data visualization
- React Router - Routing

## 📁 Project Structure

```
smart-career-ai-platform/
│
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── models.py              # Database models
│   ├── database.py            # Database configuration
│   ├── routes/
│   │   ├── upload_resume.py   # Resume upload endpoint
│   │   └── recommend.py       # Recommendation endpoint
│   ├── utils/
│   │   └── extract_text.py    # PDF text extraction
│   ├── jobs_dataset.csv       # Job descriptions dataset
│   └── requirements.txt       # Python dependencies
│
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── ResumeUploader.jsx    # Resume upload component
    │   │   └── Recommendations.jsx   # Recommendations display
    │   ├── pages/
    │   │   ├── Home.jsx              # Home page
    │   │   └── Dashboard.jsx         # Dashboard page
    │   ├── services/
    │   │   └── api.js                # API service
    │   ├── App.jsx                   # Main app component
    │   └── main.jsx                  # Entry point
    ├── package.json
    └── tailwind.config.js
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- PostgreSQL (optional, SQLite is used by default)
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
   - For SQLite (default): The database will be created automatically
   - For PostgreSQL: Set the `DATABASE_URL` environment variable:
     ```bash
     export DATABASE_URL=postgresql://username:password@localhost/smart_career_db
     ```

5. Run the Flask application:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:3000`

## 🎯 Usage

1. **Upload Resume**:
   - Go to the Home page
   - Click on "Upload Resume" tab
   - Select a PDF file and upload
   - The system will extract text and generate recommendations

2. **Enter Skills**:
   - Go to the Home page
   - Click on "Enter Skills" tab
   - Enter your skills, experience, or career interests
   - Click "Get Recommendations"

3. **View Dashboard**:
   - Navigate to the Dashboard page
   - Enter your user ID to view all your recommendations
   - View analytics and charts

## 📊 API Endpoints

### POST /api/upload_resume
Upload a PDF resume and extract text.

**Request:**
- Form data with `file` (PDF) and optional `email`

**Response:**
```json
{
  "success": true,
  "message": "Resume uploaded and processed successfully",
  "extracted_text": "...",
  "user_id": 1,
  "resume_id": 1
}
```

### POST /api/upload_text
Upload text input directly.

**Request:**
```json
{
  "text": "I have experience in Python, machine learning...",
  "email": "user@example.com"
}
```

### POST /api/recommend
Get career recommendations based on text input.

**Request:**
```json
{
  "text": "I have experience in Python, machine learning...",
  "user_id": 1,
  "top_n": 5
}
```

**Response:**
```json
{
  "success": true,
  "recommendations": [
    {
      "title": "Data Scientist",
      "description": "...",
      "score": 85.5
    }
  ],
  "count": 5
}
```

### GET /api/recommendations/<user_id>
Get all stored recommendations for a user.

### GET /api/health
Health check endpoint.

## 🤖 AI Recommendation Engine

The platform uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization combined with cosine similarity to match user profiles with job descriptions:

1. **Text Processing**: User input and job descriptions are processed
2. **TF-IDF Vectorization**: Text is converted to numerical vectors
3. **Cosine Similarity**: Similarity scores are calculated between user profile and job descriptions
4. **Ranking**: Top matches are ranked by similarity score

## 📝 Jobs Dataset

The `jobs_dataset.csv` file contains job titles and descriptions. You can:
- Add more jobs to the dataset
- Use a larger dataset from Kaggle or other sources
- Customize job descriptions to match your needs

## 🔧 Configuration

### Backend Configuration

Edit `backend/app.py` to configure:
- Database URL (via environment variable `DATABASE_URL`)
- File upload size limit
- CORS settings

### Frontend Configuration

Edit `frontend/src/services/api.js` to configure:
- API base URL
- Request timeouts
- Default headers

## 🚨 Troubleshooting

### Backend Issues

1. **Database connection error**:
   - Ensure PostgreSQL is running (if using PostgreSQL)
   - Check database URL in environment variables
   - For SQLite, ensure write permissions in the backend directory

2. **PDF extraction error**:
   - Ensure the PDF file is not corrupted
   - Check file size (max 16MB)
   - Verify pdfminer.six is installed correctly

### Frontend Issues

1. **API connection error**:
   - Ensure backend is running on port 5000
   - Check CORS settings in backend
   - Verify API base URL in `api.js`

2. **Build errors**:
   - Clear node_modules and reinstall: `rm -rf node_modules && npm install`
   - Check Node.js version (16+)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or support, please open an issue on the repository.

