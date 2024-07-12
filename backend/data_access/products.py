from psycopg2.extras import RealDictCursor
from database.decorators import query_function
from backend.models.products import Product
from backend.data_access.utils.update_check import was_id_updated


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
def get_product_by_filter(conn, name: str=None, min_price: int=None, max_price: int=None, min_stock: int=None, max_stock: int=None, category_id: int=None, producer_id: int=None) -> list[RealDictCursor]:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = "SELECT * FROM products WHERE TRUE"
    params = []
    
    if name:
        query += " AND name ILIKE %s"
        params.append(f"%{name}%")
    
    if min_price is not None:
        query += " AND price >= %s"
        params.append(min_price)
    
    if max_price is not None:
        query += " AND price <= %s"
        params.append(max_price)
    
    if min_stock is not None:
        query += " AND stock >= %s"
        params.append(min_stock)
    
    if max_stock is not None:
        query += " AND stock <= %s"
        params.append(max_stock)
    
    if category_id is not None:
        query += " AND category_id = %s"
        params.append(category_id)
    
    if producer_id is not None:
        query += " AND producer_id = %s"
        params.append(producer_id)
    
    cursor.execute(query,params)
    conn.commit()
    
    products = cursor.fetchall()
    return products


@query_function
def add_product(conn, product: Product):
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