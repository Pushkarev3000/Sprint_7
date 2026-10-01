import pytest
import requests
from urls import courier, login
from helpers import register_new_courier_and_return_login_password

@pytest.fixture
def created_courier():
    body, list, response = register_new_courier_and_return_login_password()
    yield body, list, response
    body_2 = {
            "login": list[0],
            "password": list[1]
        }
    response = requests.post(login, json=body_2)
    courier_id = response.json()["id"]
    requests.delete(f"{courier}{courier_id}")