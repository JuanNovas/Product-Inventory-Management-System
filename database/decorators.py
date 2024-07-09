from database.connection import get_db_connection

def query_function(func):
    def decorator(*args, **kwargs):
        conn = get_db_connection()
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return decorator