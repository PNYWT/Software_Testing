import unittest
from rectangle import Rectangle

class TestRectangleWithSetup(unittest.TestCase):

    def setUp(self):
        print("in setup method")
        self.rec = Rectangle(5, 8)

    def tearDown(self) -> None:
        print("in tear down method")
        return super().tearDown()

    def test_area(self):
        print("in test_area")
        area = self.rec.get_area()
        self.assertEqual(40, area)

    def test_perimeter(self):
        print("in test_perimeter")
        perimeter = self.rec.get_perimeter()
        self.assertEqual(800, perimeter)

if __name__ == "__main__":
    unittest.main()
