from dao.employee_dao import EmployeeDAO
from factories.employee_factory import EmployeeFactory


def add_employee(employee_type, name, salary, hours_per_week, department_id, role_id, project_id):
    employee = EmployeeFactory.create_employee(employee_type, name, salary, hours_per_week, department_id, role_id, project_id)
    EmployeeDAO.add_employee(employee)


def get_all_employees_with_details():
    return EmployeeDAO.get_all_employees_with_details()
