from database import get_connection

def add_order(customer_id, product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (customer_id, product_id) VALUES (?, ?)", (customer_id, product_id))
    conn.commit()
    conn.close()

def view_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT orders.id, customers.name, products.name
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        JOIN products ON orders.product_id = products.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_order(order_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
    conn.commit()
    conn.close()