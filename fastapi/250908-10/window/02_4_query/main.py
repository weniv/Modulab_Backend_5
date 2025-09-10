from fastapi import FastAPI


app = FastAPI()

items = [
    {"item_id": "Foo"},
    {"item_id": "Bar"},
    {"item_id": "Baz"},
    {"item_id": "Qux"},
    {"item_id": "Quux"},
    {"item_id": "Corge"},
    {"item_id": "Grault"},
    {"item_id": "Garply"},
    {"item_id": "Waldo"},
    {"item_id": "Fred"},
    {"item_id": "Plugh"},
    {"item_id": "Xyzzy"},
    {"item_id": "Thud"},
    {"item_id": "A"},
    {"item_id": "B"},
    {"item_id": "C"},
    {"item_id": "D"},
    {"item_id": "E"},
    {"item_id": "F"},
    {"item_id": "G"},
    {"item_id": "H"},
    {"item_id": "I"},
    {"item_id": "J"},
    {"item_id": "K"},
    {"item_id": "L"},
    {"item_id": "M"},
    {"item_id": "N"},
    {"item_id": "O"},
    {"item_id": "P"},
    {"item_id": "Q"},
    {"item_id": "R"},
    {"item_id": "S"},
    {"item_id": "T"},
    {"item_id": "U"},
    {"item_id": "V"},
    {"item_id": "W"},
    {"item_id": "X"},
    {"item_id": "Y"},
    {"item_id": "Z"},
]


# @app.get("/items")
# def read_items(skip: int = 0, limit: int = 10):
#     return_items = items[skip : skip + limit]
#     return {"return_items": return_items}


# @app.get("/items")
# def read_items(hello: str = "FastAPI", limit: int = 10):
#     return {"hello": hello, "limit": limit}


# @app.get("/items")
# def read_items(
#     skip: int,
# ):
#     return {"skip": skip}


# @app.get("/items")
# def read_items(item_id: int, q: str | None = None):
#     item = items[item_id]
#     if q:
#         item.update({"q": q})
#     return {"item": item}


@app.get("/items")
def read_items(item_id: bool):
    print(f"item_id: {item_id} / type: {type(item_id)}")
