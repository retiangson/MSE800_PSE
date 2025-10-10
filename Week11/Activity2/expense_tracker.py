"""
Personal Expense Tracker
Week 11 – Activity 2

A simple OOP-based program that allows adding expenses
and calculating total expenses.
"""

from typing import List


class Expense:
    """Represents a single expense entry."""

    def __init__(self, description: str, amount: float) -> None:
        self.description = description
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.description}: ${self.amount:.2f}"


class ExpenseTracker:
    """Main class to handle expenses."""

    def __init__(self) -> None:
        self.expenses: List[Expense] = []

    def add_expense(self, description: str, amount: float) -> None:
        """Add a new expense to the list."""
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.expenses.append(Expense(description, amount))

    def calculate_total(self) -> float:
        """Calculate and return the total amount of all expenses."""
        return sum(exp.amount for exp in self.expenses)

    def list_expenses(self) -> None:
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            for exp in self.expenses:
                print(exp)


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense("Groceries", 75.50)
    tracker.add_expense("Transport", 25.00)
    tracker.add_expense("Coffee", 4.75)

    print("\n--- Expense List ---")
    tracker.list_expenses()

    print("\nTotal Expenses: $", tracker.calculate_total())
