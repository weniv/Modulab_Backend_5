from typing import List, Optional, Union
from fastapi import FastAPI, Response, status, HTTPException
from models import Item

# 1번 버전
# "/items"
# "/items/{item_id}"
# 2번 버전
# "/api/v1/items"

app = FastAPI(
    title="CRUD 앱", description="CRUD 경험해보는 간단한 앱입니다.", version="1.0.0"
)

items = []


# Create
@app.post("/items", response_model=Item, tags=["items"])
def create_item(item: Item):
    for existing_item in items:
        if existing_item.name == item.name:
            raise Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                content="이미 존재하는 아이템 이름입니다.",
            )
    items.append(item)
    return item


# Read
@app.get("/items", tags=["items"])
def read_items(skip: int = 0, limit: int = 10):
    return_items = items[skip : skip + limit]
    # 조회된 아이템이 없는 경우 에러 반환
    # [] -> False
    # not [] -> True
    if not return_items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="조회된 아이템이 없습니다.",
        )
    return return_items


# Update
# put -> 수정할거야
# items -> item들을 대상으로
# item_id -> 수정하고 싶은 대상 아이템의 id
@app.put("/items/{item_id}", response_model=Item, tags=["items"])
def update_item(item_id: int, item: Item):
    # 예외 처리
    # item_id 인덱스 범위에 대한 예외처리
    if item_id < 0 or item_id >= len(items):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="존재하지 않는 아이템입니다."
        )
    # 업데이트
    items[item_id] = item

    return item


# Delete
# 삭제할거야 -> restfuk api delete
# 어떤 대상을? -> items
# 특정 아이템을 지정 -> {item_id}
@app.delete("/items/{item_id}", tags=["items"])
def delete_item(item_id: int):
    # 삭제하려는 아이템이 없는 경우도 있나요?
    if item_id < 0 or item_id >= len(items):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="존재하지 않는 아이템입니다."
        )
    # 삭제
    # items = [item1, item2, item3]
    # item_id = 인덱스
    # items.remove(items[item_id])
    # del items[item_id]
    deleted_item = items.pop(item_id)
    return deleted_item


# 특정 단어가 이름에 포함된 경우 삭제하는 API
# 요청 메서드 삭제할거니까 -> delete
# 엔드 포인트 /items
@app.delete("/items", tags=["items"])
def delete_items_by_name(name: Optional[str] = None):
    # 요청은 받았는데 쿼리 파라미터로 name이 없는 경우
    if name is None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="삭제하려는 아이템 이름을 전달하세요.",
        )

    # name이 있는 경우
    # items 리스트에서 item 요소들 중 가지고 있는 name이 쿼리 파라미터로 전달된 name을 포함하는 경우 삭제
    deleted_items = list(filter(lambda item: name in item.name, items))

    for item in deleted_items:
        items.remove(item)

    return {"deleted_item": deleted_items}
