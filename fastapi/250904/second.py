from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)  # HTML 형태로 응답
def index():
    return "<h1> 오늘은 비가 오니까 전을 먹어야지 </h1>"


"""
get /about -> h2 태그활용
get /notice -> h3 태그활용
get /contact -> h4 태그활용
"""


@app.get("/about", response_class=HTMLResponse)
def about():
    return "<h1>hello world 2</h1>"


@app.get("/contact", response_class=HTMLResponse)
def contact():
    return "<h1>hello world 3</h1>"


@app.get("/notice", response_class=HTMLResponse)
def notice():
    return "<h1>hello world 4</h1>"


@app.get("/index", response_class=HTMLResponse)
def index2():
    return """
    <h1>hello world 1</h1>
    <p>안녕</p>
    <ol>
        <li>첫 번째</li>
        <li>두 번째</li>
        <li>세 번째</li>
    </ol>
    """


from fastapi import Request
from fastapi.templating import Jinja2Templates  # 템플릿 연동

templates = Jinja2Templates("templates")  # 템플릿 위치 설정


@app.get("/home")
def home(
    request: Request,
):  # 첫번째 인자에는 반드시 넣어야함.
    return templates.TemplateResponse(
        request, "index.html", {"name": "max", "good": "okay"}
    )


"""
home.html을 templates 폴더 아래에 만들어서 
/me 라는 곳에 접속하면 동적데이터 3개를 만들어 fastapi에서 매핑후 
html 반환
"""


@app.get("/me")
def me(
    request: Request,
):  # 첫번째 인자에는 반드시 넣어야함.
    return templates.TemplateResponse(
        request, "home.html", {"var1": "data1", "var2": "data2", "var3": "data3"}
    )
