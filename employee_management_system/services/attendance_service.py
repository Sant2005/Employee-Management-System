from dao.attendance_dao import AttendanceDAO
from models.attendance import Attendance


def add_attendance(employee_id, date, status):
    attendance = Attendance(employee_id, date, status)
    AttendanceDAO.add_attendance(attendance)


def get_all_attendance():
    return AttendanceDAO.get_all_attendance()
