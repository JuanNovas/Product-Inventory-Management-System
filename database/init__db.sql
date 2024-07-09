CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS producers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL DEFAULT 0 CHECK (price > 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock > 0),
    category_id INTEGER REFERENCES categories(id),
    producer_id INTEGER REFERENCES producers(id)
);

CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    total_price INTEGER CHECK (amount >= 0),
    amount INTEGER DEFAULT 1 CHECK (amount > 0),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

BEGIN;

INSERT INTO categories (name) VALUES ('food');
INSERT INTO categories (name) VALUES ('clothes');

INSERT INTO producers (name) VALUES ('productor');
INSERT INTO producers (name) VALUES ('productora');

COMMIT;
