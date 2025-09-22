from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt

app = FastAPI()

SECRET_KEY = "TEST-ASDASDASDASDASDASDASDSA"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

users_db = {}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


def create_token(username: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = {"sub": username, "exp": expire}
    return jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="토큰이 유효하지 않습니다.")
        return username
    except:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/signup")
def signup(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="유저이름이 이미 있습니다.")
    users_db[user.username] = user.password
    return {"message": "유저를 만들었습니다."}

@app.post("/token",response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_password = users_db.get(form_data.username)
    if not user_password or user_password != form_data.password:
        raise HTTPException(status_code=401,detail="Incorrect username or password")
    
    access_token = create_token(form_data.username)
    return {"access_token":access_token,"token_type": "bearer"}

@app.get("/protected")
def protected_route(current_user:str= Depends(get_current_user)):
    return {"message":f"hello {current_user}!"}