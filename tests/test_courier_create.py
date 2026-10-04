import allure
import requests
import pytest
from helpers import register_new_courier_and_return_login_password
from urls import courier

@allure.feature('Тесты на проверку создания курьера')
class TestCourierCreation:

    @allure.story("Тестируем позитивный сценарий: успешное создание")
    def test_create_new_courier(self, delete_courier):
        list, response  = register_new_courier_and_return_login_password()[1:3]
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        delete_courier(list)


    @allure.story("Тестируем негативный сценарий: передаваемый логин уже занят")
    def test_create_double_courier(self, created_courier):
        response = requests.post(courier, json=created_courier[0])
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.story("Тестируем негативный сценарий: отсуствуют поля логин/пароль")
    @pytest.mark.parametrize('body',
                            [{"password": "123qaz", "firstName": "Тестовичок"},
                            {"login": "test007",  "firstName": "Тестер"},
                            {"firstName": "Тестомер"},
                            {}
                            ]
                            )
    def test_create_wrong_body_courier(self, body):
        response = requests.post(courier, json=body)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"