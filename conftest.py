import pytest
import requests
from urls import delete_courier_url, courier, login
from helpers import register_new_courier_and_return_login_password

# @pytest.fixture
# def delete_courier(params=[num]):
#     yield
#     op = f'{delete_courier_url}{num}'
#     print(op)
#     response = requests.delete(op)
#     print(response.json())
#     assert response.status_code == 200
#     assert response.json() == {'ok': True}
#     return 'Тестовые данные удалены'

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
    requests.delete(f"{delete_courier_url}{courier_id}") 