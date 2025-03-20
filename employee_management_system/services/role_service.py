from dao.role_dao import RoleDAO
from models.role import Role


def add_role(title):
    role = Role(title)
    RoleDAO.add_role(role)

def get_all_roles():
    return RoleDAO.get_all_roles()
