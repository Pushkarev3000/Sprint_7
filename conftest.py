import pytest
import requests
from urls import delete_courier_url, login
from helpers import register_new_courier_and_return_login_password

@pytest.fixture
def created_courier():
    body, list, response = register_new_courier_and_return_login_password()
    body_2 = {
        "login": list[0],
        "password": list[1]
    }
    response_2 = requests.post(login, json=body_2)
    courier_id = response_2.json()["id"]
    yield body, response, response_2
    check = requests.delete(f"{delete_courier_url}{courier_id}")
    assert check.status_code == 200