from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import time
import hashlib
from app.redis_client import redis_client

router = APIRouter()


class UserData(BaseModel):
    user_id: int
    name: str
    email: str
    age: int


class CacheStats(BaseModel):
    total_requests: int
    cache_hits: int
    cache_misses: int
    hit_rate: float


def slow_database_query(user_id: int) -> Optional[UserData]:
    time.sleep(2)  # 2초 지연

    # 가상 데이터
    fake_users = {
        1: UserData(user_id=1, name="김철수", email="kim@example.com", age=25),
        2: UserData(user_id=2, name="이영희", email="lee@example.com", age=30),
        3: UserData(user_id=3, name="박민수", email="park@example.com", age=28),
    }

    return fake_users.get(user_id)


# cache/user/{user_id}
@router.get("/user/{user_id}")
def get_user_with_cache(user_id: int):
    # ex) user:1 , user:2
    cache_key = f"user:{user_id}"

    cached_user = redis_client.get(cache_key)
    # 캐시 히트의 경우
    if cached_user:
        # 통계 업데이트
        redis_client.increment("cache:hits")
        redis_client.increment("cache:total_requests")

        return {"data": cached_user, "from_cache": True, "cache_key": cache_key}

    # 캐시 미스의 경우
    user_data = slow_database_query(user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    # 캐시에 저장 (10분간 유효)
    redis_client.set(cache_key, user_data.dict(), expire=600)

    # 통계 업데이트
    redis_client.increment("cache:misses")
    redis_client.increment("cache:total_requests")

    return {"data": user_data.dict(), "from_cache": False, "cache_key": cache_key}


@router.post("/user/{user_id}")
def update_user_cache(user_id: int, user_data: UserData):
    # 사용자 데이터 업데이트 및 캐시 갱신
    cache_key = f"user:{user_id}"

    # 캐시 갱신
    redis_client.set(cache_key, user_data.dict(), expire=600)

    return {
        "message": "사용자 데이터가 업데이트되었습니다",
        "cache_key": cache_key,
        "data": user_data.dict(),
    }


@router.delete("/user/{user_id}")
def invalidate_user_cache(user_id: int):
    # 특정 사용자의 캐시를 무효화

    cache_key = f"user:{user_id}"

    if redis_client.delete(cache_key):
        return {"message": f"사용자 {user_id}의 캐시가 삭제되었습니다."}
    else:
        return {"message": "삭제할 캐시가 없습니다."}


@router.get("/stats")
def get_cache_stats() -> CacheStats:
    # 캐시 통계 조회

    total_requests = redis_client.get("cache:total_requests") or 0
    cache_hits = redis_client.get("cache:hits") or 0
    cache_misses = redis_client.get("cache:misses") or 0

    hit_rate = (cache_hits / total_requests * 100) if total_requests > 0 else 0

    return CacheStats(
        total_requests=total_requests,
        cache_hits=cache_hits,
        cache_misses=cache_misses,
        hit_rate=round(hit_rate, 2),
    )
