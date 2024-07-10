from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: int = 0
    stock: int = 0
    category_id: int = None
    producer_id: int = None