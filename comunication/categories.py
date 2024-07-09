from psycopg2.extras import RealDictCursor
from database.decorators import query_function

@query_function
def get_all_categories(conn):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    return categories

@query_function
def add_category(conn, name):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO categories (name) VALUES (%s)', (name,))
    conn.commit()