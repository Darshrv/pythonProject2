from wsgiref.util import request_uri

import allure
import pytest


@allure.title("verify the Get Request of Restfull Booker")
@allure.description("This Testcase check Booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    URL="https://restful-booker.herokuapp.com/apidoc/index.html"
    response_data=request.get(url=URL)
    assert response_data.status_code==200

