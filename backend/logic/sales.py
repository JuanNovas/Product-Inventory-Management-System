from backend.data_access.sales import get_all_sales, get_sale_by_id, add_sale, delete_sale, update_sale
from backend.models.sales import Sale
from psycopg2.extras import RealDictCursor


def get_all_sales_data() -> list[RealDictCursor]:
    return get_all_sales()


def get_sale_data_by_id(id: int) -> RealDictCursor:
    return get_sale_by_id(id)


def create_new_sale(sale: Sale) -> None:
    return add_sale(sale)


def delete_sale_data(id: int) -> None:
    return delete_sale(id)


def update_sale_data(id: int, sale: Sale) -> None:
    return update_sale(id, sale)
