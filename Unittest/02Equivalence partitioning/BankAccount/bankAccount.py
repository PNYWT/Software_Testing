# import tkinter
# from tkinter import messagebox
class BankAccount:

    def __init__(self,balance) -> None:
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            #throw error Bal < amount need withdraw, func is return not do action
            # messagebox.showinfo("AttributeError", "Balance must be more than amount")
            raise AttributeError("Balance must be more than amount") 
        if amount <= 0:
            #throw error amount <= 0, func is return not do action
            raise ValueError("Amount must be positive") 
        self.balance = self.balance - amount 
        #no error, func do action

if __name__ == "__main__":
    abcAccount = BankAccount(1000)
    abcAccount.withdraw(1300)
    print(abcAccount.balance)