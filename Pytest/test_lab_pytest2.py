import pytest
import allure
@allure.title("verify that create booking, with valid data is working")
@allure.description("This testcase check for the positive create booking ")
@pytest.mark.positive

def test_create_booking_positive():
    print("test1")
    assert 1-1==2

@allure.title("verify that create booking, with valid data is working")
@allure.description("This testcase check for the negative create booking ")
@pytest.mark.negative
def test_create_booking_negative_1():
    print("test2")
    assert 1+1==2

@allure.title("verify that create booking, with valid data is working")
@allure.description("This testcase check for the negative create booking ")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("test2")
    assert 1 + 1 == 2