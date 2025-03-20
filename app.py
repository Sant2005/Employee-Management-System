from flask import Flask, render_template, request, redirect, url_for
from employee_management_system.services import (
    employee_service,
    department_service,
    role_service,
    project_service,
    attendance_service
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Add Employee
@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        # Gather employee data from form
        name = request.form['name']
        employee_type = request.form['type']
        salary = request.form['salary']
        hours_per_week = request.form['hours_per_week']
        department_id = request.form['department_id']
        role_id = request.form['role_id']
        project_id = request.form['project_id']

        # Add employee using service layer
        employee_service.add_employee(employee_type,name, salary, hours_per_week, department_id, role_id, project_id)
        return redirect(url_for('index'))
    
    return render_template('add_employee.html')

# View All Employees with Joined Data
@app.route('/view_employees')
def view_employees():
    employees = employee_service.get_all_employees_with_details()
    return render_template('view_employees.html', employees=employees)

# Add Department
@app.route('/add_department', methods=['GET', 'POST'])
def add_department():
    if request.method == 'POST':
        name = request.form['name']
        department_service.add_department(name)
        return redirect(url_for('index'))
    
    return render_template('add_department.html')

# View Departments
@app.route('/view_departments')
def view_departments():
    departments = department_service.get_all_departments()
    print(departments)
    if (departments):
        return render_template('view_department.html', departments=departments)

# Add Role
@app.route('/add_role', methods=['GET', 'POST'])
def add_role():
    if request.method == 'POST':
        title = request.form['title']
        role_service.add_role(title)
        return redirect(url_for('index'))
    
    return render_template('add_role.html')

# View Roles
@app.route('/view_roles')
def view_roles():
    roles = role_service.get_all_roles()
    return render_template('view_role.html', roles=roles)

# Add Project
@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        project_service.add_project(name, description)
        return redirect(url_for('index'))
    
    return render_template('add_project.html')

# View Projects
@app.route('/view_projects')
def view_projects():
    projects = project_service.get_all_projects()
    return render_template('view_project.html', projects=projects)

# Add Attendance
@app.route('/add_attendance', methods=['GET', 'POST'])
def add_attendance():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        date = request.form['date']
        status = request.form['status']
        attendance_service.add_attendance(employee_id, date, status)
        return redirect(url_for('index'))
    
    return render_template('add_attendance.html')

# View Attendance
@app.route('/view_attendance')
def view_attendance():
    attendance_records = attendance_service.get_all_attendance()
    return render_template('view_attendance.html', attendance=attendance_records)

if __name__ == '__main__':
    app.run(debug=True)
