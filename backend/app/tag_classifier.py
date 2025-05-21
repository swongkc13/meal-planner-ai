from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch
import joblib
import os

class QueryTagger:
    def __init__(self, model_dir=None, threshold=0.3):
        model_dir = model_dir or os.path.join(os.path.dirname(__file__), "..", "tagger_model")
        self.tokenizer = DistilBertTokenizerFast.from_pretrained(model_dir)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_dir)
        self.model.eval()
        self.mlb = joblib.load(os.path.join(model_dir, "mlb.joblib"))
        self.threshold = threshold

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        probs = torch.sigmoid(logits).numpy()
        tags = self.mlb.inverse_transform(probs > self.threshold)
        return tags[0] if tags else []
