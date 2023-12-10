import unittest
from calculator import Calculator

class TestAddCalculator(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(10,50)
        print("result", result)
        self.assertEqual(60, result)

    def test_add_negative(self):
        calculator = Calculator()
        result = calculator.add(-2, -8)
        print("result", result)
        self.assertEqual(-10, result)

if __name__ == "__main__":
    unittest.main()