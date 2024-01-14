from customer import Customer
from bank import Bank

if __name__ == '__main__':
    ku_bank = Bank("KU Bank")
    ku_bank.add_all_customers()

    print(  ku_bank.validate_customer(1, 1234)  )
    print(  ku_bank.validate_customer(5, 1234)  )

    print(  ku_bank.find_customer_by_id(3).name  )
