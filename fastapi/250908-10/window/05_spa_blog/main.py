from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import PatchPost, Post

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=[
    #     "http://localhost:3000",
    #     "https://heoni.com",
    # ],
    # allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_origins=["*"],  # 모든 도메인을 허용
    allow_credentials=True,  # 쿠키, 인증 헤더 허용
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


posts = [
    Post(
        post_id=1,
        title="첫 번째 포스트",
        content="첫 번째 포스트 내용입니다.",
        author="hwang",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Post(
        post_id=2,
        title="두 번째 포스트",
        content="두 번째 포스트 내용입니다.",
        author="태진",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Post(
        post_id=3,
        title="세 번째 포스트",
        content="세 번째 포스트 내용입니다.",
        author="영서",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
]


# Create
@app.post("/posts")
def create_post(post: Post):
    # TODO: 생성 시 post_id 중복 체크 유효성 검사 추가
    post.created_at = datetime.now()
    post.updated_at = datetime.now()
    posts.append(post)
    return post


# Read
@app.get("/posts")
def get_posts():
    return posts


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.post_id == post_id:
            return post


# Update
@app.put("/posts/{post_id}")
def put_post(post_id: int, updated_post: Post):
    # TODO: 수정 요청 시 created_at 유지
    updated_post.updated_at = datetime.now()
    for i, post in enumerate(posts):
        if post.post_id == post_id:
            posts[i] = updated_post
            return post[i]


@app.patch("/posts/{post_id}")
def fetch_post(post_id: int, updated_post: PatchPost):
    for post in posts:
        if post.post_id == post_id:
            for key, value in updated_post.model_dump().items():
                if value is not None:
                    print(key, value)
                    setattr(post, key, value)
            post.updated_at = datetime.now()

            return post


# Delete
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for post in posts:
        if post.post_id == post_id:
            posts.remove(post)
            return post
