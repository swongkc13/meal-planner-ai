import json

def recommend(query):
    with open("recipes.json", "r") as f:
        recipes = json.load(f)

        results = [
            recipes for recipe in recipes
            if query.lower() in recipe["description"].lower()
        ]
        return results
    