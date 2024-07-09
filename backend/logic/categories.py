from backend.data_access.categories import get_all_categories, get_category_by_id, add_category, delete_category, update_category
from backend.models.categories import Category
from psycopg2.extras import RealDictCursor


def get_all_categories_data() -> list[RealDictCursor]:
    return get_all_categories()


def get_category_data_by_id(id: int) -> RealDictCursor:
    return get_category_by_id(id)


def create_new_category(category: Category) -> None:
    return add_category(category)


def delete_category_data(id: int) -> None:
    return delete_category(id)


def update_category_data(id: int, category: Category) -> None:
    return update_category(id, category)
