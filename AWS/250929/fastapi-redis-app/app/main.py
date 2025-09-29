from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.redis_client import redis_client
from app.routers import cache
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cache.router, prefix="/cache", tags=["cache"])


@app.get("/")
def read_root():
    return {"message": "FastAPI + Redis 연결완료."}


@app.get("/health")
def health_check():
    # redis 연결 상태 확인
    try:
        redis_client.redis_client.ping()
        return {"status": "healthy", "redis": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"redis연결 실패 {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
