from flask import Blueprint, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os
from database import db
from models import Recommendation, User

bp = Blueprint("recommend", __name__)

# Load jobs dataset
JOBS_DATASET_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'jobs_dataset.csv')

def load_jobs_dataset():
    """Load the jobs dataset from CSV"""
    try:
        if os.path.exists(JOBS_DATASET_PATH):
            df = pd.read_csv(JOBS_DATASET_PATH)
            return df
        else:
            # Return empty dataframe with required columns
            return pd.DataFrame(columns=['title', 'description'])
    except Exception as e:
        print(f"Error loading jobs dataset: {str(e)}")
        return pd.DataFrame(columns=['title', 'description'])

@bp.route("/recommend", methods=["POST"])
def recommend():
    """
    Generate career recommendations based on user text input
    """
    try:
        data = request.get_json()
        user_text = data.get("text", "")
        user_id = data.get("user_id", None)
        top_n = data.get("top_n", 5)
        
        if not user_text or len(user_text.strip()) < 10:
            return jsonify({'error': 'Text input is too short. Please provide more details about your skills or experience.'}), 400
        
        # Load jobs dataset
        jobs_df = load_jobs_dataset()
        
        if jobs_df.empty or 'description' not in jobs_df.columns or 'title' not in jobs_df.columns:
            return jsonify({'error': 'Jobs dataset is not available or malformed'}), 500
        
        # Prepare documents for TF-IDF
        documents = jobs_df['description'].tolist() + [user_text]
        
        # Create TF-IDF vectorizer
        vectorizer = TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1, 2))
        tfidf_matrix = vectorizer.fit_transform(documents)
        
        # Calculate cosine similarity
        user_vector = tfidf_matrix[-1]
        job_vectors = tfidf_matrix[:-1]
        
        cosine_sim = cosine_similarity(user_vector, job_vectors)
        scores = list(enumerate(cosine_sim[0]))
        
        # Get top matches
        top_matches = sorted(scores, key=lambda x: x[1], reverse=True)[:top_n]
        
        # Prepare results
        results = []
        for idx, score in top_matches:
            if score > 0:  # Only include matches with positive similarity
                job_title = jobs_df.iloc[idx]['title']
                job_description = jobs_df.iloc[idx].get('description', '')
                confidence_score = round(score * 100, 2)
                
                results.append({
                    'title': job_title,
                    'description': job_description,
                    'score': confidence_score
                })
                
                # Save recommendation to database if user_id is provided
                if user_id:
                    try:
                        user = User.query.get(user_id)
                        if user:
                            recommendation = Recommendation(
                                user_id=user_id,
                                job_title=job_title,
                                score=confidence_score
                            )
                            db.session.add(recommendation)
                    except Exception as e:
                        print(f"Error saving recommendation: {str(e)}")
        
        if user_id:
            db.session.commit()
        
        return jsonify({
            'success': True,
            'recommendations': results,
            'count': len(results)
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route("/recommendations/<int:user_id>", methods=["GET"])
def get_recommendations(user_id):
    """
    Get stored recommendations for a user
    """
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        recommendations = Recommendation.query.filter_by(user_id=user_id).order_by(Recommendation.score.desc()).all()
        
        results = [
            {
                'id': rec.id,
                'job_title': rec.job_title,
                'score': rec.score,
                'created_at': rec.created_at.isoformat()
            }
            for rec in recommendations
        ]
        
        return jsonify({
            'success': True,
            'user_id': user_id,
            'recommendations': results,
            'count': len(results)
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

