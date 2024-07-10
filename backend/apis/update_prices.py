from fastapi import Body
from fastapi.routing import APIRouter
from backend.apis.status_response import status_response
from backend.logic.products import update_multiple_price_data


router = APIRouter()


@router.post("/update_prices")
async def update_prices(producer_id: int=Body(None), category_id: int=Body(None), rate: float=Body(...)):
    status = update_multiple_price_data(rate, producer_id=producer_id, category_id=category_id)
    return status_response(status)