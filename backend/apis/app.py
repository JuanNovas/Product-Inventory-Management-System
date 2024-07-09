from fastapi import FastAPI
from backend.apis import producers, categories, products, sales

app = FastAPI()

app.include_router(producers.router, prefix="")
app.include_router(categories.router, prefix="")
app.include_router(products.router, prefix="")
app.include_router(sales.router, prefix="")