import unittest
from trigangle import Trigangle
#i.	Condition coverage Cover 100% 
class TestGeometry(unittest.TestCase):

    def setUp(self) -> None:
        self.trigangle = Trigangle()

    def test_invalid_triangle(self):
        self.assertEqual("Invalid", self.trigangle.get_triangle_type(-1,3,3))
        self.assertEqual("Invalid", self.trigangle.get_triangle_type(1,2,4))
        self.assertEqual("Invalid", self.trigangle.get_triangle_type(1,1,3))

    def test_Equilateral(self):
        self.assertEqual("Equilateral", self.trigangle.get_triangle_type(3,3,3))

    def test_Isosceles(self):
        self.assertEqual("Isosceles", self.trigangle.get_triangle_type(5,5,3))
        self.assertEqual("Isosceles", self.trigangle.get_triangle_type(3,5,5))
        self.assertEqual("Isosceles", self.trigangle.get_triangle_type(3,5,3))

    def test_Scalene(self):
        self.assertEqual("Scalene", self.trigangle.get_triangle_type(3,4,7))
        self.assertEqual("Scalene", self.trigangle.get_triangle_type(5,6,7))

if __name__ == "__main__":
    unittest.main()
