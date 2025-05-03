FROM python:3.10

# Set working directory
WORKDIR /app

# Install system-level build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libopenblas-dev \
    liblapack-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements first and install (better caching)
COPY requirements.txt .
RUN pip install --default-timeout=300 -r requirements.txt

# Copy rest of the code
COPY . .

# Start your app
CMD ["python", "app.py"]
