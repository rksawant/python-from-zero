from fastapi import APIRouter

router = APIRouter()

@router.get("/all_contacts")
def get_all_contacts():
    return {"message": "All contacts"}

contacts = [
    {"name": "Sam", "phone": "555-0100", "city": "Lagos"},
    {"name": "Mina", "phone": "555-0142", "city": "Seoul"},
]


@router.get("/contacts")
def list_contacts():
    return contacts


@router.post("/contacts")
def add_contact(contact: dict):
    contacts.append(contact)
    return contact


product_router = APIRouter()

products = [
    {"name": "Pen", "price": 1.5, "in_stock": True},
    {"name": "Notebook", "price": 3.0, "in_stock": False},
]


@product_router.get("/products")
def list_products():
    return products


@product_router.post("/products")
def add_product(product: dict):
    products.append(product)
    return product
