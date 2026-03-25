import requests
from sqlalchemy.orm import Session
from models.customer import Customer

# FLASK_API = "http://localhost:5000/api/customers"

FLASK_API = "http://mock-server:5000/api/customers"

def fetch_all_customers():
    all_data = []
    page = 1
    limit = 10

    while True:
        response = requests.get(FLASK_API, params={"page": page, "limit": limit})
        data = response.json()

        customers = data.get("data", [])
        if not customers:
            break

        all_data.extend(customers)
        page += 1

    return all_data


def upsert_customer(db: Session, customer_data):
    existing = db.query(Customer).filter(Customer.customer_id == customer_data["customer_id"]).first()

    if existing:
        for key, value in customer_data.items():
            setattr(existing, key, value)
    else:
        new_customer = Customer(**customer_data)
        db.add(new_customer)