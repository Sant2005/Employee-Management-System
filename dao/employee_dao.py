import sqlite3
from config import DATABASE_PATH
from factories.employee_factory import EmployeeFactory

class EmployeeDAO:
    @staticmethod
    def add_employee(employee):
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO employees (name, type, salary, hours_per_week, department_id, role_id, project_id)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                       (employee.name, employee.get_type(), employee.salary, employee.hours_per_week, employee.department_id, employee.role_id, employee.project_id))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all_employees_with_details():
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM EMPLOYEES''')
        employees = cursor.fetchall()
        connection.close()
        return employees
