import sqlite3
from config import DATABASE_PATH

class AttendanceDAO:
    @staticmethod
    def add_attendance(attendance):
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO attendance (employee_id, date, status) VALUES (?, ?, ?)", 
                       (attendance.employee_id, attendance.date, attendance.status))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all_attendance():
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM attendance")
        attendance_records = cursor.fetchall()
        connection.close()
        return attendance_records
