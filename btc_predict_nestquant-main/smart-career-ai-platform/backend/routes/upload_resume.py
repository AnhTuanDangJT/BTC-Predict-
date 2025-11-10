from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from utils.extract_text import extract_text_from_pdf_bytes
from database import db
from models import User, Resume
from datetime import datetime

bp = Blueprint("upload_resume", __name__)

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route("/upload_resume", methods=["POST"])
def upload_resume():
    """
    Upload a PDF resume and extract text from it
    """
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        email = request.form.get('email', 'anonymous@example.com')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400
        
        # Read file bytes
        file_bytes = file.read()
        
        # Extract text from PDF
        extracted_text = extract_text_from_pdf_bytes(file_bytes)
        
        if not extracted_text or len(extracted_text.strip()) < 50:
            return jsonify({'error': 'Could not extract meaningful text from PDF'}), 400
        
        # Get or create user
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email)
            db.session.add(user)
            db.session.commit()
        
        # Save resume record
        resume = Resume(
            user_id=user.id,
            filename=secure_filename(file.filename),
            extracted_text=extracted_text
        )
        db.session.add(resume)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Resume uploaded and processed successfully',
            'extracted_text': extracted_text,
            'user_id': user.id,
            'resume_id': resume.id
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route("/upload_text", methods=["POST"])
def upload_text():
    """
    Accept text input directly (skills, experience, etc.)
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        email = data.get('email', 'anonymous@example.com')
        
        if not text or len(text.strip()) < 10:
            return jsonify({'error': 'Text input is too short'}), 400
        
        # Get or create user
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email)
            db.session.add(user)
            db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Text processed successfully',
            'text': text,
            'user_id': user.id
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

