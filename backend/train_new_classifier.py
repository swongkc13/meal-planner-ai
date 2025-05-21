import json
import joblib
from sklearn.preprocessing import MultiLabelBinarizer
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import torch

# Load data
with open("training_data.json", "r") as f:
    
    data = json.load(f)

texts = [item["query"] for item in data]
labels = [item["tags"] for item in data]

# Encode labels
mlb = MultiLabelBinarizer()
binary_labels = mlb.fit_transform(labels)

# Tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")
encodings = tokenizer(texts, truncation=True, padding=True)

# Dataset
class MealTagDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()} | {"labels": torch.tensor(self.labels[idx], dtype=torch.float)}
    def __len__(self):
        return len(self.labels)

train_dataset = MealTagDataset(encodings, binary_labels)

# Model
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=len(mlb.classes_), problem_type="multi_label_classification")

# Training
training_args = TrainingArguments(
    output_dir="./tagger_model",
    per_device_train_batch_size=4,
    num_train_epochs=4,
    logging_dir="./logs",
    logging_steps=10,
    save_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset
)

trainer.train()

# Save everything
model.save_pretrained("./tagger_model")
tokenizer.save_pretrained("./tagger_model")
joblib.dump(mlb, "./tagger_model/mlb.joblib")
