# backend/Dockerfile

# Use lightweight Python base
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
 && rm -rf /var/lib/apt/lists/*

# Copy all backend files into the image
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the default command to run the training script
CMD ["python", "train_new_classifier.py"]

# Add this to requirements.txt or directly in Dockerfile
RUN pip install "huggingface_hub[hf_xet]"