from fastapi import FastAPI
from backend.apis import producers

app = FastAPI()

app.include_router(producers.router, prefix="")