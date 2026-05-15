from hr import SalaryPolicy, CommissionPolicy, HourlyPolicy
from productivity import ManagerRole, SecretaryRole, SalesRole, FactoryRole

# from abc import ABC, abstractmethod

# class Employee(ABC):
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # @abstractmethod
    # def calculate_payroll(self):
    #     pass

class Manager(Employee, SalaryPolicy, ManagerRole):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        SalaryPolicy.__init__(self, weekly_salary)

class Secretary(Employee, SalaryPolicy, SecretaryRole):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        SalaryPolicy.__init__(self, weekly_salary)

class FactoryWorker(Employee, HourlyPolicy, FactoryRole):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        HourlyPolicy.__init__(self, hours_worked, hourly_rate)

class SalesPerson(Employee, CommissionPolicy, SalesRole):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name)
        CommissionPolicy.__init__(self, weekly_salary, commission)

class TemporarySecretary(Employee, HourlyPolicy, SecretaryRole):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        HourlyPolicy.__init__(self, hours_worked, hourly_rate)

class FactorySales(Employee, CommissionPolicy, FactoryRole):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name)
        CommissionPolicy.__init__(self, weekly_salary, commission)



















