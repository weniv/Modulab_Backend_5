# 기본 이미지 설정
FROM python:3.12-slim
# 컨테이너 내부 작업공간(폴더) 설정
WORKDIR /app 

# 호스트(로컬)에서 컨테이너 내부로 복사
COPY requirements.txt .

# Python 패키지 설치
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
# 포트 노출
EXPOSE 8000
# 최종 실행 명령어 수행 (현재는 main.py가 없어서 실행x)
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]