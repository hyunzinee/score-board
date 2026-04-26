# Python 경량 이미지
FROM python:3.11-slim

# 작업 디렉토리
WORKDIR /app

# 시스템 패키지 (psycopg2 필요)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY ./app ./app

# 포트
EXPOSE 10000

# 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
