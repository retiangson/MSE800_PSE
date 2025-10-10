# Base class
class Operation:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is a mathematical operation: {self.name}"


# Derived class 1
class Addition(Operation):
    def __init__(self):
        super().__init__("Addition")

    def add(self, x, y):
        return x + y


# Derived class 2
class Multiplication(Operation):
    def __init__(self):
        super().__init__("Multiplication")

    def multiply(self, x, y):
        return x * y


# Derived class 3 (inherits from Multiplication)
class AdvancedMath(Multiplication):
    def __init__(self):
        super().__init__()

    def power(self, x, y):
        return x ** y


# Standalone function for testing
def multiply(x, y):
    """Multiply two numbers and return the product."""
    return x * y
