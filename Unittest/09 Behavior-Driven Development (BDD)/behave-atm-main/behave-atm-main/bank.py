class BankAccount:

   def __init__(self, balance = 0):
      self.balance = balance
 
   def deposit(self, amount):
      self.balance = self.balance + amount

   def withdraw(self, amount):
      self.balance = self.balance - amount

class Customer:

   def __init__(self, id, pin, balance = 0):
      self.id = id
      self.pin = pin
      self.account = BankAccount(balance)

   def match(self, pin):
      return self.pin == pin

class Bank:

   def __init__(self, name):
      self.name = name
      self.customers = dict()

   def open_account(self, customer):
      self.customers[customer.id] = customer

   def get_customer(self, id):
      return self.customers[id]

   def match_customer(self, id, pin):
      customer = self.customers[id]
      if customer != None and customer.match(pin):
         return customer
      return None

   def transfer(self, giver_id, receiver_id, amount):
      self.customers[giver_id].account.withdraw(amount)
      self.customers[receiver_id].account.deposit(amount)