from backend.data_access.products import get_all_products, get_product_by_id, add_product, delete_product, update_product, set_stock, update_multiple_price_by_producer, update_multiple_price_by_category, update_all_price, update_multiple_price_by_producer_category, get_product_by_filter
from backend.models.products import Product
from backend.models.product_query import ProductQuery
from psycopg2.extras import RealDictCursor
from backend.logic.validations.product_verification import is_valid_product
from backend.logic.validations.id_verification import check_id


def get_all_products_data() -> list[RealDictCursor]:
    return get_all_products()


def get_product_data_by_id(id: int) -> RealDictCursor:
    if not (error := check_id(id)):
        return error
    
    
    return get_product_by_id(id)


def get_product_data_by_filter(product_query: ProductQuery) -> list[RealDictCursor]:
    if type(product_query.name) != str and product_query.name is not None:
        return TypeError("Name has to be an string")
    product_query.name = product_query.name.strip()
    if len(product_query.name) > 255:
        return ValueError("Name len must be less than 255")
    if len(product_query.name) == 0:
        return ValueError("Name cannot be null")
    
    if type(product_query.min_price) != int and product_query.min_price is not None or type(product_query.max_price) != int and product_query.max_price is not None:
        return TypeError("Price must be an int")
    if product_query.min_price < 0:
        return ValueError("Price must be at least 0")
    if product_query.max_price < product_query.min_price:
        return ValueError("Max price must be more or equal than min price")
    
    if type(product_query.min_stock) != int and product_query.min_stock is not None or type(product_query.max_stock) != int and product_query.max_stock is not None:
        return TypeError("Stock must be an int")
    if product_query.min_stock < 0:
        return ValueError("Stock must be at least 0")
    if product_query.max_stock < product_query.min_stock:
        return ValueError("Max stock must be more or equal than min stock")
    
    if type(product_query.producer_id) != int and product_query.producer_id is not None:
        return TypeError("Producer_id must be a number")
    if product_query.producer_id:
        if product_query.producer_id <= 0:
            return ValueError("Invalid producer_id number, must be more than 0.")
        
    if type(product_query.category_id) != int and product_query.category_id is not None:
        return TypeError("Category_id must be a number")
    if product_query.category_id:
        if product_query.category_id <= 0:
            return ValueError("Invalid category_id number, must be more than 0.")
    
    
    return get_product_by_filter(name=product_query.name, min_price=product_query.min_price, max_price=product_query.max_price, min_stock=product_query.min_stock, max_stock=product_query.max_stock, category_id=product_query.category_id, producer_id=product_query.producer_id)


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
