
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    orders = relationship("Order", back_populates="product")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product", back_populates="orders")

    def __repr__(self):
        return f"<Order(id={self.id}, customer={self.customer.name}, product={self.product.name})>"