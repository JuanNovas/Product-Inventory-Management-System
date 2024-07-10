from backend.data_access.products import get_all_products, get_product_by_id, add_product, delete_product, update_product, set_stock
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


def update_stock_data(id: int, new_stock: int) -> None:
    return set_stock(id, new_stock)


def add_stock_data(id: int, new_stock: int) -> None:
    product = get_product_by_id(id)
    if product == None:
        return ValueError("ID not found")
    new_stock = product["stock"] + new_stock
    return set_stock(id, new_stock)