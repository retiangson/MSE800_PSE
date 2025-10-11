"""
Week 11 – Activity 1: Math Operations with Inheritance, Doctest, and Unittest
Author: Ronald Ephraim C. Tiangson
"""

# ==============================
# Base class and Derived Classes
# ==============================

class Operation:
    """Base class for mathematical operations."""
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is a mathematical operation: {self.name}"


# Derived class 1
class Addition(Operation):
    """
    Returns the sum of two numbers.

    Example:
    >>> Addition().add(5, 3)
    8
    >>> Addition().add(-2, 5)
    3
    """
    def __init__(self):
        super().__init__("Addition")

    def add(self, x, y):
        return x + y


def subtract(x: float, y: float) -> float:
    """
    Returns the difference between two numbers.

    Example:
    >>> subtract(10, 4)
    6
    >>> subtract(2, 5)
    -3
    """
    return x - y


# Derived class 2
class Multiplication(Operation):
    """
    Returns the product of two numbers.

    Example:
    >>> Multiplication().multiply(4, 3)
    12
    >>> Multiplication().multiply(-2, 5)
    -10
    """
    def __init__(self):
        super().__init__("Multiplication")

    def multiply(self, x, y):
        return x * y


def divide(x: float, y: float) -> float:
    """
    Returns the division result of two numbers.

    Example:
    >>> divide(10, 2)
    5.0
    >>> divide(5, 2)
    2.5
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


# Derived class 3 (inherits from Multiplication)
class AdvancedMath(Multiplication):
    """Advanced math operations, extending Multiplication."""
    def __init__(self):
        super().__init__()

    def power(self, x, y):
        """Returns x raised to the power of y."""
        return x ** y


# Standalone function for testing
def multiply(x, y):
    """
    Multiply two numbers and return the product.

    Example:
    >>> multiply(4, 3)
    12
    >>> multiply(0, 10)
    0
    """
    return x * y


# ==============================
# Run Doctests
# ==============================
if __name__ == "__main__":
    import doctest
    print("Running doctests...")
    doctest.testmod(verbose=True)
