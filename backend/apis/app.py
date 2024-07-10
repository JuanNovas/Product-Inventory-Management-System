from fastapi import FastAPI
from backend.apis import producers, categories, products, sales, update_stock, update_prices

app = FastAPI()

app.include_router(producers.router, prefix="")
app.include_router(categories.router, prefix="")
app.include_router(products.router, prefix="")
app.include_router(sales.router, prefix="")
app.include_router(update_stock.router, prefix="")
app.include_router(update_prices.router, prefix="")