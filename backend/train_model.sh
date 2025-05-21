#!/bin/bash

# For Linux/macOS/Git Bash on Windows

echo "📦 Building Docker image: meal-trainer"
docker build -t meal-trainer .

echo "🏃 Running training container..."
docker run --rm -v "$(pwd)/tagger_model:/app/tagger_model" meal-trainer

echo "✅ Model trained and saved to ./tagger_model/"