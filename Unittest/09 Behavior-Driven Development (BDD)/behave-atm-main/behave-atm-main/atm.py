from bank import *

class ATM:

	def __init__(self, bank):
		self.bank = bank

	def validate_customer(self, id, pin):
		self.current_customer = self.bank.match_customer(id, pin)
		if (self.current_customer != None):
			self.current_account = self.current_customer.account
			return True
		return False

	def withdraw(self, value):
		if self.current_account != None:
			self.current_account.withdraw(value)

	def deposit(self, value):
		if self.current_account != None:
			self.current_account.deposit(value)

	def get_balance(self):
		if self.current_account != None:
			return self.current_account.balance
		return -1

	def transfer(self, receiver_id, amount):
		if self.current_account != None:
			self.bank.transfer(self.current_customer.id, receiver_id, amount)

	def reset(self):
		self.currentCustomer = None
		self.currentAccount = None
