FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y tk && rm -rf /var/lib/apt/lists/*

COPY app /app/app
COPY config /app/config

CMD ["python", "/app/app/main.py"]