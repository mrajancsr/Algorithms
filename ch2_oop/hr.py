"""Processes company's payroll"""

class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("====================")
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')

class Employee:
    """Base clas for all employees"""
    def __init__(self,id_,name):
        self.id = id_
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id_,name,weekly_salary):
        super().__init__(id_, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
