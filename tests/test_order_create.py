import allure
import requests
import pytest
from urls import order

@allure.feature('Тесты на проверку создание заказа')

@allure.story("Тестируем позитивный сценарий: успешное создание заказа с разными комбинациями цветов")
@pytest.mark.parametrize('body',
                         [{"color":["BLACK","GREY"]},
                          {"color":["GREY"]},
                          {"color":["BLACK"]},
                          {"color":[]}
                          ]
                         )
def test_order_create(body):
    response = requests.post(order, json=body)
    assert response.status_code == 201
    assert "track" in response.json()
    assert isinstance(response.json()["track"], int)
