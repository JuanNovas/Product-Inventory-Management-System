from database.connection import get_db_connection

def query_function(func):
    def decorator(*args, **kwargs):
        conn = get_db_connection()
        result = None
        try:
            result = func(conn, *args, **kwargs)
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return result
    return decorator