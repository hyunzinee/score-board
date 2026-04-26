# score-board

# Structure
```
project-root/
 ├── app/
 │    ├── __init__.py
 │    ├── main.py
 │    ├── db.py
 │    ├── models.py
 │    ├── schemas.py
 │    ├── crud.py
 │    └── deps.py
 ├── requirements.txt
 ├── Dockerfile
 └── .dockerignore
```

# How to local test
```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

## Swagger:
```
http://localhost:10000/docs
```

# How to release through Render
## 7.1 서비스 생성

👉 Render 접속

New + → Web Service
GitHub repo 연결

## 7.2 설정
Build & Deploy
Environment: Docker
(자동으로 Dockerfile 인식됨)

## Start Command (비워둬도 됨)

Dockerfile CMD 사용

## 7.3 환경변수 설정

Environment Variables

DATABASE_URL=postgresql+psycopg2://neondb_owner:****@.../neondb?sslmode=require

👉 반드시:

비밀번호 새로 발급 (앞에서 말한 보안 이유)
절대 코드에 하드코딩 금지

## 7.4 포트

Render는 자동으로 PORT 환경변수 제공

👉 하지만 현재 Dockerfile은 10000 고정이라 OK

# 8. 배포 후 확인

배포 완료 후:

https://your-service.onrender.com/docs
