from fastapi import FastAPI

app = FastAPI()


@app.get("/blog/{post_id}")  # 경로 매개변수수
def blog_detail(post_id: int):
    print(post_id)
    return {"게시물 번호": post_id + post_id}


@app.get("/blog/{post_tag}/{post_author}")
def tag_author_list(post_tag: str, post_author: str):
    return {"태그": post_tag, "저자": post_author}
