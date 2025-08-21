import pandas as pd
import sqlite3
from ucimlrepo import fetch_ucirepo

# -------------------- Data Handler Classes --------------------
class DataHandler:
    def __init__(self, dataset_id: int, parquet_file: str = "dataset.parquet"):
        self.dataset_id = dataset_id
        self.parquet_file = parquet_file
        self.data = None

    def fetch_data(self):
        dataset = fetch_ucirepo(id=self.dataset_id)
        X = dataset.data.features
        y = dataset.data.targets
        self.data = pd.concat([X, y], axis=1)

    def save_as_parquet(self):
        self.data.to_parquet(self.parquet_file, index=False)

class DataAnalyzer:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

# -------------------- Database Initialisation --------------------
def init_database():
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()

    # Create Users and Students tables
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT,
        Email TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        Stu_ID INTEGER PRIMARY KEY,
        Stu_name TEXT,
        Stu_address TEXT
    )
    """)

    # Check if Users table already has data
    cur.execute("SELECT COUNT(*) FROM Users")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO Users (Username, Email) VALUES (?, ?)", [
            ("john_doe", "john@example.com"),
            ("jane_smith", "jane@example.com")
        ])
        print("Default Users added.")
    else:
        print("Users table already has data. Skipping insert.")

    # Check if Students table already has data
    cur.execute("SELECT COUNT(*) FROM Students")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO Students (Stu_ID, Stu_name, Stu_address) VALUES (?, ?, ?)", [
            (1, "Alice Johnson", "123 Baker Street"),
            (2, "Bob Williams", "45 Queen Street")
        ])
        print("Default Students added.")
    else:
        print("ℹStudents table already has data. Skipping insert.")

    conn.commit()
    conn.close()

# -------------------- CRUD Functions --------------------
def view_records(table):
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    print(f"\n--- {table} Table Records ---")
    for row in rows:
        print(row)
    conn.close()

def add_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (Username, Email) VALUES (?, ?)", (username, email))
    conn.commit()
    conn.close()
    print(f"User '{username}' added.")

def add_student():
    stu_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    address = input("Enter student address: ")
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Students (Stu_ID, Stu_name, Stu_address) VALUES (?, ?, ?)", (stu_id, name, address))
    conn.commit()
    conn.close()
    print(f"Student '{name}' added.")

def edit_record(table):
    id_field = "User_ID" if table == "Users" else "Stu_ID"
    record_id = input(f"Enter {id_field} to edit: ")

    if table == "Users":
        username = input("Enter new username: ")
        email = input("Enter new email: ")
        query = f"UPDATE Users SET Username=?, Email=? WHERE {id_field}=?"
        values = (username, email, record_id)

    else:
        name = input("Enter new student name: ")
        address = input("Enter new student address: ")
        query = f"UPDATE Students SET Stu_name=?, Stu_address=? WHERE {id_field}=?"
        values = (name, address, record_id)

    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute(query, values)
    conn.commit()
    conn.close()
    print("Record updated successfully.")

def delete_record(table):
    id_field = "User_ID" if table == "Users" else "Stu_ID"
    record_id = input(f"Enter {id_field} to delete: ")
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table} WHERE {id_field}=?", (record_id,))
    conn.commit()
    conn.close()
    print("Record deleted successfully.")


# -------------------- Menu --------------------
def menu():
    while True:
        print("\nMENU:")
        print("1. View Users")
        print("2. Add User")
        print("3. Edit User")
        print("4. Delete User")
        print("5. View Students")
        print("6. Add Student")
        print("7. Edit Student")
        print("8. Delete Student")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_records("Users")
        elif choice == "2":
            add_user()
        elif choice == "3":
            edit_record("Users")
        elif choice == "4":
            delete_record("Users")
        elif choice == "5":
            view_records("Students")
        elif choice == "6":
            add_student()
        elif choice == "7":
            edit_record("Students")
        elif choice == "8":
            delete_record("Students")
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# -------------------- Main --------------------
def main():
    handler = DataHandler(dataset_id=320, parquet_file="student_performance.parquet")
    handler.fetch_data()
    handler.save_as_parquet()

    init_database()
    view_records("Users")
    view_records("Students")
    menu()

if __name__ == "__main__":
    main()