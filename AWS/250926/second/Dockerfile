FROM pyhton:3.12-slim

WORKDIR /app

# COPY requirements.txt .
# COPY app.py .

# 전체 폴더 카피
COPY . .
# 의존성 설치
RUN pip install -r requirements.txt

# 포트 노출
EXPOSE 8000

# 애플리케이션 실행
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

