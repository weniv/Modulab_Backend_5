from fastapi import FastAPI

app = FastAPI()


@app.get("/users") # 127.0.0.1:8000/users
def get_users():

    return {
        "user1": {"name": "max", "password": 1234},
        "user2": {"name": "good", "password": 1111},
    }
