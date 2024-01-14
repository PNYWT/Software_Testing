import unittest
from findFirst import FindFirst

class testFindFrist(unittest.TestCase):

    def setUp(self) -> None:
        self.ff = FindFirst()

    def test_LoopCoverage(self):
        self.assertEqual(-1, self.ff.find_first([],2))
        self.assertEqual(1, self.ff.find_first([0,1,2],1))
        self.assertEqual(2, self.ff.find_first([0,1,2],2))

    def test_EdgePairCoverage(self):
        self.assertEqual(-1, self.ff.find_first([],1))
        self.assertEqual(1, self.ff.find_first([0,1,2],1))
        self.assertEqual(2, self.ff.find_first([0,1,2],2))

    def test_McCabe(self):
        self.assertEqual(-1, self.ff.find_first([],2))
        self.assertEqual(-1, self.ff.find_first([],2))
        self.assertEqual(2, self.ff.find_first([0,1,2],2))

if __name__ == "__main__":
    unittest.main()