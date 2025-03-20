import sqlite3
from config import DATABASE_PATH

class RoleDAO:
    @staticmethod
    def add_role(role):
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO roles (title) VALUES (?)", (role.title,))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all_roles():
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roles")
        roles = cursor.fetchall()
        connection.close()
        return roles
