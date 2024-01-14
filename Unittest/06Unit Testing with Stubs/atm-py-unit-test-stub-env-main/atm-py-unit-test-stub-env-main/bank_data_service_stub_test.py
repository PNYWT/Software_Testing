import unittest
from customer import Customer
from bank import Bank
from data_service import DataService

class BankDataServiceStubTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank("KU Bank")
        self.bank.data_service = DataServiceStub()
        self.bank.add_all_customers()

    def test_find_customer(self):
        customer = self.bank.find_customer_by_id(1)
        self.assertEqual("Kwan", customer.name)
    
    # . . .

class DataServiceStub(DataService):
    def get_all_data(self):
        customers = []
        customers.append(Customer(1, 123, "Kwan"))
        customers.append(Customer(2, 456, "Noon"))
        return customers
