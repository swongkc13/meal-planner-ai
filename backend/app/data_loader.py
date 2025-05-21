import os
import json
from app.config import Config
from app.mealdb_client import fetch_meals_from_mealdb

def load_or_fetch_meals():
    if os.path.exists(Config.CACHE_FILE):
        print("📦 Loading meals from cache...")
        with open(Config.CACHE_FILE, "r") as f:
            return json.load(f)

    print("🌐 Fetching meals from TheMealDB...")
    meals = fetch_meals_from_mealdb()

    with open(Config.CACHE_FILE, "w") as f:
        json.dump(meals, f, indent=2)

    return meals
