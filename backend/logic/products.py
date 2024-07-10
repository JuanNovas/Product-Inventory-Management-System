from backend.data_access.products import get_all_products, get_product_by_id, add_product, delete_product, update_product, set_stock, update_multiple_price_by_producer, update_multiple_price_by_category, update_all_price, update_multiple_price_by_producer_category
from backend.models.products import Product
from psycopg2.extras import RealDictCursor
from backend.logic.validations.product_verification import is_valid_product
from backend.logic.validations.id_verification import check_id


def get_all_products_data() -> list[RealDictCursor]:
    return get_all_products()


def get_product_data_by_id(id: int) -> RealDictCursor:
    if not (error := check_id(id)):
        return error
    
    
    return get_product_by_id(id)


def create_new_product(product: Product) -> None:
    if not (error := is_valid_product(product)):
        return error
    
    
    return add_product(product)


def delete_product_data(id: int) -> None:
    if not (error := check_id(id)):
        return error
    
    
    return delete_product(id)


def update_product_data(id: int, product: Product) -> None:
    if not (error := check_id(id)):
        return error
    if not (error := is_valid_product(product)):
        return error
    
    
    return update_product(id, product)


def update_stock_data(id: int, new_stock: int) -> None:
    if not (error := check_id(id)):
        return error
    if type(new_stock) != int:
        return TypeError("New stock must be an int")
    if new_stock < 0:
        return ValueError("New stock cannot be negative")
    
    
    return set_stock(id, new_stock)


def add_stock_data(id: int, new_stock: int) -> None:
    if not (error := check_id(id)):
        return error
    if type(new_stock) != int:
        return TypeError("New stock must be an int")
    product = get_product_by_id(id)
    if product == None:
        return KeyError("ID not found")
    new_stock = product["stock"] + new_stock
    if new_stock < 0:
        new_stock = 0
        
        
    return set_stock(id, new_stock)


def update_multiple_price_data(rate: float, producer_id: int=None, category_id: int=None):
    # Validation
    if type(rate) != float or (type(producer_id) != int and producer_id is not None) or (type(category_id) != int and category_id is not None):
        return TypeError("Invalid type of arguments.")
    if producer_id:
        if producer_id <= 0:
            return ValueError("Invalid producer_id number, must be more than 0.")
    if category_id:
        if category_id <= 0:
            return ValueError("Invalid category_id number, must be more than 0.")
    
    # Function calling
    if producer_id and category_id:
        return update_multiple_price_by_producer_category(producer_id, category_id, rate)
    elif producer_id:
        return update_multiple_price_by_producer(producer_id, rate)
    elif category_id:
        return update_multiple_price_by_category(category_id, rate)
    else:
        return update_all_price(rate)
