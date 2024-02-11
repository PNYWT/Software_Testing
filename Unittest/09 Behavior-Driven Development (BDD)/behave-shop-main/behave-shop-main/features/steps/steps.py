from behave import *
from order import Order, OrderItem
from product import Product, ProductCatalog

@given('the store is ready to service customers')
def the_store_is_ready_to_service_customers(context):
    context.catalog = ProductCatalog()
    context.order = Order()

@given('a product {name} with price {price:f} and stock of {stock:d} exists')
def a_product_exists(context, name, price, stock):
    context.catalog.add_product(name, price, stock)

@when('I buy {name} with quantity {quantity:d}')
def i_buy_with_quantity(context, name, quantity):
    product = context.catalog.get_product(name)
    context.order.add_item(product, quantity)

@then('total should be {total:f}')
def total_should_be(context, total):
    assert context.order.get_total() == total

@then('cut stock {name}, Remaining {name} stock of {stock_left:d} exists')
def cut_stock(context, name, stock_left):
    product = context.catalog.get_product(name)
    assert context.catalog.get_productStock(name) == stock_left