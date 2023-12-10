import unittest
from bankAcoount import BankAccount

class bankAccountTest(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount(100)
        account.deposit(50)
        self.assertEqual(150, account.balance)

if __name__ == "__main__":
    unittest.main()