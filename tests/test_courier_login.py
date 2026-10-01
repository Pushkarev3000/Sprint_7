import requests
import pytest
import allure
from urls import login, courier

@allure.feature('Тесты на проверку логина курьера')
class TestCourierLogin:

    @allure.story("Тестируем позитивный сценарий: успешный логин")
    def test_login_courier(self, created_courier):
        list = created_courier[1]
        body = {
            "login": list[0],
            "password": list[1]
        }
        response = requests.post(login, json=body)
        courier_id = response.json()["id"]
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(courier_id, int)

    @allure.story("Тестируем негативный сценарий: не правильный логин/пароль")
    @allure.title("Передан некорректный логин")
    def test_login_courier_wrong_login(self):
        response = requests.post(login, json={"login": "tester3000", "password": "qwerty54321"})
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.story("Тестируем негативный сценарий: не правильный логин/пароль")
    @allure.title("Передан некорректный пароль к существующему логину")
    def test_login_courier_wrong_password(self, created_courier):
        created_login = created_courier[1][0]
        response = requests.post(login, json={"login": created_login,  "password": "Тест"})
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.story("Тестируем негативный сценарий: отсутствуют поля логин/пароль")
    @pytest.mark.parametrize('body',
                            [({"login": None,"password": "123qaz"}),
                            ({"login": "test007","password": None}),
                            ({})
                            ]
                            )
    def test_login_wrong_body_courier(self, body) :
        response = requests.post(login, json=body)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
