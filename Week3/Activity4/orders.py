from database import conn, cursor
from products import view_products
from customers import view_customers

def create_order():
    view_customers()
    customer_id = int(input("Enter customer ID for this order: "))
    cursor.execute('INSERT INTO orders (customer_id) VALUES (?)', (customer_id,))
    order_id = cursor.lastrowid
    conn.commit()
    print(f"Order {order_id} created successfully!")

    while True:
        view_products()
        product_id = int(input("Enter product ID to add to order (0 to finish): "))
        if product_id == 0:
            break
        quantity = int(input("Enter quantity: "))
        cursor.execute('SELECT price, stock_quantity FROM products WHERE product_id = ?', (product_id,))
        result = cursor.fetchone()
        if result:
            price, stock = result
            if quantity > stock:
                print("Not enough stock! Try a lower quantity.")
                continue
            cursor.execute('INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)',
                           (order_id, product_id, quantity, price))
            cursor.execute('UPDATE products SET stock_quantity = stock_quantity - ? WHERE product_id = ?',
                           (quantity, product_id))
            conn.commit()
            print(f"Added {quantity} of product {product_id} to order.\n")
        else:
            print("Product not found.")

def view_orders():
    cursor.execute('''
        SELECT o.order_id, c.first_name || ' ' || c.last_name, o.order_date, o.status
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
    ''')
    orders = cursor.fetchall()
    print("\n--- Orders ---")
    for o in orders:
        print(f"Order ID: {o[0]}, Customer: {o[1]}, Date: {o[2]}, Status: {o[3]}")
        cursor.execute('''
            SELECT p.name, oi.quantity, oi.price
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            WHERE oi.order_id = ?
        ''', (o[0],))
        items = cursor.fetchall()
        for item in items:
            print(f"   Product: {item[0]}, Quantity: {item[1]}, Price: {item[2]}")
    print()

def order_menu():
    while True:
        print("\n--- Order Menu ---")
        print("1. Create Order")
        print("2. View Orders")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            create_order()
        elif choice == '2':
            view_orders()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.\n")