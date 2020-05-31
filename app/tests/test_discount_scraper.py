import pytest

from app.discount_scraper import get_discount


class Request:
    def __init__(self, content):
        self.content = content


@pytest.fixture
def response():
    with open('/Users/sbleidner/git/yello_discount_checker/app/tests/fixtures/static_response.html') as response:
        content = response.read()
        return content


def test_discount_scraper(mocker, response):
        mocker.patch('app.discount_scraper.requests.get', return_value=Request(response))

        discount = get_discount('00000')

        assert discount == '10'
