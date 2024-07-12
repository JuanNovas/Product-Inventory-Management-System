from pydantic import BaseModel

class ProductQuery(BaseModel):
    name: str = None
    min_price: int = None
    max_price: int = None
    min_stock: int = None
    max_stock: int = None
    category_id: int = None
    producer_id: int = None