from flask import Blueprint, request, jsonify
from app.recommender import MealRecommender
from app.data_loader import load_or_fetch_meals
from app.config import Config
from app.tag_classifier import QueryTagger  # 🧠 Import the classifier

recommend_bp = Blueprint("recommend", __name__)
recommender = MealRecommender(Config.MODEL_NAME, load_or_fetch_meals())
tagger = QueryTagger()  # 🧠 Load the trained model

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Missing 'query'"}), 400

    # 🧠 Predict tags using your AI
    predicted_tags = tagger.predict(query)

    # 🔍 Get top recommended meals
    results = recommender.recommend(query, top_k=Config.TOP_K)

    return jsonify({
        "tags": predicted_tags,  # 👈 New field
        "results": results
    })
