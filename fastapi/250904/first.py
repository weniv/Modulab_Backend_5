from fastapi import FastAPI

app = FastAPI()

""" 
경로	함수명	설명
/	read_root	{"Hello": "World"}를 반환합니다.
/about	about	{"message": "about page"}를 반환합니다.
/contact	contact	{"message": "contact page"}를 반환합니다.
/notice	notice	공지사항 목록을 반환합니다.
"""


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"message": "about page"}


@app.get("/contact")
def contact():
    return {"message": "contact page"}


@app.get("/notice")
def notice():

    return {"users": {"user1": "max", "user2": "good"}}
