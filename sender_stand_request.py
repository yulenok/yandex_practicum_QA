import configuration
import requests
import data

#Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers
    )

# Получить заказ по треку
def get_track_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER + "?t=" + str(track))