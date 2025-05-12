# app/mealdb_client.py

import requests

def fetch_meals_from_mealdb(query="chicken"):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    response = requests.get(url)
    data = response.json()
    meals = data.get("meals", [])

    def extract_ingredients(meal):
        ingredients = []
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")
            if ingredient and ingredient.strip():
                if measure:
                    ingredients.append(f"{measure.strip()} {ingredient.strip()}")
                else:
                    ingredients.append(ingredient.strip())
        return ingredients

    enriched = []
    for meal in meals:
        enriched.append({
            "id": meal.get("idMeal"),
            "name": meal.get("strMeal"),
            "category": meal.get("strCategory"),
            "area": meal.get("strArea"),
            "instructions": meal.get("strInstructions"),
            "thumbnail": meal.get("strMealThumb"),
            "youtube": meal.get("strYoutube"),
            "ingredients": extract_ingredients(meal),
            "description": f"{meal['strMeal']} - {meal.get('strInstructions', '')[:150]}..."
        })

    return enriched
