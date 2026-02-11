# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy app and frontend
COPY app /app/app
COPY frontend /app/frontend
COPY config /app/config

# Install Python dependencies
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]