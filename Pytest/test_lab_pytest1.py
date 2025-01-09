import pytest

    
@pytest.mark.smoke
def test_method2():
    print("This is Pytest case")
    assert 5==6

def test_method3():
    print("This is Pytest case")
    assert 1+1==2