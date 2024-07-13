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
    price INTEGER NOT NULL DEFAULT 0 CHECK (price >= 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL,
    producer_id INTEGER REFERENCES producers(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id) ON DELETE SET NULL,
    total_price INTEGER CHECK (amount >= 0),
    amount INTEGER DEFAULT 1 CHECK (amount > 0),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION update_stock_on_sale()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE products SET stock = stock - NEW.amount
    WHERE id = NEW.product_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_stock_on_sale_trigger
BEFORE INSERT ON sales
FOR EACH ROW
EXECUTE FUNCTION update_stock_on_sale();

BEGIN;

INSERT INTO categories (name) VALUES ('food');
INSERT INTO categories (name) VALUES ('clothes');

INSERT INTO producers (name) VALUES ('ABC');
INSERT INTO producers (name) VALUES ('123');

COMMIT;
