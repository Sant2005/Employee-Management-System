import sqlite3
from config import DATABASE_PATH

def initialize_db():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        type TEXT,
                        salary REAL,
                        hours_per_week INTEGER,
                        department_id INTEGER,
                        role_id INTEGER,
                        project_id INTEGER
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS roles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS projects (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        description TEXT
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        employee_id INTEGER,
                        date TEXT,
                        status TEXT,
                        FOREIGN KEY (employee_id) REFERENCES employees(id)
                    )''')
    
    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_db()
