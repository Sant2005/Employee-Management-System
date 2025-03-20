from models.employee import FullTimeEmployee, PartTimeEmployee

class EmployeeFactory:
    @staticmethod
    def create_employee(employee_type, name, salary, hours_per_week, department_id, role_id, project_id):
        if employee_type == "FullTime":
            return FullTimeEmployee(name, salary, hours_per_week, department_id, role_id, project_id)
        elif employee_type == "PartTime":
            return PartTimeEmployee(name, salary, hours_per_week, department_id, role_id, project_id)
        else:
            raise ValueError("Invalid employee type")
