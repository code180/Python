import requests
import pytest

# Позитивные
Base_url = "https://yougile.com/api-v2/"
token = ""


def test_create_project():
    project = {
        "title": "Postman",
        "users": {
            "036bade1-6003-4588-a1e5-005361722e1d": "admin"
        }
    }

    my_headers = {
        "Authorization": f"Bearer {token}",  # Добавлен Bearer токен
        "Content-Type": "application/json"
    }

    YouGile_project = requests.post(
        Base_url + "projects", json=project, headers=my_headers)

    assert YouGile_project.status_code == 201
    # Сохранение полученного ID проекта
    project_id = YouGile_project.json()["id"]


def test_get_projects():
    my_headers = {
        "Authorization": f"Bearer {token}",  # Используем ваш токен
        "Content-Type": "application/json"
    }

    response = requests.get(f"{Base_url}projects", headers=my_headers)

    assert response.status_code == 200


def test_update_project():
    payload = {
        "deleted": True,
        "title": "Updated Project2",
        "users": {
            "036bade1-6003-4588-a1e5-005361722e1d": "admin"
        }
    }

    my_headers = {
        "Authorization": f"Bearer {token}",  # Добавлен Bearer токен
        "Content-Type": "application/json"
    }

    project_id = "25fbba8c-0a17-4a0e-8a8e-f5424bc79b13"

    response = requests.put(
        f"{Base_url}projects/{project_id}", json=payload, headers=my_headers)

    assert response.status_code == 200


def test_get_project_by_id():
    my_headers = {
        "Authorization": f"Bearer {token}",  # Добавлен Bearer токен
        "Content-Type": "application/json"
    }

    response = requests.get(f"{Base_url}projects")
    project_id = response.json()[0]["id"]
    response = requests.get(
        f"{Base_url}projects/{project_id}", headers=my_headers)

    assert response.status_code == 200
    assert response.json()["id"] == project_id


# Негативные

def test_create_project_without_title():
    project = {
        "users": {
            "036bade1-6003-4588-a1e5-005361722e1d": "admin"
        }
    }

    my_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    YouGile_project = requests.post(
        Base_url + "projects", json=project, headers=my_headers)

    assert YouGile_project.status_code == 401


def test_get_projects_without_authorization():
    response = requests.get(f"{Base_url}projects")
    assert response.status_code == 401


def test_update_project_without_users():
    payload = {
        "deleted": True,
        "title": "Updated Project2"
    }

    my_headers = {
        "Authorization": f"Bearer {token}",  
        "Content-Type": "application/json"
    }

    project_id = "25fbba8c-0a17-4a0e-8a8e-f5424bc79b13"

    response = requests.put(
        f"{Base_url}projects/{project_id}", json=payload, headers=my_headers)

    assert response.status_code == 401

def test_get_project_without_id():
    my_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(f"{Base_url}projects")
    response = requests.get(
        f"{Base_url}projects", headers=my_headers)

    assert response.status_code == 401
