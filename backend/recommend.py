import requests
import random

def get_recommendations(query, tags, max_budget, max_time, preferred_ingredients):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    response = requests.get(url)
    data = response.json()

    if not data.get("meals"):
        return []

    results = []
    for meal in data["meals"]:
        ingredients = [meal.get(f"strIngredient{i}") for i in range(1, 21)]
        ingredients = [ing for ing in ingredients if ing]

        if preferred_ingredients:
            if not any(ing.lower() in [i.lower() for i in ingredients] for ing in preferred_ingredients):
                continue

        results.append({
            "name": meal["strMeal"],
            "description": meal["strInstructions"],
            "prep_time": random.randint(10, 30),  # Simulated
            "budget": random.choice([3, 5, 8, 10]),  # Simulated
            "tags": [meal["strCategory"], meal["strArea"]],
            "ingredients": ingredients
        })

    return results[:3]
