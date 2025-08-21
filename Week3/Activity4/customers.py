from database import conn, cursor

def add_customer():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")
    cursor.execute('INSERT INTO customers (first_name, last_name, email, phone, address) VALUES (?, ?, ?, ?, ?)',
                   (first_name, last_name, email, phone, address))
    conn.commit()
    print("Customer added successfully!\n")

def delete_customer():
    customer_id = int(input("Customer ID to delete: "))
    cursor.execute('DELETE FROM customers WHERE customer_id = ?', (customer_id,))
    conn.commit()
    print("Customer deleted successfully!\n")

def view_customers():
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    print("\n--- Customers ---")
    for c in customers:
        print(f"ID: {c[0]}, Name: {c[1]} {c[2]}, Email: {c[3]}, Phone: {c[4]}")
    print()

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Add Customer")
        print("2. Delete Customer")
        print("3. View Customers")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            add_customer()
        elif choice == '2':
            delete_customer()
        elif choice == '3':
            view_customers()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.\n")