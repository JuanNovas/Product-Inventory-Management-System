from psycopg2.extras import RealDictCursor
from database.decorators import query_function

@query_function
def get_all_producers(conn):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM producers')
    producers = cursor.fetchall()
    return producers

@query_function
def add_producer(conn, name: str):
    if len(name) > 100:
        raise ValueError("Name len must be less than 100")
    if len(name.strip()) == 0:
        raise ValueError("Name cannot be null")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO producers (name) VALUES (%s)', (name,))
    conn.commit()