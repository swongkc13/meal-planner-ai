from flask import Blueprint, request, jsonify
from app.recommender import MealRecommender
from app.data_loader import load_or_fetch_meals
from app.config import Config
from app.tag_classifier import QueryTagger  # 🧠 AI tag predictor
from app.generator import generate_meal    # 🧠 GPT-2 meal generator

recommend_bp = Blueprint("recommend", __name__)

# Initialize components once
recommender = MealRecommender(Config.MODEL_NAME, load_or_fetch_meals())
tagger = QueryTagger()

# -----------------------------
# 📌 /recommend route
# -----------------------------
@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Missing 'query'"}), 400

    predicted_tags = tagger.predict(query)
    results = recommender.recommend(query, top_k=Config.TOP_K)

    return jsonify({
        "tags": predicted_tags,
        "results": results
    })

# -----------------------------
# ✨ /generate-meal route
# -----------------------------
@recommend_bp.route("/generate-meal", methods=["GET"])
def generate_meal_endpoint():
    prompt = request.args.get("prompt", "Name:")
    text = generate_meal(prompt)
    return jsonify({"generated": text})
