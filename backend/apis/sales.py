from fastapi.routing import APIRouter
from backend.apis.utils.status_response import status_response
from backend.logic.sales import get_all_sales_data, get_sale_data_by_id, create_new_sale, delete_sale_data, update_sale_data
from backend.models.sales import Sale

router = APIRouter()

@router.get("/sales")
async def get_sales():
    data = get_all_sales_data()
    return data


@router.get("/sales/{id}")
async def get_sale_by_id(id: int):
    data = get_sale_data_by_id(id)
    return data


@router.post("/sales")
async def post_sales(sale: Sale):
    status = create_new_sale(sale)
    return status_response(status)


@router.delete("/sales/{id}")
async def delete_sale(id: int):
    status = delete_sale_data(id)
    return status_response(status)


@router.put("/sales/{id}")
async def put_sale(id: int, sale: Sale):
    status = update_sale_data(id, sale)
    return status_response(status)
