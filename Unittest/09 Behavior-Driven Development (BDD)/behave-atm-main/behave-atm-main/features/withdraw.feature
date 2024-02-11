Feature: withdraw
    As a customer
    I want to withdraw from my account using ATM

Background:
    Given an ATM exists
    And a customer with id 1 and pin 111 with balance 200.00 exists
    When I login to ATM with id 1 and pin 111

Scenario: Withdraw an amount
    When I withdraw 50.00 from ATM
    Then my account balance is 150.00
