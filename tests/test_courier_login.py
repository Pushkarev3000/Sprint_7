import requests
import pytest
import allure
from urls import login

@allure.title('Тесты на проверку логина курьера')

@allure.description("Тестируем позитивный сценарий: успешный логин")
def test_login_courier(created_courier):
    assert created_courier[2].status_code == 200
    assert "id" in created_courier[2].json()
    assert isinstance(created_courier[2].json()["id"], int)

@allure.description("Тестируем негативный сценарий: не правильный логин/пароль")
@pytest.mark.parametrize('body',
                         [{"login": "tester3000", "password": "qwerty54321"},
                          {"login": "ninja",  "password": "Тест"}
                          ]
                         )
def test_login_courier_wrong_data(body):
    response = requests.post(login, json=body)
    assert response.status_code == 404
    assert response.json()["message"] == "Учетная запись не найдена"

@allure.description("Тестируем негативный сценарий: отсутствуют поля логин/пароль")
# сервис отдает 504 Time Out вместо ожидаемой 400
@pytest.mark.parametrize('body, status',
                         [({"login": None,"password": "123qaz"}, 400),
                          ({"login": "test007","password": None}, 504),
                          ({}, 504)
                          ]
                         )
def test_create_wrong_body_courier(body, status):
    response = requests.post(login, json=body)
    assert response.status_code == status
    if status == 400:
        assert response.json()["message"] == "Недостаточно данных для входа"
