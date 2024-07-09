from psycopg2.extras import RealDictCursor
from database.decorators import query_function

@query_function
def get_all_sales(conn):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM sales')
    sales = cursor.fetchall()
    return sales


@query_function
def add_sale(conn, product_id: int, total_price: int=None, amount: int=1):
    if total_price < 0:
        raise ValueError("Error: total price must be at least 0")
    if amount < 1:
        raise ValueError("Error: amount must be at least 1")
    
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sales (product_id,total_price,amount) VALUES (%s,%s,%s)',(product_id,total_price,amount))
    conn.commit()