import requests
import random
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_recommendations(query, tags, max_budget, max_time, preferred_ingredients):
    search_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    response = requests.get(search_url)
    data = response.json()

    if not data.get("meals"):
        print(f"❌ No meals for query: '{query}', using fallback: 'chicken'")
        fallback_url = "https://www.themealdb.com/api/json/v1/1/search.php?s=chicken"
        response = requests.get(fallback_url)
        data = response.json()

    if not data.get("meals"):
        print("❌ Still no results after fallback.")
        return []

    raw_meals = data["meals"]
    print(f"📥 {len(raw_meals)} meals fetched")

    texts = []
    recipes = []

    for meal in raw_meals:
        ingredients = [meal.get(f"strIngredient{i}") for i in range(1, 21)]
        ingredients = [ing for ing in ingredients if ing]

        if preferred_ingredients:
            if not any(ing.lower() in [i.lower() for i in ingredients] for ing in preferred_ingredients):
                continue

        texts.append(f"{meal['strMeal']}. {meal['strInstructions']}")
        recipes.append({
            "name": meal["strMeal"],
            "description": meal["strInstructions"],
            "prep_time": random.randint(10, 30),
            "budget": random.choice([3, 5, 8, 10]),
            "tags": [meal["strCategory"], meal["strArea"]],
            "ingredients": ingredients,
            "thumbnail": meal["strMealThumb"]  # 👈 Add thumbnail URL
        })

    if not recipes:
        print("❌ No recipes after filtering.")
        return []

    recipe_embeddings = model.encode(texts)
    query_embedding = model.encode([query])[0]
    similarities = cosine_similarity([query_embedding], recipe_embeddings)[0]

    print("🔍 Similarity scores:", similarities)

    top_indices = np.argsort(similarities)[::-1][:3]
    return [recipes[i] for i in top_indices]
