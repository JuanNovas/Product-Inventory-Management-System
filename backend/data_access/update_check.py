from psycopg2.extensions import cursor as Psycopg2Cursor

def was_id_updated(cursor: Psycopg2Cursor):
    """Checks if the cursor is returning something to check if the query was valid.
       Requires a RETURNING id at the end of the query.

    Args:
        cursor (Psycopg2Cursor): conection cursor

    Raises:
        ValueError: If there is no returning value
    """
    updated_row = cursor.fetchone()
    if updated_row is None:
        raise ValueError("ID not found")