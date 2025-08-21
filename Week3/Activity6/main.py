from database import engine
from models import Base
import customers
import products
import orders

# Create tables if not exist
Base.metadata.create_all(bind=engine)

def menu():
    while True:
        print("\n===== Activity 4 (SQLAlchemy ORM) =====")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Delete Customer")
        print("4. Add Product")
        print("5. View Products")
        print("6. Delete Product")
        print("7. Add Order")
        print("8. View Orders")
        print("9. Delete Order")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            customers.add_customer(name, email)
            print("Customer added.")

        elif choice == "2":
            for c in customers.view_customers():
                print(c)

        elif choice == "3":
            cid = int(input("Enter customer ID to delete: "))
            customers.delete_customer(cid)
            print("Customer deleted.")

        elif choice == "4":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            products.add_product(name, price)
            print("Product added.")

        elif choice == "5":
            for p in products.view_products():
                print(p)

        elif choice == "6":
            pid = int(input("Enter product ID to delete: "))
            products.delete_product(pid)
            print("Product deleted.")

        elif choice == "7":
            cid = int(input("Enter customer ID: "))
            pid = int(input("Enter product ID: "))
            orders.add_order(cid, pid)
            print("Order added.")

        elif choice == "8":
            orders.view_orders()

        elif choice == "9":
            oid = int(input("Enter order ID to delete: "))
            orders.delete_order(oid)
            print("Order deleted.")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()