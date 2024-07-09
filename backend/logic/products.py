from backend.data_access.products import get_all_products, get_product_by_id, add_product, delete_product, update_product
from backend.models.products import Product
from psycopg2.extras import RealDictCursor


def get_all_products_data() -> list[RealDictCursor]:
    return get_all_products()


def get_product_data_by_id(id: int) -> RealDictCursor:
    return get_product_by_id(id)


def create_new_product(product: Product) -> None:
    return add_product(product)


def delete_product_data(id: int) -> None:
    return delete_product(id)


def update_product_data(id: int, product: Product) -> None:
    return update_product(id, product)
