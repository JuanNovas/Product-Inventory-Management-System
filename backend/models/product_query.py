from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel
from typing import Optional

class ProductQuery(BaseModel):
    name: Optional[str] = Query(None)
    min_price: Optional[int] = Query(None)
    max_price: Optional[int] = Query(None)
    min_stock: Optional[int] = Query(None)
    max_stock: Optional[int] = Query(None)
    category_id: Optional[int] = Query(None)
    producer_id: Optional[int] = Query(None)