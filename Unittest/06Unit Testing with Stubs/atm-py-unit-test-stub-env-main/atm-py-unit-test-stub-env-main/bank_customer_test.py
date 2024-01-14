import unittest
from customer import Customer
from bank import Bank

class BankCustomerTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("My Bank")
        self.customer = Customer(1, 123, "Kwan")
        self.bank.add_customer(self.customer)

    def test_find_customer(self):
        found = self.bank.find_customer_by_id(1)
        self.assertIsNotNone(found)
        self.assertIs(self.customer, found)

    def test_validate_customer_valid(self):
        self.assertTrue(self.bank.validate_customer(1,123))

    def test_validate_customer_not_valid(self):
        self.assertFalse(self.bank.validate_customer(1,999))        