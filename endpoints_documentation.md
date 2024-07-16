# API Endpoints

## Test endpoint
- **GET //**
  - **Returns:**
  ```json
    {
      "hello": "world"
    }
    ```

## Producers

- **GET /producers/**
  - Lists all producers.
- **GET /producers/{id}**
  - Retrieves a producer by its ID.
- **POST /producers/**
  - Creates a new producer.
  - **Request body:**
  ```json
    {
      "name": "producer_name"
    }
    ```
- **PUT /producers/{id}**
  - Updates a producer by its ID.
  - **Request body:**
  ```json
    {
      "name": "producer_name"
    }
    ```
- **DELETE /producers/{id}**
  - Deletes a producer by its ID.

## Categories

- **GET /categories/**
  - Lists all categories.
- **GET /categories/{id}**
  - Retrieves a category by its ID.
- **POST /categories/**
  - Creates a new category.
  - **Request body:**
  ```json
    {
      "name": "category_name"
    }
    ```
- **PUT /categories/{id}**
  - Updates a category by its ID.
  - **Request body:**
  ```json
    {
      "name": "category_name"
    }
    ```
- **DELETE /categories/{id}**
  - Deletes a category by its ID.

## Products

- **GET /products/**
  - Lists all products.
- **GET /products/{id}**
  - Retrieves a product by its ID.
- **GET /products/filter**
  - Retrieves products by the specifications.
  - **Request body:**
  ```json
    {
      "name": "product_name",(optional)
      "min_price": 11,(optional)
      "max_price": 22,(optional)
      "min_stock": 33,(optional)
      "max_stock": 44,(optional)
      "category_id": 55,(optional)
      "producer_id": 66 (optional)
    }
    ```
- **POST /products/**
  - Creates a new product.
  - **Request body:**
  ```json
    {
      "name": "product_name",
      "price": 11,(optional)
      "stock": 22,(optional)
      "category_id": 33,(optional)
      "producer_id": 44 (optional)
    }
    ```
- **PUT /products/{id}**
  - Updates a product by its ID.
  - **Request body:**
  ```json
    {
      "name": "product_name",
      "price": 11,(optional)
      "stock": 22,(optional)
      "category_id": 33,(optional)
      "producer_id": 44 (optional)
    }
    ```
- **DELETE /products/{id}**
  - Deletes a product by its ID.

## Sales

- **GET /sales/**
  - Lists all sales.
- **GET /sales/{id}**
  - Retrieves a sale by its ID.
- **POST /sales/**
  - Creates a new sale.
  - **Request body:**
  ```json
    {
      "product_id": 11,
      "total_price": 22,
      "amount": 33 (optional)
    }
    ```
- **PUT /sales/{id}**
  - Updates a sale by its ID.
  - **Request body:**
  ```json
    {
      "product_id": 11,
      "total_price": 22,
      "amount": 33 (optional)
    }
    ```
- **DELETE /sales/{id}**
  - Deletes a sale by its ID.

## Update Prices

- **POST /update_prices**
  - Updates the prices of a group of products.
  - **Request body:**
  ```json
    {
      "producer_id": 11,(optional)
      "category_id": 22,(optional)
      "rate": 0.33
    }
    ```

## Update Stock

- **POST /set_stock/**
  - Sets the stock of a specific product.
  - **Request body:**
  ```json
    {
      "id": 11,
      "stock": 22
    }
    ```
- **POST /add_stock/**
  - Adds stock for a specific product.
  - **Request body:**
  ```json
    {
      "id": 11,
      "stock": 22
    }
    ```
