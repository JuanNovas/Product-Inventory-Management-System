from psycopg2.extras import RealDictCursor
from database.connection import get_db_connection

def get_all_categories():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    conn.close()
    return categories

def add_category(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO categories (name) VALUES (%s)', (name,))
    conn.commit()
    conn.close()
    
    

