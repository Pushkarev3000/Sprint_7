import allure
import requests
from urls import order_list

@allure.feature('Тест на проверку списка заказов')

@allure.story("Тестируем позитивный сценарий: возвращается список заказов")
def test_get_order_list():
    response = requests.get(order_list)
    assert response.status_code == 200
    assert "orders" in response.json()
    assert response.json()["orders"] is not None