from fastapi.routing import APIRouter
from backend.apis.status_response import status_response
from backend.logic.categories import get_all_categories_data, get_category_data_by_id, create_new_category, delete_category_data, update_category_data
from backend.models.categories import Category

router = APIRouter()

@router.get("/categories")
async def get_categories():
    data = get_all_categories_data()
    return data


@router.get("/categories/{id}")
async def get_category_by_id(id: int):
    data = get_category_data_by_id(id)
    return data


@router.post("/categories")
async def post_categories(category: Category):
    status = create_new_category(category)
    return status_response(status)


@router.delete("/categories/{id}")
async def delete_category(id: int):
    status = delete_category_data(id)
    return status_response(status)


@router.put("/categories/{id}")
async def put_category(id: int, category: Category):
    status = update_category_data(id, category)
    return status_response(status)
