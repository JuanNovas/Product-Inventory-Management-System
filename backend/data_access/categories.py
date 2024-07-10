from psycopg2.extras import RealDictCursor
from database.decorators import query_function
from backend.models.categories import Category
from backend.data_access.utils.update_check import was_id_updated


def is_valid_category(category: Category) -> None:
    if len(category.name.strip()) > 100:
        raise ValueError("Name len must be less than 100")
    if len(category.name.strip()) == 0:
        raise ValueError("Name cannot be null")


@query_function
def get_all_categories(conn) -> list[RealDictCursor]:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    return categories


@query_function
def get_category_by_id(conn, id: int) -> RealDictCursor:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM categories WHERE id = (%s)",(id,))
    return cursor.fetchone()


@query_function
def add_category(conn, category: Category) -> None:
    is_valid_category(category)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO categories (name) VALUES (%s)', (category.name,))
    conn.commit()
    
    
@query_function
def delete_category(conn, id: int) -> None:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categories WHERE id = (%s) RETURNING id",(id,))
    conn.commit()
    
    was_id_updated(cursor)
    
    
@query_function
def update_category(conn, id: int, category: Category) -> None:
    is_valid_category(category)
    cursor = conn.cursor()
    cursor.execute("UPDATE categories SET name = (%s) WHERE id = (%s)",(category.name, id))
    conn.commit()
    
    was_id_updated(cursor)