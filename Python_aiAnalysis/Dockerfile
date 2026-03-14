FROM python:3.11-slim

WORKDIR /app

# 安裝編譯工具與 PostgreSQL headers
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# 複製 requirements.txt 並安裝套件
COPY requirements.txt .

# 先安裝其他套件，再安裝 CPU 版 torch
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# 複製程式碼
COPY . .

# CMD 可換成你的測試檔或 consumer.py
CMD ["python", "test_redis.py"]
