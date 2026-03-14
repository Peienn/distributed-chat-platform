FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# 安裝小套件
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "test_redis.py"]
