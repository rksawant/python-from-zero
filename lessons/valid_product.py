from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field
from fastapi import APIRouter

valid_product_router = APIRouter()

class ProductIn(BaseModel):
    name: str
    price: float = Field(gt=0)
    in_stock: bool

class Product(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)
    in_stock: bool

@valid_product_router.post("/valid_products")
def add_product(item: ProductIn):
    return item
