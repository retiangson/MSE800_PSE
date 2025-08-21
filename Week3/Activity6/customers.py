from database import get_connection

def add_customer(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def view_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    conn.commit()
    conn.close()