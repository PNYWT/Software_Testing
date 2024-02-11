Feature: transfer
    As a customer
    I want to transfer money from my account to my friend's account

Background:
    Given an ATM exists
    And a customer with id 1 and pin 111 with balance 200.00 exists
    And a customer with id 2 and pin 222 with balance 50.00 exists
    When I login to ATM with id 1 and pin 111

Scenario: Transfer amount less than my balance
    When I transfer 20.00 to customer id 2
    Then my account balance is 180.00
    And customer id 2 account balance is 70.00