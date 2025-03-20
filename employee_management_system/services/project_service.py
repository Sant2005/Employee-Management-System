from dao.project_dao import ProjectDAO
from models.project import Project


def add_project(name, description):
    project = Project(name, description)
    ProjectDAO.add_project(project)

def get_all_projects():
    return ProjectDAO.get_all_projects()
