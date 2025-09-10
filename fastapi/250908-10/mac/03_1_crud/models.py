from typing import Optional
from pydantic import BaseModel, field_validator


class Item(BaseModel):
    name: str
    # description: str|None = None
    description: Optional[str] = None
    price: float

    @field_validator("price")
    @classmethod
    def validate_price(cls, price):
        if price <= 0:
            raise ValueError("가격은 양수여야 합니다.")
        return price
