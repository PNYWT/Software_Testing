Feature: deposit
    As a customer
    I want to deposit from my account using ATM

Background:
    Given an ATM exists
    And a customer with id 1 and pin 111 with balance 150.00 exists
    When I login to ATM with id 1 and pin 111

Scenario: Deposit an amount
    When I deposit 1000.00 from ATM
    Then my account balance is 1150.00