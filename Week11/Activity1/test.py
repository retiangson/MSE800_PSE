import unittest
from project import multiply, Multiplication


class TestMultiplyFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply(5, 3), 15)

    def test_with_zero(self):
        self.assertEqual(multiply(7, 0), 0)


class TestMultiplicationClass(unittest.TestCase):

    def setUp(self):
        self.calc = Multiplication()

    def test_multiply_method(self):
        result = self.calc.multiply(4, 2)
        self.assertEqual(result, 8)

    def test_inheritance_description(self):
        desc = self.calc.describe()
        self.assertIn("mathematical operation", desc)


if __name__ == '__main__':
    unittest.main()
