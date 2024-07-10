from backend.data_access.sales import get_all_sales, get_sale_by_id, add_sale, delete_sale, update_sale
from backend.models.sales import Sale
from psycopg2.extras import RealDictCursor
from backend.logic.validations.sale_verification import is_valid_sale
from backend.logic.validations.id_verification import check_id


def get_all_sales_data() -> list[RealDictCursor]:
    return get_all_sales()


def get_sale_data_by_id(id: int) -> RealDictCursor:
    if not (error := check_id(id)):
        return error
    return get_sale_by_id(id)


def create_new_sale(sale: Sale) -> None:
    if not (error := is_valid_sale(sale)):
        return error
    return add_sale(sale)


def delete_sale_data(id: int) -> None:
    if not (error := check_id(id)):
        return error
    return delete_sale(id)


def update_sale_data(id: int, sale: Sale) -> None:
    if not (error := check_id(id)):
        return error
    if not (error := is_valid_sale(sale)):
        return error
    return update_sale(id, sale)
