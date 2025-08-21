from database import init_db
import customers
import products
import orders

def menu():
    while True:
        print("\n===== Activity 4 Menu =====")
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
            for row in customers.view_customers():
                print(row)

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
            for row in products.view_products():
                print(row)

        elif choice == "6":
            pid = int(input("Enter product ID to delete: "))
            products.delete_product(pid)
            print("Product deleted.")

        elif choice == "7":
            print("\nCustomers :")
            for row in customers.view_customers():
                print(row)
            print("\nProducts :")
            for row in products.view_products():
                print(row)

            cid = int(input("Enter customer ID: "))
            pid = int(input("Enter product ID: "))
            orders.add_order(cid, pid)
            print("Order added.")

        elif choice == "8":
            for row in orders.view_orders():
                print(row)

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
    init_db()
    menu()