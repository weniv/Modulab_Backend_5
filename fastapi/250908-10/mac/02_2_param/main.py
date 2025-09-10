from fastapi import FastAPI

app = FastAPI()

posts = [
    {"id": 1, "author": "Hwang", "tag": "FastAPI"},
    {"id": 2, "author": "Lee", "tag": "Python"},
    {"id": 3, "author": "Kim", "tag": "Python"},
    {"id": 4, "author": "Park", "tag": "FastAPI"},
    {"id": 5, "author": "Choi", "tag": "Backend"},
    {"id": 6, "author": "Jung", "tag": "Backend"},
]


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/blog")
def blog_list():
    return {"posts": posts}


# posts = [
#     {"id": 1, "author": "Hwang", "tag": "FastAPI"},
#     {"id": 2, "author": "Lee", "tag": "Python"},
#     {"id": 3, "author": "Kim", "tag": "Python"},
#     {"id": 4, "author": "Park", "tag": "FastAPI"},
#     {"id": 5, "author": "Choi", "tag": "Backend"},
#     {"id": 6, "author": "Jung", "tag": "Backend"},
# ]
@app.get("/blog/{post_id}")
def blog_detail(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return {"post": post}
    return {"message": "Post not found"}


@app.get("/blog/tag/{tag_name}")
def blog_tag_list(tag_name: str):
    tag_name = tag_name.lower()
    tag_posts = list(filter(lambda post: post["tag"].lower() == tag_name, posts))
    return {"tag": tag_name, "posts": tag_posts}


@app.get("/blog/tag/{tag_name}/{author_name}")
def blog_tag_author_list(tag_name: str, author_name: str):
    tag_name = tag_name.lower()
    author_name = author_name.lower()
    tag_author_posts = list(
        filter(
            lambda post: post["tag"].lower() == tag_name
            and post["author"].lower() == author_name,
            posts,
        )
    )
    return {"tag": tag_name, "author": author_name, "posts": tag_author_posts}
