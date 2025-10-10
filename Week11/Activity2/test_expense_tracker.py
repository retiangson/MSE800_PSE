import unittest
from expense_tracker import ExpenseTracker


class TestExpenseTracker(unittest.TestCase):
    """Unit tests for ExpenseTracker."""

    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense_increases_list_size(self):
        self.tracker.add_expense("Lunch", 10.0)
        self.assertEqual(len(self.tracker.expenses), 1)

    def test_calculate_total_returns_correct_sum(self):
        self.tracker.add_expense("Food", 20.0)
        self.tracker.add_expense("Transport", 30.0)
        total = self.tracker.calculate_total()
        self.assertEqual(total, 50.0)

    def test_negative_amount_raises_error(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense("Invalid", -5.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
