from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "welcome!"}


@app.get("/health")
def health_check():
    return {"status": "okay"}
