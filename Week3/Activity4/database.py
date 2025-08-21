import sqlite3

def create_connection():
    conn = sqlite3.connect("store.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock_quantity INTEGER NOT NULL
        )
    ''')

    # Create Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            address TEXT
        )
    ''')

    # Create Orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')

    # Create OrderItems table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')

    conn.commit()
    conn.close()
