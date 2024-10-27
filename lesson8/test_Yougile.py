from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests

Base_url = 'https://yougile.com/api-v2/'

def test_Login():

    User = {
        'login' : 'sasha1996sorok@mail.ru',
        'password' : 'Qa!353584584',
        'companyId' : 'ce4d7199-d191-413e-a32c-b1757196365c'
        }
    YouGile_Login = requests.post(Base_url + 'auth/keys', json=User)
    assert YouGile_Login.status_code == 201
    global token
    token = YouGile_Login.json()['key']

def test_Создание_Проекта():
    project = {
        'title': 'python',
        'users': {
            '036bade1-6003-4588-a1e5-005361722e1d': 'admin'}
            }

    my_headers = {}
    my_headers['Authorization'] = token

    YouGile_project = requests.post(
        Base_url+'company', json=project, headers=my_headers)
    assert YouGile_project.status_code == 201 or 200


def test_Получить_список_проектов():
    YouGile_projects = requests.get(Base_url + "projects")
    projects = YouGile_projects.json

