
class Employee:

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def raise_salary(self, rate):
        self.salary = self.salary + (self.salary * rate)
    
class HumanResourceService:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def raise_salary_all(self, rate):
        for employee in self.employees:
            employee.raise_salary(rate)
