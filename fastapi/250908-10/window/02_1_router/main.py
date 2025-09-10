from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# @app.get(
#     "/",
#     tags=["Root"],
#     summary="루트 경로에 대한 반환",
#     description="루트 경로에 대한 설명",
# )
# def read_root():
#     return {"Hello": "FastAPI"}


# @app.get("/about")
# def about():
#     return {"message": "FastAPI에 대해서"}


# @app.get("/contact")
# def contact():
#     return {"message": "FastAPI 연락 정보"}


# @app.get("/notice")
# def notice():
#     return {
#         "notice": [
#             {"title": "FastAPI 시작하기", "content": "FastAPI 시작하기 내용"},
#             {"title": "FastAPI 심화", "content": "FastAPI 심화 내용"},
#             {"title": "FastAPI 배포", "content": "FastAPI 배포 내용"},
# ]
#     }


# @app.get("/", response_class=HTMLResponse)
# def index():
#     return """
#     <h1>Hello FastAPI</h1>
#     <a href="/docs">Go to Swagger UI</a><br>
#     <a href="/redoc">Go to ReDoc</a>
#     """


# @app.get("/about", response_class=HTMLResponse)
# def about():
#     return """
#     <h1>About FastAPI</h1>
#     <p>FastAPI에 대해서</p>
#     <a href="/">Go to Home</a>
#     """


# @app.get("/contact", response_class=HTMLResponse)
# def contact():
#     return """
#     <h1>Contact FastAPI</h1>
#     <p>FastAPI 연락 정보</p>
#     <a href="/">Go to Home</a>
#     """


# @app.get("/notice", response_class=HTMLResponse)
# def notice():
#     return f"""
#     <h1>Notice FastAPI</h1>
#     <p>FastAPI 공지 정보</p>
#     <a href="/">{20 + 30}</a>
#     <ol>
#         <li>첫 번째</li>
#         <li>두 번째</li>
#         <li>세 번째</li>
#     </ol>
#     """

from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
