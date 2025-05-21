from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch
import joblib

# Load your model, tokenizer, and label encoder
model = DistilBertForSequenceClassification.from_pretrained("tagger_model")
tokenizer = DistilBertTokenizerFast.from_pretrained("tagger_model")
mlb = joblib.load("tagger_model/mlb.joblib")
model.eval()

def predict_tags(query):
    # Tokenize
    inputs = tokenizer(query, return_tensors="pt", truncation=True, padding=True)
    # Get predictions
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.sigmoid(logits).numpy()
    # Decode predictions
    tags = mlb.inverse_transform(probs > 0.5)
    return tags[0] if tags else []

# Example queries
print(predict_tags("I want something spicy and low-carb"))
print(predict_tags("Do you have a gluten-free dinner idea?"))
print(predict_tags("I’m looking for a quick vegan snack"))
