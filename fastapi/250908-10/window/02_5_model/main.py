from typing import Union
from fastapi import FastAPI, Response, status
from models import Item, Message, User


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


users = []


@app.post("/users")
def create_user(
    user: User,
):  # User가 모델로 들어오는 단계에서 유효성 검사를 자동으로 수행
    # 유효성 검사 메서드 실행 코드
    users.append(user)
    return Response(content={"user": user}, status_code=201)


items = []


# item 생성
# 정상 생성의 경우 201 응답 코드와 함께 생성된 item을 응답
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return Response(status_code=status.HTTP_201_CREATED)


@app.get("/items")
def read_items():
    return {"items": items}


# items = [Item instance, Item instance, Item instance]
# -1, 4 -> 404
# @app.get("/items/{item_id}", response_model=Item)
# def read_item(item_id: int):
#     if item_id < 0 or item_id >= len(items):
#         raise HTTPException(status_code=404, detail="찾으시는 아이템이 없습니다.")
#     return items[item_id]


@app.get("/items/{item_id}", response_model=Union[Item, Message])
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return Message(message="찾으시는 아이템이 없습니다.")
    return items[item_id]
