========================================
Store Management CLI Application
Yoobee Colleges – Ronald Ephraim Tiangson – Week 3 Activity 6
========================================

Project Description:
--------------------
This project is a Python-based command-line application for managing a small store’s operations using SQLAlchemy ORM.
It allows you to keep track of customers, products, and orders through a simple interactive menu, making it easier 
to perform basic store management tasks without needing a graphical interface.
Features

Customer Management
--------------------
Add new customers with their details
View all registered customers
Delete customers by ID

Product Management
--------------------
Add new products with price information
View available products in the store
Delete products by ID

Order Management
--------------------
Create new orders linking customers and products
View all existing orders
Delete orders by ID

Key Features:
-------------
1. Add Records
   - Add customers, products, and orders.
2. View Records
   - View stored customers, products, and orders.
3. Delete Records
   - Delete customers, products, and orders by ID.

Technical Details:
------------------
- Language: Python 3
- ORM: SQLAlchemy
- Database: SQLite3 (file-based, store.db)
- Modular Code:
  * config.py    - database configuration
  * database.py  - SQLAlchemy engine and session
  * models.py    - ORM classes for Customers, Products, Orders
  * customers.py - Customer functions
  * products.py  - Product functions
  * orders.py    - Order functions
  * main.py      - Command-line menu

Installation & Usage:
-----------
1. Install dependencies:
   > pip install sqlalchemy

2. Run the program:
   > python main.py

Database Schema:
---------
The database file store.db will be automatically created on first run.
Tables:
customers (id, name, email)
products (id, name, price)
orders (id, customer_id, product_id)

Author:
-------
Ronald Ephraim Tiangson
Yoobee Colleges – Week 3 Activity 6 Submission