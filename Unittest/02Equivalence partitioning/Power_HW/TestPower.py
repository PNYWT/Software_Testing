import unittest
from power import Power

class TestPower(unittest.TestCase):

    def setUp(self):
        print("in setup method")
        self.pow = Power()

    def test_Exp_lessthanZero_ResultMinusone(self):
        result = self.pow.power(2,-1)
        self.assertEqual(-1,result)

    def test_Exp_EqualZero_ResultOne(self):
        result = self.pow.power(2,0)
        self.assertEqual(1,result)

    def test_Exp_MorethanZero_ResultMinusNine(self):
        result = self.pow.power(-3,2)
        self.assertEqual(-9,result) #AssertionError: -9 != 9

    def test_Exp_NotNumber_ResultMinusone(self):
        result = self.pow.power(2,"A") #TypeError: '<' not supported between instances of 'str' and 'int'
        self.assertEqual(-1,result)

    def test_Base_NotNumber_ResultMinusone(self):
        result = self.pow.power("A", 2) #TypeError: '<' not supported between instances of 'str' and 'int'
        self.assertEqual(-1,result)

if __name__ == "__main__":
    unittest.main()