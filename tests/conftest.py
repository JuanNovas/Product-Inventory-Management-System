import pytest
import psycopg2
from configparser import ConfigParser

def config(filename="database/database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} is not found in the {filename} file.")
    
    return db


@pytest.fixture(scope="session", autouse=True)
def clean_db():
    data = config()
    conn = psycopg2.connect(**data)
    cursor = conn.cursor()
    # Truncar tablas
    cursor.execute("TRUNCATE TABLE sales, products, producers, categories RESTART IDENTITY CASCADE")
    conn.commit()
    cursor.close()
    conn.close()

