from psycopg2.extras import RealDictCursor
from database.decorators import query_function
from backend.models.producers import Producer
from backend.data_access.update_check import was_id_updated


def is_valid_producer(producer: Producer) -> None:
    if len(producer.name.strip()) > 100:
        raise ValueError("Name len must be less than 100")
    if len(producer.name.strip()) == 0:
        raise ValueError("Name cannot be null")


@query_function
def get_all_producers(conn) -> list[RealDictCursor]:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM producers')
    return cursor.fetchall()


@query_function
def get_producer_by_id(conn, id: int) -> RealDictCursor:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM producers WHERE id = (%s)",(id,))
    return cursor.fetchone()


@query_function
def add_producer(conn, producer: Producer) -> None:
    is_valid_producer(producer)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO producers (name) VALUES (%s)', (producer.name,))
    conn.commit()


@query_function
def delete_producer(conn, id: int) -> None:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producers WHERE id = (%s) RETURNING id",(id,))
    conn.commit()
    
    was_id_updated(cursor)
    
    
@query_function
def update_producer(conn, id: int, producer: Producer) -> None:
    is_valid_producer(producer)
    cursor = conn.cursor()
    cursor.execute("UPDATE producers SET name = (%s) WHERE id = (%s) RETURNING id",(producer.name, id))
    conn.commit()
    
    was_id_updated(cursor)