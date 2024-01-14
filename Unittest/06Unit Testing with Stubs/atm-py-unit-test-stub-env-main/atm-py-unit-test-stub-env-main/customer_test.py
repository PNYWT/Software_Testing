import unittest
from customer import Customer

class CustomerTest(unittest.TestCase):
    def setUp(self):
       self.customer = Customer(1, 123, "Kwan")

    def test_get_id(self):
        self.assertEqual(1, self.customer.id)

    def test_get_name(self):
        self.assertEqual("Kwan", self.customer.name)

    def test_set_name(self):
        self.customer.name = "Noon"
        self.assertEqual("Noon", self.customer.name)

    def test_pin_match(self):
        self.assertTrue(self.customer.match(123))    

    def test_pin_not_match(self):
        self.assertFalse(self.customer.match(999))