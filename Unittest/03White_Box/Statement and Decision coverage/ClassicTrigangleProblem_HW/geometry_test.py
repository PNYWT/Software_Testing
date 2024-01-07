# import unittest
# from geometry import get_triangle_type

# class TestGeometry(unittest.TestCase):
#     def test_invalid_triangle(self):
#         self.assertEqual("Invalid", get_triangle_type(-1,3,3))
#         self.assertEqual("Invalid", get_triangle_type(1,2,4))
#         self.assertEqual("Invalid", get_triangle_type(1,1,3))

#     def test_Equilateral(self):
#         self.assertEqual("Equilateral", get_triangle_type(3,3,3))

#     def test_Isosceles(self):
#         self.assertEqual("Isosceles", get_triangle_type(5,5,3))
#         self.assertEqual("Isosceles", get_triangle_type(3,5,5))
#         self.assertEqual("Isosceles", get_triangle_type(3,5,3))

#     def test_Scalene(self):
#         self.assertEqual("Scalene", get_triangle_type(3,4,7))
#         self.assertEqual("Scalene", get_triangle_type(5,6,7))
