"""
Database setup script
Run this script to initialize the database and create tables
"""
from flask import Flask
from database import db, init_db
import os

# Create Flask app instance
app = Flask(__name__)
database_url = os.getenv('DATABASE_URL', 'sqlite:///smart_career_db.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Import models to register them with SQLAlchemy
from models import User, Resume, Recommendation

def setup_database():
    """Initialize the database and create all tables"""
    with app.app_context():
        print("Creating database tables...")
        init_db()
        print("Database tables created successfully!")
        print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

if __name__ == '__main__':
    setup_database()

