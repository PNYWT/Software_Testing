import unittest
from bankAccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(1000)

    def test_withdraw_valid(self): #normal case, No Error
        self.account.withdraw(200)
        self.assertEqual(800, self.account.balance)

    def test_withdraw_too_much_amount(self):
        with self.assertRaises(AttributeError): # tell class throw AttributeError
            self.account.withdraw(1500)
        self.assertEqual(1000, self.account.balance) #check balance is 1000

    def test_withdraw_invalid_amount(self):
        with self.assertRaises(ValueError) as err: # tell class throw ValueError
            self.account.withdraw(-50)
        self.assertEqual("Amount must be positive", str(err.exception))
        self.assertEqual(1000, self.account.balance) #check balance is 1000

if __name__ == "__main__":
    unittest.main()