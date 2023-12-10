import unittest

class DeltaTest(unittest.TestCase):
    def test_delta_fail(self):
        self.assertAlmostEqual(5.00, 4.99, delta=0.00001)

    def test_delta_pass(self):
        self.assertAlmostEqual(5.00, 4.99, delta = 0.1)

if __name__ == "__main__":
    unittest.main()