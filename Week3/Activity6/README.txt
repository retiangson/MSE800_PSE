========================================
Yoobee Colleges - Ronald Ephraim Tiangson - Week 3 Activity 6
Command-Line Application with SQLAlchemy ORM
========================================

Project Description:
--------------------
This project is a Python-based command-line application that demonstrates
basic database operations using SQLAlchemy ORM (similar to Entity Framework).
It manages Customers, Products, and Orders through a simple text menu.

Key Features:
-------------
1. Add Records
   - Add customers, products, and orders.
2. View Records
   - View stored customers, products, and orders.
3. Delete Records
   - Delete customers, products, and orders by ID.

Technical Aspects:
------------------
- Language: Python 3
- ORM: SQLAlchemy
- Database: SQLite3 (file-based, activity4.db)
- Modular Code:
  * config.py    - database configuration
  * database.py  - SQLAlchemy engine and session
  * models.py    - ORM classes for Customers, Products, Orders
  * customers.py - Customer functions
  * products.py  - Product functions
  * orders.py    - Order functions
  * main.py      - Command-line menu

How to Run:
-----------
1. Install dependencies:
   > pip install sqlalchemy

2. Run the program:
   > python main.py

Database:
---------
The database file (activity4.db) will be created automatically.

Tables:
- customers(id, name, email)
- products(id, name, price)
- orders(id, customer_id, product_id)

Author:
-------
Ronald Ephraim Tiangson - Yoobee Colleges - Week 3 Activity 6 Submission