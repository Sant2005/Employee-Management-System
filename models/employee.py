from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary, hours_per_week, department_id, role_id, project_id):
        self.name = name
        self.salary = salary
        self.hours_per_week = hours_per_week
        self.department_id = department_id
        self.role_id = role_id
        self.project_id = project_id

    @abstractmethod
    def get_type(self):
        pass

class FullTimeEmployee(Employee):
    def get_type(self):
        return "FullTime"

class PartTimeEmployee(Employee):
    def get_type(self):
        return "PartTime"


