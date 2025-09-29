import redis
import json
from typing import Any, Optional
from app.config import settings

class RedisClient:
    def __init__(self):
        self.redis_client: redis.Redis = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            password=settings.redis_password,
            decode_responses=True
        )
    
    def get(self, key: str) -> Optional[Any]:
        """Redis에서 값 조회"""
        try:
            value: Optional[str] = self.redis_client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            print(f"Redis GET 오류: {e}")
            return None
    
    def set(self, key: str, value: Any, expire: Optional[int] = None) -> bool:
        """Redis에 값 저장"""
        try:
            json_value = json.dumps(value, ensure_ascii=False)
            result = self.redis_client.set(key, json_value, ex=expire)
            return bool(result)
        except Exception as e:
            print(f"Redis SET 오류: {e}")
            return False
    
    def delete(self, key: str) -> bool:
        """Redis에서 키 삭제"""
        try:
            result: int = self.redis_client.delete(key)
            return result > 0
        except Exception as e:
            print(f"Redis DELETE 오류: {e}")
            return False
    
    def exists(self, key: str) -> bool:
        """키 존재 여부 확인"""
        try:
            result: int = self.redis_client.exists(key)
            return result > 0
        except Exception as e:
            print(f"Redis EXISTS 오류: {e}")
            return False
    
    def increment(self, key: str, amount: int = 1) -> Optional[int]:
        """숫자 값 증가"""
        try:
            result: int = self.redis_client.incr(key, amount)
            return result
        except Exception as e:
            print(f"Redis INCR 오류: {e}")
            return None

# 전역 Redis 클라이언트 인스턴스
redis_client = RedisClient()