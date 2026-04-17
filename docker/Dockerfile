# ==============================
# Base Python Image
# ==============================
FROM python:3.10-slim

# ==============================
# Set working directory
# ==============================
WORKDIR /app

# ==============================
# Install system dependencies (important for ML + chroma + builds)
# ==============================
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# ==============================
# Copy requirements first (for caching)
# ==============================
COPY requirements.txt .

# ==============================
# Install Python dependencies
# ==============================
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ==============================
# Copy full project
# ==============================
COPY . .

# ==============================
# Environment variables (IMPORTANT for Streamlit)
# ==============================
ENV PYTHONUNBUFFERED=1

# Streamlit config for Docker
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# ==============================
# Expose port
# ==============================
EXPOSE 8501

# ==============================
# Run Streamlit app
# ==============================
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]