# app/recommender.py

from sentence_transformers import SentenceTransformer, util
import torch

class MealRecommender:
    def __init__(self, model_name, meals):
        self.model = SentenceTransformer(model_name)
        self.meals = meals
        self.texts = [m["description"] for m in meals]
        self.embeddings = self.model.encode(self.texts, convert_to_tensor=True)

    def recommend(self, query, top_k=3):
        query_vec = self.model.encode(query, convert_to_tensor=True)
        similarities = util.cos_sim(query_vec, self.embeddings)[0]
        top_indices = torch.topk(similarities, k=top_k).indices.tolist()
        return [self.meals[i] for i in top_indices]
