from backend.models.sales import Sale


def is_valid_sale(sale: Sale):
    if type(sale.product_id) != int:
        return TypeError("Product_id must be an int")
    if sale.product_id <= 0:
        return ValueError("Product_id must be positive")
    
    if type(sale.total_price) != int:
        return TypeError("Total_price must be an int")
    if sale.total_price < 0:
        return ValueError("Total price must be at least 0")
    
    if type(sale.amount) != int:
        return TypeError("Amount must be an int")
    if sale.amount < 1:
        return ValueError("Amount must be at least 1")