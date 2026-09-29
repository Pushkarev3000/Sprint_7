import allure
import requests
import pytest
from urls import courier

@allure.title('Тесты на проверку создания курьера')

@allure.description("Тестируем позитивный сценарий: успешное создание")
def test_create_new_courier(created_courier):
    assert created_courier[1].status_code == 201
    assert created_courier[1].json() == {'ok': True}

@allure.description("Тестируем негативный сценарий: передаваемый логин уже занят")
def test_create_double_courier(created_courier):
    response = requests.post(courier, json=created_courier[0])
    assert response.status_code == 409
    assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

@allure.description("Тестируем негативный сценарий: отсуствуют поля логин/пароль")
@pytest.mark.parametrize('body',
                         [{"password": "123qaz", "firstName": "Тестовичок"},
                          {"login": "test007",  "firstName": "Тестер"},
                          {"firstName": "Тестомер"},
                          {}
                          ]
                         )
def test_create_wrong_body_courier(body):
    response = requests.post(courier, json=body)
    assert response.status_code == 400
    assert response.json()["message"] == "Недостаточно данных для создания учетной записи"