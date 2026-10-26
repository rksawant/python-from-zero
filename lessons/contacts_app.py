from fastapi import FastAPI
from routes import router, product_router
from valid_product import valid_product_router

app = FastAPI()
app.include_router(router)
app.include_router(product_router)
app.include_router(valid_product_router)
