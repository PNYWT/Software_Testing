from customer import Customer
from customer_file_data_service import CustomerFileDataService

class Bank:
    def __init__(self, name, data_service = CustomerFileDataService()):
        self.bank_name = name
        self.customers = {}
        self.data_service = data_service
    
    def add_all_customers(self):
        customers = self.data_service.get_all_data()
        for customer in customers:
            self.add_customer(customer)
    
    def add_customer(self, customer):
        self.customers[customer.id] = customer
        
    def find_customer_by_id(self, cust_id):
        if cust_id in self.customers:
            return self.customers[cust_id]
        return None
    
    def validate_customer(self, cust_id, pin):
        customer = self.find_customer_by_id(cust_id)
        if customer != None and customer.match(pin):
            return True
        return False

