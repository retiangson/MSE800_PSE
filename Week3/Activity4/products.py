from database import conn, cursor

def add_product():
    name = input("Product name: ")
    description = input("Description: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))
    cursor.execute('INSERT INTO products (name, description, price, stock_quantity) VALUES (?, ?, ?, ?)',
                   (name, description, price, stock))
    conn.commit()
    print("Product added successfully!\n")

def delete_product():
    product_id = int(input("Product ID to delete: "))
    cursor.execute('DELETE FROM products WHERE product_id = ?', (product_id,))
    conn.commit()
    print("Product deleted successfully!\n")

def view_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    print("\n--- Products ---")
    for p in products:
        print(f"ID: {p[0]}, Name: {p[1]}, Price: {p[3]}, Stock: {p[4]}")
    print()

def product_menu():
    while True:
        print("\n--- Product Menu ---")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. View Products")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            view_products()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.\n")