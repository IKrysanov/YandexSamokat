import configuration
import requests
import data
from http import HTTPStatus

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


def get_order(track_n):
    get_order_url_api = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_n}"
    response = requests.get(get_order_url_api)
    return response

#Функция автотеста
def test_create_order():
    response = create_order(data.order_body)
    track_n = response.json()["track"]
    print(f"Заказ создан. Номер заказа:\n{track_n}")
    o_response = get_order(track_n)

    assert o_response.status_code == HTTPStatus.OK, f"Ошибка: {o_response.status_code}"
    
    order_data = o_response.json()
    print(f"Данные заказа:\n{order_data}\nСтатус запроса:\n{get_order(track_n)}")


test_create_order()