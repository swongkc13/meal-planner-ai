from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch
import joblib

# Load model
model = DistilBertForSequenceClassification.from_pretrained("tagger_model")
tokenizer = DistilBertTokenizerFast.from_pretrained("tagger_model")
mlb = joblib.load("tagger_model/mlb.joblib")
model.eval()

def predict_tags(query, threshold=0.3):
    inputs = tokenizer(query, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.sigmoid(logits).numpy()
    print(f"🔍 Raw probabilities: {probs.round(2)}")
    tags = mlb.inverse_transform(probs > threshold)
    return tags[0] if tags else []

def top_k_tags(query, k=3):
    inputs = tokenizer(query, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.sigmoid(logits).numpy().flatten()
    top_indices = probs.argsort()[-k:][::-1]
    return [(mlb.classes_[i], round(probs[i], 2)) for i in top_indices]

# Example predictions
print("Predicted tags:", predict_tags("I want something spicy and low-carb"))
print("Top 3 tag scores:", top_k_tags("I want something spicy and low-carb"))
