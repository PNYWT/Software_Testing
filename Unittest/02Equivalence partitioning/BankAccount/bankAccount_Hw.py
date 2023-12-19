class BankAccount_Hw:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise AttributeError('Balance must be more than amount')
        if amount <= 0:
            raise ValueError('Amount must be positive')
        self.balance = self.balance - amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        self.balance = self.balance + amount