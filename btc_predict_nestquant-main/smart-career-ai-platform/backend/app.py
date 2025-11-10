from flask import Flask, jsonify
from flask_cors import CORS
from database import db, init_db
from routes.upload_resume import bp as upload_bp
from routes.recommend import bp as recommend_bp
import os

app = Flask(__name__)
# Use environment variable or default to SQLite for easier setup
database_url = os.getenv('DATABASE_URL', 'sqlite:///smart_career_db.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

CORS(app)

# Initialize database
db.init_app(app)

# Import models to register them with SQLAlchemy
from models import User, Resume, Recommendation

# Register blueprints
app.register_blueprint(upload_bp, url_prefix='/api')
app.register_blueprint(recommend_bp, url_prefix='/api')

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'Smart Career AI Platform API is running'})

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True, port=5000)

