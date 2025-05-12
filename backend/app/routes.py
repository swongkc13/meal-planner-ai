# app/routes.py

from flask import Blueprint, request, jsonify
from app.recommender import MealRecommender
from app.data_loader import load_or_fetch_meals
from app.config import Config

recommend_bp = Blueprint("recommend", __name__)
recommender = MealRecommender(Config.MODEL_NAME, load_or_fetch_meals())

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Missing 'query'"}), 400
    results = recommender.recommend(query, top_k=Config.TOP_K)
    return jsonify(results)
