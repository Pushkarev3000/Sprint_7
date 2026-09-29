import allure
import requests
from urls import order_list

@allure.title('Тест на проверку списка заказов')

@allure.description("Тестируем позитивный сценарий: возвращается список заказов")
def test_order_create():
    response = requests.get(order_list)
    assert response.status_code == 200
    assert "orders" in response.json()