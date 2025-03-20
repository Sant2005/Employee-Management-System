import sqlite3
from config import DATABASE_PATH

class ProjectDAO:
    @staticmethod
    def add_project(project):
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO projects (name, description) VALUES (?, ?)", (project.name, project.description))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all_projects():
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()
        connection.close()
        return projects
