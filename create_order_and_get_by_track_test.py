# Юлия Митрофанова, 35-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_track_order():
    # 1) создаём заказ
    create_response = sender_stand_request.post_new_order(data.order_body)
    assert create_response.status_code in (200, 201)

    track = create_response.json()["track"]

    # 2) получаем заказ по треку
    track_response = sender_stand_request.get_track_order(track)
    assert track_response.status_code == 200