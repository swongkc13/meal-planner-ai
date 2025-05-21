

class Config:
    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
    CACHE_FILE = "cached_meals.json"
    TOP_K = 3
    MEALDB_URL = "https://www.themealdb.com/api/json/v1/1/search.php?s="  # Meal search endpoint
