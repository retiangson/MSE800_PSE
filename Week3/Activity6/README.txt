========================================
Yoobee Colleges - Week 3 Activity 6
Command-Line Application with SQLite3
========================================

Project Description:
--------------------
This project is a Python-based command-line application that demonstrates
basic database operations using SQLite3. It manages Customers, Products,
and Orders through a simple text menu.

Key Features:
-------------
1. Add Records
   - Add customers, products, and orders into the database.
2. View Records
   - View stored customers, products, and orders.
3. Delete Records
   - Delete customers, products, and orders by ID.

Technical Aspects:
------------------
- Language: Python 3
- Database: SQLite3 (file-based, store.db)
- Modular Code:
  * database.py - initializes and connects to DB
  * customers.py - CRUD operations for Customers
  * products.py  - CRUD operations for Products
  * orders.py    - CRUD operations for Orders
  * main.py      - Command-line interface menu

How to Run:
-----------
1. Ensure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run the program:
   > python main.py

Database:
---------
The database file (activity4.db) will be created automatically.
Tables:
- customers(id, name, email)
- products(id, name, price)
- orders(id, customer_id, product_id)

Example Usage:
--------------
1. Add a Customer (choice 1)
   Enter name and email.
2. View Customers (choice 2)
   Shows all stored customers.
3. Add an Order (choice 7)
   Requires valid customer_id and product_id.

Author:
-------
Ronald Ephraim Tiangson - Yoobee Colleges - Week 3 Activity 6 Submission