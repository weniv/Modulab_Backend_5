from fastapi import FastAPI

app = FastAPI() # fastapi 인스턴스 생성


@app.get("/") # 엔드포인트 설정 -> 127.0.0.1:8000 
def read_root():
    return {"Hello": "world!"} # 반환 값 설정
