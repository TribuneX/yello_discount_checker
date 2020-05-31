from boddle import boddle
import json

from app.server import price


def test_discount_endpoint(mocker):
    discount = '15'
    mocker.patch('app.server.get_discount', return_value=discount)
    with boddle():
        response = json.loads(price('00000'))
        assert response['discount'] == int(discount)
