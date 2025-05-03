from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')  # Free, small, fast

with open("recipes.json", "r") as f:
    recipes = json.load(f)
    descriptions = [r["description"] for r in recipes]
    embeddings = model.encode(descriptions)

def recommend(query, top_n=3):
    query_embedding = model.encode(query)
    similarities = util.cos_sim(query_embedding, embeddings)[0]
    top_matches = sorted(zip(recipes, similarities), key=lambda x: -x[1])
    return [match[0] for match in top_matches[:top_n]]
