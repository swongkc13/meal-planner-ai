# train_classifier.py

import json
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression

# Load training data
with open("training_data.json") as f:
    data = json.load(f)

texts = [item["query"] for item in data]
tags = list(set(tag for item in data for tag in item["tags"]))
tag_index = {tag: i for i, tag in enumerate(tags)}

# Convert tags to multi-hot vectors
import numpy as np
y = np.zeros((len(data), len(tags)))
for i, item in enumerate(data):
    for tag in item["tags"]:
        y[i, tag_index[tag]] = 1

# Train classifier
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultiOutputClassifier(LogisticRegression()))
])
pipeline.fit(texts, y)

# Save
joblib.dump((pipeline, tags), "meal_query_classifier.joblib")
print("✅ Model trained and saved as meal_query_classifier.joblib")
