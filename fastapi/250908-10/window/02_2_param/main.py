from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()
posts = [
    {"id": 1, "title": "First Post", "tag": "fastapi", "author": "천수겸"},
    {"id": 2, "title": "Second Post", "tag": "python", "author": "장민경"},
    {"id": 3, "title": "Third Post", "tag": "backend", "author": "mr. kim"},
    {"id": 4, "title": "Fourth Post", "tag": "fastapi", "author": "신가람"},
    {"id": 5, "title": "Fifth Post", "tag": "backend", "author": "경환"},
    {"id": 6, "title": "Sixth Post", "tag": "fastapi", "author": "경환"},
    {"id": 7, "title": "Seventh Post", "tag": "python", "author": "경환"},
    {"id": 8, "title": "Eighth Post", "tag": "backend", "author": "경환"},
]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/blog")
def blog_list():
    return {"posts": posts}


# id 값은 개별로 유일하다
# posts = [
#     {"id": 1, "title": "First Post"},
#     {"id": 2, "title": "Second Post"},
#     {"id": 3, "title": "Third Post"},
#     {"id": 4, "title": "Fourth Post"},
#     {"id": 5, "title": "Fifth Post"},
# ]
# GET /blog/1 -> {"id": 1, "title": "First Post"}
# GET /blog/2 -> {"id": 2, "title": "Second Post"}
# GET /blog/3 -> {"id": 3, "title": "Third Post"}
# GET /blog/4 -> {"id": 4, "title": "Fourth Post"}
# GET /blog/5 -> {"id": 5, "title": "Fifth Post"}
@app.get("/blog/{post_id}")
def blog_detail(post_id: int):
    filtered_post = [post for post in posts if post["id"] == post_id]
    return {"post": filtered_post[0]}


# posts = [
#     {"id": 1, "title": "First Post", "tag": "fastapi"},
#     {"id": 2, "title": "Second Post", "tag": "python"},
#     {"id": 3, "title": "Third Post", "tag": "backend"},
#     {"id": 4, "title": "Fourth Post", "tag": "fastapi"},
#     {"id": 5, "title": "Fifth Post", "tag": "backend"},
# ]
@app.get("/blog/tag/{post_tag}")
def blog_tag_list(post_tag: str):
    filtered_post = []
    for post in posts:
        if post["tag"] == post_tag:
            filtered_post.append(post)
    return {"filtered_post": filtered_post}


# posts = [
#     {"id": 1, "title": "First Post", "tag": "fastapi", "author": "천수겸"},
#     {"id": 2, "title": "Second Post", "tag": "python", "author": "장민경"},
#     {"id": 3, "title": "Third Post", "tag": "backend", "author": "mr. kim"},
#     {"id": 4, "title": "Fourth Post", "tag": "fastapi", "author": "신가람"},
#     {"id": 5, "title": "Fifth Post", "tag": "backend", "author": "경환"},
#     {"id": 6, "title": "Sixth Post", "tag": "fastapi", "author": "경환"},
#     {"id": 7, "title": "Seventh Post", "tag": "python", "author": "경환"},
#     {"id": 8, "title": "Eighth Post", "tag": "backend", "author": "경환"},
# ]
# GET /blog/tag/backend/경환
# post_tag = backend
# post_author = 경환
# filtered_posts = [
#     {"id": 5, "title": "Fifth Post", "tag": "backend", "author": "경환"},
#     {"id": 8, "title": "Eighth Post", "tag": "backend", "author": "경환"},
# ]
@app.get("/blog/tag/{post_tag}/{post_author}")
def blog_tag_author_list(post_tag: str, post_author: str):
    filtered_posts = []
    for post in posts:
        if post["tag"] == post_tag and post["author"] == post_author:
            filtered_posts.append(post)
    return {"filtered_posts": filtered_posts}
