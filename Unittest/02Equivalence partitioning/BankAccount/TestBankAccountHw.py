import unittest
from bankAccount_Hw import BankAccount_Hw

class TestBankAccountHw(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount_Hw(1000)

    def test_withdraw_Balance_lessthan_amount_EP(self):
        with self.assertRaises(AttributeError):
            self.account.withdraw(1100)
        self.assertEqual(1000, self.account.balance)

    def test_withdraw_amount_greaterthan_balance_EP(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-99)
        self.assertEqual(1000, self.account.balance)

    def test_withdraw_balance_greaterthanorequalto_amount_EP(self):
        self.account.withdraw(200)
        self.assertEqual(800, self.account.balance)

    def test_withdraw_Balance_lessthan_amount_BVA(self):
        with self.assertRaises(AttributeError):
            self.account.withdraw(1001)
        self.assertEqual(1000, self.account.balance)

    def test_withdraw_amount_greaterthan_balance_BVA(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-1)
        self.assertEqual(1000, self.account.balance)

    def test_withdraw_balance_greaterthanorequalto_amount_BVA(self):
        self.account.withdraw(999)
        self.assertEqual(1, self.account.balance)

if __name__ == "__main__":
    unittest.main()