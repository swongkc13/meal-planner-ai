from flask import Blueprint, request, jsonify
from app.recommender import MealRecommender
from app.data_loader import load_or_fetch_meals
from app.config import Config
from app.tag_classifier import QueryTagger  # ✅ Updated transformer-based classifier
from app.generator import generate_meal    # Your GPT-2 generator

recommend_bp = Blueprint("recommend", __name__)

# ✅ Initialize components once
meals = load_or_fetch_meals()
recommender = MealRecommender(Config.MODEL_NAME, meals)
tagger = QueryTagger()  # Uses ./tagger_model

# -----------------------------
# 📌 /recommend
# -----------------------------
@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Missing 'query'"}), 400

    # 🧠 Predict tags using new model
    predicted_tags = tagger.predict(query)

    # 🤖 Recommend meals (tag/semantic-based logic can evolve later)
    results = recommender.recommend(query, top_k=Config.TOP_K)

    return jsonify({
        "tags": predicted_tags,
        "results": results
    })

# -----------------------------
# ✨ /generate-meal
# -----------------------------
@recommend_bp.route("/generate-meal", methods=["GET"])
def generate_meal_endpoint():
    prompt = request.args.get("prompt", "Name:")
    text = generate_meal(prompt)
    return jsonify({"generated": text})
