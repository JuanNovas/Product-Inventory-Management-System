from fastapi.routing import APIRouter
from backend.apis.status_response import status_response
from backend.logic.products import get_all_products_data, get_product_data_by_id, create_new_product, delete_product_data, update_product_data
from backend.models.products import Product

router = APIRouter()

@router.get("/products")
async def get_products():
    data = get_all_products_data()
    return data


@router.get("/products/{id}")
async def get_product_by_id(id: int):
    data = get_product_data_by_id(id)
    return data


@router.post("/products")
async def post_products(product: Product):
    status = create_new_product(product)
    return status_response(status)


@router.delete("/products/{id}")
async def delete_product(id: int):
    status = delete_product_data(id)
    return status_response(status)


@router.put("/products/{id}")
async def put_product(id: int, product: Product):
    status = update_product_data(id, product)
    return status_response(status)
