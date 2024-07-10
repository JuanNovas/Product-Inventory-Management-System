from backend.models.products import Product


def is_valid_product(product: Product) -> None:
    if type(product.name) != str:
        return TypeError("Name must be a string")
    product.name = product.name.strip()
    if len(product.name) > 255:
        return ValueError("Name len must be less than 255")
    if len(product.name) == 0:
        return ValueError("Name cannot be null")
    
    
    if type(product.price) != int:
        return TypeError("Price must be an int")
    if product.price < 0:
        return ValueError("Price must be at least 0")
    
    
    if type(product.stock) != int:
        return TypeError("Stock must be an int")
    if product.stock < 0:
        return ValueError("Stock must be at least 0")
    
    
    if type(product.category_id) != int:
        if product.category_id is not None:
            return TypeError(f"Category_id connot be {type(product.category_id)}")
    elif product.category_id <= 0:
        return ValueError("Category_id must be positive")
    
    
    if type(product.producer_id) != int:
        if product.producer_id is not None:
            return TypeError(f"Producer_id connot be {type(product.producer_id)}")
    elif product.producer_id <= 0:
        return ValueError("Producer_id must be positive")
    
    
    return True
