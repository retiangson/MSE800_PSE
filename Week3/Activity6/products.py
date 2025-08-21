from database import get_connection

def add_product(name, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()

def view_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()