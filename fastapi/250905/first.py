from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index(name: str, price: int = 0):  # localhost:8000/?name={값}&price={숫자 값}
    print(name, price)
    return {"name": name, "price": price}


#  price: int = 0) price를 입력하지 않으면 0이 기본값

items = []


@app.get("/item")
def get_items():
    return {"items": items}


@app.post("/item")
def create_item(item: dict):  # JSON을 본문(BODY)로 받겠다.
    items.append(item)
    return {"item": item}


@app.post("/todos")
def todos(todo: dict):
    return {
        "title": todo.get("title"),
        "description": todo.get("description"),
        "priority": todo.get("priority"),
        "due_date": todo.get("due_date"),
    }
