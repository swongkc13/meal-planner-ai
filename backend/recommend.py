import requests
import random
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# Global cache
MEAL_DATA = []
MEAL_EMBEDDINGS = []

def fetch_and_cache_meals():
    print("📥 Fetching and caching meals...")
    combined_meals = []

    # Optionally use multiple queries to diversify results
    for q in ["chicken", "beef", "rice", "pasta", "fish", "soup", "salad"]:
        response = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={q}")
        data = response.json()
        if data.get("meals"):
            combined_meals.extend(data["meals"])

    print(f"✅ Fetched {len(combined_meals)} meals in total.")

    cached_meals = []
    texts = []

    for meal in combined_meals:
        if not meal["strInstructions"]:
            continue

        ingredients = [meal.get(f"strIngredient{i}") for i in range(1, 21)]
        ingredients = [i for i in ingredients if i]

        text = f"{meal['strMeal']}. {meal['strInstructions']}"
        texts.append(text)

        cached_meals.append({
            "name": meal["strMeal"],
            "description": meal["strInstructions"],
            "prep_time": random.randint(10, 30),
            "budget": random.choice([3, 5, 8, 10]),
            "tags": [meal["strCategory"], meal["strArea"]],
            "ingredients": ingredients,
            "thumbnail": meal["strMealThumb"]
        })

    embeddings = model.encode(texts)
    return cached_meals, embeddings

# 🔁 Load cache at module load
MEAL_DATA, MEAL_EMBEDDINGS = fetch_and_cache_meals()

def get_recommendations(query, tags, max_budget, max_time, preferred_ingredients):
    if not MEAL_DATA:
        print("⚠️ No cached meals available.")
        return []

    query_embedding = model.encode([query])[0]
    similarities = cosine_similarity([query_embedding], MEAL_EMBEDDINGS)[0]

    # Get top matches
    top_indices = np.argsort(similarities)[::-1][:3]
    top_meals = [MEAL_DATA[i] for i in top_indices]

    return top_meals
