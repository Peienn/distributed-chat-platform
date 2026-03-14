FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# 安裝 requirements.txt 內的全部套件
RUN pip install --no-cache-dir -r requirements.txt \
    torch --index-url https://download.pytorch.org/whl/cpu

COPY . .

CMD ["python", "test_redis.py"]
