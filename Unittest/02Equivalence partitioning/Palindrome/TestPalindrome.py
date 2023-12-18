import unittest
from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):

    def test_not_palindrome(self):
        actual = Palindrome.is_palindrome("cat")
        self.assertFalse(actual)

    def test_palindrome_true_empty(self):
        self.assertTrue(Palindrome.is_palindrome(""))

    def test_palindrome_true_even(self):
        self.assertTrue(Palindrome.is_palindrome("noon"))
        self.assertTrue(Palindrome.is_palindrome("redder"))

    def test_palindrome_true_odd(self):
        self.assertTrue(Palindrome.is_palindrome("racecar"))
        self.assertTrue(Palindrome.is_palindrome("civic"))

if __name__ == "__main__":
    unittest.main()