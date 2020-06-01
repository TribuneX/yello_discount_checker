from boddle import boddle
import json

from app.server import discount


def test_discount_endpoint(mocker):
    discount_value = '15'
    mocker.patch('app.server.get_discount', return_value=discount_value)
    with boddle():
        response = json.loads(discount('00000'))
        assert response['discount'] == int(discount_value)
