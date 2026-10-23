from fastapi import FastAPI

app = FastAPI()
contacts = [
    {"name": "Sam", "phone": "555-0100", "city": "Lagos"},
    {"name": "Mina", "phone": "555-0142", "city": "Seoul"},
]


@app.get("/contacts")
def list_contacts():
    return contacts


@app.post("/contacts")
def add_contact(contact: dict):
    contacts.append(contact)
    return contact
