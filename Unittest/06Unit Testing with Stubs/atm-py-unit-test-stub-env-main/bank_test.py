import unittest
from customer import Customer
from bank import Bank

class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("My Bank")
        self.customer = CustomerStub(1, 123, "Kwan")
        self.bank.add_customer(self.customer)

    def test_find_customer(self):
        found = self.bank.find_customer_by_id(1)
        self.assertIsNotNone(found)
        self.assertIs(self.customer, found)

    def test_validate_customer_valid(self):
        self.customer.hard_code_match = True
        self.assertTrue(self.bank.validate_customer(1,123))

    def test_validate_customer_not_valid(self):
        self.customer.hard_code_match = False
        self.assertFalse(self.bank.validate_customer(1,999))   

## -------- customer stub ---------
class CustomerStub(Customer):

    def __init__(self, id, pin, name):
        super().__init__(id, pin, name)

    # override complex / slow method
    def match(self, pin):
        # hard code
        return self.hard_code_match