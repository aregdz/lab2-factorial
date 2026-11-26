import unittest
from main import factorial


class TestFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_five(self):
        self.assertEqual(factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
