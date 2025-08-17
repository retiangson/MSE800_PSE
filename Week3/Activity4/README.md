Week 3 - Activity 4: design a database for your college

1.Project scope (short paragraph)

This database powers a small retail store's digital backbone, streamlining operations from inventory tracking to customer orders. It manages four core entities: products, customers, orders, and order items. The system ensures accurate stock levels, records customer details, and tracks each order's lifecycle—from placement to fulfillment. By linking products to orders and customers, it enables efficient sales reporting, customer service, and inventory control.

2.Entities and EER diagram : 



3.Table design

### 🧾 **Table: `products`**
| Column Name      | Data Type | Constraints                  | Description                        |
|------------------|-----------|------------------------------|------------------------------------|
| `product_id`     | INTEGER   | PRIMARY KEY AUTOINCREMENT    | Unique ID for each product         |
| `name`           | TEXT      | NOT NULL                     | Product name                       |
| `description`    | TEXT      |                              | Optional product description       |
| `price`          | REAL      | NOT NULL                     | Price per unit                     |
| `stock_quantity` | INTEGER   | NOT NULL                     | Available stock count              |

---

### 👤 **Table: `customers`**
| Column Name   | Data Type | Constraints               | Description                      |
|---------------|-----------|---------------------------|----------------------------------|
| `customer_id` | INTEGER   | PRIMARY KEY AUTOINCREMENT | Unique ID for each customer      |
| `first_name`  | TEXT      | NOT NULL                  | Customer's first name            |
| `last_name`   | TEXT      | NOT NULL                  | Customer's last name             |
| `email`       | TEXT      | UNIQUE                    | Customer's email address         |
| `phone`       | TEXT      |                           | Optional phone number            |
| `address`     | TEXT      |                           | Optional physical address        |

---

### 📦 **Table: `orders`**
| Column Name   | Data Type | Constraints               | Description                          |
|---------------|-----------|---------------------------|--------------------------------------|
| `order_id`    | INTEGER   | PRIMARY KEY AUTOINCREMENT | Unique ID for each order             |
| `customer_id` | INTEGER   | NOT NULL, FOREIGN KEY     | Links to `customers(customer_id)`    |
| `order_date`  | DATETIME  | DEFAULT CURRENT_TIMESTAMP | Timestamp of order creation          |
| `status`      | TEXT      | DEFAULT 'Pending'         | Order status (e.g., Pending, Shipped)|

---

### 🧮 **Table: `order_items`**
| Column Name     | Data Type | Constraints               | Description                          |
|------------------|-----------|---------------------------|--------------------------------------|
| `order_item_id`  | INTEGER   | PRIMARY KEY AUTOINCREMENT | Unique ID for each item in an order  |
| `order_id`       | INTEGER   | NOT NULL, FOREIGN KEY     | Links to `orders(order_id)`          |
| `product_id`     | INTEGER   | NOT NULL, FOREIGN KEY     | Links to `products(product_id)`      |
| `quantity`       | INTEGER   | NOT NULL                  | Number of units ordered              |
| `price`          | REAL      | NOT NULL                  | Price per unit at time of order      |
