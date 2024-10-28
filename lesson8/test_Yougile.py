import requests
import pytest

# Позитивные
Base_url = "https://yougile.com/api-v2/"
token = ""


def test_Login():
    User = {
        "login": "sasha1996sorok@mail.ru",
        "password": "Qa!353584584",
        "companyId": "ce4d7199-d191-413e-a32c-b1757196365c",
    }
    YouGile_Login = requests.post(Base_url + "auth/keys", json=User)
    assert YouGile_Login.status_code == 201
    global token
    token = YouGile_Login.json()["key"]


def test_список_Проектов():
    User = {
        "login": "sasha1996sorok@mail.ru",
        "password": "Qa!353584584",
        "companyId": "ce4d7199-d191-413e-a32c-b1757196365c",
    }
    YouGile_Login = requests.post(Base_url + "auth/keys", json=User)
    token = YouGile_Login.json()["key"]

    my_headers = {}
    my_headers["Authorization"] = token
    YouGile_projects = requests.get(f"{Base_url}projects", headers=my_headers)
    assert YouGile_projects.status_code == 200
    assert len(YouGile_projects.json()) > 0


def test_Создание_Проекта():
    project = {
        "title": "python",
        "description": "This is a test project",
        "users": {"036bade1-6003-4588-a1e5-005361722e1d": "admin"}
    }

    my_headers = {}
    my_headers["Authorization"] = token

    YouGile_project = requests.post(
        Base_url + "projects", json=project, headers=my_headers)
    assert YouGile_project.status_code == 201
    assert YouGile_project.json()["name"] == "python"


def test_Получить_Проект_by_id():
    my_headers = {}
    my_headers["Authorization"] = token

    response = requests.get(f"{Base_url}projects")
    project_id = response.json()[0]["id"]
    response = requests.get(
        f"{Base_url}projects/{project_id}", headers=my_headers)
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_update_project():
    payload = {
        "name": "Updated Project",
        "description": "This is an updated project"
    }

    my_headers = {}
    my_headers["Authorization"] = token

    response = requests.post(f"{Base_url}projects")
    project_id = response.json()["id"]
    
    response = requests.put(
        f"{Base_url}projects/{project_id}", json=payload, headers=my_headers)
    
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Project"


# Негативные

def test_create_project_without_required_fields():
    response = requests.post(f"{Base_url}projects")
    assert response.status_code == 401

def test_get_projects():
    response = requests.get(f"{Base_url}projects")
    assert response.status_code == 400

def test_update_project_without_required_fields():
    response = requests.put(f"{Base_url}projects/1")
    assert response.status_code == 400

def test_get_project_by_id():
    response = requests.get(f"{Base_url}projects/1")
    assert response.status_code == 404

