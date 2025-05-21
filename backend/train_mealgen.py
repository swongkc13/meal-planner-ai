import json

with open("cached_meals.json", "r", encoding="utf-8") as f:
    meals = json.load(f)

with open("meal_corpus.txt", "w", encoding="utf-8") as out:
    for meal in meals:
        ingredients = ", ".join(meal.get("ingredients", []))
        text = (
            f"Name: {meal['name']}\n"
            f"Ingredients: {ingredients}\n"
            f"Instructions: {meal['instructions']}\n"
            "---\n"
        )
        out.write(text)

print("✅ meal_corpus.txt created!")
