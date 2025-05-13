import joblib
import numpy as np

class QueryTagger:
    def __init__(self, model_path="meal_query_classifier.joblib"):
        self.pipeline, self.tags = joblib.load(model_path)

    def predict(self, query, threshold=0.5):
        proba = self.pipeline.predict_proba([query])
        predicted_tags = []

        # Loop over each tag's probability
        for i, class_proba in enumerate(proba):
            if class_proba[0][1] >= threshold:  # get probability of "1" (positive class)
                predicted_tags.append(self.tags[i])

        return predicted_tags
