from data_service import DataService
from customer import Customer

class CustomerFileDataService(DataService):
    def get_all_data(self):
        customers = []
        file = open('customers.csv', 'r')
        lines = file.readlines()
 
        for line in lines:
            row = line.strip().split(",")
            customer = Customer(int(row[0]), int(row[1]), row[2])
            customers.append(customer)
        return customers
        