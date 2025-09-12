#New Services (UserService, OrderService)
#Use one shared connection (through Database).
#Cursor is created quickly, no reconnect each call.
#More efficient for multiple queries.
#Old Services (UserServiceOld, OrderServiceOld)
#Open a new SQLite connection every method call.
#Create cursor, run query, close connection → repeated overhead.
#Much slower if you call repeatedly.

import sqlite3
import random
from faker import Faker
import time

class Database:
    def __init__(self, db_path="app.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # Access results like dicts

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    # Context manager support
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()


class UserService:
    def __init__(self, db: Database):
        self.db = db

    def get_user(self, user_id):
        cur = self.db.get_cursor()
        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cur.fetchone()


class OrderService:
    def __init__(self, db: Database):
        self.db = db

    def get_orders(self, user_id):
        cur = self.db.get_cursor()
        cur.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        return cur.fetchall()


def init_db(db: Database):
    fake = Faker()
    cur = db.get_cursor()

    # Drop existing tables
    cur.execute("DROP TABLE IF EXISTS orders;")
    cur.execute("DROP TABLE IF EXISTS users;")

    # Create tables
    cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        product TEXT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    # Insert 100 users
    users = [(fake.name(), fake.unique.email()) for _ in range(100)]
    cur.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

    # Insert random orders for each user
    for user_id in range(1, 101):
        for _ in range(random.randint(1, 5)):
            product = fake.word().capitalize()
            amount = round(random.uniform(10, 500), 2)
            cur.execute(
                "INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)",
                (user_id, product, amount)
            )

    db.commit()
    print("Database initialized with 100 users and random orders.")


class UserServiceOld:
    def get_user(self, user_id):
        conn = sqlite3.connect('app.db')  # New connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result
 
class OrderServiceOld:
    def get_orders(self, user_id):
        conn = sqlite3.connect('app.db')  # Another new connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result

if __name__ == "__main__":
    # Use context manager so connection closes safely
    with Database("app.db") as db:
        #init_db(db)

        # New service instances
        user_service = UserService(db)
        order_service = OrderService(db)
        # ---------------------------
        # Measure NEW service timing
        # ---------------------------
        start_new = time.perf_counter()
        user_new = user_service.get_user(1)
        orders_new = order_service.get_orders(1)
        end_new = time.perf_counter()

        print("New Service User:", dict(user_new) if user_new else None)
        print("New Service Orders:", len(orders_new))
        print(f"New Services took: {end_new - start_new:.6f} seconds\n")

   

    # Old service instances
    us = UserServiceOld()
    os = OrderServiceOld()

    # ---------------------------
    # Measure OLD service timing
    # ---------------------------
    start_old = time.perf_counter()
    user_old = us.get_user(1)
    orders_old = os.get_orders(1)
    end_old = time.perf_counter()

    print("Old Service User:", user_old)
    print("Old Service Orders:", len(orders_old))
    print(f"Old Services took: {end_old - start_old:.6f} seconds\n")