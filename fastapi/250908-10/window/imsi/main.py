from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None
