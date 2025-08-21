from database import SessionLocal
from models import Order, Customer, Product

def add_order(customer_id, product_id):
    session = SessionLocal()
    customer = session.query(Customer).get(customer_id)
    product = session.query(Product).get(product_id)

    if customer and product:
        order = Order(customer=customer, product=product)
        session.add(order)
        session.commit()
    session.close()

def view_orders():
    session = SessionLocal()
    try:
        orders = session.query(Order).all()
        listOfOrders = []
        print("\n--- Orders Table Records ---")
        if orders:
            for order in orders:
               print(order)
        else:
            print("No orders found.")

        return order
    finally:
        session.close()

def delete_order(order_id):
    session = SessionLocal()
    order = session.query(Order).get(order_id)
    if order:
        session.delete(order)
        session.commit()
    session.close()