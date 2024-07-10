from psycopg2.extras import RealDictCursor
from database.decorators import query_function
from backend.models.sales import Sale
from backend.data_access.utils.update_check import was_id_updated

@query_function
def get_all_sales(conn) -> list[RealDictCursor]:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM sales')
    sales = cursor.fetchall()
    return sales


@query_function
def get_sale_by_id(conn, id: int) -> RealDictCursor:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM sales WHERE id = (%s)",(id,))
    return cursor.fetchone()


@query_function
def add_sale(conn, sale: Sale) -> None:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sales (product_id,total_price,amount) VALUES (%s,%s,%s)',(sale.product_id,sale.total_price,sale.amount))
    conn.commit()
    
    
@query_function
def delete_sale(conn, id: int) -> None:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sales WHERE id = (%s) RETURNING id",(id,))
    conn.commit()
    
    was_id_updated(cursor)
    
    
@query_function
def update_sale(conn, id: int, sale: Sale) -> None:
    cursor = conn.cursor()
    cursor.execute("UPDATE sales SET product_id = (%s), total_price = (%s), amount = (%s) WHERE id = (%s) RETURNING id",(sale.product_id, sale.total_price, sale.amount, id))
    conn.commit()
    
    was_id_updated(cursor)