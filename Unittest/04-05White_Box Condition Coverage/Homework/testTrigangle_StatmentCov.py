import unittest
from trigangle import Trigangle
#i.	Condition coverage Cover 100% 
class testTrigangle_StatmentCov(unittest.TestCase):

    def setUp(self) -> None:
        self.trigangle = Trigangle()

    def test_invalid_triangle(self):
        self.assertEqual("Invalid", self.trigangle.get_triangle_type(-1,3,3)) #check
        self.assertEqual("Invalid", self.trigangle.get_triangle_type(1,2,4)) #check
        self.assertEqual("Invalid", self.trigangle.get_triangle_type(1,1,3)) #check

    def test_Equilateral(self):
        self.assertEqual("Equilateral", self.trigangle.get_triangle_type(3,3,3)) #check

    def test_Isosceles(self):
        self.assertEqual("Isosceles", self.trigangle.get_triangle_type(5,5,3)) #check
        self.assertEqual("Isosceles", self.trigangle.get_triangle_type(3,5,5)) #check
        self.assertEqual("Isosceles", self.trigangle.get_triangle_type(3,5,3)) #check

    def test_Scalene(self):
        self.assertEqual("Scalene", self.trigangle.get_triangle_type(3,4,7)) #check
        self.assertEqual("Scalene", self.trigangle.get_triangle_type(5,6,7)) #check