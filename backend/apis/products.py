from fastapi import Depends
from fastapi.routing import APIRouter
from backend.apis.utils.status_response import status_response
from backend.apis.utils.data_response import data_response
from backend.logic.products import get_all_products_data, get_product_data_by_id, create_new_product, delete_product_data, update_product_data, get_product_data_by_filter
from backend.models.products import Product
from backend.models.product_query import ProductQuery

router = APIRouter()

@router.get("/products")
async def get_products():
    data = get_all_products_data()
    return data_response(data)


# @router.get("/products/{id}")
# async def get_product_by_id(id: int):
#     data = get_product_data_by_id(id)
#     return data_response(data)


@router.get("/products/filter")
async def get_products_by_filter(product_query: ProductQuery = Depends(ProductQuery)):
    data = get_product_data_by_filter(product_query)
    return data_response(data)


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
