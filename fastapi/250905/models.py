from pydantic import BaseModel
from typing import Optional  # 옵션


class Item(BaseModel):
    name: str  # 반드시 요청 본문에 입력 필수
    price: float = 1000  # 요청 본문에 입력하지 않으면 기본값 1000 적용
    data: Optional[float] = None  # 기본값은 없음(None)


"""
    return {
        "title": todo.get("title"),
        "description": todo.get("description"),
        "priority": todo.get("priority"),
        "due_date": todo.get("due_date"),
    }
"""


class Todo(BaseModel):
    title: str
    description: str
    priority: str
    due_date: str
