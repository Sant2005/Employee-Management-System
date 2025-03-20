from dao.department_dao import DepartmentDAO
from models.department import Department


def add_department(name):
    department = Department(name)
    DepartmentDAO.add_department(department)

def get_all_departments():
    return DepartmentDAO.get_all_departments()
