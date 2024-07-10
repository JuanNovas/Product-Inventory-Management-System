from psycopg2.extras import RealDictCursor
from database.decorators import query_function
from backend.models.products import Product
from backend.data_access.update_check import was_id_updated

def is_valid_product(product: Product) -> None:
    if len(product.name.strip()) > 255:
        raise ValueError("Name len must be less than 255")
    if len(product.name.strip()) == 0:
        raise ValueError("Name cannot be null")
    if product.price < 0:
        raise ValueError("Price must be at least 0")
    if product.stock < 0:
        raise ValueError("Stock must be at least 0")


@query_function
def get_all_products(conn) -> list[RealDictCursor]:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    return products


@query_function
def get_product_by_id(conn, id: int) -> RealDictCursor:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM products WHERE id = (%s)",(id,))
    return cursor.fetchone()


@query_function
def add_product(conn, product: Product):
    is_valid_product(product) # Raises exception if not valid
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name,price,stock,category_id,producer_id) VALUES (%s,%s,%s,%s,%s)',(product.name,product.price,product.stock,product.category_id,product.producer_id))
    conn.commit()
    
    
@query_function
def delete_product(conn, id: int) -> None:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = (%s) RETURNING id",(id,))
    conn.commit()
    
    was_id_updated(cursor)
    
    
@query_function
def update_product(conn, id: int, product: Product) -> None:
    is_valid_product(product) # Raises exception if not valid
    cursor = conn.cursor()
    cursor.execute("""
                   UPDATE products SET name = (%s),
                   price = (%s),
                   stock = (%s),
                   category_id = (%s),
                   producer_id = (%s) 
                   WHERE id = (%s)
                   RETURNING id
                   """,
                   (product.name, product.price, product.stock, product.category_id, product.producer_id, id))
    conn.commit()
    
    was_id_updated(cursor)
    
    
@query_function
def set_stock(conn, id: int, new_stock: int):
    if new_stock < 0:
        new_stock = 0
    
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET stock = (%s) WHERE id = (%s) RETURNING id",(new_stock,id))
    conn.commit()
    
    was_id_updated(cursor)
    
    
@query_function
def update_multiple_price_by_producer(conn, producer_id: int, rate: float):
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = price * (%s) WHERE producer_id = (%s) RETURNING id",(rate, producer_id))
    conn.commit()
    
    was_id_updated(cursor)
    
    
@query_function
def update_multiple_price_by_category(conn, category_id: int, rate: float):
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = price * (%s) WHERE category_id = (%s) RETURNING id",(rate, category_id))
    conn.commit()
    
    was_id_updated(cursor)
    
    
@query_function
def update_multiple_price_by_producer_category(conn, producer_id: int, category_id: int, rate: float):
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = price * (%s) WHERE producer_id = (%s) AND category_id = (%s) RETURNING id",(rate, producer_id, category_id))
    conn.commit()
    
    was_id_updated(cursor)
    
    
@query_function
def update_all_price(conn, rate: float):
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = price * (%s)",(rate,))
    conn.commit()