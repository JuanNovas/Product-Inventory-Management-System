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
        raise ValueError("Name len must be less than 255")
    if len(name.strip()) == 0:
        raise ValueError("Name cannot be null")
    if price < 0:
        raise ValueError("Price must be at least 0")
    if stock < 0:
        raise ValueError("Stock must be at least 0")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name,price,stock,category_id,producer_id) VALUES (%s,%s,%s,%s,%s)',(name,price,stock,category,producer))
    conn.commit()