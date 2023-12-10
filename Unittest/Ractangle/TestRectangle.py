import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rec = Rectangle(5, 8)
        area = rec.get_area()
        self.assertEqual(40, area)

if __name__ == "__main__":
    unittest.main()
