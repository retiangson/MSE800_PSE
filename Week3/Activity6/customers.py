from database import SessionLocal
from models import Customer

def add_customer(name, email):
    session = SessionLocal()
    customer = Customer(name=name, email=email)
    session.add(customer)
    session.commit()
    session.close()

def view_customers():
    session = SessionLocal()
    customers = session.query(Customer).all()
    session.close()
    return customers

def delete_customer(customer_id):
    session = SessionLocal()
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()
    session.close()