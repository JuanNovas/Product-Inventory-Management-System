from pydantic import BaseModel

class Sale(BaseModel):
    product_id: int
    total_price: int
    amount: int = 1