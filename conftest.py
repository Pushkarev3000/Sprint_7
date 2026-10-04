import pytest
import requests
from urls import courier, login
from helpers import register_new_courier_and_return_login_password

@pytest.fixture
def created_courier(delete_courier):
    body, list, response = register_new_courier_and_return_login_password()
    yield body, list, response
    delete_courier(list)

@pytest.fixture
def delete_courier():
    list_2 = []

    def add_credentials(cred):
        list_2.append(cred)

    yield add_credentials
    body = {
            "login": list_2[0][0],
            "password": list_2[0][1]
        }
    response = requests.post(login, json=body)
    courier_id = response.json()["id"]
    requests.delete(f"{courier}{courier_id}")