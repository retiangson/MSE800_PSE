from database import SessionLocal
from models import Product

def add_product(name, price):
    session = SessionLocal()
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()
    session.close()

def view_products():
    session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return products

def delete_product(product_id):
    session = SessionLocal()
    product = session.query(Product).get(product_id)
    if product:
        session.delete(product)
        session.commit()
    session.close()