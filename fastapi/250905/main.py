from fastapi import FastAPI
from models import Item, Todo

app = FastAPI()

items = []


@app.get("/item")
def get_items():
    return {"items": items}


@app.post("/item")
def create_item(item: Item):
    items.append(item)
    return {"이름": item.name, "가격": item.price}


@app.post("/todos")
def todos(todo: Todo):
    return {
        "title": todo.title,
        "description": todo.description,
        "priority": todo.priority,
        "due_date": todo.due_date,
    }
