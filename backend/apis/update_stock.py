from fastapi import Body
from fastapi.routing import APIRouter
from backend.apis.status_response import status_response
from backend.logic.products import update_stock_data, add_stock_data

router = APIRouter()

@router.post("/set_stock")
async def set_stock(id: int=Body(...), stock: int=Body(...)):
    status = update_stock_data(id, stock)
    return status_response(status)


@router.post("/add_stock")
async def add_stock(id: int=Body(...), stock: int=Body(...)):
    status = add_stock_data(id, stock)
    return status_response(status)