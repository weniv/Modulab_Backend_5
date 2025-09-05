from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "웰컴"}


@app.get("/blog")
def blog_list():
    return {"블로그 목록": ["게시물1", "게시물2"]}


@app.get("/blog/{post_tag}/{post_author}")
def tag_author_list(post_tag: str, post_author: str):
    return {"태그": post_tag, "저자": post_author}


@app.get("/blog/{post_id}")
def blog_detail(post_id: int):
    return {"게시물 번호": post_id}


@app.get("/blog/tag/{post_tag}")
def tag_list(post_tag: str):
    return {"태그": post_tag}


@app.get("/hello/{name}")
def greet_user(name: str):
    return {"인사말": f"안녕하세여 {name} 입니다."}


@app.get("/calculate/{operation}/{a}/{b}")
def calculate(operation: str, a: int, b: int):
    if operation == "add":
        result = a + b
        operation_korean = "덧셈"
    elif operation == "subtract":
        result = a - b
        operation_korean = "뺄셈"
    elif operation == "multiply":
        result = a * b
        operation_korean = "곱셈"
    elif operation == "divide":
        if b == 0:
            return {"오류": "0으로는 나눌 수 없어요."}
        result = a / b
        operation_korean = "나눗셈"
    else:
        return {
            "오류": "지원하지 않는 연산입니다. add, subtract, multiply, divide 중 하나를 사용하세요."
        }
    return {
        "연산": operation_korean,
        "첫번째 숫자": a,
        "두번째 숫자": b,
        "결과": result,
        "계산식": f"{a} {operation} {b} = {result}",
    }
