from behave import *
from bank import Bank, Customer, BankAccount
from atm import ATM

@given('an ATM exists')
def atm_exists(context):
    context.bank = Bank("KU Bank")
    context.atm = ATM(context.bank)

@given('a customer with id {id:d} and pin {pin:d} exists')
def a_customer_with_id_and_pin_exists(context, id, pin):
    context.bank.open_account(Customer(id, pin))

@given('a customer with id {id:d} and pin {pin:d} with balance {balance:f} exists')
def a_customer_with_id_and_pin_with_balance_exists(context, id, pin, balance):
    context.bank.open_account(Customer(id, pin, balance))

@when('I login to ATM with id {id:d} and pin {pin:d}')
def i_login_to_ATM_with_id_and_pin(context, id, pin):
    context.valid_login = context.atm.validate_customer(id, pin);

@then('I can login')
def i_can_login(context):
    assert context.valid_login

@then('I cannot login')
def i_cannot_login(context):
    assert not context.valid_login

@when('I withdraw {amount:f} from ATM')
def i_withdraw_from_atm(context, amount):
    context.atm.withdraw(amount)

@then('my account balance is {balance:f}')
def my_account_balance_is(context, balance):
    assert balance == context.atm.get_balance()

@when('I transfer {amount:f} to customer id {id:d}')
def i_transfer_to_customer_id(context, amount, id):
    context.atm.transfer(id, amount)

@then('customer id {id:d} account balance is {balance:f}')
def customer_id_account_balance_is(context, id, balance):
    assert balance == context.bank.get_customer(id).account.balance

@when('I deposit {amount:f} from ATM')
def i_deposit_from_atm(context, amount):
    context.atm.deposit(amount)

