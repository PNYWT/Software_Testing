import unittest
from trigangle import Trigangle
#i.	Condition coverage Cover 100% 
class TestTrigangle(unittest.TestCase):

    def setUp(self) -> None:
        self.trigangle = Trigangle()

    def test_abc_lessthanZeroABC(self):
        result = self.trigangle.get_triangle_type(0,0,0)
        self.assertEqual("Invalid", result) #Check

    def test_abc_lessthanZeroA(self):
        result = self.trigangle.get_triangle_type(-1,0,0)
        self.assertEqual("Invalid", result) #Check

    def test_abc_lessthanZeroB(self):
        result = self.trigangle.get_triangle_type(0,-1,0)
        self.assertEqual("Invalid", result) #Check
    
    def test_abc_lessthanZeroC(self):
        result = self.trigangle.get_triangle_type(0,0,-1)
        self.assertEqual("Invalid", result) #Check

    def test_typeZero_is_InvalidCaseA(self):
        result = self.trigangle.get_triangle_type(1,2,4)
        self.assertEqual("Invalid", result)#Check

    def test_typeZero_is_InvalidCaseB(self):
        result = self.trigangle.get_triangle_type(1,4,2)
        self.assertEqual("Invalid", result)#Check

    def test_typeZero_is_InvalidCaseC(self):
        result = self.trigangle.get_triangle_type(4,1,2)
        self.assertEqual("Invalid", result)#Check

    def test_typeZero_is_ScaleneA(self):
        result = self.trigangle.get_triangle_type(1,2,3)
        self.assertEqual("Scalene", result) #Check

    def test_typeZero_is_ScaleneB(self):
        result = self.trigangle.get_triangle_type(1,3,2)
        self.assertEqual("Scalene", result) #Check

    def test_typeZero_is_ScaleneC(self):
        result = self.trigangle.get_triangle_type(3,1,2)
        self.assertEqual("Scalene", result) #Check

    def test_typeLessthanThree_is_Equilateral(self):
        result = self.trigangle.get_triangle_type(3,3,3)
        self.assertEqual("Equilateral", result)#Check

    def test_typeEqualOne_is_Isosceles(self):
        result = self.trigangle.get_triangle_type(3,3,4)
        self.assertEqual("Isosceles", result)#Check

    def test_typeEqualTwo_is_Isosceles(self):
        result = self.trigangle.get_triangle_type(3,4,3)
        self.assertEqual("Isosceles", result)#Check

    def test_typeEqualThree_is_Isosceles(self):
        result = self.trigangle.get_triangle_type(4,3,3)
        self.assertEqual("Isosceles", result)#Check

    def test_InvalidLastReturn(self):
        result = self.trigangle.get_triangle_type(1,1,3)
        self.assertEqual("Invalid", result)#Check

# if __name__ == "__main__":
#     unittest.main()