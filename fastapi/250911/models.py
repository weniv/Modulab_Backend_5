from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    post_id: int  # post의 id
    title: str  # post의 제목
    content: str  # post의 내용
    author: str  # post의 작성자
    created_at: Optional[datetime] = None  # post의 생성일
    updated_at: Optional[datetime] = None  # post의 수정일


class PatchPost(BaseModel):
    title: Optional[str] = None  # post의 제목
    content: Optional[str] = None  # post의 내용
    author: Optional[str] = None  # post의 작성자
    updated_at: Optional[datetime] = None  # post의 수정일
