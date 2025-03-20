import sqlite3
from config import DATABASE_PATH

class DepartmentDAO:
    @staticmethod
    def add_department(department):
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO departments (name) VALUES (?)", (department.name,))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all_departments():
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM departments")
        departments = cursor.fetchall()
        connection.close()
        return departments
