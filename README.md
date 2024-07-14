# Product Inventory Management System
This project showcase the backend of a product inventory managment system built using FastAPI as the Framework, PosgreSQL as the Database and following a Layered Architechture.

## Table of content
- [Project Scope](#project-scope)
- [Technologies](#technologies-used)
- [Architecture](#architecture)
- [Database](#database)
- [Testing](#testing)
- [API Endpoints](#api-endpoints)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)

## Project Scope
This projects simulates the backend of an inventory managment system with a focus on creating a robust and scalable code. The project scope includes functionalities such as all CRUD interactions with the products alongside the posibility to group them by category or producer. Also the posibility to track sales, automatically updating the stock count. 

## Technologies Used
- Python 🐍
- FastAPI ⚡
- PosgreSQL 🐘
- Docker 🐋
- Pytest 🧪

## Architecture
The projects code organization follows a layered architecture, where every layer only comunicates with the one upper or below itself. This allows to divide some process like data validations, and database querys making it easier to track process and prevent security errors.
![Layered architecture graph](readme_images/architecture_graph.png)
### APIs Layer
This layer handle the http requests. After receiving the request it calls the logic layer and after receiving the response returns a json with the information.
### Logic Layer
After the http request this layer validates the data received from the APIs layer and if the data is valid calls the Data Access layer, if not, returns an error message.
### Data Access Layer
This layer makes the Database querys with the validated data from the Logic layer and returns the information.
### Database Layer
The last layer is the Database itself, where the app data is stored.

## Database
![Database schema image](readme_images/database_schema.JPG)
The database is a PosgreSQL one and is hosted in a docker container. It contains 4 different tables:
- **Categories**: Contains the categories of the products.
- **Producers**: Contains the diferents producers.
- **Products**: Contains all the products of the bussiness and their information.
- **Sales**: Contains the transaction history.

### Categories & Producers
Stores the name of the category/producer to be refered in the products table. Making it easier to divide the products in diferent groups and manipulated them more efficiently.
### Products
Stores the name, price, stock, category and producer of a product. 
### Sales
Stores the sales made keeping track of the stock movement and updates the stock of the products after every sale autocatically.

## Testing
This project contains 50 tests that checks APIs functionalities alongside the data validation process, making requests with invalid data and checking if the error message pops up correctly. All this test are automatically executed by github after every push/pull request. You can check the green checkmark "✅" in the top of the repository, who ensures everything is working correctly.
#### Important note before testing execution
To test CRUD endpoint correctly the database needs to be recreated before runing the tests or they will fail.

## API endpoints
The endpoints include CRUD posibilities over the 4 tables, a filter query for products,  update stock options and a simple way to update a lot of prices all by one. This last feature is speacially usefull in country with high inflation , thing that is not normally present in inventory managment systems.  
For specific information about all the endpoints and methods allowed [click here!](endpoints_documentation.md)

## Directory Structure

- **.github/workflows/**: Tells githb to run the tests.
- **backend/**: Backend layers.
    - **apis/**: App endpoints.
        - **utils/**: Response functions used in the apis.
    - **logic/**: Data validation process.
        - **validations/**: Validation functions used in multiple instances.
    - **data_access/**: Database comunication.
        - **utils/**: Success check function.
    - **models/**: Models used to encapsulate data.
- **database/**: Database scripts.
- **tests/**: Project tests.
- **readme_images/**: Images for the README you are reading

## Instalation

### Prerequisites

- Python
- Docker
- Git

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/JuanNovas/Product-Inventory-Management-System.git
    cd Product-Inventory-Management-System
    ```
2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up the database container**:
    ```bash
    docker-compose up -d
    ```
5. **Execute the main script**:
    ```bash
    python3 main.py
    ```

## Usage
To try this app by yourself you can use tools like Postman or Insomnia. There is also a built-in option by FastAPI, wich is a Swagger web page available at http://127.0.0.1:8000/docs when executing the program.
![Swagger page screenshot](readme_images/swagger_screenshot.JPG)

## Thank You ❤️

Thanks for checking my project for any questions or feedback, please contact me via [juanignacionovas@gmail.com](mailto:juanignacionovas@gmail.com).