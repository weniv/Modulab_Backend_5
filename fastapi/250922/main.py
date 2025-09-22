from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer,primary_key=True,index=True)
    name =  Column(String,index=True)
    description = Column(String,index=True)
    price = Column(Float)

Base.metadata.create_all(bind=engine)

class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float

class ItemResponse(ItemCreate):
    id: int

app = FastAPI()


@app.post("/items/",response_model=ItemResponse)
def create_item(item:ItemCreate,db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

@app.get("/items/",response_model=list[ItemResponse])
def read_items(db:Session = Depends(get_db)):
    return db.query(Item).all()


@app.get("/items/{item_id}",response_model=ItemResponse)
def read_item(item_id = int, db:Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404,detail="아이템이 없어요.")
    
    return db_item

