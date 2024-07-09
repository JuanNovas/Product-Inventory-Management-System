from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: int = 0
    stock: int = 0
    category_id: int
    producer_id: int