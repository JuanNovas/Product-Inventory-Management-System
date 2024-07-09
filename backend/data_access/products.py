from psycopg2.extras import RealDictCursor
from database.decorators import query_function

@query_function
def get_all_products(conn):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    return products


@query_function
def add_product(conn, name: str, price: int=0, stock: int=0, category: int=None, producer: int=None):
    if len(name) > 255:
        raise ValueError("Error: Name len must be less than 255")
    if price < 0:
        raise ValueError("Error: price must be at least 0")
    if stock < 0:
        raise ValueError("Error stock must be at least 0")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name,price,stock,category_id,producer_id) VALUES (%s,%s,%s,%s,%s)',(name,price,stock,category,producer))
    conn.commit()